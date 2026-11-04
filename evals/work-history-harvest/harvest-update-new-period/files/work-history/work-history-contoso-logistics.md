# Work history: Contoso Logistics

## How to read this document

This is a record of one person's work at one employer, collected from work systems, documents and the person's own answers, and checked for confidentiality. Anyone helping the person (a career tool, an AI assistant, the person a year from now) can use it as it is.

- **Records.** Each record, headed `### E-<number> <title>`, describes one body of work: a project, an initiative, a recurring duty, a credential, public work or recognition. It sits under the job title the person held at the time. Its fields: Type, Employer and title, Period, Problem, Action, Result (the challenge, what the person did, what changed), My role, Team, Technologies, Skills shown, Basis, Confidentiality and Status.
- **My role** sets the strongest verb a text built on the record may use. `led`: owned the outcome and directed others' work (led, drove, owned). `built`: did the core work personally (built, designed, wrote, automated). `contributed`: one of several people doing the work (contributed to, worked on, implemented part of). `supported`: reviewed, advised or unblocked others' work (reviewed, advised, supported). Credentials and recognition take `n/a`.
- **Team** is the size of the team the work happened in, the person included. It is not the number of people the person led.
- **Basis** says what backs the record. `verified`: artifacts such as merged merge requests, resolved tickets, written pages or a review document show the person's part and every figure. `mixed`: artifacts show the work, and the part the Basis names rests on the person's word. `self-reported`: the record rests on the person's word only. Before a self-reported claim goes into a CV or a profile, the person confirms they can explain it in a job interview.
- **Status.** `approved`: the person approved the record. `pending`: not approved yet; use it only to ask the person about it.
- **Confidentiality.** The text names no clients, partners or colleagues, no internal systems, services, repositories or code names, no ticket numbers or internal links, no code, and none of the employer's business figures. Keep it that way in everything made from this document, and follow the extra rules under "About this document". `generalized` in a record's Confidentiality field names the kind of detail removed, never the detail.
- **Reviewed by owner.** `no`: the person has not yet read the whole document, so treat it as a draft. `yes` with a date: the person read all of it and confirmed it on that date.

## About this document

- Employer: Contoso Logistics
- What the employer does, in public words: logistics software for retailers
- Titles: Senior QA Engineer, 2021-03 to now
- Employment period: 2021-03 to now
- End of employment: 
- Language of the records: English
- Reviewed by owner: yes, 2025-11-20
- Next update: 2026-11-03
- Last record ID: E-005

### Sources covered

| Source | Covered from | Covered to | Harvested on | Notes |
|---|---|---|---|---|
| Jira tickets (export) | 2021-03 | 2025-10 | 2025-11-03 | assigned and reported tickets |
| Performance review 2025 | 2025-01 | 2025-10 | 2025-11-03 | goals, manager and peer feedback |

### Harvest log

| Date | Run | Sources | Period | Records added | Records updated |
|---|---|---|---|---|---|
| 2025-11-03 | first harvest | Jira export, performance review 2025 | 2021-03 to 2025-10 | E-001 to E-005 | none |

### Extra confidentiality rules

- No figures from the operations dashboard, such as order or parcel volumes.

## Senior QA Engineer, 2021-03 to now

### E-001 Cut flaky end-to-end test failures from 15% to under 2% of nightly runs
- Type: work
- Employer and title: Contoso Logistics, Senior QA Engineer
- Period: 2025-01 to 2025-09
- Problem: The nightly end-to-end runs of the checkout test suite failed on about 15% of nights for reasons unrelated to code changes, so the team had stopped trusting a failed run.
- Action: Traced the failures to test accounts shared between parallel workers and to timeouts that were too short, gave each parallel worker its own test accounts, and built a weekly flakiness report from the continuous integration results.
- Result: Flaky failures fell to 1.8% of nightly runs by September 2025, and the team uses a passing nightly run as a release criterion again.
- My role: led
- Team: 6 engineers
- Technologies: Playwright, TypeScript, GitLab CI
- Skills shown: test automation; root-cause analysis; quality process
- Basis: verified (performance review and tickets, checked 2025-11-03)
- Confidentiality: generalized (internal test suite name removed)
- Status: approved

### E-002 Introduced consumer-driven contract tests between a core service and a retail client's integration
- Type: work
- Employer and title: Contoso Logistics, Senior QA Engineer
- Period: 2025-06 to 2025-10
- Problem: Changes to the API of a core backend service broke a retail client's integration in production twice in one quarter.
- Action: Introduced consumer-driven contract tests with Pact for the order and tracking endpoints of the service, and added them to the continuous integration pipeline.
- Result: 42 contract tests caught 6 breaking changes before release.
- My role: built
- Team: 2 QA engineers, working with the service's developers
- Technologies: Pact, TypeScript, GitLab CI
- Skills shown: API testing; contract testing; CI/CD
- Basis: verified (performance review and tickets, checked 2025-11-03)
- Confidentiality: generalized (client and service names removed)
- Status: approved

### E-003 Moved part of the regression suite from Selenium to Playwright
- Type: work
- Employer and title: Contoso Logistics, Senior QA Engineer
- Period: 2023-09 to 2024-04
- Problem: The Selenium regression suite took 70 minutes to run and broke on most changes to the user interface.
- Action: Rewrote the shipment-tracking tests in Playwright, as part of a migration that three QA engineers shared.
- Result: unknown
- My role: contributed
- Team: 3 QA engineers
- Technologies: Playwright, Selenium, TypeScript, Java
- Skills shown: test automation; test framework migration
- Basis: verified (tickets, checked 2025-11-03)
- Confidentiality: clean
- Status: approved

### E-004 Mentored two junior QA engineers until they ran regression cycles on their own
- Type: work
- Employer and title: Contoso Logistics, Senior QA Engineer
- Period: 2025-02 to 2025-10
- Problem: Two newly hired junior QA engineers had no experience of testing logistics software.
- Action: Paired with them on regression cycles, reviewed their test cases, and wrote an onboarding checklist for new QA engineers.
- Result: Both ran release regression cycles on their own within six months.
- My role: supported
- Team: 2 junior QA engineers
- Technologies: none specific
- Skills shown: mentoring; onboarding
- Basis: verified (performance review, checked 2025-11-03)
- Confidentiality: generalized (names removed)
- Status: approved

### E-005 Found 9 defects in a new returns flow before user acceptance testing
- Type: work
- Employer and title: Contoso Logistics, Senior QA Engineer
- Period: 2025-10
- Problem: A new returns flow had to be ready for user acceptance testing within two weeks.
- Action: Ran structured exploratory testing sessions on the flow and reported each defect with steps to reproduce it.
- Result: 9 defects were found and fixed before user acceptance testing.
- My role: built
- Team: 1 QA engineer and 4 developers
- Technologies: exploratory testing
- Skills shown: exploratory testing; risk analysis
- Basis: verified (tickets, checked 2025-11-03)
- Confidentiality: clean
- Status: approved

## Open questions

- E-003, the tickets: roughly how much faster did the migrated part of the suite run?
