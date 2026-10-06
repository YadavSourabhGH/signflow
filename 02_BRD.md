# Business Requirements Document
## SignFlow — Digital Document Approval Workflow for a University

**Case Study no. 89**  
**Course:** Software Engineering & Project Management, Semester III  
**Document status:** Final documentation set

## 1. Executive summary

University administration currently moves about 2,000 approval files each month between offices. The paper process takes an average of 12 days, and files can be lost while in transit. SignFlow is proposed as a controlled digital workflow for submitting, routing, approving, signing, reminding, and tracking these files.

The recommended first release covers purchase requests, leave, and event approvals. Together they represent 1,600 files per month, or 80% of the stated monthly volume. The supplied per-file-type effort gives an indicative 27 person-days for this three-type option, compared with 108 person-days for all 12 file types.

## 2. Business problem

| Current condition | Business effect |
|---|---|
| Files move physically between offices | Files can be delayed or lost |
| Average approval time is 12 days | Administration cannot meet a faster service target |
| Status is difficult to see while a file is moving | Staff spend time asking for updates |
| Senior officers have mixed comfort with computers | A digital process may be rejected or bypassed without assisted adoption |
| Signature validity must be established | A technically working process may still be unusable for official approvals |

## 3. Business objectives and success measures

| Objective | Measure | Target |
|---|---|---|
| Reduce approval delay | Average approval time | Under 4 days |
| Prevent lost records | Submitted files that cannot be retrieved by ID | Zero |
| Cover the highest-volume work first | Monthly volume handled by first release | 1,600 of 2,000 files, or 80% |
| Preserve accountability | Test transactions with complete audit records | 100% |
| Make digital signing acceptable | Production signature method | Written legal/compliance approval before release |
| Make progress visible | Reporting cadence | After each phase and after each pilot reporting period |

## 4. Stakeholder needs

| Stakeholder | Need | Decision or contribution |
|---|---|---|
| Registrar | Faster, traceable approvals and a clear exception path | Owns scope, acceptance, and escalation |
| IT head | A maintainable workflow with measurable quality | Owns technical design and release recommendation |
| Administration staff | Simple intake, clear errors, and status visibility | Supplies process knowledge and file metadata |
| Section officers | Correct routes and manageable inboxes | Confirms rules and performs UAT |
| Senior officers | A short approval path and confidence in the signature step | Participates in walkthroughs and UAT |
| Records/audit staff | Complete, searchable history | Validates retention and audit evidence |
| Legal/compliance representative | Signature method that can be accepted for official records | Approves the method in writing |

## 5. Business scope

### In scope for the proposed first release

- Digital registration of purchase requests, leave, and event approvals.
- Routing by file type and approved amount bands.
- Inbox views for reviewers and approvers.
- Approval, rejection, return, and signature actions.
- Reminders, escalation, search, audit history, and reporting.
- Assisted onboarding for senior officers who need it.

### Later release or controlled interim process

The remaining file types should be handled through a documented interim process until their rules are baselined. The all-types option remains a valid later release and is estimated at 108 person-days using the supplied figures.

### Outside this business case

SignFlow does not replace the university’s finance, HR, or event systems; define a new legal framework; decide paper-disposal policy; or procure hardware and network infrastructure.

## 6. Business process: proposed future state

1. An authorised staff member creates a file and attaches the required documents.
2. SignFlow validates required information and issues a unique file ID.
3. The routing rules select the approval path using file type and amount where applicable.
4. The current owner receives the file in an inbox and sees the due date.
5. The approver approves, rejects, or returns the file with a reason.
6. If required, the signature service returns a validation result.
7. SignFlow records each event, sends reminders, and escalates overdue work.
8. The requester and authorised managers can see status and reports.

## 7. Business rules

| Rule | Business requirement |
|---|---|
| BR-01 | Every submitted file receives a unique identifier. |
| BR-02 | A file cannot be routed until required metadata and attachments pass validation. |
| BR-03 | Routing is determined from approved file-type and amount rules. |
| BR-04 | An approval requiring a signature cannot become final until the signature result is validated. |
| BR-05 | A return or rejection requires a reason. |
| BR-06 | Every lifecycle event is recorded in an append-only audit history. |
| BR-07 | An overdue item creates the configured reminder or escalation event. |
| BR-08 | The production signature method requires written legal/compliance approval. |

## 8. Business requirements catalogue

| ID | Requirement | Priority | Linked SRS |
|---|---|---|---|
| BR-01 | Administration staff shall register and track approval files digitally. | Must | FR-01, FR-04 |
| BR-02 | The process shall cover the top three monthly file types first. | Must | Scope, FR-03 |
| BR-03 | The process shall reduce the average approval time below 4 days. | Must | NFR-05, FR-10 |
| BR-04 | No submitted file shall be lost from the digital record. | Must | NFR-06, FR-08 |
| BR-05 | Approvals and signatures shall be attributable and auditable. | Must | FR-05, FR-06, FR-08, NFR-01, NFR-02 |
| BR-06 | Users shall receive reminders and managers shall see overdue work. | Must | FR-07, FR-10 |
| BR-07 | Senior officers shall have an assisted path during adoption. | Should | Stakeholder need; UI design |
| BR-08 | The design shall allow later expansion to all 12 file types. | Should | Architecture and project plan |

## 9. Options considered

| Option | Coverage | Supplied effort | Business view |
|---|---:|---:|---|
| Digitise all 12 types immediately | 2,000 files, assuming the listed categories account for the full volume | 108 person-days | Broader first release, but more rules and more change at once |
| Start with top three | 1,600 files / 80% | 27 person-days | Recommended pilot; leaves a controlled 20% interim process |

## 10. Risks and constraints

The main business risks are resistance from senior officers, lack of legal acceptance for signatures, incorrect routing, incomplete rules for less common types, and continued delay if queue ownership is unclear. The project risk register contains the scored risks, owners, and responses.

## 11. Business acceptance

The Registrar accepts the business case when the selected release boundary is recorded, the target measures and owners are agreed, the signature method has a legal/compliance review path, and the interim process for the remaining file types is documented.

**Registrar:** ____________________  
**IT head:** ____________________  
**Date:** ____________________
