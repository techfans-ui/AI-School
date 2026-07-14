"""Generate a professional PDF resume for Manse Soura."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable
)
from reportlab.lib import colors

OUT = r"C:\Users\techf\Documents\VetAI-School\Resume_Manse_Soura.pdf"

NAVY = colors.HexColor("#1a3c6e")
GREY = colors.HexColor("#444444")

styles = getSampleStyleSheet()
name_style = ParagraphStyle("Name", parent=styles["Title"], fontSize=20,
    alignment=TA_CENTER, textColor=NAVY, spaceAfter=2, leading=22)
subtitle_style = ParagraphStyle("Sub", parent=styles["Normal"], fontSize=10.5,
    alignment=TA_CENTER, textColor=GREY, spaceAfter=2, leading=14)
contact_style = ParagraphStyle("Contact", parent=styles["Normal"], fontSize=9.5,
    alignment=TA_CENTER, textColor=GREY, spaceAfter=2, leading=13)
section_style = ParagraphStyle("Section", parent=styles["Heading2"], fontSize=11.5,
    textColor=NAVY, spaceBefore=10, spaceAfter=2, leading=14)
role_style = ParagraphStyle("Role", parent=styles["Normal"], fontSize=10.5,
    textColor=colors.black, spaceBefore=5, spaceAfter=0, leading=13, fontName="Helvetica-Bold")
org_style = ParagraphStyle("Org", parent=styles["Normal"], fontSize=10,
    textColor=GREY, spaceAfter=1, leading=12)
date_style = ParagraphStyle("Date", parent=styles["Normal"], fontSize=9.5,
    textColor=NAVY, spaceAfter=2, leading=12, fontName="Helvetica-Oblique")
bullet_style = ParagraphStyle("Bullet", parent=styles["Normal"], fontSize=9.5,
    leftIndent=12, spaceAfter=1.5, leading=12.5, alignment=TA_JUSTIFY)
body_style = ParagraphStyle("Body", parent=styles["Normal"], fontSize=9.8,
    spaceAfter=3, leading=13, alignment=TA_JUSTIFY)

story = []

def hr():
    story.append(Spacer(1, 1))
    story.append(HRFlowable(width="100%", thickness=1, color=NAVY,
                            spaceBefore=1, spaceAfter=4))

def section(title):
    story.append(Paragraph(title.upper(), section_style))
    story.append(HRFlowable(width="100%", thickness=0.6, color=NAVY,
                            spaceBefore=0, spaceAfter=4))

def job(role, org, dates, bullets):
    story.append(Paragraph(role, role_style))
    story.append(Paragraph(org, org_style))
    story.append(Paragraph(dates, date_style))
    for b in bullets:
        story.append(Paragraph("&bull;&nbsp; " + b, bullet_style))

# Header
story.append(Paragraph("MANSE SOURA", name_style))
story.append(Paragraph("Service-Disabled Veteran &nbsp;|&nbsp; AI/ML Developer &nbsp;|&nbsp; Cloud &amp; Reliability Engineer", subtitle_style))
story.append(Paragraph("6527 E 128th St, Grandview, MO 64030", contact_style))
story.append(Paragraph("(254) 216-0899 &nbsp;|&nbsp; contracts@vetaiml.com", contact_style))
story.append(Paragraph("U.S. Army Veteran (92F) &nbsp;|&nbsp; 90% Service-Connected Disabled Veteran", contact_style))
hr()

# Summary
section("Professional Summary")
story.append(Paragraph(
    "Results-driven technology professional and U.S. Army veteran with approximately 15 years of "
    "combined military and civilian experience spanning artificial intelligence, machine learning, "
    "cloud engineering, site reliability, and logistics operations. Proven record of designing, "
    "deploying, and maintaining large-scale cloud and data systems while leading mission-critical "
    "operations under pressure. Founder and Managing Member of VETAI Academy LLC (d/b/a VETAIML "
    "Academy), delivering AI/ML education and training. Strong foundation in mathematics, statistics, "
    "and big-data analytics, combined with military-grade discipline, accountability, and leadership.",
    body_style))

# Core Competencies
section("Core Competencies")
story.append(Paragraph(
    "Machine Learning &amp; AI Model Development &nbsp;&bull;&nbsp; Cloud Architecture (AWS) &nbsp;&bull;&nbsp; "
    "Site Reliability Engineering &nbsp;&bull;&nbsp; CI/CD &amp; Infrastructure-as-Code &nbsp;&bull;&nbsp; "
    "Data Pipelines &amp; MLOps &nbsp;&bull;&nbsp; System Monitoring &amp; Incident Response &nbsp;&bull;&nbsp; "
    "Statistical Analysis &amp; Feature Engineering &nbsp;&bull;&nbsp; Capacity Planning &amp; Scaling &nbsp;&bull;&nbsp; "
    "Security &amp; Compliance &nbsp;&bull;&nbsp; Logistics &amp; Supply-Chain Operations &nbsp;&bull;&nbsp; "
    "Team Leadership &amp; Project Coordination",
    body_style))

# Experience
section("Professional Experience")
job("AI/ML Developer", "UMB Bank &mdash; Kansas City, MO", "January 2026 &ndash; Present", [
    "Develop, train, and deploy machine learning and AI models to support enterprise business solutions.",
    "Build and scale AI chatbots for multiple departments to improve productivity and customer service.",
    "Build and maintain data pipelines for model training, testing, and production deployment.",
    "Apply statistical analysis, feature engineering, and model evaluation techniques to optimize performance.",
    "Integrate ML models into applications and production environments.",
    "Collaborate with data, engineering, and business teams to deliver data-driven solutions.",
    "Monitor model performance and ensure accuracy, scalability, and regulatory compliance.",
])
job("Cloud Engineer", "Amazon Web Services (AWS) &mdash; Remote", "June 2020 &ndash; May 2025", [
    "Designed, deployed, and managed scalable cloud infrastructure on AWS.",
    "Built and automated CI/CD pipelines and infrastructure-as-code (IaC) solutions.",
    "Configured and maintained compute, storage, networking, and security services.",
    "Monitored system performance and optimized cost, scalability, and reliability.",
    "Implemented security best practices, access controls, and compliance standards.",
    "Collaborated with development teams to support cloud migrations and deployments.",
])
job("Site Reliability Engineer (SRE)", "Oracle / Cerner &mdash; Kansas City, MO", "January 2018 &ndash; May 2020", [
    "Ensured reliability, availability, and performance of large-scale cloud and database systems.",
    "Automated infrastructure, monitoring, and incident-response processes to reduce downtime.",
    "Managed deployments, capacity planning, and system scaling.",
    "Diagnosed and resolved production issues, performing root-cause analysis.",
    "Collaborated with engineering teams to improve system stability and operational efficiency.",
    "Served concurrently in the Missouri National Guard during this period.",
])
job("Petroleum Supply Specialist (92F), Rank E-4", "U.S. Army / Missouri National Guard", "November 2015 &ndash; January 2022", [
    "Received, stored, issued, and accounted for bulk petroleum products and supplies.",
    "Operated and maintained fuel storage, pumping, and distribution equipment.",
    "Conducted quality-control checks and tests on petroleum products.",
    "Maintained accurate inventory, dispatch, and accountability records.",
    "Ensured compliance with safety, environmental, and hazardous-material handling regulations.",
    "Supported logistics, supply-chain, and resource-management operations.",
    "Developed strong skills in leadership, accountability, operational planning, and team coordination.",
])

# Entrepreneurial
section("Entrepreneurial Experience")
job("Founder, Sole Owner &amp; Managing Member", "VETAI Academy LLC (d/b/a VETAIML Academy) &mdash; Grandview, MO", "May 2026 &ndash; Present", [
    "Founded and direct a veteran-owned small business providing AI/ML education, training, and curriculum development; SDVOSB certification in progress through the U.S. Small Business Administration (SBA).",
    "Hold 100% ownership and unconditional control over all strategic, financial, and day-to-day operations.",
    "Oversee curriculum design, instruction, client engagement, marketing, contracting, and financial management.",
])

# Education
section("Education")
story.append(Paragraph("<b>Master of Science (M.S.)</b>, Big Data Analytics &amp; Information Technology", body_style))
story.append(Paragraph("<b>Bachelor of Science (B.S.)</b>, Mathematics &amp; Statistics", body_style))

# Military
section("Military Service")
story.append(Paragraph(
    "United States Army / Missouri National Guard &nbsp;&bull;&nbsp; MOS: 92F &mdash; Petroleum Supply Specialist "
    "&nbsp;&bull;&nbsp; Rank: E-4 &nbsp;&bull;&nbsp; 90% Service-Connected Disabled Veteran &nbsp;&bull;&nbsp; Honorable Service",
    body_style))

# Technical Skills
section("Technical Skills")
story.append(Paragraph("<b>Languages &amp; Tools:</b> Python, SQL, machine learning frameworks, data pipeline tooling", body_style))
story.append(Paragraph("<b>Cloud:</b> AWS (compute, storage, networking, security), CI/CD, Infrastructure-as-Code", body_style))
story.append(Paragraph("<b>Practices:</b> MLOps, SRE, monitoring &amp; observability, incident response, automation", body_style))
story.append(Paragraph("<b>Domains:</b> AI/ML model development, big-data analytics, logistics &amp; supply chain", body_style))

doc = SimpleDocTemplate(OUT, pagesize=letter,
    leftMargin=0.7*inch, rightMargin=0.7*inch,
    topMargin=0.6*inch, bottomMargin=0.6*inch,
    title="Resume - Manse Soura")
doc.build(story)
print("Resume PDF written to", OUT)
