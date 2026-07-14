"""
VETAIML AI Document Assistant — Flask web app.

A proof-of-capability demo: upload a policy/SOP document (PDF or TXT) and ask
natural-language questions. Answers are retrieved with semantic search over
local sentence-transformer embeddings (no external API, runs offline).
"""
from __future__ import annotations

import io
import os

import fitz  # PyMuPDF
from flask import Flask, jsonify, render_template, request

from rag import DocumentIndex

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB upload cap

INDEX = DocumentIndex()

SAMPLE_PATH = os.path.join(os.path.dirname(__file__), "sample_docs", "va_benefits_policy.txt")


def extract_text(filename: str, data: bytes) -> str:
    """Extract plain text from an uploaded PDF or text file."""
    lower = filename.lower()
    if lower.endswith(".pdf"):
        text_parts = []
        with fitz.open(stream=data, filetype="pdf") as doc:
            for page in doc:
                text_parts.append(page.get_text())
        return "\n".join(text_parts)
    # treat everything else as utf-8 text
    return data.decode("utf-8", errors="ignore")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/load-sample", methods=["POST"])
def load_sample():
    if not os.path.exists(SAMPLE_PATH):
        return jsonify({"error": "Sample document not found."}), 404
    with open(SAMPLE_PATH, "r", encoding="utf-8") as fh:
        text = fh.read()
    n = INDEX.build(text, source_name="VA Benefits Policy (sample)")
    return jsonify({"source": INDEX.source_name, "chunks": n})


@app.route("/api/upload", methods=["POST"])
def upload():
    file = request.files.get("document")
    if file is None or file.filename == "":
        return jsonify({"error": "No file provided."}), 400
    data = file.read()
    text = extract_text(file.filename, data)
    if not text.strip():
        return jsonify({"error": "Could not extract any text from that file."}), 400
    n = INDEX.build(text, source_name=file.filename)
    if n == 0:
        return jsonify({"error": "Document produced no searchable content."}), 400
    return jsonify({"source": INDEX.source_name, "chunks": n})


@app.route("/api/ask", methods=["POST"])
def ask():
    payload = request.get_json(silent=True) or {}
    question = (payload.get("question") or "").strip()
    if not question:
        return jsonify({"error": "Please enter a question."}), 400
    if not INDEX.ready:
        return jsonify({"error": "Load or upload a document first."}), 400
    results = INDEX.search(question, top_k=3)
    return jsonify({"source": INDEX.source_name, "question": question, "results": results})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
