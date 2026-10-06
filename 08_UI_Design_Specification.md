# UI design specification and screen set
## SignFlow — Digital Document Approval Workflow for a University

This document defines the proposed interface as a **static UI representation** for the project documentation. It is not a functional application. The accompanying PNG screens are high-fidelity desktop mockups with consistent spacing, readable labels, clear states, and sample records. Editable HTML/CSS source is included under `ui/source/`.

## 1. Design goals

- Make the next action obvious for users who work with approval files occasionally.
- Keep the inbox and file status visible without opening several screens.
- Reduce uncertainty around signatures, due dates, and returned files.
- Support assisted use for senior officers who are uncomfortable with computers.
- Use plain language and avoid hiding important state behind icons alone.

## 2. Information architecture

| Navigation item | Purpose | Primary users |
|---|---|---|
| Dashboard | Overview of open, overdue, and completed work | All authorised users |
| New file | Create and submit a file | Administration staff |
| My inbox | Review assigned files and take action | Section and senior officers |
| All files | Search and filter the file register | Administration, Registrar, audit |
| Reports | Approval-time, overdue, and exception measures | Registrar, IT head |
| Administration | Rules, reminder settings, users, and audit access | IT head, authorised administrators |

## 3. Screen inventory

| Screen | Main job | Key controls | Related requirements |
|---|---|---|---|
| UI-01 Dashboard | Show work at a glance | Metric cards, queue list, quick actions | FR-04, FR-07, FR-10 |
| UI-02 New file | Create a valid submission | File type, subject, amount, attachments, save/submit | FR-01, FR-02 |
| UI-03 My inbox | Decide on assigned work | Search, filters, approve, return, reject | FR-04, FR-05, FR-07 |
| UI-04 File detail | Explain status and history | Timeline, route, attachments, signature state | FR-06, FR-08 |
| UI-05 Reports | Monitor outcome and exceptions | Date range, metrics, export | FR-10, NFR-05, NFR-06 |

## 4. Screen specifications

### UI-01 Dashboard

The dashboard opens with a four-card summary: pending action, overdue, approved this month, and average approval time. A queue table shows the items requiring attention. The primary actions are “New file” and “View inbox”.

### UI-02 New file

The form begins with file type because it determines the remaining fields and route. Required fields are marked in text, not colour alone. The amount field is shown when relevant to the selected file type. The user can save a draft or submit after validation.

### UI-03 My inbox

The inbox is deliberately table-based. Each row includes file ID, type, subject, requester, current step, due date, and status. An overdue badge is paired with text and an icon. Opening a row leads to the file detail screen.

### UI-04 File detail

The detail page places the status and current owner at the top, followed by the approval route and an activity timeline. Signature state is shown separately so an approver can tell whether approval is waiting on a signing step or on another person.

### UI-05 Reports

The report screen provides the average approval time, completed volume, overdue count, and lost-file exceptions for the selected period. It should show the target alongside the result so a reader does not have to remember the target of under 4 days.

## 5. Component and interaction rules

- Use one primary action per screen. Secondary actions use neutral styling.
- Confirmation text must name the file ID and action, for example: “Approve PR-2026-0041?”
- Return and reject require a reason.
- Signature status uses text values: Pending, Validated, Invalid, or Provider error.
- Dates use a consistent university-approved format; the wireframes use `12 Sep 2026` as sample data only.
- Empty states explain what the user can do next.
- Validation errors appear beside the field and in a short summary at the top of the form.

## 6. Accessibility and usability notes

- Colour is supplementary; status also has a text label.
- Body text and controls should meet the university’s chosen contrast standard.
- All primary actions are reachable by keyboard in a logical order.
- Tables have clear column headings and a mobile fallback that stacks file attributes.
- Focus state is visible.
- Avoid time-limited actions; a user should be able to pause and return to a draft.
- Provide short onboarding guidance and an assisted-approval procedure for senior officers.

## 7. Sample data note

Names, IDs, dates, amounts, and statuses shown in the UI screens are sample values for visual explanation. They are not project records and should not be treated as measured results.

## 8. UI acceptance checklist

- A first-time user can locate the New file action from the dashboard.
- A user can identify the current owner and due date from the inbox.
- A return or rejection always exposes the reason field.
- A signed approval displays the signature state and validation result.
- A report places the under-4-day target beside the measured value.
- All screens use the same status vocabulary as the SRS state model.

## 9. Screen source and review note

The five screenshots are rendered from the shared stylesheet `ui/source/app.css` and the page sources `UI-01_Dashboard.html` through `UI-05_Reports.html`. The redesign uses a common sidebar, top search bar, spacing scale, status badges, button hierarchy, and card treatment across all screens. The screenshots are documentation artefacts only; the buttons, search fields, filters, and navigation links are visual representations rather than implemented behaviour.
