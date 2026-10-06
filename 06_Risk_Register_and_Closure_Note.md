# Risk register and closure note
## SignFlow — Digital Document Approval Workflow for a University

## 1. Scoring method

Probability and impact use a 1–5 scale. Exposure is:

\[
\text{Exposure} = \text{Probability} \times \text{Impact}
\]

| Score | Meaning |
|---:|---|
| 1 | Very low |
| 2 | Low |
| 3 | Medium |
| 4 | High |
| 5 | Very high |

## 2. Probability-impact matrix

| Impact \ Probability | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| 5 | 5 | 10 | 15 | 20 | 25 |
| 4 | 4 | 8 | 12 | 16 | 20 |
| 3 | 3 | 6 | 9 | 12 | 15 |
| 2 | 2 | 4 | 6 | 8 | 10 |
| 1 | 1 | 2 | 3 | 4 | 5 |

## 3. Exposure-ranked risk register

| ID | Risk | P | I | Exposure | Response | Owner |
|---|---|---:|---:|---:|---|---|
| R1 | Senior officers resist digital approvals, slowing adoption and keeping work on paper. | 4 | 4 | 16 | Pilot with assisted use, short walkthroughs, and an escalation path; measure adoption and approval time. | Registrar |
| R2 | The selected digital-signature method is not accepted by legal/compliance. | 3 | 5 | 15 | Obtain written approval before release; test validation and retain provider evidence; keep a controlled fallback process. | Legal/compliance representative |
| R3 | Incorrect routing by file type or amount sends work to the wrong approver. | 3 | 5 | 15 | Approve a decision table, test each band and boundary, require business sign-off, and monitor exceptions. | IT head and section officers |
| R4 | Approval rules are incomplete for some of the 12 file types. | 4 | 3 | 12 | Start with the top three, maintain an interim register for other types, and baseline remaining rules. | Business analyst |
| R5 | Poor scans or missing attachments cause rework and delay. | 3 | 3 | 9 | Validate metadata and attachment presence at intake; show clear correction messages. | Administration lead |
| R6 | Reminder or notification failure leaves files waiting without visibility. | 3 | 3 | 9 | Log notification outcomes, retry transient failures, and expose overdue items in reports. | Workflow developer |
| R7 | Audit records are incomplete or can be altered. | 2 | 5 | 10 | Use append-only event handling, test 100% required fields, and restrict audit administration. | IT head |
| R8 | The under-4-day target is missed because queue ownership is unclear. | 3 | 4 | 12 | Track phase metrics, assign owners, and escalate at the thresholds in the monitoring plan. | Registrar and section officers |

## 4. RMMM for the top three risks

### R1 — Resistance from senior officers

- **Risk reduction:** include senior officers in prototype walkthroughs; simplify the approval screen; provide assisted onboarding.
- **Monitoring:** track the share of approvals completed digitally, returned files, help requests, and approval time by office.
- **Management:** if an officer cannot complete a digital approval, use the approved assisted process and record the reason; the Registrar decides whether additional training or policy action is required.
- **Owner:** Registrar.

### R2 — Legal validity of digital signatures

- **Risk reduction:** document the signature method, identity binding, validation response, timestamp, and retention behaviour; obtain written legal/compliance approval.
- **Monitoring:** check signature validation status and provider errors in every test cycle and pilot report.
- **Management:** stop release of signature-required workflows if approval is missing or validation fails; use the controlled paper fallback until the issue is resolved.
- **Owner:** Legal/compliance representative.

### R3 — Incorrect routing

- **Risk reduction:** approve routing rules with section officers; represent them as a decision table; include lower-bound, threshold, and upper-bound tests.
- **Monitoring:** review exception-queue entries, returned files, reassignment events, and route-related defects after each reporting period.
- **Management:** freeze the affected rule, correct it, rerun impacted tests, and obtain IT head and business-owner approval before reactivation.
- **Owner:** IT head and section officers.

## 5. Issue log

Problems that have already occurred are kept separate from future risks. The source brief does not provide an executed project issue list, so these are the known case issues that must be tracked at initiation.

| Issue ID | Current issue | Impact | Immediate action | Owner | Status |
|---|---|---|---|---|---|
| I-01 | Physical files are lost during office-to-office movement. | Records cannot be located; approval is delayed. | Record every submitted digital file by unique ID and reconcile intake. | IT head and administration lead | Open at project start |
| I-02 | Average approval takes 12 days. | Current process misses the target by 8 days or more. | Measure time by phase and review queues after each reporting period. | Registrar | Open at project start |
| I-03 | Some senior officers are uncomfortable with computers. | Digital adoption may be slow. | Schedule prototype walkthroughs and assisted onboarding. | Registrar | Open at project start |
| I-04 | Scope disagreement exists between all-types digitisation and a top-three start. | Project may expand before rules are understood. | Use the 80% coverage and 27 vs 108 person-day comparison for a staged decision. | Registrar and IT head | Decision required |

## 6. Closure note

### 6.1 Closure conditions

The SignFlow release can be closed when:

1. The agreed release scope and all Must requirements have acceptance evidence.
2. The signature method has written legal/compliance approval.
3. The test plan has no open critical defect.
4. Every submitted acceptance-test file is retrievable.
5. Audit records meet the required field-completeness target.
6. The measured approval-time report is under 4 days for the agreed reporting period, or the Registrar records an approved corrective-action plan.
7. Residual risks have owners and review dates.

### 6.2 Lessons learned

- A staged release is easier to govern when the high-volume file types are clearly identified. The top three account for 80% of monthly volume.
- Routing rules need business-owner review before configuration is treated as complete.
- Signature validity is a release gate, not a detail to be checked after implementation.
- Senior-officer walkthroughs should happen before UAT because usability issues can affect adoption and approval time.
- Approval-time reporting should be designed with the workflow so the project can see delays by phase rather than relying on anecdotal complaints.

### 6.3 Handover checklist

| Handover item | Evidence |
|---|---|
| Approved SRS and UML package | Baseline files and review record |
| Configured routing rules | Signed decision table |
| Signature method | Legal/compliance approval and provider validation evidence |
| Test and defect evidence | Completed test log and retest results |
| Operations guide | User, assisted-use, and escalation instructions |
| Metrics ownership | Named report owner and reporting frequency |
| Residual risks/issues | Updated register with owners |

### 6.4 Closure decision

**Decision:** Pending final acceptance evidence.  
**Registrar:** ____________________  
**IT head:** ____________________  
**Legal/compliance representative:** ____________________  
**Date:** ____________________
