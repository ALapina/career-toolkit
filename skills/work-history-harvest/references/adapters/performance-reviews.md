# Performance reviews adapter

Goals, review outcomes and feedback from tools such as Leapsome, Lattice or Culture Amp. Reviews hold verified achievements and the themes colleagues praise, which later help the person choose whom to ask for a recommendation.

## Available when

The person can still sign in to the tool. Access usually ends with employment, so collect this source first ([harvest](../harvest.md), step 3). It almost always arrives as documents the person saves:

- a PDF, CSV or Excel export, where the tool offers one;
- pages saved with the browser's print dialog ("Save as PDF"), or screenshots, where it does not;
- text the person pastes.

Leapsome is the exception: when Leapsome tools are among your tools, you can read goals and feedback through them (the Connector item under [Leapsome](#leapsome)).

Ask the person to save every file in `local-only/`: they are the employer's documents. Whether the person may keep copies depends on the employer's policy and their contract, so ask them to check before exporting.

When access has already ended, go to [After access ends](#after-access-ends).

## Save the documents

The labels in each tool can differ from the ones below; look for the nearest match.

### Leapsome

- **Reviews.** Reviews > Dashboard > "Show past reviews" lists past assessments; some pages call it "Show past assessments". Filter for the ones the person received. Full results are under Reviews > Dashboard > You. The person sees what the cycle's visibility settings allow. When the manager took part in an assessment, the person later gets access to the manager's answers.
- **Self-assessments.** Actions > Download PDF, at the top of a self-assessment, exports all its answers. Leapsome's help does not say whether this PDF includes the manager's answers, so save the results page as PDF too.
- **Goals.** In the Goals module, Actions > Export saves a filtered goal report as an Excel file. The help article sits in Leapsome's admin section, so the person may not have this option; then save the goal pages as PDF.
- **Feedback and praise.** In the Instant Feedback module, Quick-Filters > "All feedback received by you" lists all feedback shared with the person. Leapsome's help describes no export for it: save the pages as PDF.
- **Connector.** Leapsome's MCP connector is in beta. It gives an AI client such as Claude only the Leapsome data and actions the person can already access. A Leapsome admin must enable it for the organization, choose what it may read, and give the person the "Use the MCP integration" permission. In Claude, the person then connects it under Connectors > Leapsome. Its read scopes include the goals, feedback and praise visible to the person. For reviews, the help page lists cycles, participants, statuses and the person's review tasks, and does not mention the answers: take review text from the PDFs. Use it to read only. Never use its write actions, which are off by default.
- **When the account ends.** A deactivated user's data stays in Leapsome; the help page does not say whether that user can still sign in. Deleting a user cannot be undone: their past feedback and reviews then show as "Deleted user", and Leapsome keeps no record of their information.
- **Admins.** An admin can export a cycle's review PDFs (Reviews > Cycles > the cycle > Actions > "Export review PDFs"; a download link arrives by email) or one person's PDF report (Actions > Download PDF on their results overview). The cycle export follows the admin visibility settings. Inference: a person who has lost access can ask HR or a Leapsome admin for their PDF report.

### Lattice

- **Reviews.** Once a review cycle has ended and a manager or admin has shared the review, the person can download the review packet: Performance > Performance Reviews, View packet next to the review, then Download PDF. They pick a grouping and a format (Standard or Optimized) and select Download. A packet the person has not acknowledged yet needs their acknowledgement first. Admins decide what a packet contains.
- **Goals.** Every user can export the goals they have access to: Goals > Explore, remove the filters, then Download CSV. The file includes public and private goals and drafts.
- **Feedback.** Under Feedback, the filter "You've received" shows the feedback the person received. Lattice's help describes no employee download for it: save the pages as PDF.
- **When the account ends.** Deactivation keeps the person's data but ends their access to Lattice. Admins can still open a deactivated user's reviews, 1:1s and feedback.
- **Managers and admins.** Managers and super admins can download one person's PDF review packets across several cycles at once. The reviewee version holds only the responses the reviewee could see. An admin can also export feedback as CSV from Admin > Feedback > Feedback log. Inference: one request to the former manager can cover every cycle. The page does not say whether a manager can still download the packets after the person's deactivation; admins can still open a deactivated user's reviews.

### Culture Amp

- **Self-reflections.** Culture Amp's employee guide gives these steps: Performance > Self-Reflections, open the cycle with the arrow next to View, choose "View and edit your self-reflection" under You, then Export PDF. Each self-reflection exports on its own. Another Culture Amp page lists self-reflections among the features without an export, so this option may not be available; then save the page as PDF. Active and closed cycles are on Performance > Reviews.
- **Goals.** On the Goals page, Export Goals at the top right of each tab downloads the goals the person can access as a CSV file. Remove view filters first; the export covers two years by default.
- **Pages without an export.** Culture Amp has no built-in employee export for manager reviews, Anytime Feedback, Shoutouts, 1-on-1s and development plans. It suggests the browser's print dialog (Cmd + P on Mac, Ctrl + P on Windows) and Save as PDF, which captures the current screen data, and screenshots for small sections. Received feedback is under Feedback > Anytime Feedback, with the filter "Feedback received by you".
- **When the account ends.** The Culture Amp pages under Sources do not say what a deactivated user can still open.
- **Managers and admins.** A manager can export individual manager reviews as PDF. Managers cannot export the peer and upward feedback their direct reports received, though they may share screenshots of it. CSV exports of manager reviews and of peer and upward feedback are only for administrators and people with Performance permissions. Inference: the person can ask their former manager for a PDF of each manager review.

### Other tools

Look in the same places: a download on the review itself, an export on the goals page, and Save as PDF for the rest.

Done when every document the person chose to save is in `local-only/`, or the person has decided to skip it.

## After access ends

The person can ask HR or their former manager for the documents. The request names the review cycles and what each should include: the review results or packet, goals, and feedback received. The tool sections say what managers and admins can export. In Leapsome, deleting a user cannot be undone, and Leapsome then keeps no record of their information. Inference: after a deletion, HR may no longer be able to provide the reviews, so the person asks soon.

Offer to draft the request in the conversation, with `[Name]` as the placeholder for the recipient. The person sends it.

Done when the person has a request ready to send, or has decided to go without this source.

## Read

From each review cycle, read:

- goals and key results, with what was achieved, how it was measured, and who recorded it (the person or a reviewer);
- strengths and competency ratings, as themes;
- feedback from peers and the manager: what they praised, and what they asked for more of;
- promotions, title changes and scope changes, with dates.

## Turn into themes

Each item becomes a theme; [harvest](../harvest.md) step 6 turns the themes of all sources into records together.

- Achieved goals with measurable results become themes for `work` records. They count as `verified (performance review)` when the manager's or a peer's part of the review confirms the result, or the review cites a measurement such as a dashboard or report. A goal status or figure the person entered, and everything in a self-assessment, is self-reported, as in the [documents](documents.md) adapter: the basis is then `mixed` or `self-reported` and names that part.
- Recurring praise becomes themes for `recognition` records: the theme in clean words and who said it by relationship ("praised by the manager and two peers for clear technical writing, three review cycles"), with no names and no quotes. The relationship lets the person pick the right colleague later for a recommendation request.
- Title changes and promotions, with their dates, go into the themes file next to the themes; [harvest](../harvest.md) step 6 adds them to the Titles line and the title sections ([document format](../document-format.md)).
- If the person plans to ask colleagues for recommendations, suggest they do it soon, while the colleagues are still easy to reach. The `linkedin-profile-coach` skill drafts LinkedIn requests from this document.

## Leave out

Names of reviewers and colleagues, quotes, ratings on the employer's internal scale ("4 of 5" means nothing outside), compensation, and anything about other people's performance.

## Sources

Checked 2026-10-30. help.leapsome.com blocked automated reading, so the Leapsome articles were read through Leapsome's public help-center API, and their dates are its `updated_at` field. Lattice dates are those shown on the pages. Culture Amp shows mostly relative dates, given as they read that day.

Leapsome:

- [Writing a self-assessment](https://help.leapsome.com/hc/en-us/articles/360011850234-Writing-a-self-assessment), updated 2026-09-23
- [Finding past assessments that you've completed for others or others have completed of you](https://help.leapsome.com/hc/en-us/articles/4405447290129-Finding-past-assessments-that-you-ve-completed-for-others-or-others-have-completed-of-you), updated 2025-12-10
- [How to set up a review (step by step)](https://help.leapsome.com/hc/en-us/articles/115004136154-How-to-set-up-a-review-step-by-step), updated 2026-09-14
- [Understanding export labels in Reviews](https://help.leapsome.com/hc/en-us/articles/9836741169565-Understanding-export-labels-in-Reviews), updated 2025-08-06
- [Sharing Instant Feedback](https://help.leapsome.com/hc/en-us/articles/4413159867793-Sharing-Instant-Feedback), updated 2024-09-10
- [Working with goal analytics](https://help.leapsome.com/hc/en-us/articles/360019686858-Working-with-goal-analytics), updated 2025-04-22
- [Deactivating, deleting and reactivating users](https://help.leapsome.com/hc/en-us/articles/360018691594-Deactivating-deleting-and-reactivating-users), updated 2024-10-17
- [Leapsome MCP (Model Context Protocol)](https://help.leapsome.com/hc/en-us/articles/37637705235229-Leapsome-MCP-Model-Context-Protocol), updated 2026-10-02

Lattice:

- [Download Your Review Packet](https://help.lattice.com/en-us/articles/15179662-download-your-review-packet), dated 2026-09-24
- [Bulk Export PDF Review Packets](https://help.lattice.com/en-us/articles/15178376-bulk-export-pdf-review-packets), dated 2026-09-24
- [Export Goals as a CSV](https://help.lattice.com/en-us/articles/15178659-export-goals-as-a-csv), dated 2026-09-25
- [View Feedback Given and Received](https://help.lattice.com/en-us/articles/15179422-view-feedback-given-and-received), dated 2026-09-23
- [Export Feedback via a Custom CSV](https://help.lattice.com/en-us/articles/15179535-export-feedback-via-a-custom-csv), "Updated over 3 weeks ago" on 2026-10-30
- [Access a Deactivated User's Data](https://help.lattice.com/en-us/articles/15178321-access-a-deactivated-user-s-data), dated 2026-09-25

Culture Amp:

- [Employee Guide to Performance Reviews](https://support.cultureamp.com/en/articles/10423247-employee-guide-to-performance-reviews), "Updated over a week ago" on 2026-10-30
- [Exporting Your Personal Data From Culture Amp](https://support.cultureamp.com/en/articles/11506508-exporting-your-personal-data-from-culture-amp), dated 2026-07-23
- [Exporting Performance Data](https://support.cultureamp.com/en/articles/7048413-exporting-performance-data), "Updated over 3 weeks ago" on 2026-10-30
- [Give and Request Anytime Feedback](https://support.cultureamp.com/en/articles/11797451-give-and-request-anytime-feedback), "Updated this week" on 2026-10-30
