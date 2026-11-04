# Confidentiality procedure

`SKILL.md` defines clean text and the front-page test. This file says how to keep the workspace, the drafts and everything else the person publishes clean. `rules-3` gives LinkedIn's terms behind the rule; the clean rule goes further. After a layoff, the person's contract decides what stays confidential, through the extra rules in the work history documents and those that setup records in `progress.md`.

## While collecting

These hold in every phase that reads a source, a screenshot or an answer.

- **Clean before you write.** Read the raw item, decide what it shows about the person's work, and write only the clean sentence. Raw text never goes into a workspace file, not even temporarily. When a large source needs a file to process, such as an API response or an export, save it in `local-only/` and delete it once its themes are written.
- **Generalize until nobody can tell.** "A large Scandinavian furniture retailer" still names the client when the employer has one such client. Go up a level ("a retail client", "a client") until the description fits many companies. Generalize the scale of a layoff too. "A company-wide layoff" tells about other people's jobs, so it is clean only when the employer announced the cut publicly. Otherwise write the person's own fact, such as "my role ended in a layoff" (`career-break-4`).
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

   When `local-only/confidential-terms.txt` is not at hand, as in light mode or after the move to personal storage, ask the person for the file or for their names (clients, partners, colleagues, code names, internal systems) before the scan. Write the names to a temporary file outside the workspace, pass it with `--terms`, and delete it after the scan. Leave out `--terms` only when the person says there are none. Pass a folder, such as `<workspace>/drafts`, to scan every text file in it; the scanner skips `local-only/` and `linkedin-export/` directly inside the folder you pass. It reports what it cannot read (files of other types, symlinked folders, a nested git repository) as `unscanned-file` or `unscanned-folder`: open each one yourself, or move it to `local-only/`. Without code execution, make the same checks by reading: secrets, ticket keys, merge-request numbers, links, email addresses, host names, IP addresses, @handles, and the person's confidential terms.

2. **Fix what it finds.**
   - `block` findings (secrets, confidential terms): remove the secret's whole line and tell the person a secret turned up, without repeating it; generalize every confidential term.
   - `review` findings (ticket keys, merge-request numbers, links with or without a scheme, email addresses, host names, IP addresses, local paths, @handles): generalize them, except public links and handles the person wants to keep, such as their open-source repository.
   - names marked `?` in the terms file, which are also ordinary words or public products: show the sentence; keep it when it uses the word in its ordinary or public sense, otherwise generalize.

3. **Read everything the pass covers** against the front-page test, the "Clean text leaves out" list in `SKILL.md` and the extra rules in `progress.md`. An item on those lists, such as a client's name or an employer's business figure, is not borderline: generalize or remove it yourself, and tell the person what changed without repeating the detail. Then collect each sentence that could still let a reader recognize a client, a colleague or an internal system.

4. **Show the borderline list.** For each sentence: why it may identify someone, and a generalized version. The person picks keep, generalize or remove. Keep it only when they confirm that no reader could tell which client, colleague or system it is about. Without an answer, generalize.

5. **Record the outcome** in each evidence record's Confidentiality field: the kind of detail removed, never the detail.

Done when the pass is clean: the scanner reports no `block` findings, every `review` finding is fixed or approved by the person, every borderline sentence is kept, generalized or removed, and the person has a proposal for every image and received recommendation that fails the front-page test.

## linkedin-export/

- It holds only the profile files from the person's LinkedIn data download, as [LinkedIn export](linkedin-export.md) step 3 sets out. They are the person's own data, so the scanner skips the folder, and the folder may go with the workspace to personal storage.
- The Profile file also holds the birth date and address, and the Recommendations Received file holds the writers' names and texts. They stay in these files. Workspace files take only what the audit uses and describe each writer by relationship ([LinkedIn export](linkedin-export.md) step 4).

## local-only/

Everything in `local-only/` stays on this computer:

- `confidential-terms.txt`: one name per line, for the scanner, which matches it in any case and with any separator. Lines starting with `#` are comments, and a ` # comment` may follow a name. `?Name` marks a name that is also an ordinary word or a public product, for review instead of a block. A line such as `LOG-` names the employer's ticket key prefix, so keys like `log-1201` are found in any form.
- Employer documents the person provides, such as performance reviews, exports and saved lists from work systems, a reference letter that is an employer document (`recommendations-9`) and old internal documents. Each adapter says which files it saves here.

In light mode, `local-only/` is the folder the person keeps on their own computer ([Modes](../SKILL.md#modes)). Its files reach the conversation only as uploads for the step that reads them: never write their content into a workspace file and never hand them back, apart from `confidential-terms.txt` when you create or change it.

**Final check before the copy.** Before the person moves the workspace to personal storage, list every file outside `local-only/`, hidden ones included. Move each file that is not a workspace file (`progress.md`, `targets.md`, `audit.md`, `reference-update-*.md`, `drafts/` and the keep-list files in `linkedin-export/`), such as a raw export, a saved page, a PDF, a screenshot or a `.claude/` folder, to `local-only/`, or delete it with the person's yes. Then run steps 1 and 2 of the NDA pass with `<workspace>` as the path. Once it is clean, the person copies everything except `local-only/`. Once they have left the employer, they can delete `local-only/`.
