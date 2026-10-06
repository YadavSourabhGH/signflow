# Software Requirements Specification
## SignFlow — Digital Document Approval Workflow for a University

**Case Study no. 89**  
**Course:** Software Engineering & Project Management, Semester III  
**Document status:** Final academic submission draft

## 1. Introduction

### 1.1 Purpose

SignFlow will move the university’s internal approval files through a controlled digital workflow. It will route files, collect digital approvals and signatures, send reminders, and maintain a searchable history.

The current process handles about 2,000 files a month on paper. Files move between offices, can be lost, and take an average of 12 days to receive approval. The target is an average approval time under 4 days with zero lost files.

### 1.2 Scope

**In scope**

- Submission and registration of approval files.
- Routing by file type and amount where an amount exists.
- Assignment to officers and approval levels.
- Digital signature capture and signature validation status.
- Reminders and escalation for overdue actions.
- Searchable status and audit history.
- Reporting of approval time and exceptions.
- Digitisation of the three highest-volume types in the first option: purchase requests, leave, and event approvals.
- A later all-types option covering 12 file types.

**Out of scope for this case study**

- Replacing the university’s finance, HR, or event systems.
- Defining a new legal framework for electronic signatures.
- Paper-file disposal policy.
- Hardware procurement and network redesign.

### 1.3 Stakeholders

| Stakeholder | Interest and responsibility |
|---|---|
| Registrar | Sponsor, policy owner, escalation authority |
| IT head | Technical owner and release approver |
| Administration staff | File entry, scanning, correction, and status checks |
| Section officers | Review and routing decisions |
| Senior officers | Approvals and digital signatures; some may need assisted use |
| Records/audit staff | Audit trail and retention checks |
| Legal/compliance representative | Confirmation that the selected signature method is acceptable |

### 1.4 Definitions

- **File:** A university approval record and its attached documents.
- **Approval level:** One ordered decision point in the route.
- **Route:** The sequence of officers or roles that receive a file.
- **DRE:** Defect removal efficiency, calculated as defects found before release divided by all defects found before and after release.
- **MoSCoW:** Must have, Should have, Could have, Won’t have for this release.

## 2. Overall description

### 2.1 Product perspective

SignFlow is a workflow application with separate modules for file intake, routing, approvals, signatures, reminders, audit, and reporting. The routing module should decide who receives a file without embedding the implementation of the signature provider. This allows either module to change without forcing a redesign of the other.

### 2.2 Operating assumptions

1. The university supplies the official approval hierarchy and file-type rules before configuration.
2. A legally accepted digital-signature method is selected and approved before production use.
3. Users have university accounts or another approved identity source.
4. Scanning and attachment quality remain the responsibility of the submitting office.
5. Calendar duration and staffing are planning assumptions in the project plan, not facts supplied by the case.

### 2.3 Constraints

- The Registrar wants all file types digitised in one go, while the IT head recommends starting with the three most common types.
- Some senior officers are uncomfortable with computers and may require assisted onboarding.
- The system must preserve a reliable history of actions.
- The stated target is under 4 days average approval time and zero lost files.

### 2.4 Recommended release boundary

The top-three option covers 1,600 of 2,000 monthly files, or 80% of volume:

\[
700 + 600 + 300 = 1,600
\]
\[
1,600 / 2,000 \times 100 = 80\%
\]

The three types are purchase requests, leave, and event approvals. This option requires 27 person-days of the supplied per-type workflow effort, compared with 108 person-days for all 12 types. It gives the team a meaningful pilot while covering most of the monthly workload. The remaining 20% should be handled through a documented interim process until the later release.

## 3. Functional requirements

Priority uses MoSCoW. Every requirement has a stable identifier for traceability.

| ID | Requirement | Priority | Acceptance measure |
|---|---|---|---|
| FR-01 | The system shall allow an authorised staff member to create a file with file type, subject, requester, attachments, and required metadata. | Must | A valid file can be saved and receives a unique identifier. |
| FR-02 | The system shall validate mandatory fields and attachment metadata before submission. | Must | Invalid submissions are rejected with field-level messages. |
| FR-03 | The system shall route a submitted file using configured file-type and amount rules. | Must | The route selected in the decision table is created for each tested rule. |
| FR-04 | The system shall display the current owner, approval level, status, and due date. | Must | An authorised user can see these four values for an assigned file. |
| FR-05 | The system shall allow an assigned approver to approve, reject, or return a file with a reason. | Must | Each action changes status and records the actor, time, and reason where required. |
| FR-06 | The system shall request and record a digital signature for an approval that requires signing. | Must | A signature request has a provider reference and a verifiable result status. |
| FR-07 | The system shall send reminders at the configured interval and escalate overdue items according to policy. | Must | A due item creates a reminder event; an overdue item creates an escalation event. |
| FR-08 | The system shall maintain an append-only audit history for creation, routing, viewing, approval, rejection, return, signature, reminder, and escalation events. | Must | Each event records actor/system, timestamp, event type, and file identifier. |
| FR-09 | The system shall allow authorised users to search and filter files by identifier, type, status, date, requester, and current owner. | Should | Each supported filter returns only matching records in test data. |
| FR-10 | The system shall provide reports for average approval time, open items, overdue items, and lost-file exceptions. | Should | Reports calculate from recorded workflow timestamps and show the reporting period. |

## 4. Non-functional requirements

Each NFR has a measurable target. The targets below are acceptance targets for the case; they are not measurements of an existing system.

| ID | Category | Requirement and measurable target | Priority |
|---|---|---|---|
| NFR-01 | Legal validity | The production signature method shall be approved in writing by the university’s authorised legal/compliance representative before release, and every signed approval shall retain the provider reference, signer identity, timestamp, and validation result. | Must |
| NFR-02 | Auditability | For 100% of test transactions, the audit record shall include file ID, event type, actor or system identity, timestamp, and previous/new status where a status changes. | Must |
| NFR-03 | Availability | During the agreed service window, monthly availability shall be at least 99.5%, excluding approved maintenance. | Must |
| NFR-04 | Performance | At least 95% of normal page requests shall complete within 3 seconds under the agreed pilot load. | Should |
| NFR-05 | Approval-time outcome | The system and configured workflow shall support an average approval time under 4 days for the measured reporting period. | Must |
| NFR-06 | Data-loss prevention | No submitted file shall be lost in acceptance testing; every submitted file shall be retrievable by its unique identifier. | Must |
| NFR-07 | Security | All authenticated sessions shall use the university-approved identity mechanism; unauthorised access attempts shall be denied and logged in 100% of security test cases. | Must |

## 5. External interfaces

- **User interface:** Browser-based screens for intake, inbox, file detail, approval, signature status, search, and reports.
- **Identity interface:** University-approved authentication source.
- **Signature interface:** Selected digital-signature provider or university signing service. The provider is not named in the case study.
- **Notification interface:** University-approved email or messaging service for reminders and escalations.

## 6. Data and state model summary

A file starts as **Draft**, moves to **Submitted**, then **In Review**, and may enter **Awaiting Signature** before **Approved**. It may instead move to **Rejected**, **Returned**, **Cancelled**, or **Archived**. Every transition must be recorded in the audit history.

## 7. Requirements elicitation and validation

The team will use questionnaires with administration staff and section officers, interviews with the Registrar and IT head, and prototype walkthroughs with senior officers. The walkthrough should focus on the inbox, approval action, signature step, and reminder message because these are the areas most likely to expose usability and policy problems.

A requirement is accepted when its owner confirms the wording, its MoSCoW priority is agreed, and at least one acceptance test is linked to it.

## 8. Traceability matrix

| Requirement | Test case(s) |
|---|---|
| FR-01 | TC-01, TC-02 |
| FR-02 | TC-03, TC-04 |
| FR-03 | TC-10 to TC-17 |
| FR-04 | TC-05 |
| FR-05 | TC-06, TC-07 |
| FR-06 | TC-08, TC-09 |
| FR-07 | TC-18, TC-19 |
| FR-08 | TC-20 |
| FR-09 | TC-21 |
| FR-10 | TC-22 |
| NFR-01 | TC-23 |
| NFR-02 | TC-20, TC-24 |
| NFR-03 | TC-25 |
| NFR-04 | TC-26 |
| NFR-05 | TC-27 |
| NFR-06 | TC-28 |
| NFR-07 | TC-29 |

## 9. Acceptance criteria

The top-three release is ready for Registrar acceptance when all Must requirements pass, no submitted file is unretrievable in acceptance testing, the legal/compliance approval for the signature method is recorded, the audit checks pass, and the measured average approval time is under 4 days for the agreed reporting period. Should requirements may be deferred only with written approval from the Registrar and IT head.
