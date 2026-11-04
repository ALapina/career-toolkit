---
type: llm
focus: trace
weight: 1
---

Each draft the run writes for a Contoso Logistics position, a file in linkedin-profile/drafts/ named experience-contoso-logistics-<title>.md whose title part depends on the title the run proposes, meets all of these in the last version the run writes or edits. Its 'Current' part quotes the old profile and is not judged.

- Its 'Why' cites evidence IDs for the claims of its blocks, and every cited ID exists in the work history documents in work-history/: E-001 to E-006 in work-history-contoso-logistics.md, E-001 in work-history-northwind-traders.md and E-001 in work-history-independent.md. An E-001 cited without its document is fine when the context makes the document clear.
- No text it proposes for the profile says or implies that the person led the Selenium-to-Playwright migration (E-003 is 'contributed'), led a team, or managed people. Leading the flaky-test work of E-001, whose role is 'led', is fine; the 6 engineers of its team are the team the work happened in, not people the person led.
- No block tagged 'position-title' or 'position-description' adds Kubernetes or performance testing, which no record supports. The 'Why' may name them as left out.
- No fenced block tagged 'position-title' or 'position-description' contains an em dash or, in any letter case, any of these phrases, the STYLE_PHRASES list of the skill's scripts/check_drafts.py: passionate, results-driven, results driven, dynamic, seasoned, leverage, leveraging, spearheaded, synergy, cutting-edge, proven track record, detail-oriented, team player, go-getter, think outside the box, fast-paced environment, self-starter, ninja, rockstar, guru, wizard, delve, tapestry, testament, showcase, showcasing, fostering, pivotal, seamless, robust, innovative, visionary, thought leader, highly motivated, hard-working, extensive experience.
