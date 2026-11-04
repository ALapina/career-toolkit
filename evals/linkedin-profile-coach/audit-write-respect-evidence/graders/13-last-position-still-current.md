---
type: llm
focus: { source: file, path: linkedin-profile/audit.md }
weight: 1
---

linkedin-profile/audit.md flags both of these problems with the Contoso Logistics position. In the LinkedIn export it reads 'QA Engineer', from Mar 2021 with no end date; progress.md and work-history/work-history-contoso-logistics.md give 'Senior QA Engineer', employed from 2021-03 to 2026-10.

- The position still shows as current although the job ended in 2026-10. The audit rates it 'needs work' with priority high.
- The title on the profile, QA Engineer, is a level below Senior QA Engineer. The audit flags the difference and leaves it to the person whether a promotion explains it, for example by asking, or by proposing one position per title in case there was one.

The rules behind this check are `career-break-1`, `experience-1` and `experience-2`. The audit need not cite these three by number.
