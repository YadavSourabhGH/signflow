# Complete project documentation index
## SignFlow — Digital Document Approval Workflow for a University

## Submission purpose

This is a documentation-first Software Engineering & Project Management submission. The proposed system is explained through business requirements, software requirements, process and design diagrams, project planning, estimation, quality evidence, risk control, and static UI screens. No functional application or deployment is included or required.

## Document map

| Area | Deliverable | What it answers |
|---|---|---|
| Business need | `02_BRD.md` | Why the university needs SignFlow and what business outcome is expected |
| Software requirements | `01_SRS.md` | What the system must do and how quality is measured |
| System design | `03_UML_Package.md` and `uml/06_architecture.mmd` | Who interacts with the system, how objects relate, and how a file moves |
| Project management | `04_Project_Plan.md` and `uml/07_gantt.mmd` | How the work is sequenced, monitored, and governed |
| Estimation | `05_Estimation_Sheet.md` | How the supplied effort figures were calculated |
| Quality assurance | `06_Test_Plan_and_Evidence.md` | How routing, boundaries, signatures, audit, and performance will be tested |
| Risk and closure | `07_Risk_Register_and_Closure_Note.md` | What could affect delivery and how acceptance/closure will work |
| UI representation | `08_UI_Design_Specification.md` and `ui/` | What users will see and how the proposed workflow is represented |

## Recommended reading order

1. Read the BRD for the problem, business objectives, and release recommendation.
2. Read the SRS for functional and non-functional requirements.
3. Review the UI specification and screens to connect requirements to user interaction.
4. Review the UML and architecture diagrams for the proposed design.
5. Read the project plan and Gantt chart for sequencing and control.
6. Read the estimation, testing, and risk documents for feasibility and assurance.

## Consistency checks

- The top-three release uses purchase requests, leave, and event approvals.
- The top-three release covers 1,600 of 2,000 files, or 80%.
- The supplied per-type effort totals 27 person-days for three types and 108 person-days for 12 types.
- The file lifecycle uses Draft, Submitted, In Review, Awaiting Signature, Approved, Returned, Rejected, Cancelled, and Archived consistently across the SRS, UML, test plan, and UI detail screen.
- Routing and digital signatures remain separate responsibilities in the architecture and class/sequence diagrams.
- UI labels use the same terms as the requirements: file ID, current owner, due date, route, signature status, audit, reminder, and report.

## Submission note

The UI files are static design representations. They show proposed layout, labels, sample data, and interaction intent. They do not claim working navigation, authentication, routing, signature integration, or report generation.
