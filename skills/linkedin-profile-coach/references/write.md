# Write

Draft paste-ready texts for the sections the person agreed to in the audit, and a checklist of the fields and settings they change by hand.

## Draft

1. **Settle the person's choices.** Some rules leave a decision to the person. Ask the ones the agreed sections need and neither `audit.md` nor `progress.md` settles, in one round: the standard title of each position (`experience-1`), how far back Experience goes (`experience-7`), a career break entry (`career-break-2`), a mention of the layoff (`career-break-4`), an interim job (`career-break-5`), older gaps (`career-break-6`), graduation years (`sections-8`) and, while the person is still employed, whether About names the search (`about-2`). Content a rule adds only when the person wants it, such as a layoff sentence or a status phrase in the headline, waits for a yes. Mark every other open choice in the draft's Why. Done when each choice has the person's answer or is marked open.

2. **Create one draft per agreed section** in `drafts/`, from the skill's `templates/draft.md`:
   - `headline.md`: two or three variants (`headline-5`), each written to `headline-1` to `headline-4`.
   - `about.md`: one About text with two or three variants of its opening lines (`about-1`), written to `about-1` to `about-7`. Put each variant in its own `about` block as the complete text, opening plus the shared rest, so the script checks each full length. A mention of the layoff follows `career-break-4`.
   - `experience-<employer>-<title>.md`: one per position the person keeps (`experience-2`, `experience-7`), with the employer and title in lowercase and hyphens, such as `experience-tailspin-toys-backend-engineer.md`. Add the start year when one employer gave the same title twice. Each follows `experience-1` to `experience-9`; the last position also follows `career-break-1`, and an interim job `career-break-5`.
   - `career-break.md`: the entry for the time since the last job (`career-break-2`, `career-break-3`). The type to pick goes under "In the form", and the description in a `position-description` block, since a career break is an Experience entry. An older gap the person asks for gets `career-break-<start year>.md` (`career-break-6`).
   - `skills.md`: the `skills` block, one skill per line in the display order (`skills-4`), with the Top Skills when the person's About editor offers them (`skills-5`), the skills to tick per position and the entries to tick per skill (`skills-3`), and each endorsed skill the draft would delete, rename or translate (`skills-7`). The list follows `skills-1`, `skills-2`, `skills-6` and `skills-10` to `skills-12`.
   - `featured.md`: the items to add and the items to remove (`featured-1` to `featured-4`), with a label for any synthetic media (`rules-9`).
   - `sections.md`: one heading per other section the person agreed to, such as Education (`sections-3`, `sections-8`), Licenses and certifications (`sections-4`), Courses (`sections-4`), Languages (`sections-5`), Projects (`sections-6`) and Services (`sections-10`).

   `settings.md` takes the shape in step 4, and the messages in step 6 go in files of their own. Done when every agreed section has its file, named as above.

3. **Write each draft from the evidence.**
   - Fill the Current part as the template says. When no input holds a section's text, ask the person to paste it. The current text stays beside the proposal, so the person can go back (`rules-5`).
   - Put paste-ready text in fenced blocks tagged with the field: the fence opens with three backticks and the tag at the start of a line, with nothing after the tag, and closes with three backticks at the start of a line. The script fails any other field fence as "not checked". `scripts/check_drafts.py` checks the tags `headline`, `about`, `position-title`, `position-description` and `skills`, which holds one skill per line. Give other paste-ready text a short tag of its own, such as `education`.
   - Before drafting a section, read the rules its bullet in step 2 cites, in the area files listed in the Areas table of [best practices](best-practices.md#areas), and apply what each rule says the write phase does.
   - Take every claim from an approved evidence record (`rules-2`), with the verb its My role allows in [the document format](document-format.md). Prefer verified records for the headline, the opening of About and the latest position. A Team size is the team the work happened in, never people the person led (the document format).
   - Place each keyword from the audit's add list where its evidence sits (`search-1` to `search-3`).
   - Follow the house style, the `style-` conventions in [best practices](best-practices.md#this-skills-own-conventions-area-style-).
   - When the person points to a profile they admire, take only its patterns (`rules-8`).

   Done when every agreed draft is written, each rule its bullet cites is applied, and its Why names those rules and the evidence ID behind each claim.

4. **Draft `settings.md`**, the person's checklist of the fields and settings they change by hand. List every item the audit flagged and every step below that applies, under these headings and in this order. Each item is a checkbox line with the field or setting, the screen where its rule names one, the value or the person's choice, and the rule ID. Explain the choices a rule leaves to the person, such as the Industry (`search-6`) or the Open to Work audience (`opentowork-3`), and record the answers.
   1. **First.** A personal primary email (`settings-1`), then LinkedIn's workplace verification while the work email still works (`settings-3`).
   2. **Before pasting.** Profile-update notices off (`settings-10`), with a note that accepting a recommendation sends its own update (`recommendations-7`) and LinkedIn does not say whether the setting stops it. The Data for Generative AI Improvement setting, the person's choice (`rules-10`), and the primary profile language when it is not English (`sections-2`).
   3. **With the paste.** The drafts, each position with the "In the form" part of its draft. Then the other profile fields and settings: the name fields (`rules-4`), location (`search-4`), Industry (`search-6`), contact info and email visibility (`sections-1`, `settings-6`), photo and cover image (`photo-1`, `photo-3` to `photo-5`), public profile and custom URL (`url-1` to `url-3`), Off-LinkedIn visibility (`url-5`), the primary profile button (`sections-11`), and any other section of the profile level meter still missing (`search-5`).
   4. **Once the new headline, About and latest position are live.** Open to Work with its preferences, audience and later changes (`opentowork-1` to `opentowork-3`, `opentowork-5`), InMail and Open Profile (`settings-2`), sharing the profile when applying (`settings-4`), the resume on LinkedIn (`settings-5`) and the resume lines to update (`experience-6`), target companies (`settings-7`) and other-language versions (`sections-7`).
   5. **When applying.** By hand and at a steady pace (`settings-9`), with an answer to every recruiter InMail while Open to Work is on (`opentowork-4`).
   6. **Any time.** The other flagged items, such as job alerts (`settings-8`), Jobs data in the EEA or Switzerland (`settings-11`) and the viewer list (`settings-12`).

   Write the Open to Work job titles and locations as drafted text, with the titles one per line in a block tagged `open-to-work-titles` (`opentowork-2`). Done when every flagged field and setting has its checkbox line under its heading, with its rule ID, and the Open to Work job titles are drafted.

## Check

5. **Check every draft.**
   - Run `python3 <skill>/scripts/check_drafts.py <workspace>/drafts`. It fails a block only when the block is empty or over a limit LinkedIn documents; position titles and descriptions have none, so for them it reports the length only (`experience-9`). Shorten what fails, rewrite what it flags, and record each block's length in the draft's Checks. It skips tags it does not know, such as `open-to-work-titles`, so read those blocks against the house style yourself. In light mode without code execution, count by hand and use the phrase list at the top of the script.
   - Every claim in a block has its evidence ID in the Why and stays within its record: a verb its My role allows (`style-4`), the record's own figures with their qualifiers such as "about", and no scope or team size the record does not hold. A figure you derive, such as a percentage from two times, keeps the qualifier and shows its arithmetic in the Why.
   - Run the NDA pass from the [confidentiality procedure](confidentiality.md) over `drafts/`.
   - Every self-reported claim stays defensible: list each claim the drafts take from a self-reported record or from the self-reported part of a mixed record, and ask the person whether they can explain it in an interview. Rephrase or drop what they cannot.

   Done when the script reports no failure, every claim has its evidence ID, the NDA pass is clean, and the person has confirmed or dropped every self-reported claim.

## Hand over

6. **Draft the messages the person asks for.** Recommendation requests and the other messages that [recommendations](recommendations.md) drafts, endorsement asks included (`skills-9`), go in `drafts/recommendation-requests.md`. The person sends the requests after pasting the positions (`recommendations-4`). Short yes and no replies to recruiter InMails go in `drafts/recruiter-replies.md` (`opentowork-4`). Run the NDA pass over both files. Done when each message the person asked for is drafted and clean.

7. **Hand over** the drafts and `settings.md`, in light mode in the workspace ZIP. Tell the person:
   - why they paste and set everything by hand, with both reasons from [Hand-paste only](../SKILL.md#hand-paste-only);
   - to paste back any draft they changed before they paste it into LinkedIn, so you can check it as in step 5 while it is still private;
   - to work through `settings.md` in its order;
   - in each position's form, to set what its draft lists under "In the form": the end month and year, with "I am currently working here" cleared (`career-break-1`), the employment type (`experience-2`), the company Page (`experience-3`), the skills to tick from `skills.md` (`skills-3`), and the notification toggle, before saving (`experience-8`);
   - to watch the counter in each editor while pasting (`headline-3`, `about-6`, `experience-9`);
   - that pasted text is public (`rules-10`), and that search engines may take weeks or months to show it (`url-4`);
   - that the LinkedIn export and each draft's Current part keep the old texts, and to copy any text found in neither before replacing it (`rules-5`);
   - to save their own Featured files and links before removing them (`featured-4`);
   - to bring new evidence, such as a course, a certificate or a freelance project, to another write round (`search-8`, `skills-6`).

   Done when the person has every draft and knows why and how they paste and set everything by hand.

8. **Update `progress.md`** with the sections drafted and, as the next step, the final check in step 9. While the person is still employed, the next step also reminds them to end the last position after their last day (`career-break-1`). Done when `progress.md` names the sections drafted and the final check.

## Final check

9. **After the paste**, ask the person to paste the final texts back, the Skills list and the Open to Work job titles included. Check them against the drafts and the work history documents as in step 5: claims with no evidence record, verbs stronger than the record's role, numbers or scope that changed, skills with no record, limits and the NDA pass. Then:
   - tell the person to keep the profile current while they search (`search-8`).

   Report what you find; the person decides. Done when the pasted texts are checked and the person knows to keep the profile current.

The write phase is done when steps 1 to 8 are done: every agreed section has a checked draft, `settings.md` holds every flagged field and setting in the order the person acts, and the person knows why they paste and set everything by hand. Step 9 runs when the person comes back after pasting.
