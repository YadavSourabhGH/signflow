from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, Image, KeepTogether)
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "report.pdf")

NAVY = HexColor("#0B1F3A")
BLUE = HexColor("#176B87")
TEAL = HexColor("#2A9D8F")
GOLD = HexColor("#E9C46A")
PALE = HexColor("#EAF3F5")
SLATE = HexColor("#425466")
LIGHT = HexColor("#F6F8FA")
RED = HexColor("#C84B31")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="ReportTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=30, leading=35, textColor=NAVY, alignment=TA_CENTER, spaceAfter=12))
styles.add(ParagraphStyle(name="Subtitle", parent=styles["Normal"], fontName="Helvetica", fontSize=14, leading=19, textColor=SLATE, alignment=TA_CENTER))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=18, leading=23, textColor=NAVY, spaceBefore=4, spaceAfter=10))
styles.add(ParagraphStyle(name="Subsection", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=12.5, leading=16, textColor=BLUE, spaceBefore=9, spaceAfter=5))
styles.add(ParagraphStyle(name="Body", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.5, leading=14, textColor=HexColor("#263238"), spaceAfter=7))
styles.add(ParagraphStyle(name="Small", parent=styles["BodyText"], fontName="Helvetica", fontSize=8, leading=10, textColor=SLATE))
styles.add(ParagraphStyle(name="Callout", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=11, leading=15, textColor=NAVY, alignment=TA_CENTER))
styles.add(ParagraphStyle(name="TableHead", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=8.2, leading=10, textColor=colors.white))
styles.add(ParagraphStyle(name="TableBody", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.2, leading=10, textColor=HexColor("#263238")))

def P(text, style="Body"):
    return Paragraph(text, styles[style])

def table(data, widths, header=True, font_size=8.2):
    formatted = []
    for row_i, row in enumerate(data):
        style = "TableHead" if header and row_i == 0 else "TableBody"
        formatted.append([Paragraph(str(cell), styles[style]) if isinstance(cell, str) else cell for cell in row])
    t = Table(formatted, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    commands = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.25, HexColor("#D9E2E7")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), font_size),
        ("TEXTCOLOR", (0, 0), (-1, -1), HexColor("#263238")),
    ]
    if header:
        commands += [("BACKGROUND", (0, 0), (-1, 0), NAVY), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white), ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")]
    for row in range(1 if header else 0, len(data)):
        if row % 2 == 0:
            commands.append(("BACKGROUND", (0, row), (-1, row), LIGHT))
    t.setStyle(TableStyle(commands))
    return t

def footer(canvas, doc):
    canvas.saveState()
    w, _ = A4
    canvas.setStrokeColor(HexColor("#D9E2E7")); canvas.line(doc.leftMargin, 1.25*cm, w-doc.rightMargin, 1.25*cm)
    canvas.setFont("Helvetica", 7.5); canvas.setFillColor(SLATE)
    canvas.drawString(doc.leftMargin, .82*cm, "SignFlow | Digital Document Approval Workflow")
    canvas.drawRightString(w-doc.rightMargin, .82*cm, f"Page {doc.page}")
    canvas.restoreState()

story=[]
# Cover
story += [Spacer(1, 3.0*cm), P("PROJECT REPORT", "Subtitle"), Spacer(1, .35*cm), P("SignFlow", "ReportTitle"), P("Digital Document Approval Workflow for a University", "Subtitle"), Spacer(1, 1.2*cm)]
cover = Table([[P("<b>2,000</b><br/><font size=8>files each month</font>", "Callout"), P("<b>80%</b><br/><font size=8>volume in first release</font>", "Callout"), P("<b>&lt; 4 days</b><br/><font size=8>approval-time target</font>", "Callout")]], colWidths=[5.1*cm]*3)
cover.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PALE),("BOX",(0,0),(-1,-1),.6,TEAL),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("TOPPADDING",(0,0),(-1,-1),14),("BOTTOMPADDING",(0,0),(-1,-1),14),("LINEAFTER",(0,0),(1,0),.4,TEAL)]))
story += [cover, Spacer(1, 1.4*cm), P("Case Study No. 89 | Software Engineering & Project Management", "Subtitle"), Spacer(1, .4*cm), P("Documentation-only submission — no deployed application is represented by this report.", "Small"), PageBreak()]

# Executive summary
story += [P("Executive summary", "Section"), P("SignFlow is a proposed controlled digital workflow for university approval files. It is designed to replace slow, difficult-to-track paper movement with digital registration, routing, approval, signing, reminders, audit history, and reporting."),
          P("The current process handles about 2,000 files per month and takes an average of 12 days. The recommended first release focuses on purchase requests, leave, and event approvals: 1,600 monthly files, or 80% of stated volume. This staged scope concentrates effort on the most frequent work while remaining expandable to all 12 file types."),
          P("Problem and intended outcome", "Subsection")]
story.append(table([
    ["Current challenge", "SignFlow response", "Success measure"],
    ["Files move between offices and may be lost", "Unique IDs, searchable file records and append-only audit history", "Zero submitted files unretrievable"],
    ["Approval average is 12 days", "Rules-based routing, owner inboxes, reminders and escalation", "Average approval time under 4 days"],
    ["Status is opaque", "Current owner, due date, lifecycle state and reporting", "Managers can monitor open and overdue files"],
    ["Signature validity must be confirmed", "Separate signature validation and legal/compliance release gate", "Written approval before release"],
], [4.4*cm, 7.4*cm, 4.0*cm]))
story += [Spacer(1, .3*cm), P("Recommended release boundary", "Subsection"), P("The first release includes digital registration and tracking, routing by file type and approved amount bands, inboxes, approval/rejection/return actions, signature handling, reminders, audit, search and reporting. Remaining file types retain a documented interim process until their routing rules are baselined.")]

# Scope and workflow
story += [P("Proposed workflow and scope", "Section"), P("An authorised staff member creates a file, attaches supporting material, and submits it. The system validates the record, creates a unique ID, chooses a route, and places the item in the current owner’s inbox. Approval decisions are recorded with actor and timestamp; signature-required approvals are not final until validation returns successfully."), P("Core lifecycle", "Subsection")]
flow = Table([[P("1. Create & validate", "Callout"), P("2. Route", "Callout"), P("3. Review & decide", "Callout"), P("4. Sign & close", "Callout")]], [4.0*cm]*4)
flow.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PALE),("BOX",(0,0),(-1,-1),.5,TEAL),("LINEAFTER",(0,0),(2,0),.4,TEAL),("TOPPADDING",(0,0),(-1,-1),12),("BOTTOMPADDING",(0,0),(-1,-1),12)]))
story += [flow, Spacer(1, .3*cm), P("First-release requirements", "Subsection")]
story.append(table([
    ["Area", "Commitment for the proposed first release"],
    ["File types", "Purchase requests, leave, and event approvals"],
    ["Routing", "Approved file-type and amount-band rules; unsupported types enter an exception queue"],
    ["Decisions", "Approve, reject, or return; a return/rejection requires a reason"],
    ["Control", "Append-only audit history, due dates, reminders, escalation, and authorised search"],
    ["Adoption", "Short approval path and assisted onboarding for senior officers"],
], [4.2*cm, 11.6*cm]))

# Delivery and estimate
story += [P("Delivery approach and estimate", "Section"), P("The supplied effort is treated as person-days: 3 days for workflow design, 4 days for configuration, and 2 days for testing per file type. Calendar duration depends on staffing and rule availability, so the report does not make a delivery-time promise."), P("Release comparison", "Subsection")]
story.append(table([
    ["Option", "File types", "Monthly coverage", "Supplied effort", "Assessment"],
    ["All types", "12", "2,000 files (assumed full stated volume)", "108 person-days", "Broadest scope; more rules and organisational change at once"],
    ["Recommended pilot", "3", "1,600 files / 80%", "27 person-days", "High-volume coverage with 81 fewer person-days"],
], [2.5*cm, 2.0*cm, 3.6*cm, 3.0*cm, 4.7*cm]))
story += [Spacer(1,.25*cm), P("Indicative delivery plan", "Subsection")]
story.append(table([
    ["Phase", "Planning duration", "Main milestone"],
    ["Initiation", "2 working days", "Scope decision"], ["Requirements", "5 working days", "SRS baseline"], ["Design and UML", "5 working days", "Design review"], ["Configuration and build", "9 working days", "Configured build"], ["Integration testing", "4 working days", "Test evidence"], ["UAT and training", "4 working days", "UAT decision"], ["Pilot and closure", "3 working days", "Pilot release / closure"],
], [6.2*cm, 4.0*cm, 6.1*cm]))
story += [P("Critical-path planning assumption: initiation → requirements → design → configuration/build → integration testing → UAT/training → pilot/closure = 32 working days. Legal/signature review and data/rule preparation run as parallel branches and must be monitored for delay.", "Small")]

# Quality and risks
story += [P("Quality assurance and risk control", "Section"), P("Quality assurance is based on configuration/unit, integration, system, security/audit, performance, and user-acceptance testing. Exit requires all Must tests to pass, no open critical defect, successful audit and signature checks, and zero unretrievable submitted test files."), P("Key test focus", "Subsection")]
story.append(table([
    ["Control", "Evidence expected"],
    ["Routing correctness", "Decision-table coverage for top-three types and threshold/boundary tests"],
    ["Auditability", "Decision, actor, timestamp, lifecycle state and required audit fields for every test transaction"],
    ["Signature", "Provider validation result plus written legal/compliance approval"],
    ["Reliability", "Search/retrieval reconciliation with zero lost submitted files"],
    ["Performance", "95% of normal page requests within 3 seconds; monthly availability target of 99.5%"],
], [5.0*cm, 11.3*cm]))
risks_table = table([
    ["Risk", "Exposure", "Planned response"],
    ["Senior-officer resistance to digital approval", "16", "Assisted pilot, brief walkthroughs, adoption monitoring and escalation path"],
    ["Signature method not accepted by legal/compliance", "15", "Written approval before release; controlled fallback process"],
    ["Incorrect amount/type routing", "15", "Approved decision table, boundary tests, business sign-off and exception monitoring"],
    ["Incomplete rules for other file types", "12", "Top-three staged scope and maintained interim-process register"],
], [6.0*cm, 2.1*cm, 8.2*cm])
story.append(KeepTogether([Spacer(1,.25*cm), P("Highest-priority risks", "Subsection"), risks_table]))

# Governance & conclusion
story += [P("Governance, release gates and next actions", "Section"), P("The Registrar owns scope, acceptance and escalation. The IT head owns technical design and release recommendation. Administration representatives and section officers validate process rules and participate in UAT; legal/compliance approves the signature approach."), P("Release gates", "Subsection")]
story.append(table([
    ["Gate", "Decision evidence"],
    ["Scope", "Recorded first-release boundary and named owners for all Must requirements"],
    ["Rules", "Signed routing decision table, including amount bands and exception handling"],
    ["Signature", "Written legal/compliance approval and provider validation evidence"],
    ["Quality", "No open critical defect; acceptance tests, audit check and lost-file check pass"],
    ["Pilot", "Under-four-day approval-time result, or Registrar-approved corrective-action plan"],
], [4.2*cm, 12.1*cm]))
story += [Spacer(1,.35*cm), P("Conclusion", "Subsection"), P("SignFlow offers a practical staged route from paper movement to accountable digital approvals. Starting with the three highest-volume file types provides measurable value at 80% of monthly volume while avoiding premature expansion into incomplete rules. The key conditions for a safe release are validated routing, a legally accepted signature method, complete audit evidence, and assisted adoption."), Spacer(1,.5*cm), P("Source basis: Business Requirements Document, SRS, UML Package, Project Plan, Estimation Sheet, Test Plan and Evidence, Risk Register and Closure Note, and UI Design Specification in the SignFlow documentation set.", "Small")]

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=2.0*cm, rightMargin=2.0*cm, topMargin=1.8*cm, bottomMargin=1.7*cm, title="SignFlow Project Report", author="SignFlow Project Team")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
