# Setup

First run only. Creates the workspace, records who the person is aiming at, and settles what needs their work email and accounts before access ends. The evidence itself comes from the work history documents ([Start of every run](../SKILL.md#start-of-every-run), step 3).

Your first reply covers steps 1 and 2 and asks the questions of steps 3, 4 and 6 together, so the person can answer in one go. Mention there that the audit will need their LinkedIn data download, which can take up to 48 hours to arrive ([LinkedIn export](linkedin-export.md), step 2). Ask the rest as each step comes up.

1. **Explain the plan** in two or three sentences: evidence of their work first, from their work history documents (the `work-history-harvest` skill makes them), then an audit of the profile, then texts they paste themselves; nothing is posted for them, and only clean text is kept.

   Done when the person knows the phases and that they paste every text themselves.

2. **Create the workspace.**
   - Full mode: propose `~/linkedin-profile/` and create it once the person agrees. Check that the folder is not inside a git repository: run `git -C <parent folder> rev-parse --is-inside-work-tree` on the folder that will hold it; it prints `true` inside a repository. If it does, pick another folder, so the files can never end up in a commit.
   - Copy the files from the skill's `templates/` folder into the workspace: `progress.md` and `targets.md`. Create `drafts/`, `linkedin-export/` and `local-only/`.
   - Light mode: create the same files and folders, except `local-only/`, in a working folder, and hand them back as the first workspace ZIP ([Modes](../SKILL.md#modes)). Ask the person to make one folder for this work on their own computer, with a `local-only/` folder inside it: the ZIPs go in the folder, and every employer document they gather, and `confidential-terms.txt`, go in `local-only/`.

   Done when the two files and the three folders exist outside any git repository, or, in light mode, the person has the first ZIP and has made the folder.

3. **Ask about the computer.** If it belongs to the employer and goes back when the person leaves, write that in `progress.md`. The plan then includes copying the workspace, without `local-only/`, to personal storage before the last day.

   Done when `progress.md` says whether the computer goes back.

4. **Record the employment facts** in `progress.md`: current or last employer, title, employment period, employment end date, and the day access to work systems ends, if known. Take the employer, the titles and the period from the About section of the work history documents, and ask only for what they lack. The end date is the last day of employment, past or planned, or "none yet" while the job goes on. The audit checks the last LinkedIn position against these dates (`career-break-1`). Once the end date has passed, ask whether the last position on LinkedIn shows it yet, and fill in "LinkedIn end date added". While it is ahead, write in "Next step" that the person adds the end month on LinkedIn after their last day.

   Done when each of these fields holds a value, "unknown" included.

5. **Ask about the LinkedIn account.** Record each answer under "Before access ends" in `progress.md`:
   - Ask which address is primary on the account, and record only whether it is a work or a personal address. If it is a work address, suggest making a personal address primary now (`settings-1`). The link to the LinkedIn data download for the audit goes to that address too ([LinkedIn export](linkedin-export.md), step 2).
   - Ask which LinkedIn services the employer pays for, such as LinkedIn Learning or a Recruiter seat. Tell the person that the account stays theirs and those services stay the employer's (`rules-7`). Ask them to save the courses and certificates of a LinkedIn Learning seat before access ends; `work-history-harvest` records them.
   - While the work email still works, suggest that the person add LinkedIn's workplace verification (`settings-3`). Once the work email is gone, record it as not available.
   - Set the other lines (the LinkedIn Learning courses, colleagues to connect with, the workspace copy) to "not yet", or to "not needed" where they do not apply.

   An unanswered question keeps "not checked" or "not yet", and the next run raises it again. Done when every line under "Before access ends" holds a state.

6. **Record the targets** in `targets.md`:
   - target roles and seniority, each role under its standard title: the form most postings use (`headline-1`);
   - where the person is based now (`search-4`); the places and workplace types they would accept, remote included, the employment types, and when they can start (`opentowork-2`);
   - industries, target companies in priority order (`settings-7`), and must-haves;
   - two to five job postings the person likes, with the language each is written in (`sections-2`). Ask for the posting text: job sites often block automated reading, and a pasted text is complete. Optional; a role description in words also works.
   - From the postings, for each target role: the required and the preferred qualifications, in the postings' words (`search-1`). Then fill the keyword table: skills, tools and terms that recur, with how many postings name each. The evidence columns stay empty until the audit.

   Done when every target role has its standard title, and every posting or role description the person gave has its qualifications and keywords in `targets.md`.

7. **Add the person's own confidentiality rules.** Show the clean / leave-out lists from `SKILL.md`. The extra rules in each work history document's About section already apply. Then ask:
   - whether their contract or NDA adds anything the documents do not hold yet (write it into `progress.md` under "Extra confidentiality rules");
   - for the `local-only/confidential-terms.txt` that `work-history-harvest` made: copy it into this workspace's `local-only/`, or, in light mode, ask for it as an upload. Without one, ask which names must never appear: clients, partners, colleagues, internal product code names, and internal systems, services and repositories. Write them one per line to `local-only/confidential-terms.txt`, with each short form or spelling people use on a line of its own, such as `Fabrikam` next to `Fabrikam Retail` and `Falcon` next to `Project Falcon`. A name that is also an ordinary word or a public product gets a leading `?`, such as `?Harbor`: the scanner then reports it for review instead of blocking it. Add the employer's ticket key prefixes as lines such as `LOG-`, so the scanner finds keys in any form. Explain that this file stays on the person's computer, apart from the files they copy, and exists only so the scanner can catch the names. In light mode, hand it back on its own ([Modes](../SKILL.md#modes)).

   Done when the person has seen both lists, and their extra rules and names are written down or they have said there are none.

8. **Propose the next phase:** the audit, once the work history documents are read and the LinkedIn data download is at hand. Without work history documents, suggest `work-history-harvest` first, above all while the person still has access to work systems: some sources expire with the job. Update the phase table in `progress.md`.

   Done when the person has agreed the next phase and the phase table shows setup as done.

Done when the workspace exists, `progress.md` holds the employment facts and a state on every line under "Before access ends", `targets.md` holds the targets, the person has seen the confidentiality rules, and the next phase is agreed.
