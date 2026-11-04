# Setup

The first run for an employer. Creates the folder and the document, records the employment facts, and settles the confidentiality rules before any source is read.

**Opening questions.** On a first run, your first reply is the [intro](intro.md) followed by these questions as one numbered list, one line each, so the person can answer in one go; explain a term only where the person needs it to answer:

- employer, job titles and the period of each, and whether the job has ended or when it ends;
- whether they can still reach work systems, and which documents they have (old CV, reviews, certificates);
- whether you may create the folder (propose `~/work-history/`, or say how light mode works);
- whether they have an NDA or a confidentiality clause to give you, and which names must never appear.

Ask the rest as each step comes up. When the person already has a folder from an earlier employer, skip step 1 and the parts of step 4 already settled.

1. **Create the folder.**
   - Full mode: propose `~/work-history/` and create it once the person agrees. Check that it is not inside a git repository: run `git -C <parent folder> rev-parse --is-inside-work-tree` on the folder that will hold it; it prints `true` inside a repository. If it does, pick another folder, so the files can never end up in a commit. Create `local-only/` inside it, and copy `progress.md` from the skill's `templates/` folder.
   - Light mode: create the same in a working folder, without `local-only/`, and hand it back as the first ZIP ([Modes](../SKILL.md#modes)). Ask the person to make one folder for this work on their own computer, with a `local-only/` folder inside it: the ZIPs go in the folder, and every employer document they gather, the NDA clauses and `confidential-terms.txt` go in `local-only/`.

   Done when the folder, `local-only/` and `progress.md` exist outside any git repository, or, in light mode, the person has the first ZIP and has made the folder.

2. **Ask about the computer.** If it belongs to the employer and goes back when the person leaves, write that in `progress.md`. The plan then includes copying the document, after the final check, to personal storage before the last day.

   Done when `progress.md` says whether the computer goes back.

3. **Create the document** `work-history-<employer>.md` from `templates/work-history.md`, named as [document format](document-format.md) says, and fill its About section:
   - the employer, and what it does in public words (ask when you cannot tell from public knowledge);
   - every official title with the month and year it began, promotions and role changes included; when a title is internal or unusual, also ask what the role did and at what level, so a profile can later name a standard title of the same function and level;
   - the employment period, and in `progress.md` the employment end date ("none yet" while the job goes on) and the day access to work systems ends, if known;
   - "End of employment" only when the job has ended and the person wants the plain fact recorded.

   Leave Reviewed by owner at `no`. Next update and the Harvest log are filled at the end of the first run.

   Done when the document exists with its opening block and every About line holds a value, "unknown" included.

4. **Settle the confidentiality rules.** The intro's "What I never save" gives the person the short form of the clean and leave-out lists. Show the full lists from `SKILL.md` when the person asks for them or brings rules of their own. Then:
   - **NDA clauses.** When the person gives clauses from an NDA, a contract or a termination agreement, give the disclosures of [harvest](harvest.md) step 1 first and wait for their yes, then follow [NDA clauses](confidentiality.md#nda-clauses). The rules you take from them go under "Extra confidentiality rules" in the document, in general words, after the person confirms them. Without clauses, ask whether their contract adds anything they know of, and write "none" when it does not.
   - **Names.** Ask which names must never appear: clients, partners, colleagues, internal product code names, and internal systems, services and repositories. Write them one per line to `local-only/confidential-terms.txt`, with each short form or spelling people use on a line of its own, such as `Fabrikam` next to `Fabrikam Retail` and `Falcon` next to `Project Falcon`. A name that is also an ordinary word or a public product gets a leading `?`, such as `?Harbor`: the scanner then reports it for review instead of blocking it. Add the employer's ticket key prefixes as lines such as `LOG-`, so the scanner finds keys in any form. Tell the person that this file stays on their computer, apart from the document, and exists only so the scanner can catch the names. In light mode, hand it back on its own ([Modes](../SKILL.md#modes)).

   Done when the person has seen the lists, in the intro or in full, the extra rules are confirmed or "none", and the names are written down or the person has said there are none.

5. **Propose the next step:** [harvest](harvest.md) while the person still has access to work systems or has documents of their work; the [interview](interview.md) when they have neither. If the harvest has to wait, tell the person which sources expire in the meantime ([harvest](harvest.md) step 3).

   Done when the person has agreed the next step and `progress.md` shows setup as done.

Done when the folder and the document exist, the About section holds the employment facts, the confidentiality rules are settled, and the next step is agreed.
