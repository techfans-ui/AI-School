"""
RAG engine for the VETAIML AI Document Assistant.

Real machine learning: documents are split into chunks, each chunk is encoded
into a dense vector with a sentence-transformer embedding model, and questions
are answered by semantic (cosine) similarity search over those vectors.
"""
from __future__ import annotations

import re
import numpy as np
from sentence_transformers import SentenceTransformer

# Small, fast, local model — downloads once (~80 MB) then runs fully offline.
_MODEL_NAME = "all-MiniLM-L6-v2"
_model: SentenceTransformer | None = None


def get_model() -> SentenceTransformer:
    """Lazy-load the embedding model so startup stays fast."""
    global _model
    if _model is None:
        _model = SentenceTransformer(_MODEL_NAME)
    return _model


def chunk_text(text: str, max_words: int = 120, overlap: int = 25) -> list[str]:
    """Split text into overlapping word windows that respect paragraph breaks."""
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks: list[str] = []
    for para in paragraphs:
        words = para.split()
        if len(words) <= max_words:
            chunks.append(para)
            continue
        start = 0
        while start < len(words):
            window = words[start : start + max_words]
            chunks.append(" ".join(window))
            start += max_words - overlap
    return chunks


class DocumentIndex:
    """Holds the chunks of one document and their embeddings."""

    def __init__(self) -> None:
        self.chunks: list[str] = []
        self.embeddings: np.ndarray | None = None
        self.source_name: str = ""

    @property
    def ready(self) -> bool:
        return self.embeddings is not None and len(self.chunks) > 0

    def build(self, text: str, source_name: str) -> int:
        """Chunk and embed a document. Returns the number of chunks indexed."""
        self.chunks = chunk_text(text)
        self.source_name = source_name
        if not self.chunks:
            self.embeddings = None
            return 0
        model = get_model()
        self.embeddings = model.encode(
            self.chunks, normalize_embeddings=True, convert_to_numpy=True
        )
        return len(self.chunks)

    def search(self, question: str, top_k: int = 3) -> list[dict]:
        """Return the top_k most relevant chunks with similarity scores."""
        if not self.ready:
            return []
        model = get_model()
        q_vec = model.encode(
            [question], normalize_embeddings=True, convert_to_numpy=True
        )[0]
        scores = self.embeddings @ q_vec  # cosine sim (vectors are normalized)
        top_idx = np.argsort(scores)[::-1][:top_k]
        results = []
        for rank, idx in enumerate(top_idx, start=1):
            results.append(
                {
                    "rank": rank,
                    "score": round(float(scores[idx]), 4),
                    "text": self.chunks[int(idx)],
                }
            )
        return results
