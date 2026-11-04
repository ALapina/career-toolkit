# Setup

The first run for an employer. Creates the folder and the document, records the employment facts, and settles the confidentiality rules before any source is read.

**Opening questions.** On a first run, your first reply is the [intro](intro.md) followed by these questions as one numbered list, one line each, so the person can answer in one go; explain a term only where the person needs it to answer:

- employer, job titles and the period of each, and whether the job has ended or when it ends;
- whether they can still reach work systems, and which documents they have (old CV, reviews, certificates);
- whether you may create the folder (propose `~/work-history/`, or say how light mode works);
- whether they have an NDA or a confidentiality clause to give you, and which names must never appear.

As soon as the person says that access to work systems ends within days, in their first message or a later one, add to your reply, one line each, the items of [harvest](harvest.md) step 3 that need only their own action. Say that they come first, that the person saves the files on this computer, in `local-only/` once the folder exists or until then in a new folder in their home folder rather than the Desktop or Documents, which cloud services often sync, and that they keep the files there until you ask for them after the disclosures of harvest step 1. Record the person's decisions under "Before access ends" once `progress.md` exists; harvest step 3 then only checks them.

Ask the rest as each step comes up. When the person already has a folder from an earlier employer, skip step 1 and the parts of step 4 already settled, and add a section for the new employer to `progress.md` from the template, leaving the other employers' sections as they are. When the new employer's name, a short form or a transliteration of it is already a line of `local-only/confidential-terms.txt`, make it a `?` line with a note that says so, such as `?Fabrikam # client at Contoso; my employer 2019-2021`, and tell the person.

1. **Create the folder.**
   - Full mode: propose `~/work-history/` and create it once the person agrees. Check that it is not inside a git repository: run `git -C <parent folder> rev-parse --is-inside-work-tree` on the folder that will hold it; it prints `true` inside a repository. If it does, pick another folder, so the files can never end up in a commit. Check also that no cloud service syncs it: a path inside iCloud Drive, OneDrive, Dropbox or Google Drive shows it, and the Desktop and Documents folders are often synced too, so ask the person about those; the home folder is usually safe. Create `local-only/` inside it, and copy `progress.md` from the skill's `templates/` folder, with a section for this employer.
   - Light mode: create the same in a working folder, without `local-only/`; step 5 hands it back as the first ZIP ([Modes](../SKILL.md#modes)). Ask the person to make one folder for this work on their own computer, with a `local-only/` folder inside it, in a place no cloud service syncs: their home folder (on a Mac: Finder > Go > Home), not the Desktop or Documents, which many computers sync, and not iCloud Drive, OneDrive, Dropbox or Google Drive. The ZIPs go in the folder, and every employer document they gather, the NDA clauses and `confidential-terms.txt` go in `local-only/`. The ZIPs may also go to cloud storage; `local-only/` stays on this computer.

   Done when the folder, `local-only/` and `progress.md` exist outside any git repository and any synced folder, or, in light mode, the working folder and `progress.md` exist and the person has made their folder; in both modes, `progress.md` holds under "Before access ends" every decision the person has given so far.

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
   - **Names.** Ask which names must never appear: clients, partners, colleagues, internal product code names, and internal systems, services and repositories. Write them one per line to `local-only/confidential-terms.txt`, with each short form or spelling people use on a line of its own, such as `Fabrikam` next to `Fabrikam Retail` and `Falcon` next to `Project Falcon`; a note goes after ` # `, such as `Fabrikam Retail # client`. A name written in another script than the document's also goes in as the sources and an English text spell it, with its common transliterations and, for a code name, its English translation: for the client ООО «Ромашка» and the code name «Сокол», the lines `Ромашка`, `Romashka`, `Сокол`, `Sokol` and `?Falcon`. A name that is also an ordinary word or a public product gets a leading `?`, such as `?Harbor`: the scanner then reports it for review instead of blocking it. So does a name that is also one of the person's own employers or a company they want to work for, with a note that says so, such as `?Fabrikam # client at Contoso; my employer 2019-2021`; ask the person whether any name on the list is one. Add the employer's ticket key prefixes as lines such as `LOG-`, so the scanner finds keys in any form. Tell the person that this file stays on their computer, apart from the document, and exists only so the scanner can catch the names. In light mode, write it outside the working folder, hand it back on its own ([Modes](../SKILL.md#modes)), and pass it with `--terms` for this run's scans.

   Done when the person has seen the lists, in the intro or in full, the extra rules are confirmed or "none", and the names are written down or the person has said there are none.

5. **Propose the next step:** [harvest](harvest.md) while the person still has access to work systems or has documents of their work; the [interview](interview.md) when they have neither. If the harvest has to wait, tell the person which sources expire in the meantime ([harvest](harvest.md) step 3). Then run the [NDA pass](confidentiality.md#nda-pass) over the document and `progress.md` and, in light mode, hand back the first ZIP ([Modes](../SKILL.md#modes)).

   Done when the person has agreed the next step, the Step line of `progress.md` names it, such as "next: harvest step 1", the NDA pass is clean and, in light mode, the person has the ZIP.

Done when the folder and the document exist, the About section holds the employment facts, the confidentiality rules are settled, the NDA pass is clean, and the next step is agreed.
