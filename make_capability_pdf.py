"""Generate a federal-style Capability Statement PDF for VETAIML Academy LLC."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)
from reportlab.lib import colors

OUT = r"C:\Users\techf\Documents\VetAI-School\VETAIML_Capability_Statement.pdf"

NAVY = colors.HexColor("#1a3c6e")
GREY = colors.HexColor("#444444")
LIGHT = colors.HexColor("#eef2f8")

styles = getSampleStyleSheet()
name_style = ParagraphStyle("Name", parent=styles["Title"], fontSize=20,
    alignment=TA_CENTER, textColor=NAVY, spaceAfter=2, leading=23)
subtitle_style = ParagraphStyle("Sub", parent=styles["Normal"], fontSize=10.5,
    alignment=TA_CENTER, textColor=GREY, spaceAfter=2, leading=14)
contact_style = ParagraphStyle("Contact", parent=styles["Normal"], fontSize=9.5,
    alignment=TA_CENTER, textColor=GREY, spaceAfter=1, leading=13)
section_style = ParagraphStyle("Section", parent=styles["Heading2"], fontSize=11.5,
    textColor=NAVY, spaceBefore=10, spaceAfter=2, leading=14)
body_style = ParagraphStyle("Body", parent=styles["Normal"], fontSize=9.8,
    spaceAfter=3, leading=13, alignment=TA_JUSTIFY)
bullet_style = ParagraphStyle("Bullet", parent=styles["Normal"], fontSize=9.6,
    leftIndent=12, spaceAfter=2, leading=12.8, alignment=TA_LEFT)
cell_label = ParagraphStyle("CellLabel", parent=styles["Normal"], fontSize=9,
    textColor=NAVY, leading=12, fontName="Helvetica-Bold")
cell_val = ParagraphStyle("CellVal", parent=styles["Normal"], fontSize=9,
    textColor=colors.black, leading=12)

story = []

def section(title):
    story.append(Paragraph(title.upper(), section_style))
    story.append(HRFlowable(width="100%", thickness=0.6, color=NAVY,
                            spaceBefore=0, spaceAfter=4))

def bullets(items):
    for b in items:
        story.append(Paragraph("&bull;&nbsp; " + b, bullet_style))

# ---- Header ----
story.append(Paragraph("VETAIML ACADEMY LLC", name_style))
story.append(Paragraph("Artificial Intelligence / Machine Learning Development &amp; IT Systems Support", subtitle_style))
story.append(Paragraph("Service-Disabled Veteran-Owned Small Business (SDVOSB &mdash; certification in progress)", subtitle_style))
story.append(HRFlowable(width="100%", thickness=1, color=NAVY, spaceBefore=4, spaceAfter=2))
story.append(Paragraph("6527 E 128th St, Grandview, MO 64030 &nbsp;|&nbsp; vetaiml.com", contact_style))
story.append(Paragraph("Manse Soura, Managing Member &nbsp;|&nbsp; (254) 216-0899 &nbsp;|&nbsp; contracts@vetaiml.com", contact_style))
story.append(Spacer(1, 6))

# ---- Overview ----
section("Company Overview")
story.append(Paragraph(
    "VETAIML Academy LLC is a veteran-owned small business delivering "
    "<b>artificial intelligence and machine learning (AI/ML) development, data analytics, "
    "and IT systems support</b> to federal agencies. Led by a U.S. Army veteran and practicing "
    "AI/ML developer, we design, build, and operationalize data-driven solutions&mdash;and we "
    "build agency workforce capacity through applied AI/ML training. We combine hands-on "
    "engineering capability with a disciplined, mission-focused delivery model.",
    body_style))

# ---- Core Competencies ----
section("Core Competencies")
bullets([
    "<b>AI/ML Engineering:</b> model development, training, evaluation, and deployment; "
    "generative AI and large language model (LLM) integration.",
    "<b>Data Analytics &amp; Engineering:</b> data pipelines (ETL), big-data processing, "
    "analytics, dashboards, and decision-support tooling.",
    "<b>MLOps &amp; Cloud:</b> model operations, CI/CD, monitoring, and secure deployment "
    "across AWS, Azure, and GCP.",
    "<b>IT Systems Support:</b> systems design, integration, modernization, and "
    "operations &amp; maintenance (O&amp;M).",
    "<b>AI/ML Workforce Training:</b> applied, outcomes-driven AI/ML upskilling for "
    "government and partner teams.",
])

# ---- Differentiators ----
section("Differentiators")
bullets([
    "Veteran-led, mission-structured delivery with direct, senior AI/ML expertise on every engagement.",
    "Practitioner depth: leadership holds an MS in Big Data Analytics and works as a full-time AI/ML developer.",
    "Agile small-business responsiveness with low overhead and direct access to decision-makers.",
    "Local to the Kansas City, MO federal corridor&mdash;able to support on-site needs.",
    "Dual capability: we both <b>build</b> AI/ML systems and <b>train</b> the workforce that sustains them.",
])

# ---- Past Performance ----
section("Past Performance &amp; Outcomes")
bullets([
    "Delivered AI/ML training pilot cohort: 100% completion; 80% placed within 60 days (beta results).",
    "Designed and deployed cloud-based ML workflows and analytics solutions in commercial settings.",
    "Available for sources-sought responses, teaming, and subcontracting to build federal past performance.",
])

# ---- Company Data table ----
section("Company Data")

def row(label, value):
    return [Paragraph(label, cell_label), Paragraph(value, cell_val)]

data = [
    row("Legal Name", "VETAI Academy LLC (DBA: VETAIML Academy)"),
    row("UEI", "UHUMP38XMEU8"),
    row("CAGE Code", "219N8"),
    row("SAM.gov Status", "Active (expires Jun 01, 2027)"),
    row("Business Type", "Veteran-Owned Small Business; SDVOSB certification in progress (SBA VetCert)"),
    row("Primary NAICS", "541512 &mdash; Computer Systems Design Services"),
    row("Additional NAICS", "541511, 541519, 611430 (Professional &amp; Mgmt Development Training)"),
    row("Location", "6527 E 128th St, Grandview, MO 64030"),
    row("Point of Contact", "Manse Soura, Managing Member"),
    row("Phone / Email", "(254) 216-0899 &nbsp;|&nbsp; contracts@vetaiml.com"),
]

tbl = Table(data, colWidths=[1.55*inch, 4.95*inch])
tbl.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), LIGHT),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#c9d4e6")),
]))
story.append(tbl)

doc = SimpleDocTemplate(OUT, pagesize=letter,
    leftMargin=0.7*inch, rightMargin=0.7*inch,
    topMargin=0.6*inch, bottomMargin=0.6*inch)
doc.build(story)
print("Wrote", OUT)
