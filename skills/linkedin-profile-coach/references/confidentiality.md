# Confidentiality procedure

`SKILL.md` defines clean text and the front-page test. This file says how to keep the workspace, the drafts and everything else the person publishes clean. `rules-3` gives LinkedIn's terms behind the rule; the clean rule goes further. After the job ends, the person's contract still decides what stays confidential, through the extra rules in the work history documents and those that setup records in `progress.md`.

## While collecting

These hold in every phase that reads a source, a screenshot or an answer.

- **Clean before you write.** Read the raw item, decide what it shows about the person's work, and write only the clean sentence. Raw text never goes into a workspace file, not even temporarily. When a large source needs a file to process, such as an API response or an export, save it in `local-only/` and delete it once its themes are written.
- **Generalize until nobody can tell.** "A large Scandinavian furniture retailer" still names the client when the employer has one such client. Go up a level ("a retail client", "a client") until the description fits many companies. Generalize how a job ended too. Details such as how many people a change affected, or why the employer made it, tell about other people and the employer, so they are clean only when the employer has made them public. Otherwise write only the person's own fact, such as "my role ended in October 2026" (`career-break-4`).
- **Unannounced means the thing, not its name.** For a product, market, deal or plan the employer has not announced, a description gives away as much as the code name. For every product or initiative a record describes, ask the person whether the employer has announced it. Until they say yes, write only the person's work and a neutral kind ("a new product", "a greenfield service"), without its type, market, partner or launch date.
- **Keep the person's figures, drop the employer's.** "Cut release time from two days to four hours" is the person's result. "Shipped 3 million parcels a day" is the employer's business figure. LinkedIn's Talent Blog gives sales and acquisitions as sample measures for About; `about-3` replaces them with the person's own relative results.
- **Public stays public.** Open-source work, public talks and published articles can be named and linked; they are already public.
- **From a screenshot, record states.** A settings screenshot shows email addresses. Record whether the primary address is a work or a personal one and who can see it, and leave the address itself out (`settings-1`, `settings-6`). Leave out the names and photos of other people in a screenshot too.

## NDA pass

Run it before any phase hands its results to the person: before the audit and write phases hand over their files, before recommendation requests go to the person, and on the final texts the person pastes back.

The pass covers:

- **Workspace files.** Every file a phase changed, such as `audit.md` and `progress.md`, with any current text they quote from `linkedin-export/`.
- **Drafts.** Every file in `drafts/`, among them `featured.md`, the Projects entries, `settings.md` and `recommendation-requests.md`, and every message you draft for the person to send: recommendation requests, revision notes and the recommendations the person writes for others, with `[Name]` for the colleague (`recommendations-5`).
- **Images and files.** The cover image, Featured media and media attached to positions, whether the profile shows them now or a draft proposes them. The scanner reads only text, so look at each one, or ask the person what it shows, and apply the front-page test and `rules-3`. For one that fails, propose replacing or removing it; the person decides.
- **Text the person did not write.** Each received recommendation, before the person accepts it. The person pastes it, and you check it in the conversation and save none of its text. For one that fails, draft a revision note (`recommendations-7`). A connected app's capability statement comes from the app, so the person reads it against the front-page test before showing the app (`skills-10`).

1. **Scan** the files you changed. Whenever you can run code:

   ```bash
   python3 <skill>/scripts/scan_text.py --terms <workspace>/local-only/confidential-terms.txt <workspace>/audit.md
   ```

   A terms file you wrote or received in this conversation is at hand: pass it with `--terms`. When none is, as at the start of a light-mode run or after the move to personal storage, ask the person for the file or for their names (clients, partners, colleagues, code names, internal systems) before the scan, write them to a file outside the workspace, pass it with `--terms`, and keep it for this conversation's scans; outside light mode, delete it before the conversation ends. Leave out `--terms` only when the person says there are none. Pass a folder, such as `<workspace>/drafts`, to scan every text file in it; the scanner skips `local-only/` and `linkedin-export/` directly inside the folder you pass. It reports what it cannot read (files of other types, symlinked folders, a nested git repository) as `unscanned-file` or `unscanned-folder`: open each one yourself, or move it to `local-only/`. When it warns that a line of the terms file may never match, or stops because the file holds no names or ticket prefixes, fix the file with the person and scan again. Without code execution, make the same checks by reading: secrets, ticket keys, merge-request numbers, links, email addresses, host names, IP addresses, @handles, and the person's confidential terms.

2. **Fix what it finds.**
   - `block` findings (secrets, confidential terms): remove the secret's whole line and tell the person a secret turned up, without repeating it; generalize every confidential term. Two blocks are fixed in the terms file instead, followed by a new scan: a block on a company in `targets.md` or on one of the person's employers (make its line a `?` line with a note that says so, and tell the person), and a block on a public product whose name starts with a listed name, such as `HubSpot` for a name `Hub`, when the person confirms the text means that product (mark the name `?`).
   - `review` findings (ticket keys, merge-request numbers, links with or without a scheme, email addresses, host names, IP addresses, local paths, @handles, and a confidential name inside an identifier, such as `getFabrikamOrders`): generalize them, except public links and handles the person wants to keep, such as their open-source repository, and a public word that only contains a name, such as `GitHub` for a name `Hub`.
   - names marked `?` in the terms file, which are also ordinary words or public products: show the sentence; keep it when it uses the word in its ordinary or public sense, otherwise generalize. A `?` name whose note says it is the person's own employer or a company they want to work for stays, without asking, where it names that employer or target, such as in a position, `targets.md` or `settings.md`; generalize it where it names a client or partner.

3. **Read everything the pass covers** against the front-page test, the "Clean text leaves out" list in `SKILL.md`, the extra confidentiality rules in each work history document's About section, and the extra rules in `progress.md`. An item on those lists, such as a client's name or an employer's business figure, is not borderline: generalize or remove it yourself, and tell the person what changed without repeating the detail. The same holds for a transliterated or translated form of a name in the terms file, which the scanner does not match. Then collect each sentence that could still let a reader recognize a client, a colleague or an internal system.

4. **Show the borderline list.** For each sentence: why it may identify someone, and a generalized version. The person picks keep, generalize or remove. Keep it only when they confirm that no reader could tell which client, colleague or system it is about. Without an answer, generalize.

5. **Name the records to correct.** When a detail you changed came from a record's own text, tell the person which record holds it, by document and ID (such as E-004 in `work-history-contoso-logistics.md`), and the kind of detail, never the detail. The person corrects the record with `work-history-harvest`; this skill leaves the documents as they are ([Workspace](../SKILL.md#workspace)).

Done when the pass is clean: the scan ran with the person's names when they have any, with no "may never match" warning, the scanner reports no `block` findings, every `review` finding is fixed, kept by a rule of step 2, or approved by the person, every borderline sentence is kept, generalized or removed, the person has a proposal for every image and received recommendation that fails the front-page test, and every record that held a changed detail is named to the person.

## linkedin-export/

- It holds only the profile files from the person's LinkedIn data download, as [LinkedIn export](linkedin-export.md) step 3 sets out. They are the person's own data, so the scanner skips the folder, and the folder may go with the workspace to personal storage.
- The Profile file also holds the birth date and address, and the Recommendations Received file holds the writers' names and texts. They stay in these files. Workspace files take only what the audit uses and describe each writer by relationship ([LinkedIn export](linkedin-export.md) step 4).

## local-only/

Everything in `local-only/` stays on this computer:

- `confidential-terms.txt`: one name per line, for the scanner, which matches each name in any letter case, with any punctuation or none between its words, and at the start of identifiers such as `FabrikamClient` or `falcon2`. Inside an identifier, such as `getFabrikamOrders`, it reports the name for review. A note goes after ` # `, such as `Fabrikam Retail # client`, and lines starting with `#` are comments. `?Name` marks a name for review instead of a block: one that is also an ordinary word or a public product, or one of the person's own employers or target companies. A line such as `LOG-` names the employer's ticket key prefix, so keys like `log-1201` are found in any form.
- Employer documents the person provides, such as performance reviews, exports and saved lists from work systems, a reference letter that is an employer document (`recommendations-9`) and old internal documents. Each adapter says which files it saves here.

In light mode, `local-only/` is the folder the person keeps on their own computer ([Modes](../SKILL.md#modes)). Its files reach the conversation only as uploads for the step that reads them: never write their content into a workspace file and never hand them back, apart from `confidential-terms.txt` when you create or change it.

**Final check before the copy.** Before the person moves the workspace to personal storage, list every file outside `local-only/`, hidden ones included. Move each file that is not a workspace file (`progress.md`, `targets.md`, `audit.md`, `reference-update-*.md`, `drafts/` and the keep-list files in `linkedin-export/`), such as a raw export, a saved page, a PDF, a screenshot or a `.claude/` folder, to `local-only/`, or delete it with the person's yes. Then run steps 1 and 2 of the NDA pass with `<workspace>` as the path. Once it is clean, the person copies everything except `local-only/`. Once they have left the employer, they can delete `local-only/`.
