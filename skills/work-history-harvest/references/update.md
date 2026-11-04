# Update

Add a newer period to an existing document, usually once a year, when its Next update date has come. The run follows [harvest](harvest.md); this file says what differs: the time windows, and matching new work to the records already there.

1. **Read the document.** Its About section: the Sources covered table, the Harvest log, the extra confidentiality rules, Last record ID and Reviewed by owner. Read every record's title, Period and Action, so you can recognize the same work later.

   Done when you can name, for each source, the last month it covers, and the next free record ID.

2. **Set a window per source.**
   - A source already covered: from the month after its "Covered to" month, to today or to the end of employment.
   - A source picked for the first time, or one that was skipped before: the whole employment period, within what the source still holds.
   - A source the person can no longer reach: the [documents](adapters/documents.md) adapter or the [interview](interview.md) instead.

   Show the windows to the person in plain words ("Jira from November 2025 to now"), and write them under "Sources of this run" in `progress.md`.

   Done when every source the person picks has its window and the person has agreed.

3. **Collect** with [harvest](harvest.md) steps 1 and 3 to 5: the disclosures and the person's yes, what expires first, the sources and the adapters, each adapter over its window from step 2. Items from before a window that a source returns anyway stay out.

   Done when every chosen adapter has met its completion criterion or stopped with a clean reason.

4. **Match each theme to the records.** Records hold no ticket numbers or links, so match by what the work was and when:
   - **Same work:** the theme describes the same body of work as a record (the same goal, the same part of the product, the same kind of action and technologies), and its period continues or overlaps the record's Period. Update that record: extend its Period, add what is new to Action and Result in full sentences, add the source types to its Basis with today's check date, and set its status to `pending`. One body of work stays one record, however long it ran.
   - **New work:** no record describes it. Add a record with the next free ID and status `pending`.
   - **Unclear:** it could be either. Show the person the record's title and period next to the theme in one line each, and ask: same work or new? Without an answer, add it as a new `pending` record and put the pair under "Open questions": "E-014 may continue E-004: merge them?".

   Write new and updated records by the rules of [harvest](harvest.md) step 6 for My role, conflicting claims and thin themes.

   Done when every theme is an updated record, a new record, a new record with its question, or a question under "Open questions".

5. **Clean and approve** with [harvest](harvest.md) steps 7 to 10: the NDA pass, the review of new and updated records, the gaps, the closing scan.

   Done when those steps meet their completion criteria.

6. **Finish the run** as [End of every run](../SKILL.md#end-of-every-run) says:
   - each source of this run gets its "Covered to" month and "Harvested on" date moved forward, and a new source gets its row, as [Sources covered](document-format.md#sources-covered) defines a source; keep "Covered from" as it was;
   - add a Harvest log row with run `update`, the sources, the windows, the IDs added and the IDs updated;
   - Next update: one year from today, or `none, employment ended`;
   - Reviewed by owner turns to `no` when any record was added or changed ([Owner review](../SKILL.md#owner-review)), and the person hears why.

   Done when the About section shows this run and the person has heard what changed.

Done when every source of this run covers its new window or is recorded as skipped, no body of work appears in two records unless the person kept them apart or the pair is an open question, and the About section is current.
