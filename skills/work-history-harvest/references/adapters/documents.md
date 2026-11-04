# Documents adapter

Files and text the person gives you: an old CV, self-reviews, promotion write-ups, thank-you messages, reference letters, certificates, and public work such as talks, articles and open-source projects. This is also the fallback for every other adapter when its tools are missing.

## Available when

Always. Ask what the person has, and where it should go:

- material that already passes the front-page test, such as certificates and links to public work, can go anywhere in the work history folder, or be uploaded; the final check before the copy lists such files for the person to take along;
- everything else goes into `local-only/`: the employer's material (internal documents, exports from work systems, reference letters the employer issued) and the person's own documents that name clients, colleagues, internal systems or figures, such as an old CV, self-reviews, promotion write-ups and thank-you messages.

## Read

- **Old CV:** positions, dates, achievements, technologies. Every claim in it counts as `self-reported` until an artifact backs it; the person's confirmation keeps it self-reported. Old CVs often say more than the person can defend.
- **Self-reviews and promotion write-ups:** usually the richest description of results, in the person's own words. Self-reported unless a reviewer confirmed it.
- **Thank-you messages, praise and reference letters:** themes for `recognition` records, without names or quotes, naming the writer only by relationship, such as manager or client lead. The writer of a reference letter is a good person to ask for a public recommendation later.
- **Certificates and courses:** themes for `credential` records, with the issuer and the date.
- **Public work:** themes for `public` records. These are already public, so keep the title and the link; a profile or a CV can show them.
- **LinkedIn positions:** the Positions file of the person's LinkedIn data download (a CSV with company names, titles and dates), or their profile saved as PDF. Use them for the titles and periods, to start the interview from. Open only the Positions file: the rest of a LinkedIn download holds messages and contacts.

## Turn into themes

Each item becomes a theme, or joins the theme of the same work with its source type. [Harvest](../harvest.md) step 6 turns the themes of all sources into records together and matches them to the records already in the document. When an item adds a fact to work that another source shows, such as a CV figure for a project the tickets or a review show, mark that fact as self-reported, so that the record's Basis becomes `mixed` and names it. Work that only the person's own documents describe is `self-reported`. Conflicting claims, thin themes and My role follow harvest step 6.

Done when each item the person gave you is part of a theme, waits under "Open questions", or is set aside with the person, and every document that fails the front-page test is in `local-only/`.

## Leave out

What the confidentiality rules leave out, also when it appears in the person's own CV: an old CV may name clients or internal systems that a new profile should describe in clean words.
