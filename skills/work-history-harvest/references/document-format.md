# Work history document format

The format of `work-history-<employer>.md`, the document that the `work-history-harvest` skill writes and other skills read. Every skill that reads or writes the document keeps an identical copy of this file, and a test in the repository checks that the copies match: change them together.

## The document

One document holds the person's work at one employer. Its file name is `work-history-` followed by the employer's name in lowercase, with hyphens between the words: `work-history-contoso-logistics.md`. Work that belongs to no employer, such as courses, certificates, side projects and volunteering during a career break, goes in `work-history-independent.md`, with `n/a` as the employer.

The document is in English unless the person asked for another language. Its sections, in this order:

1. `# Work history: <Employer>`.
2. `## How to read this document`: the block in [The opening block](#the-opening-block), word for word. It lets a person or an AI assistant without this file use the document.
3. `## About this document`: the [header](#header).
4. One section per title the person held, newest first: `## <Title>, YYYY-MM to YYYY-MM`, or `YYYY-MM to now` while the person holds it. Each title gets its own section, promotions and role changes included, because profiles and CVs list each title as a position of its own. A record sits under the title the person held during its period; a record that spans two titles sits under the later one. `work-history-independent.md` has one section per kind instead, such as `## Courses and certificates` and `## Projects`.
5. `## Open questions`: the gaps the records leave, one line each, pointing to a record ID and the kind of source, such as "E-002, the release tickets: how much faster did releases get?". A question that a work system could still answer ends with "(before access ends)". A question the person put off ends with "(deferred)".

## Writing

The document is detailed and technical, written for a reader outside the employer: a recruiter, an interviewer, the person a year later. Write full sentences. Use the public names of technologies and methods where they fit (React, TypeScript, CI/CD, microservices, Scrum), and spell out what a reader might not know. Write no abbreviations of the employer's own, no internal jargon and no clipped notes. A record should make sense on its own.

## The opening block

`## How to read this document` holds exactly this text:

```markdown
This is a record of one person's work at one employer, collected from work systems, documents and the person's own answers, and checked for confidentiality. Anyone helping the person (a career tool, an AI assistant, the person a year from now) can use it as it is.

- **Records.** Each record, headed `### E-<number> <title>`, describes one body of work: a project, an initiative, a recurring duty, a credential, public work or recognition. It sits under the job title the person held at the time. Its fields: Type, Employer and title, Period, Problem, Action, Result (the challenge, what the person did, what changed), My role, Team, Technologies, Skills shown, Basis, Confidentiality and Status.
- **My role** sets the strongest verb a text built on the record may use. `led`: owned the outcome and directed others' work (led, drove, owned). `built`: did the core work personally (built, designed, wrote, automated). `contributed`: one of several people doing the work (contributed to, worked on, implemented part of). `supported`: reviewed, advised or unblocked others' work (reviewed, advised, supported). Credentials and recognition take `n/a`.
- **Team** is the size of the team the work happened in, the person included. It is not the number of people the person led.
- **Basis** says what backs the record. `verified`: artifacts such as merged merge requests, resolved tickets, written pages or a review document show the person's part and every figure. `mixed`: artifacts show the work, and the part the Basis names rests on the person's word. `self-reported`: the record rests on the person's word only. Before a self-reported claim goes into a CV or a profile, the person confirms they can explain it in a job interview.
- **Status.** `approved`: the person approved the record. `pending`: not approved yet; use it only to ask the person about it.
- **Confidentiality.** The text names no clients, partners or colleagues, no internal systems, services, repositories or code names, no ticket numbers or internal links, no code, and none of the employer's business figures. Keep it that way in everything made from this document, and follow the extra rules under "About this document". `generalized` in a record's Confidentiality field names the kind of detail removed, never the detail.
- **Reviewed by owner.** `no`: the person has not yet read the whole document, so treat it as a draft. `yes` with a date: the person read all of it and confirmed it on that date.
```

## Header

`## About this document` holds these lines, then three sub-sections:

```markdown
- Employer: Contoso Logistics
- What the employer does, in public words: logistics software for retailers
- Titles: Senior QA Engineer, 2023-04 to 2026-10; QA Engineer, 2021-03 to 2023-03
- Employment period: 2021-03 to 2026-10
- End of employment: role ended in a layoff
- Language of the records: English
- Reviewed by owner: no
- Next update: 2027-11-02
- Last record ID: E-012
```

- **Titles**: each official title with its period, newest first. When the person confirms a standard title of the same function and level for a position, write it first and the official one in brackets: "Backend Engineer (official title: Engineer II)".
- **Employment period**: `YYYY-MM to YYYY-MM`, or `YYYY-MM to now`.
- **End of employment**: the plain fact, in the person's words, only when they want it recorded, such as "role ended in a layoff". How broad a layoff was stays out unless the employer made it public. Empty while the job goes on.
- **Reviewed by owner**: `no`, or `yes, YYYY-MM-DD`. It turns to yes only when the person says they have read the whole document; approving single records does not count. A new record, or a change to an approved record, turns it back to `no`.
- **Next update**: one year after the latest run, while the person still works there; `none, employment ended` after the last harvest of an ended job.
- **Last record ID**: the last ID used, so that no ID is used twice.

### Sources covered

One row per source ever picked, with the period its data actually covers, which can be shorter than the period asked for: Claude Code keeps session transcripts about 30 days by default, and GitLab keeps activity events three years. A work system, such as Jira, GitLab or Claude Code, is one source however many runs or exports it took, so a later run moves its "Covered to" and "Harvested on" forward. Each document, such as one review cycle, a CV or a reference letter, is a source of its own and gets its own row.

```markdown
| Source | Covered from | Covered to | Harvested on | Notes |
|---|---|---|---|---|
| Jira tickets (export) | 2021-03 | 2026-10 | 2026-11-02 | assigned and reported tickets |
| Claude Code history | 2026-08 | 2026-10 | 2026-11-02 | transcripts reach back 30 days; prompt history from 2026-08 |
| GitLab merge requests | | | 2026-11-02 | skipped: the employer's settings block API access |
```

A skipped source keeps its row with the reason in clean words and empty dates, so that a later run knows to ask again.

### Harvest log

One row per run, oldest first. Run is `first harvest`, `update` or `interview`.

```markdown
| Date | Run | Sources | Period | Records added | Records updated |
|---|---|---|---|---|---|
| 2026-11-02 | first harvest | Jira export, old CV, performance review 2025 | 2021-03 to 2026-10 | E-001 to E-010 | none |
```

### Extra confidentiality rules

The person's own rules on top of the defaults, from their contract, NDA or termination agreement, in general words that name nothing secret, such as "no figures from the operations dashboard" or "the termination agreement itself stays confidential". "none" when the person has none.

## Record

```markdown
### E-007 Cut the nightly billing batch from five hours to 40 minutes
- Type: work
- Employer and title: Tailspin Toys, Backend Engineer (official title: Engineer II)
- Period: 2024-02 to 2024-06
- Problem: The nightly billing batch ran for about five hours and was sometimes still running when the support team started work in the morning.
- Action: Profiled the batch job, replaced row-by-row updates with set-based SQL queries, and split the run into parallel chunks by region, scheduled through Apache Airflow.
- Result: The batch finishes in about 40 minutes, and it has not run into working hours since.
- My role: led
- Team: 3 engineers
- Technologies: Python, PostgreSQL, Apache Airflow
- Skills shown: performance optimization; SQL; data pipelines
- Basis: mixed (pull requests and tickets show the work, checked 2026-10-30; run-time figures self-reported)
- Confidentiality: generalized (internal job and database names removed)
- Status: approved
```

### Fields

- **ID**: `E-` and three digits, in order of creation, unique within the document and never reused, even after a record is dropped. To cite a record from outside its document, write the employer part of the file name before the ID: `contoso-logistics E-004`.
- **Title**: one line, verb first, clean. It doubles as a draft bullet for a profile or a CV.
- **Type**: `work` (a project, initiative or recurring duty), `credential` (degree, certification, course), `public` (talk, article, open-source project, anything already public) or `recognition` (an award, or a theme of praise from reviews or a reference letter, paraphrased, naming who gave it only by relationship, such as manager or peer).
- **Employer and title**: the employer, and the title the person held during the record's period, as in the Titles line of the header. For contract work, the employer is the agency or the person's own business, never a client. For a credential or a personal project, `n/a`. An official title that holds a team or code name, such as "Squad Lead, Falcon", is generalized like any other text ("Squad Lead").
- **Period**: `YYYY-MM to YYYY-MM`, or `YYYY-MM to now`.
- **Problem / Action / Result**: the challenge, what the person did, and what changed. Write `unknown` where a part is missing; an unknown part becomes an open question.
- **My role**: `led`, `built`, `contributed`, `supported` or `n/a`, as the opening block defines them. Profiles and CVs take their verbs from it.
- **Team**: the team the work happened in, the person included, and partner teams by function ("worked with the data team"), never by name. A text says "led a team of N" only when the Action shows that the person directed those N people.
- **Technologies**: public names only. Many in-house tools share their names with public products; when a name could be an in-house tool, the person confirms it is the public product.
- **Skills shown**: the technical and interpersonal skills the work demonstrates, separated by semicolons.
- **Basis**: `verified`, `mixed` or `self-reported`, with the source types and the date of the check. A record is `verified` only when artifacts show its action and every figure in it; otherwise it is `mixed`, and the Basis names the self-reported part. Source types are words like "merge requests", "tickets", "pages", "performance review", "reference letter", "interview"; identifiers and links stay out.
- **Confidentiality**: `clean` (nothing needed changing) or `generalized` with the kind of detail removed ("client name removed"), never the detail itself.
- **Status**: `pending` until the person approves the record, then `approved`. A change to an approved record's content sets it back to `pending`.

### Verified or self-reported

A record is verified when an artifact shows the person's part: a merge request they authored and that was merged, a ticket they were assigned and resolved, a page they wrote, a review document or a reference letter that names the achievement. Counting artifacts is verification too ("34 merged merge requests in the checkout area"). Everything the person says, and every figure nobody measured, is self-reported. Claims from an old CV are self-reported until an artifact backs them. Self-reported records are welcome: their Basis tells a later reader which claims to confirm with the person.

## Reading the document

A skill that builds something from the document, such as a profile or a CV:

- takes claims only from `approved` records, and turns a `pending` record into a question for the person;
- when Reviewed by owner is `no`, tells the person the document is still a draft and suggests reading all of it first;
- uses the verb My role allows, the record's own figures with their qualifiers such as "about", and no scope or team size the record does not hold;
- follows the confidentiality rules of the opening block and the document's extra rules in everything it writes;
- leaves the document itself unchanged: new facts go into it through the `work-history-harvest` skill, which keeps the IDs, the header and the owner review right.
