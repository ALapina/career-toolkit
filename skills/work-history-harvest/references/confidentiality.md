# Confidentiality procedure

`SKILL.md` defines clean text and the front-page test. This file says how to keep the document clean: while collecting, in the NDA pass, with the person's own NDA clauses, and before the copy to personal storage. After the job ends, the person's contract still decides what stays confidential, through the extra rules in the document's About section.

## While collecting

These hold in every step that reads a source, a screenshot or an answer.

- **Clean before you write.** Read the raw item, decide what it shows about the person's work, and write only the clean sentence. Raw text never goes into the document, not even temporarily. When a large source needs a file to process, such as an API response you fetch, save it in `local-only/` and keep it, with the themes files of [harvest](harvest.md) step 5, until harvest step 8 deletes them once the records built from them are reviewed, or sooner when the person asks.
- **Generalize until nobody can tell.** "A large Scandinavian furniture retailer" still names the client when the employer has one such client. Go up a level ("a retail client", "a client") until the description fits many companies. Generalize how a job ended too. Details such as how many people a change affected, or why the employer made it, tell about other people and the employer, so they are clean only when the employer has made them public. Otherwise write only the person's own fact, such as "my role ended in October 2026".
- **Unannounced means the thing, not its name.** For a product, market, deal or plan the employer has not announced, a description gives away as much as the code name. For every product or initiative a record describes, ask the person whether the employer has announced it. Until they say yes, write only the person's work and a neutral kind ("a new product", "a greenfield service"), without its type, market, partner or launch date.
- **Keep the person's figures, drop the employer's.** "Cut release time from two days to four hours" is the person's result. "Shipped 3 million parcels a day" is the employer's business figure. Gains in speed or stability, such as "cut p95 latency by 40%", are the person's results too. A weakness they found, such as the load at which a system would fail, belongs to the employer even when their own test measured it.
- **Public stays public.** Open-source work, public talks and published articles can be named and linked; they are already public.
- **From a screenshot, record what it shows about the work.** Leave out the names, photos and email addresses of other people in it.

## NDA clauses

The person may give clauses from an NDA, the confidentiality section of a contract, or an exit agreement. Exit agreements often add terms of their own, such as keeping the agreement secret or not speaking badly of the company.

1. **Keep the text in `local-only/`.** In full mode, save what the person pasted or uploaded as `local-only/nda-clauses-<employer>.txt`, with the employer part of the document's name, or keep their file there. In light mode, it stays an upload, and the person keeps it in their own `local-only/` folder. No word of it goes into the document.
2. **Turn each clause into a rule** in general words that name nothing secret: "no figures about client accounts", "the exit agreement and its terms stay confidential", "no statements about the company's management". A clause that only names salary, notice period or other terms that touch no work description adds no rule.
3. **Read a vague clause strictly.** When a clause could cover more or less ("all information related to the business"), take the stricter reading as the rule, and tell the person that HR or a lawyer can say whether it is meant that broadly.
4. **Show the rules to the person** in plain words and ask them to confirm each one. Write the confirmed rules under "Extra confidentiality rules" in the document. When a rule would itself name a secret, write the rule in general words and put the name it hides in `local-only/confidential-terms.txt`, one name per line.
5. **Apply them with the lists in `SKILL.md`.** Where a rule is stricter than the default clean and leave-out lists, the rule wins.

Done when every clause is a confirmed rule, a strict reading the person knows about, or set aside because it touches no work description.

## NDA pass

Run it before any step hands its results to the person: at the end of setup, after records are written in a harvest or an update, after interview rounds, and on the final check before the copy. It covers the document and `progress.md`.

1. **Scan** the files you changed. Whenever you can run code:

   ```bash
   python3 <skill>/scripts/scan_text.py --terms <folder>/local-only/confidential-terms.txt <folder>
   ```

   A terms file you wrote or received in this conversation is at hand: pass it with `--terms`. When none is, as at the start of a light-mode run or after the move to personal storage, ask the person for the file or for their names (clients, partners, colleagues, code names, internal systems) before the scan, write them to a file outside the folder, pass it with `--terms`, and keep it for this conversation's scans; outside light mode, delete it before the conversation ends. Leave out `--terms` only when the person says there are none. Passing the folder scans every text file in it; the scanner skips `local-only/` directly inside the folder you pass. It reports what it cannot read (files of other types, symlinked folders, a nested git repository) as `unscanned-file` or `unscanned-folder`: ask the person, one line each, which of them they earned or made, such as a certificate, unless they said so in this conversation, and open only those. One that passes the front-page test stays where it is, for the [final check](#final-check-before-the-copy) to list for the copy. Move every other reported file or folder to `local-only/` unopened. Until the person answers, leave the files where they are; the final check asks again. When it warns that a line of the terms file may never match, or stops because the file holds no names or ticket prefixes, fix the file with the person and scan again. Without code execution, make the same checks by reading: secrets, ticket keys, merge-request numbers, links, email addresses, host names, IP addresses, @handles, and the person's confidential terms.

2. **Fix what it finds.**
   - `block` findings (secrets, confidential terms): remove the secret's whole line and tell the person a secret turned up, without repeating it; generalize every confidential term. Two blocks are fixed in the terms file instead, followed by a new scan: a block on one of the person's own employers (make its line a `?` line with a note that says so, and tell the person), and a block on a public product whose name starts with a listed name, such as `HubSpot` for a name `Hub`, when the person confirms the text means that product (mark the name `?`).
   - `review` findings (ticket keys, merge-request numbers, links with or without a scheme, email addresses, host names, IP addresses, local paths, @handles, and a confidential name inside an identifier, such as `getFabrikamOrders`): generalize them, except public links and handles the person wants to keep, such as their open-source repository, and a public word that only contains a name, such as `GitHub` for a name `Hub`.
   - Names marked `?` in the terms file, which are also ordinary words or public products: show the sentence; keep it when it uses the word in its ordinary or public sense, otherwise generalize. A `?` name whose note says it is the person's own employer or a company they want to work for stays, without asking, where it names that employer, such as in its own document or an Employer and title line; generalize it where it names a client or partner.

3. **Read the document** against the front-page test, the "Clean text leaves out" list in `SKILL.md` and the extra rules in the About section. An item on those lists, such as a client's name or an employer's business figure, is not borderline: generalize or remove it yourself, and tell the person what changed without repeating the detail. The same holds for a transliterated or translated form of a name in the terms file, which the scanner does not match. When you change a record that has a copy under "Approved text of changed records" in `progress.md`, change the copy the same way. Then collect each sentence that could still let a reader recognize a client, a colleague or an internal system.

4. **Show the borderline list,** one line per sentence: the record ID, why it may identify someone, and the generalized version. The person picks keep, generalize or remove. Keep it only when they confirm that no reader could tell which client, colleague or system it is about. Without an answer, generalize. When there are more than three, show the three that matter most and put the rest under "Open questions" in the document, worded with the generalized text, and say how many wait there.

5. **Record the outcome** in each record's Confidentiality field: the kind of detail removed, never the detail.

Done when the pass is clean: the scan ran with the person's names when they have any, with no "may never match" warning, the scanner reports no `block` findings, every `review` finding is fixed, kept by a rule of step 1 or 2, or approved by the person, and every borderline sentence is kept, generalized or removed.

## local-only/

Everything in `local-only/` stays on this computer:

- `confidential-terms.txt`: one name per line, for the scanner, which matches each name in any letter case, with any punctuation or none between its words, and at the start of identifiers such as `FabrikamClient` or `falcon2`. Inside an identifier, such as `getFabrikamOrders`, it reports the name for review. A note goes after ` # `, such as `Fabrikam Retail # client`, and lines starting with `#` are comments. `?Name` marks a name for review instead of a block: one that is also an ordinary word or a public product, or one of the person's own employers or target companies. A line such as `LOG-` names the employer's ticket key prefix, so keys like `log-1201` are found in any form.
- `nda-clauses-<employer>.txt` or the person's own file with the clauses ([NDA clauses](#nda-clauses)).
- `themes-<source>-<period>.md`: the themes of [harvest](harvest.md) step 5, kept until the person has reviewed the records built from them.
- Employer documents the person provides, such as performance reviews, exports and saved lists from work systems, a reference letter the employer issued, and old internal documents. Each adapter says which files it saves here.
- Exports of the person's own accounts that touch work, such as a claude.ai data export. A personal export also holds private chats. On an employer's computer, suggest that the person delete it once its themes are in the document.

In light mode, `local-only/` is the folder the person keeps on their own computer ([Modes](../SKILL.md#modes)). Its files reach the conversation only as uploads for the step that reads them: never write their content into the document and never hand them back, apart from `confidential-terms.txt` and the themes files of [harvest](harvest.md) step 5, when you create or change them.

## Final check before the copy

Before the person moves their documents to personal storage, list every file outside `local-only/`, hidden ones included. Ask the person, one line each, which of the files that are not a document (`work-history-*.md`) or `progress.md` they earned or made, such as a certificate, a screenshot of a course they completed or a copy of their public work. Open only those: each one that passes the front-page test stays where it is and is listed for the copy. Move every other file, such as a raw export, a saved page, an employer PDF, any other screenshot or a `.claude/` folder, to `local-only/` unopened, or delete it with the person's yes. Then run steps 1 and 2 of the NDA pass with `<folder>` as the path. Once it is clean, the person copies the documents, `progress.md` and the listed files, and nothing from `local-only/`. Remind them that the copy is theirs to check: until Reviewed by owner says yes, they have not yet read all of it. Once they have left the employer, they can delete `local-only/`.

Done when only documents, `progress.md` and the files listed for the copy remain outside `local-only/`, and the scan is clean.
