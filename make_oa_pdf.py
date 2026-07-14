"""Generate a formatted PDF of the VETAI Academy LLC Operating Agreement."""
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)
from reportlab.lib import colors

SRC = r"C:\Users\techf\Documents\VetAI-School\Operating_Agreement_VetAI_Academy_LLC.md"
OUT = r"C:\Users\techf\Documents\VetAI-School\Operating_Agreement_VetAI_Academy_LLC.pdf"

styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    "TitleC", parent=styles["Title"], fontSize=14, alignment=TA_CENTER,
    spaceAfter=14, leading=18,
)
article_style = ParagraphStyle(
    "Article", parent=styles["Heading2"], fontSize=11, spaceBefore=12,
    spaceAfter=6, textColor=colors.HexColor("#1a3c6e"),
)
body_style = ParagraphStyle(
    "Body", parent=styles["BodyText"], fontSize=10.5, alignment=TA_JUSTIFY,
    leading=15, spaceAfter=6,
)
sig_style = ParagraphStyle(
    "Sig", parent=styles["BodyText"], fontSize=10.5, leading=18, spaceAfter=4,
)

with open(SRC, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

story = []
i = 0
# First non-empty line is the title
while i < len(lines) and not lines[i].strip():
    i += 1
story.append(Paragraph(lines[i].strip(), title_style))
story.append(Spacer(1, 6))
i += 1

ARTICLE_RE = re.compile(r"^(ARTICLE [IVXLC]+:|EXHIBIT [A-Z]:)")

def is_table_row(s):
    return "|" in s and s.count("|") >= 2

while i < len(lines):
    line = lines[i].rstrip()
    stripped = line.strip()
    if not stripped:
        story.append(Spacer(1, 4))
        i += 1
        continue
    if ARTICLE_RE.match(stripped):
        story.append(Paragraph(stripped, article_style))
        i += 1
        continue
    # Table detection (markdown pipe table)
    if is_table_row(stripped):
        tbl_lines = []
        while i < len(lines) and is_table_row(lines[i].strip()):
            tbl_lines.append(lines[i].strip())
            i += 1
        rows = []
        for r in tbl_lines:
            cells = [c.strip() for c in r.strip().strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                continue  # skip separator row
            rows.append(cells)
        if rows:
            t = Table(rows, colWidths=[1.6*inch, 0.8*inch, 2.6*inch, 1.2*inch])
            t.setStyle(TableStyle([
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8eef7")),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]))
            story.append(Spacer(1, 4))
            story.append(t)
            story.append(Spacer(1, 4))
        continue
    # Bullet line
    if stripped.startswith("- "):
        story.append(Paragraph("&bull; " + stripped[2:], ParagraphStyle(
            "Bullet", parent=body_style, leftIndent=14)))
        i += 1
        continue
    # Signature/underscore lines
    if "____" in stripped or stripped.startswith("By:") or stripped.startswith("Title:") or stripped.startswith("Date:"):
        story.append(Paragraph(stripped.replace("_", "_"), sig_style))
        i += 1
        continue
    story.append(Paragraph(stripped, body_style))
    i += 1

doc = SimpleDocTemplate(
    OUT, pagesize=letter,
    leftMargin=0.9*inch, rightMargin=0.9*inch,
    topMargin=0.9*inch, bottomMargin=0.9*inch,
    title="Operating Agreement - VETAI Academy LLC",
)
doc.build(story)
print("PDF written to", OUT)
