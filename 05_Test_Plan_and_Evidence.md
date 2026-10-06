# Test plan and evidence
## SignFlow — Digital Document Approval Workflow for a University

## 1. Test objectives

The test effort checks that files are routed correctly, approval actions are recorded, signatures are handled through the selected provider, reminders work, and no submitted file becomes unretrievable. The decision table focuses on file type and amount because those values drive routing.

## 2. Test levels and entry/exit criteria

**Levels:** unit/configuration tests, integration tests, system tests, security and audit checks, performance checks, and user acceptance testing.

**Entry criteria:** approved requirements baseline, configured top-three rules, test users, test signature credentials or sandbox, and test data.

**Exit criteria:** all Must tests pass; no open critical defect; legal/signature and audit checks pass; lost-file check passes; failed tests have an owner and retest result.

## 3. Boundary-value analysis

The brief asks for BVA of approval-level count and reminder interval. Exact allowed ranges are not supplied, so the following are explicit validation assumptions to be confirmed during requirements review.

### 3.1 Approval-level count

**Assumption for test design:** allowed range is 1 to 10 inclusive.

| Test ID | Input | Expected result |
|---|---:|---|
| BVA-AL-01 | 0 | Reject; below minimum |
| BVA-AL-02 | 1 | Accept; minimum valid value |
| BVA-AL-03 | 2 | Accept; just above minimum |
| BVA-AL-04 | 9 | Accept; just below maximum |
| BVA-AL-05 | 10 | Accept; maximum valid value |
| BVA-AL-06 | 11 | Reject; above maximum |

### 3.2 Reminder interval

**Assumption for test design:** allowed range is 1 to 30 days inclusive.

| Test ID | Input | Expected result |
|---|---:|---|
| BVA-RI-01 | 0 days | Reject; below minimum |
| BVA-RI-02 | 1 day | Accept; minimum valid value |
| BVA-RI-03 | 2 days | Accept; just above minimum |
| BVA-RI-04 | 29 days | Accept; just below maximum |
| BVA-RI-05 | 30 days | Accept; maximum valid value |
| BVA-RI-06 | 31 days | Reject; above maximum |

If the Registrar approves different limits, these cases should be updated before execution rather than silently changing the expected result.

## 4. Equivalence classes

| Field | Valid classes | Invalid classes |
|---|---|---|
| File type | Purchase request, leave, event approval, configured other type | Blank, unsupported type |
| Amount | Zero or positive amount where applicable; amount in a configured band | Negative, non-numeric, missing where mandatory |
| Approval-level count | Integer 1–10 (assumption) | 0, 11+, decimal, blank, text |
| Reminder interval | Integer 1–30 days (assumption) | 0, 31+, decimal, blank, text |
| Signature result | Validated, pending | Invalid, expired, provider error |

## 5. Decision table for routing

The case does not provide exact amount thresholds or role names. The table below therefore shows the structure required for the rules; the threshold labels are configuration placeholders and must be replaced by the approved university values before release.

| Rule | File type | Amount condition | Expected route |
|---|---|---|---|
| R1 | Purchase request | Low band | Section officer → authorised approver |
| R2 | Purchase request | High band | Section officer → senior officer → authorised approver |
| R3 | Leave | Any configured amount / no amount | Section officer → senior officer |
| R4 | Event approval | Low band | Section officer → event approver |
| R5 | Event approval | High band | Section officer → senior officer → event approver |
| R6 | Unsupported/other | Any | Exception queue; no automatic approval route |

**Decision-table tests:** TC-10 through TC-15 cover R1–R6. TC-16 checks a boundary just below an approved threshold, and TC-17 checks the threshold and just above it after the Registrar supplies the actual values.

## 6. Test cases

| ID | Test | Expected result |
|---|---|---|
| TC-01 | Create valid purchase request with attachment | Unique file ID and Draft status are created. |
| TC-02 | Submit valid leave file | File moves to Submitted and is retrievable by ID. |
| TC-03 | Submit without file type | Submission is rejected with a field-level error. |
| TC-04 | Submit with unsupported attachment metadata | Submission is rejected and no route is created. |
| TC-05 | Open assigned inbox item | Current owner, level, status, and due date are shown. |
| TC-06 | Approve a review step | Decision, actor, timestamp, and next state are recorded. |
| TC-07 | Return a file with reason | File moves to Returned and requester sees the reason. |
| TC-08 | Request signature | Signature provider reference and Pending status are stored. |
| TC-09 | Receive valid signature result | Signature becomes Validated and approval continues. |
| TC-10 | Purchase request in low amount band | Route matches R1. |
| TC-11 | Purchase request in high amount band | Route matches R2. |
| TC-12 | Leave file | Route matches R3. |
| TC-13 | Event approval in low amount band | Route matches R4. |
| TC-14 | Event approval in high amount band | Route matches R5. |
| TC-15 | Unsupported file type | File enters exception queue under R6. |
| TC-16 | Amount immediately below approved threshold | Lower-band route is selected. |
| TC-17 | Amount at and immediately above approved threshold | Approved threshold route is selected and no ambiguity exists. |
| TC-18 | Reminder interval reached | Reminder event is created and notification is sent. |
| TC-19 | Due date exceeded | Escalation event is created for the configured owner. |
| TC-20 | Complete a file lifecycle | Audit contains all required events and status changes. |
| TC-21 | Search by ID, type, status, owner | Results contain only matching files. |
| TC-22 | Generate approval-time report | Report includes period, average, open, overdue, and exception values. |
| TC-23 | Validate signature method approval record | Written legal/compliance approval is present before release. |
| TC-24 | Inspect audit records for all test transactions | 100% contain required fields. |
| TC-25 | Run availability measurement in agreed window | Monthly result meets 99.5% target, excluding approved maintenance. |
| TC-26 | Run response-time sample | At least 95% of normal page requests complete within 3 seconds. |
| TC-27 | Calculate approval-time result | Average is under 4 days for the agreed reporting period. |
| TC-28 | Retrieve every submitted test file | Zero submitted files are unretrievable. |
| TC-29 | Attempt unauthorised access | Access is denied and the attempt is logged. |

## 7. Defect log and example evidence

The case does not provide an executed test log. The table below is a compact evidence template with example entries to show how DRE and defect density are calculated. Replace the example counts with actual execution results before claiming project metrics.

| Defect ID | Found in | Severity | Description | Status |
|---|---|---|---|---|
| D-01 | Integration test | High | High-band purchase request selected the low-band route. | Closed and retested |
| D-02 | System test | Medium | Reminder was sent one day late at the configured boundary. | Closed and retested |
| D-03 | UAT | Medium | Returned file did not show the return reason in requester view. | Closed and retested |
| D-04 | UAT | High | Signature validation failure left the file looking approved. | Closed and retested |
| D-05 | UAT | Low | Search by current owner used case-sensitive matching. | Closed and retested |

## 8. Metrics

### 8.1 Defect removal efficiency

Using the five example defects above:

- Defects found before release = 5.
- Defects found after release = 0 in this illustrative dataset.

\[
DRE = \frac{\text{defects found before release}}{\text{defects found before release} + \text{defects found after release}} \times 100
\]

\[
DRE = \frac{5}{5 + 0} \times 100 = 100\%
\]

This 100% is an example based on the table, not a measured production result.

### 8.2 Defect density

**Assumption for this evidence template:** 12 file-type configurations are the size unit because the case supplies 12 file types and no lines-of-code or function-point count.

\[
\text{Defect density} = \frac{5\text{ defects}}{12\text{ file-type configurations}} = 0.4167\text{ defects/configuration}
\]

Report the unit explicitly. Do not compare this number with a LOC-based defect-density benchmark without converting the denominator.

## 9. Evidence to retain

- Test execution record with tester, environment, date, input, expected result, actual result, and status.
- Screenshots or exports for route selection and audit history.
- Signature provider validation response and legal/compliance approval.
- Reminder and escalation notification records.
- Approval-time report and lost-file reconciliation.
- Defect retest results and release decision.
