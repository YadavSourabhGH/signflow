"""Create a plain-English SignFlow project report."""
import os
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, KeepTogether

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "report.pdf")
NAVY, BLUE, TEAL = HexColor("#17324D"), HexColor("#1A6B8A"), HexColor("#2F8F83")
INK, MUTED, PALE, LINE = HexColor("#263238"), HexColor("#52616B"), HexColor("#EDF6F5"), HexColor("#D4E0E3")

s = getSampleStyleSheet()
s.add(ParagraphStyle(name="CoverKicker", parent=s["Normal"], fontName="Helvetica-Bold", fontSize=11, leading=14, alignment=TA_CENTER, textColor=TEAL, spaceAfter=8))
s.add(ParagraphStyle(name="CoverTitle", parent=s["Title"], fontName="Helvetica-Bold", fontSize=31, leading=36, alignment=TA_CENTER, textColor=NAVY, spaceAfter=10))
s.add(ParagraphStyle(name="CoverSub", parent=s["Normal"], fontName="Helvetica", fontSize=14, leading=20, alignment=TA_CENTER, textColor=MUTED))
s.add(ParagraphStyle(name="H1", parent=s["Heading1"], fontName="Helvetica-Bold", fontSize=20, leading=25, textColor=NAVY, spaceBefore=0, spaceAfter=10))
s.add(ParagraphStyle(name="H2", parent=s["Heading2"], fontName="Helvetica-Bold", fontSize=13.5, leading=17, textColor=BLUE, spaceBefore=12, spaceAfter=6))
s.add(ParagraphStyle(name="Body", parent=s["BodyText"], fontName="Helvetica", fontSize=10.4, leading=15.5, textColor=INK, spaceAfter=9))
s.add(ParagraphStyle(name="Small", parent=s["BodyText"], fontName="Helvetica", fontSize=8.2, leading=10.5, textColor=MUTED))
s.add(ParagraphStyle(name="Cell", parent=s["BodyText"], fontName="Helvetica", fontSize=9, leading=11.5, textColor=INK))
s.add(ParagraphStyle(name="CellHead", parent=s["BodyText"], fontName="Helvetica-Bold", fontSize=9, leading=11.5, textColor=colors.white))
s.add(ParagraphStyle(name="Quote", parent=s["BodyText"], fontName="Helvetica-Bold", fontSize=13, leading=18, textColor=NAVY, alignment=TA_CENTER))

def p(text, style="Body"):
    return Paragraph(text, s[style])

def bullet(text):
    return Paragraph("• " + text, s["Body"])

def nice_table(rows, widths):
    cooked=[]
    for r, row in enumerate(rows):
        cooked.append([p(x, "CellHead" if r == 0 else "Cell") for x in row])
    t=Table(cooked, colWidths=widths, repeatRows=1, hAlign="LEFT")
    cmds=[("BACKGROUND",(0,0),(-1,0),NAVY),("TEXTCOLOR",(0,0),(-1,0),colors.white),("VALIGN",(0,0),(-1,-1),"TOP"),("GRID",(0,0),(-1,-1),.35,LINE),("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]
    for r in range(1,len(rows)):
        if r % 2 == 0: cmds.append(("BACKGROUND",(0,r),(-1,r),HexColor("#F7FAFA")))
    t.setStyle(TableStyle(cmds)); return t

def footer(c, doc):
    c.saveState(); w,_=A4
    c.setStrokeColor(LINE); c.line(doc.leftMargin,1.25*cm,w-doc.rightMargin,1.25*cm)
    c.setFillColor(MUTED); c.setFont("Helvetica",7.5)
    c.drawString(doc.leftMargin,.82*cm,"SignFlow project report")
    c.drawRightString(w-doc.rightMargin,.82*cm,f"Page {doc.page}")
    c.restoreState()

story=[]
# Page 1
story += [Spacer(1,2.2*cm),p("CASE STUDY 89 · PROJECT REPORT","CoverKicker"),p("SignFlow","CoverTitle"),p("A simpler way for a university to move approval files", "CoverSub"),Spacer(1,.9*cm)]
key=Table([[p("<b>The problem</b><br/>A paper file can take around 12 days to move through the university.","Cell"),p("<b>The idea</b><br/>Track each file digitally, send it to the right person, and show what is waiting.","Cell"),p("<b>The goal</b><br/>Bring the average approval time below 4 days without losing a file.","Cell")]],colWidths=[5.1*cm]*3)
key.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),PALE),("BOX",(0,0),(-1,-1),.6,TEAL),("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),12),("RIGHTPADDING",(0,0),(-1,-1),12),("TOPPADDING",(0,0),(-1,-1),14),("BOTTOMPADDING",(0,0),(-1,-1),14),("LINEAFTER",(0,0),(1,0),.4,TEAL)]))
story += [key,Spacer(1,1.2*cm),p("<b>Name:</b> Sourabh Yadav<br/><b>Roll No:</b> 150096724013<br/><b>Cohort:</b> Mark Zukerberg", "CoverSub"),PageBreak()]

# Page 2
story += [p("1. What is going wrong today?","H1"),p("Every month, the university handles about 2,000 approval files. At present, many of them move from office to office on paper. That makes it hard to answer ordinary questions such as: <i>Where is my file? Who needs to act next? Has it been signed?</i> It also means a file can be delayed, misplaced, or returned without the requester knowing why."),p("The project is not trying to replace every university system. It is trying to make the approval journey clearer and safer.","Body"),p("Before and after","H2")]
story.append(nice_table([
 ["Today", "With SignFlow"],
 ["A file is physically passed between offices.", "A file has one digital record and a unique file ID."],
 ["People often have to ask around to learn its status.", "The system shows the current owner, the due date and the latest action."],
 ["A delay can remain invisible until someone complains.", "Reminders and overdue views make waiting work visible."],
 ["A decision may be difficult to trace later.", "Each important action is kept in the file’s history."],
], [7.8*cm,7.8*cm]))
story += [Spacer(1,.35*cm),p("A simple example","H2"),p("Imagine an administrator submitting a purchase request. Instead of sending a physical file around campus, they add the details and attachment once. SignFlow checks that the form is complete, gives it an ID, and sends it to the right reviewer. If the request is returned, the reason is visible. If it is overdue, the responsible person can see that immediately."),Spacer(1,.2*cm)]
dash=os.path.join(ROOT,"ui","UI-01_Dashboard.png")
if os.path.exists(dash):
    img=Image(dash,width=14.3*cm,height=7.6*cm,kind="proportional")
    story += [KeepTogether([img,Spacer(1,.1*cm),p("Proposed dashboard screen (static design mock-up).","Small")])]
story.append(PageBreak())

# Page 3
story += [p("2. What will the first version do?","H1"),p("Trying to digitise every kind of university file at once would make the first release much harder to manage. The sensible first step is to focus on the three file types that are used most often: purchase requests, leave applications, and event approvals. Together, they make up 1,600 out of 2,000 files each month — about 80% of the work."),p("For a staff member, the journey is straightforward:","H2")]
steps=["Create the file and attach the needed documents.","Check that the important details have been filled in.","Give the file a unique ID and send it on the correct approval path.","Show the reviewer what they need to do, and by when.","Let the reviewer approve, return, or reject it. A return or rejection must include a reason.","If a signature is needed, wait for a valid signature result before treating the file as complete.","Keep a timeline of what happened and make the file searchable later."]
for i,txt in enumerate(steps,1): story.append(p(f"<b>{i}.</b> {txt}"))
story += [p("What is included now — and what can wait","H2")]
story.append(nice_table([
 ["First release", "Later, after the pilot"],
 ["The top three file types; routing; inboxes; decisions; reminders; search; reports; and an audit trail.", "The remaining file types, once their approval rules have been agreed and tested."],
 ["Help for senior officers who are less comfortable with digital tools.", "A decision about whether to expand to all 12 file types."],
], [7.8*cm,7.8*cm]))
story += [Spacer(1,.25*cm),p("A useful rule of thumb: SignFlow should never silently guess. If a file type is not configured, it should go to an exception queue rather than being sent to the wrong person.","Quote"),PageBreak()]

# Page 4
story += [p("3. How much work is this?","H1"),p("The case study gives a simple estimate: each file type needs 3 person-days to design its workflow, 4 person-days to configure it, and 2 person-days to test it. That is 9 person-days per file type. These are effort estimates, not promises about calendar dates or cost."),p("Why start small?","H2")]
story.append(nice_table([
 ["Choice", "What it covers", "Estimated effort"],
 ["Start with the top three", "Purchase requests, leave and event approvals — 80% of monthly volume.", "27 person-days"],
 ["Do all 12 types immediately", "The whole stated scope, but with many more rules to agree and test.", "108 person-days"],
], [3.7*cm,8.1*cm,3.8*cm]))
story += [p("Starting with three types saves 81 person-days of configured work. More importantly, it gives the university a chance to learn from a real pilot before expanding the system.","Body"),p("A practical timeline","H2"),p("The project plan uses a 32-working-day planning path: first agree the scope, then gather requirements, design the routes, configure the system, test it, train people, and run a pilot. Some work can happen at the same time — for example, legal review of the signature method — but it must not be left until the end."),p("The people who need to be involved","H2")]
story.append(nice_table([
 ["Person or group", "Why they matter"],
 ["Registrar", "Chooses the release scope, resolves escalations and accepts the outcome."],
 ["IT lead and project team", "Turn the agreed rules into a reliable, supportable workflow."],
 ["Administration staff and section officers", "Explain the real process, test it, and confirm that routes are correct."],
 ["Legal/compliance representative", "Approves the signature method before signature-required files go live."],
], [5.4*cm,10.2*cm]))
story.append(PageBreak())

# Page 5
story += [p("4. What must be checked before launch?","H1"),p("A system like this is useful only if people trust it. The project therefore needs to test the everyday cases — but it must also check the awkward cases: a high-value purchase request, a missing attachment, a returned file, a signature that fails, and a file that is overdue."),p("The launch should not go ahead until:","H2")]
for item in ["Every required first-release workflow has been tested and any critical fault is closed.","The routing rules have been checked by the people who own the process.","Every test file can be found again by its ID.","The audit history records who did what and when.","The legal/compliance representative has approved the signature approach in writing.","The pilot shows an average approval time below 4 days — or the Registrar has agreed a clear improvement plan."]:
    story.append(bullet(item))
story += [p("The main risks — in plain language","H2")]
story.append(nice_table([
 ["Risk", "How the project should handle it"],
 ["Some senior officers may prefer paper.", "Use short walkthroughs, simple screens and assisted approval during the pilot."],
 ["A signature provider may not meet university requirements.", "Get written legal/compliance approval before release; keep a controlled fallback process."],
 ["A wrong rule could send a file to the wrong person.", "Get business sign-off on each route and test amount boundaries carefully."],
], [6.3*cm,9.3*cm]))
story += [p("What should happen next","H2"),p("1. Confirm the three first-release file types and name the people who own their approval rules.<br/>2. Agree the amount bands and approval levels for purchase requests and event approvals.<br/>3. Ask legal/compliance to confirm the signature method.<br/>4. Walk through the screens with staff and senior officers before user acceptance testing.<br/>5. Run the pilot, measure approval time and lost-file exceptions, then decide whether to expand."),Spacer(1,.4*cm),p("<b>Bottom line:</b> SignFlow is a staged improvement, not a big-bang replacement. If the university gets the routing rules and signature approval right, the first release can make the majority of approval work faster, easier to follow and much less likely to disappear.","Quote"),Spacer(1,.4*cm),p("Source: SignFlow project documentation set — BRD, SRS, project plan, estimation sheet, test plan, risk register, UML package and UI design specification.","Small")]

doc=SimpleDocTemplate(OUT,pagesize=A4,leftMargin=2.0*cm,rightMargin=2.0*cm,topMargin=1.8*cm,bottomMargin=1.7*cm,title="SignFlow Project Report",author="SignFlow Project Team")
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT)
