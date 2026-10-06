# Estimation sheet
## SignFlow — Digital Document Approval Workflow for a University

## 1. Supplied inputs

- Monthly file volume = 2,000.
- Purchase requests = 700 per month.
- Leave = 600 per month.
- Event approvals = 300 per month.
- Circulars = 150 per month.
- Others = 250 per month.
- Workflow design per file type = 3 days.
- Configuration per file type = 4 days.
- Testing per file type = 2 days.
- Total file types = 12.

The per-type effort is treated as person-days. The case does not provide rates, team size, calendar availability, or productivity adjustments, so no cost or calendar promise is calculated.

## 2. Volume covered by the top three

Top three types are purchase requests, leave, and event approvals.

\[
700 + 600 + 300 = 1,600\text{ files/month}
\]

\[
\text{Coverage} = \frac{1,600}{2,000} \times 100 = 80\%
\]

The top-three option covers 80% of monthly volume.

## 3. Effort per file type

\[
\text{Effort per type} = 3 + 4 + 2 = 9\text{ person-days}
\]

Breakdown:

| Work | Days per type |
|---|---:|
| Workflow design | 3 |
| Configuration | 4 |
| Testing | 2 |
| **Total** | **9** |

## 4. Option A — all 12 file types

\[
\text{Design} = 12 \times 3 = 36\text{ person-days}
\]

\[
\text{Configuration} = 12 \times 4 = 48\text{ person-days}
\]

\[
\text{Testing} = 12 \times 2 = 24\text{ person-days}
\]

\[
\text{Total} = 36 + 48 + 24 = 108\text{ person-days}
\]

| Work | Formula | Effort |
|---|---|---:|
| Workflow design | 12 × 3 | 36 person-days |
| Configuration | 12 × 4 | 48 person-days |
| Testing | 12 × 2 | 24 person-days |
| **Total** | 36 + 48 + 24 | **108 person-days** |

## 5. Option B — top three file types

\[
\text{Design} = 3 \times 3 = 9\text{ person-days}
\]

\[
\text{Configuration} = 3 \times 4 = 12\text{ person-days}
\]

\[
\text{Testing} = 3 \times 2 = 6\text{ person-days}
\]

\[
\text{Total} = 9 + 12 + 6 = 27\text{ person-days}
\]

| Work | Formula | Effort |
|---|---|---:|
| Workflow design | 3 × 3 | 9 person-days |
| Configuration | 3 × 4 | 12 person-days |
| Testing | 3 × 2 | 6 person-days |
| **Total** | 9 + 12 + 6 | **27 person-days** |

## 6. Comparison and recommendation

| Option | Types | Monthly volume covered | Supplied effort |
|---|---:|---:|---:|
| All types | 12 | 2,000 files, assuming the listed categories account for the full volume | 108 person-days |
| Top three | 3 | 1,600 files | 27 person-days |

The top-three option uses 81 fewer person-days than the all-types option:

\[
108 - 27 = 81\text{ person-days}
\]

The recommendation is to start with the top three. It covers 80% of monthly files and limits the first configuration and testing effort to 27 person-days. The Registrar’s all-types goal should remain a second release decision, informed by pilot results and the remaining file-type rules.

## 7. Assumptions and confidence

- “Day” means person-day, not elapsed calendar day.
- Effort scales linearly by file type; shared platform work is not separately provided in the case.
- The 12 file types are treated as the denominator for the all-types calculation.
- No contingency, rework, procurement, training, migration, or integration effort is added because the case gives no figures for them.
- Confidence is **moderate for the arithmetic** and **low-to-moderate for the delivery estimate**. The arithmetic follows supplied inputs. The delivery estimate may change when the approval hierarchy, signature method, data quality, and user availability are confirmed.

The result is an estimate because it depends on assumptions and incomplete project information. It is not a promise of elapsed delivery time or staffing cost.
