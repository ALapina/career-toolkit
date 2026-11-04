---
type: llm
focus: { source: file, path: linkedin-profile/audit.md }
weight: 1
---

The prompt gives no screenshots, so linkedin-profile/audit.md marks as "can't tell" what only a screenshot shows, including the company Page link of each position, the skills linked to each position, the Top Skills shown with About, and the profile photo. It rates none of these 'good', 'needs work' or 'missing'. A row that also covers other parts, such as the row for each position, may carry another status for its title or dates, as long as it says which of the parts above could not be checked. Listing them on the 'Sections the inputs did not cover' line as well is fine.

The rules behind this check are `experience-3`, `skills-3` and `skills-5`, with step 5 of the skill's LinkedIn export guide.
