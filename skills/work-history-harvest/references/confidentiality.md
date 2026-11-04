# Confidentiality procedure

`SKILL.md` defines clean text and the front-page test. This file says how to keep the document clean: while collecting, in the NDA pass, with the person's own NDA clauses, and before the copy to personal storage. After a layoff, the person's contract decides what stays confidential, through the extra rules in the document's About section.

## While collecting

These hold in every step that reads a source, a screenshot or an answer.

- **Clean before you write.** Read the raw item, decide what it shows about the person's work, and write only the clean sentence. Raw text never goes into the document, not even temporarily. When a large source needs a file to process, such as an API response or an export, save it in `local-only/` and delete it once its themes are written.
- **Generalize until nobody can tell.** "A large Scandinavian furniture retailer" still names the client when the employer has one such client. Go up a level ("a retail client", "a client") until the description fits many companies. Generalize the scale of a layoff too. "A company-wide layoff" tells about other people's jobs, so it is clean only when the employer announced the cut publicly. Otherwise write the person's own fact, such as "my role ended in a layoff".
- **Unannounced means the thing, not its name.** For a product, market, deal or plan the employer has not announced, a description gives away as much as the code name. For every product or initiative a record describes, ask the person whether the employer has announced it. Until they say yes, write only the person's work and a neutral kind ("a new product", "a greenfield service"), without its type, market, partner or launch date.
- **Keep the person's figures, drop the employer's.** "Cut release time from two days to four hours" is the person's result. "Shipped 3 million parcels a day" is the employer's business figure. Gains in speed or stability, such as "cut p95 latency by 40%", are the person's results too. A weakness they found, such as the load at which a system would fail, belongs to the employer even when their own test measured it.
- **Public stays public.** Open-source work, public talks and published articles can be named and linked; they are already public.
- **From a screenshot, record what it shows about the work.** Leave out the names, photos and email addresses of other people in it.

## NDA clauses

The person may give clauses from an NDA, the confidentiality section of a contract, or a termination agreement. Termination agreements often add terms of their own, such as keeping the agreement secret or not speaking badly of the company.

1. **Keep the text in `local-only/`.** In full mode, save what the person pasted or uploaded as `local-only/nda-clauses.txt`, or keep their file there. In light mode, it stays an upload, and the person keeps it in their own `local-only/` folder. No word of it goes into the document.
2. **Turn each clause into a rule** in general words that name nothing secret: "no figures about client accounts", "the termination agreement and its terms stay confidential", "no statements about the company's management". A clause that only names salary, notice period or other terms that touch no work description adds no rule.
3. **Read a vague clause strictly.** When a clause could cover more or less ("all information related to the business"), take the stricter reading as the rule, and tell the person that HR or a lawyer can say whether it is meant that broadly.
4. **Show the rules to the person** in plain words and ask them to confirm each one. Write the confirmed rules under "Extra confidentiality rules" in the document. A rule that would itself name a secret goes to `local-only/confidential-terms.txt` instead.
5. **Apply them with the lists in `SKILL.md`.** Where a rule is stricter than the default clean and leave-out lists, the rule wins.

Done when every clause is a confirmed rule, a strict reading the person knows about, or set aside because it touches no work description.

## NDA pass

Run it before any step hands its results to the person: after records are written in a harvest or an update, after interview rounds, and on the final check before the copy. It covers the document and `progress.md`.

1. **Scan** the files you changed. Whenever you can run code:

   ```bash
   python3 <skill>/scripts/scan_text.py --terms <folder>/local-only/confidential-terms.txt <folder>
   ```

   When `local-only/confidential-terms.txt` is not at hand, as in light mode or after the move to personal storage, ask the person for the file or for their names (clients, partners, colleagues, code names, internal systems) before the scan. Write the names to a temporary file outside the folder, pass it with `--terms`, and delete it after the scan. Leave out `--terms` only when the person says there are none. Passing the folder scans every text file in it; the scanner skips `local-only/` directly inside the folder you pass. It reports what it cannot read (files of other types, symlinked folders, a nested git repository) as `unscanned-file` or `unscanned-folder`: open each one yourself, or move it to `local-only/`. Without code execution, make the same checks by reading: secrets, ticket keys, merge-request numbers, links, email addresses, host names, IP addresses, @handles, and the person's confidential terms.

2. **Fix what it finds.**
   - `block` findings (secrets, confidential terms): remove the secret's whole line and tell the person a secret turned up, without repeating it; generalize every confidential term.
   - `review` findings (ticket keys, merge-request numbers, links with or without a scheme, email addresses, host names, IP addresses, local paths, @handles): generalize them, except public links and handles the person wants to keep, such as their open-source repository.
   - Names marked `?` in the terms file, which are also ordinary words or public products: show the sentence; keep it when it uses the word in its ordinary or public sense, otherwise generalize.

3. **Read the document** against the front-page test, the "Clean text leaves out" list in `SKILL.md` and the extra rules in the About section. An item on those lists, such as a client's name or an employer's business figure, is not borderline: generalize or remove it yourself, and tell the person what changed without repeating the detail. Then collect each sentence that could still let a reader recognize a client, a colleague or an internal system.

4. **Show the borderline list,** one line per sentence: the record ID, why it may identify someone, and the generalized version. The person picks keep, generalize or remove. Keep it only when they confirm that no reader could tell which client, colleague or system it is about. Without an answer, generalize. When there are more than three, show the three that matter most and put the rest under "Open questions" in the document, worded with the generalized text, and say how many wait there.

5. **Record the outcome** in each record's Confidentiality field: the kind of detail removed, never the detail.

Done when the pass is clean: the scanner reports no `block` findings, every `review` finding is fixed or approved by the person, and every borderline sentence is kept, generalized or removed.

## local-only/

Everything in `local-only/` stays on this computer:

- `confidential-terms.txt`: one name per line, for the scanner, which matches it in any case and with any separator. Lines starting with `#` are comments, and a ` # comment` may follow a name. `?Name` marks a name that is also an ordinary word or a public product, for review instead of a block. A line such as `LOG-` names the employer's ticket key prefix, so keys like `log-1201` are found in any form.
- `nda-clauses.txt` or the person's own file with the clauses ([NDA clauses](#nda-clauses)).
- Employer documents the person provides, such as performance reviews, exports and saved lists from work systems, a reference letter the employer issued, and old internal documents. Each adapter says which files it saves here.
- Exports of the person's own accounts that touch work, such as a claude.ai data export. A personal export also holds private chats. On an employer's computer, suggest that the person delete it once its themes are in the document.

In light mode, `local-only/` is the folder the person keeps on their own computer ([Modes](../SKILL.md#modes)). Its files reach the conversation only as uploads for the step that reads them: never write their content into the document and never hand them back, apart from `confidential-terms.txt` when you create or change it.

## Final check before the copy

Before the person moves their documents to personal storage, list every file outside `local-only/`, hidden ones included. Move each file that is not a document (`work-history-*.md`) or `progress.md`, such as a raw export, a saved page, a PDF, a screenshot or a `.claude/` folder, to `local-only/`, or delete it with the person's yes. Then run steps 1 and 2 of the NDA pass with `<folder>` as the path. Once it is clean, the person copies the documents, and nothing from `local-only/`. Remind them that the copy is theirs to check: until Reviewed by owner says yes, they have not yet read all of it. Once they have left the employer, they can delete `local-only/`.

Done when only documents and `progress.md` remain outside `local-only/`, and the scan is clean.
