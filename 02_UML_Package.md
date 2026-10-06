# UML package
## SignFlow — Digital Document Approval Workflow for a University

The diagrams use the same core objects and states throughout: `StaffUser`, `File`, `ApprovalRoute`, `ApprovalStep`, `DigitalSignature`, `Reminder`, and `AuditEvent`. The routing service decides the route; the signature service handles signing and validation.

## 1. Use-case diagram

```mermaid
flowchart LR
  Staff([Administration staff])
  Officer([Section officer])
  Senior([Senior officer])
  Registrar([Registrar])
  Legal([Legal/compliance representative])
  IdP[[University identity source]]
  Sig[[Digital signature service]]
  Notify[[Notification service]]

  subgraph SignFlow
    UC1((Create and submit file))
    UC2((Route file))
    UC3((Review file))
    UC4((Approve / reject / return))
    UC5((Sign approval))
    UC6((Track status and audit))
    UC7((Receive reminder / escalation))
    UC8((Run reports))
    UC9((Approve signature method))
  end

  Staff --> UC1
  Staff --> UC6
  Officer --> UC3
  Officer --> UC4
  Senior --> UC3
  Senior --> UC4
  Senior --> UC5
  Registrar --> UC8
  Registrar --> UC6
  Legal --> UC9
  UC1 --> UC2
  UC2 --> UC3
  UC4 --> UC5
  UC5 --- Sig
  UC1 --- IdP
  UC3 --- IdP
  UC7 --- Notify
  UC9 --- Sig
```

## 2. Class diagram

```mermaid
classDiagram
  class StaffUser {
    +userId: String
    +name: String
    +role: String
    +authenticate()
  }
  class File {
    +fileId: String
    +fileType: String
    +amount: Decimal
    +status: FileStatus
    +submittedAt: DateTime
    +submit()
    +changeStatus()
  }
  class ApprovalRoute {
    +routeId: String
    +fileType: String
    +buildRoute()
  }
  class ApprovalStep {
    +stepNo: Integer
    +role: String
    +dueAt: DateTime
    +decision: String
    +recordDecision()
  }
  class DigitalSignature {
    +signatureId: String
    +providerReference: String
    +validationStatus: String
    +request()
    +validate()
  }
  class Reminder {
    +reminderId: String
    +intervalDays: Integer
    +sentAt: DateTime
    +send()
  }
  class AuditEvent {
    +eventId: String
    +eventType: String
    +actorId: String
    +occurredAt: DateTime
    +record()
  }
  class RoutingService {
    +route(file): ApprovalRoute
  }
  class SignatureService {
    +requestSignature(step): DigitalSignature
    +validate(signature): Boolean
  }
  class NotificationService {
    +sendReminder(file, step)
    +escalate(file, step)
  }

  StaffUser "1" --> "0..*" File : submits / handles
  File "1" *-- "1" ApprovalRoute
  ApprovalRoute "1" *-- "1..*" ApprovalStep
  ApprovalStep "0..1" --> "1" DigitalSignature : may require
  File "1" o-- "0..*" Reminder
  File "1" o-- "1..*" AuditEvent
  RoutingService ..> ApprovalRoute : creates
  SignatureService ..> DigitalSignature : manages
  NotificationService ..> Reminder : creates
```

## 3. Sequence diagram — route a file for digital approval

```mermaid
sequenceDiagram
  actor Staff as Administration staff
  participant UI as SignFlow UI
  participant FileSvc as File service
  participant Router as Routing service
  participant Rules as Routing rules
  participant Audit as Audit service
  participant Notify as Notification service

  Staff->>UI: Submit file(fileType, amount, attachments)
  UI->>FileSvc: validate and create file
  FileSvc->>Rules: check(fileType, amount)
  Rules-->>FileSvc: route roles and approval levels
  FileSvc->>Router: create route(file, roles)
  Router-->>FileSvc: ApprovalRoute with steps
  FileSvc->>Audit: record Submitted and Routed events
  Audit-->>FileSvc: event IDs
  FileSvc->>Notify: notify first approver
  Notify-->>FileSvc: notification result
  FileSvc-->>UI: file ID, current owner, due date
  UI-->>Staff: show routed status
```

## 4. Activity diagram

```mermaid
flowchart TD
  A([Start]) --> B[Create draft]
  B --> C{Mandatory data valid?}
  C -- No --> D[Show errors]
  D --> B
  C -- Yes --> E[Submit file]
  E --> F[Apply file-type and amount rules]
  F --> G[Create approval route]
  G --> H[Record audit event]
  H --> I[Notify current approver]
  I --> J{Decision received?}
  J -- No --> K{Due date passed?}
  K -- No --> J
  K -- Yes --> L[Send reminder / escalation]
  L --> J
  J -- Return --> M[Return to requester]
  M --> B
  J -- Reject --> N[Record rejection]
  J -- Approve, signature required --> O[Request digital signature]
  O --> P{Signature valid?}
  P -- No --> Q[Raise exception]
  Q --> J
  P -- Yes --> R[Record approval]
  J -- Approve, no signature --> R
  R --> S{More approval steps?}
  S -- Yes --> I
  S -- No --> T[Mark approved]
  T --> U[Notify requester]
  U --> V([End])
  N --> V
```

## 5. State diagram for a file

```mermaid
stateDiagram-v2
  [*] --> Draft
  Draft --> Submitted: submit()
  Submitted --> InReview: route created
  InReview --> AwaitingSignature: approval accepted and signing required
  AwaitingSignature --> InReview: signature invalid / exception
  AwaitingSignature --> Approved: signature validated
  InReview --> Approved: final approval without signature
  InReview --> Returned: return(reason)
  Returned --> Draft: requester edits
  InReview --> Rejected: reject(reason)
  Submitted --> Cancelled: cancel()
  Approved --> Archived: retention action
  Rejected --> Archived: retention action
  Cancelled --> Archived: retention action
```

## 6. Consistency and design justification

### Cohesion

- `RoutingService` contains route selection and route creation rules.
- `SignatureService` contains signature requests and validation results.
- `NotificationService` contains reminders and escalations.
- `AuditService` contains event recording.
- `FileService` owns file lifecycle changes and calls the specialist services.

Each service has one main reason to change. For example, changing the signature provider should not require changes to file-state rules.

### Coupling

Routing and signing communicate through `ApprovalStep` and a signature result. The routing service does not call provider-specific signing functions. The signature service does not decide whether a file is a purchase request or leave request. Their dependency is therefore a small domain interface rather than a shared implementation.

The sequence diagram follows the class diagram: the file service asks the rules component for roles, passes them to the routing service, records audit events, and asks notification service to contact the first approver. The state diagram uses the same approval and signature outcomes shown in the activity diagram.
