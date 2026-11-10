# Audit

Compare the person's current profile with the sourced rules in [best practices](best-practices.md), with their targets and with their approved evidence, and write `audit.md`.

## Get the profile

1. **Get the LinkedIn data download.** Follow [LinkedIn export](linkedin-export.md) steps 1 to 4, from step 3 when the person already has the download: the person requests their profile data, and only the profile files go into `linkedin-export/`. If the person cannot wait for the download, use the fallbacks in that guide's step 6.

   Done when the guide's step 4 is done, or its step 6 when a fallback replaces the download.

2. **Ask for what the download leaves out**, in one message:
   - the screenshots in [LinkedIn export](linkedin-export.md) step 5;
   - everything in the "Ask in step 2" column of the checklist in step 3. The rules of each item say where to look;
   - when Featured, a position or the cover image holds images or video, whether any of them is AI-made or altered to show a person saying or doing what they did not (`rules-9`).

   Leave out what the files from step 1 already hold. Ask for each screenshot to be cropped as the guide's step 5 says. The person may skip any item. Record each email address only by its state: work or personal, and who can see it. This step can start while the download is on its way.

   Done when the person has sent, answered or skipped every item on these lists.

## Check

3. **Go through every checklist item** in the table below. For each, write one line in `audit.md`: a status (`good`, `needs work`, `missing`, `can't tell`), the rule IDs behind the judgement, what to change, and a priority. An item without input is `can't tell`.

   In the Rules column, a prefix such as `headline-` stands for every rule of that area, and an ID for that rule alone. Apply what each rule says the audit checks. In every item, also apply `rules-2` (true claims and affiliations), `rules-3` (only what the person may share) and `rules-8` (no text copied from another member), and `rules-9` where the item holds images or video. The `style-` conventions apply to the drafts only.

   A rule that sets a priority decides it. These rules set `high` whatever the section: `rules-3` and `featured-1` (confidential detail, or material the person may not share), `rules-4` (anything but the name and pronouns in a name field), `career-break-1` and `headline-2` (an ended job still shown as current), `sections-1` (a work address as the primary email) and `url-1` (the public profile switched off). Others set a lower priority, such as `rules-4` for a credential after the name and `skills-8` for endorsement gaps. Without a rule's priority:
   - `high`: decides whether recruiters find or can reach the person, as InMail does (`settings-2`), or shapes the first impression: the headline, the top of About, the current or last position, skills, Open to Work;
   - `medium`: affects how convincing the profile is once opened;
   - `low`: polish.

   | Item | Rules | Ask in step 2 |
   |---|---|---|
   | Name fields | `rules-4` | |
   | Photo and cover image | `photo-` | |
   | Headline | `headline-` | |
   | Location | `search-4` | where the person is based now, unless setup recorded it |
   | Industry | `search-6` | |
   | Contact info and primary email | `sections-1`, `settings-1`, `settings-6` | whether the primary email is a work or a personal address, who can see it, and the websites in Contact info |
   | Custom profile URL and public profile | `url-` | the state of Off-LinkedIn visibility |
   | Primary profile button | `sections-11` | |
   | Open to Work | `opentowork-` | recruiter InMails waiting for a reply, and any email from LinkedIn asking whether the person is still open to work |
   | Services, when the targets include freelance or contract work | `sections-10` | the services listed, as a screenshot or pasted text |
   | About, starting with the part shown before "see more" | `about-` | |
   | Featured | `featured-` | |
   | Each position, one line per position: title, company Page, dates, description, linked skills | `experience-`, `skills-3` | the current resume, if the person wants it compared |
   | Gaps and the end of the last role, and any mention of how it ended | `career-break-` | |
   | Education, with graduation years as information | `sections-3`, `sections-8` | |
   | Licenses, certifications and courses | `sections-4` | |
   | Projects | `sections-6` | |
   | Skills: count, names, order, Top Skills, endorsements, fit with targets | `skills-` | a screenshot of the Skills section, with the endorsement setting if the person wants endorsements; any partner tool the person uses on a personal account |
   | Recommendations: count, relationships, positions covered, fit with targets, clean as public text | `recommendations-` | the position each recommendation covers |
   | Languages | `sections-5` | |
   | Other sections: Volunteering, Organizations, Causes, Honors, Publications, Patents, Test Scores | `rules-2`, `rules-3` | |
   | Political signals in any section, as information | `sections-9` | |
   | Profile language and other-language versions | `sections-2`, `sections-7` | |
   | Keywords across the profile, filled in step 4 | `search-1`, `search-2`, `search-3`, `search-7`, `search-8` | job match, or the skills-match insight, on two or three target postings |
   | Search appearances | `search-9` | a screenshot of Search appearances |
   | Account, privacy and job-search settings, one line per setting | `settings-2` to `settings-5`, `settings-7`, `settings-8`, `settings-10` to `settings-12` | whether InMail is on, and Open Profile with Premium; LinkedIn's workplace verification, when the profile shows none; saved resumes and resume sharing; companies signalled with I'm interested; job alerts; the viewing mode; in the EEA or Switzerland, whether Jobs is connected to LinkedIn Services |

   - Leave out an item whose condition does not hold, such as Services without freelance or contract targets.
   - Profile completeness has no item of its own. When a section that `search-5` names is empty, that section's item is `missing`, `high`, and cites `search-5` with its own rule.
   - For the photo and the cover image, check only what the `photo-` rules name: presence and recency (`photo-1`), likeness (`photo-2`), visibility (`photo-3`) and the cover image's content (`photo-5`). The person's appearance is never assessed.
   - Graduation years (`sections-8`) and political signals (`sections-9`) are information for the person. They never make an item `needs work`.

   Done when every item that applies, Keywords aside, has a line with a status and a priority, every `needs work` and `missing` line cites its rule IDs, and every item without input is `can't tell`.

4. **Match keywords** when `targets.md` has postings or roles. Sort every term of its keyword table into three lists (`search-1`):
   - **keep**: in the profile's text and backed by an approved evidence record. A record backs a term when its Action, Technologies or Skills shown name the term or a plain synonym of it; a related term in the same field does not count;
   - **add**: backed by an approved record, but missing from the headline, About and the position descriptions. A term found only in the Skills list or in Featured counts as missing (`search-2`). Name the evidence IDs and the section where the term belongs;
   - **no evidence yet**: with no record behind it, whether or not the profile names it. The person can take them to `work-history-harvest`, whose interview turns real experience into records, or leave them out of the profile.

   A qualification that job match marks as missing joins the add list when a record backs it, and the no-evidence-yet list otherwise (`search-7`). Flag a term repeated across sections without new content (`search-3`). Then write the Keywords line of the checklist.

   Done when every term of the keyword table sits in one list, every keep and add term names its evidence IDs, and the Keywords line is written; without targets, that line is `can't tell`.

5. **Write `audit.md`** from `templates/audit.md`. Open it with the five changes that would make the biggest difference, in order. Run the NDA pass from the [confidentiality procedure](confidentiality.md) over it.

   Done when `audit.md` follows the template, the five biggest changes open it, and the NDA pass is clean.

6. **Walk the person through it** and agree which sections the write phase covers.

   Done when the scope is under "Agreed scope for writing": agreed by the person, or marked as your proposal when they left the choice to you.
