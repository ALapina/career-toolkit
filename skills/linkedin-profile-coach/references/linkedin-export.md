# LinkedIn export

How the audit gets the person's current profile: from their own LinkedIn data download, plus screenshots of what the download leaves out. [Audit](audit.md) steps 1 and 2 point here. At the end, every audit checklist item has an input or is listed as not covered, and `linkedin-export/` holds only the person's profile files.

## 1. Why the download

Tell the person, in two or three sentences:

- The download is their own data, through LinkedIn's own export. LinkedIn's Privacy Policy gives members the right to a copy of the personal data they provided, in machine-readable form. The policy points to this download.
- With it, the skill never needs to open LinkedIn, which [Hand-paste only](../SKILL.md#hand-paste-only) rules out.
- It holds the profile as it is today, such as each position's title and description. The drafts quote it as the current text. It also stays as a copy of the old texts once the person pastes new ones.

Done when the person knows why the skill asks for the download and has agreed to request it, or has picked a fallback from step 6.

## 2. Request the download

Unlike work systems, the LinkedIn account stays with the person after the job ends. LinkedIn's User Agreement says the account belongs to the member, also as between them and their employer. Check two things before the request:

- **Primary email.** LinkedIn emails the download link to the account's primary email address. Inference: when that is a work address the person is about to lose, the link may never reach them. Suggest making a personal address primary first, under "Me" → "Settings & Privacy" → "Sign in & security" → "Email addresses". Only a verified address can become primary.
- **Computer.** LinkedIn says the download is not available on mobile. It advises downloading only on a personal computer, not a public one. When `progress.md` says the computer belongs to the employer, pass this advice on and let the person choose the computer.

Give the person these steps in their language. Keep LinkedIn's labels in English, in quotes, and say where each one sits: their screen may show the labels in their own language. LinkedIn is testing new Profile and More menus, so any path in this guide may differ on the person's screen. Ask what they see and adapt the path.

1. On a computer, sign in to LinkedIn.
2. Click "Me" at the top of the page, then "Settings & Privacy".
3. Click "Data privacy" in the menu on the left.
4. Under "How LinkedIn uses your data", click "Download your data". Some LinkedIn pages call it "Get a copy of your data".
5. Choose the option to select specific data, rather than the larger archive. Select the categories about your own profile: Profile, Positions, Education, Skills, Certifications, Languages and Recommendations Received. Leave every other category unselected, such as Recommendations Given, Endorsements, Invitations and Connections.
6. Click "Request archive". If LinkedIn asks for your password, type it into LinkedIn's page.
7. LinkedIn emails a link to your primary email address within minutes. Download the file: it stays available for 72 hours.

The password goes into LinkedIn only, never into this conversation. LinkedIn's help names the data categories but not the options on the screen, so the screen may group them differently. The person selects the ones about their profile. If they can find only the larger archive, it works too, more slowly; step 3 keeps the rest out of the workspace.

Recommend the specific data. LinkedIn lists every category the audit reads under "Available within 10 minutes", and leaving the other categories out keeps other people's data out of the download. The larger archive adds connections, messages, contacts and account history. LinkedIn's text says it arrives within 24 hours while its own table says 48, so allow 48 hours. Of the profile data, only Volunteering, Test Scores and Profile Summary come with the larger archive alone. The audit needs none of them. When the person wants volunteering or test scores reviewed, ask them to paste those entries.

If the email does not come, ask the person to check their spam folder and which address is primary. Inference: once the 72 hours pass, the person requests the download again; LinkedIn does not say what happens after that. When the person will download later, write the request date under "Next step" in `progress.md`.

Done when the person has requested the profile data, or picked a fallback from step 6, and knows the link goes to their primary email and stays available for 72 hours.

## 3. Put only profile files in the workspace

`linkedin-export/` holds only files about the person's own profile. LinkedIn's help names data categories, not files, and says nothing about their format. Match each file to a category by its name, ignoring case, spaces, underscores, hyphens and the extension. A close variant, such as a singular, counts. LinkedIn sends only the categories that apply to the account, so a profile without certifications gets no certifications file.

The keep list holds the files named after these categories:

- the profile and its sections: Profile, Positions, Education, Skills, Certifications, Languages, Recommendations Received, Projects, Courses, Honors, Publications, Patents, Organizations, Volunteering, Test Scores, Causes You Care About;
- two extras about the person, when present: Profile Summary and Job Seeker Preferences.

Every other file stays out of the workspace, unopened. Some hold other people's names and words: connections, messages, invitations, imported contacts, endorsements, recommendations given. The rest is account data the audit does not use, such as logins, search queries, email addresses, phone numbers, job applications, saved answers and resume data. Recommendations Received holds other people's names and words too. It stays because it is part of the person's own profile, and step 4 says how to use it. When you cannot tell where a file belongs, ask the person, and leave it closed until they answer.

- **Full mode.** Ask where the download is. If it is a compressed file, list its contents without extracting it, then extract only the files on the keep list into `linkedin-export/`. If the person already extracted it elsewhere, copy only those files. Remind the person to delete the download and any extracted folder once they no longer need them. When `progress.md` says the computer goes back to the employer, that is before the last day.
- **Light mode.** Ask the person to upload only the files on the keep list. If they upload the whole download, list its contents and open only those files. Tell them the rest stayed unopened.

**The whole download is already in `linkedin-export/`.** List the file names only and sort them by the rules above. Show the person the files that do not belong and why. Offer to move them to a folder outside the workspace that the person names, with the compressed file if it is there. Move them once the person agrees. Deleting them is the person's call. If the person wants them to stay, leave them there, closed, and note that choice in `progress.md`.

Done when you have opened no file from the download outside the keep list, and `linkedin-export/` holds only files on the keep list or the person has chosen to keep the others there.

## 4. Read the files

LinkedIn does not document the column names either. Read each kept file's header row first and map the columns by meaning. Note the date of the download for the Inputs line of `audit.md`.

| Audit checklist item | Where to look | How to read it |
|---|---|---|
| Headline; About | Profile file: a headline and a summary column | LinkedIn's help describes this category as basic biographical data: name, address, birth date, zip code. The sample profile in LinkedIn's API documentation also has Headline and Summary fields, so look for those. Without them, ask the person to paste the headline and the About text; the top-of-profile screenshot in step 5 shows the headline as readers see it. |
| Location; Industry | Profile file: a location column and an industry column | LinkedIn's help does not name them; the API sample calls them Geo Location and Industry. Copy only the columns the audit uses into workspace files. Birth date and address stay in the export. |
| Each position; gaps and the end of the last role | Positions file: company, title, description, location, start and end dates | LinkedIn's API documentation treats a position with no end date as current. Inference: an empty end date here means the profile still shows that position as current. Compare the last position's title and dates with the title and employment period in `progress.md`. LinkedIn's help does not say whether this file holds career breaks or the skills linked to each position; step 5 covers both. |
| Skills | Skills file: the skills the person added | Count the skills and compare them with `targets.md`. LinkedIn does not say whether the order matches the profile, so top skills come from the About screenshot. |
| Education; Licenses, certifications and courses; Languages | their own files | Certifications carry the issuing authority, dates and license number. |
| Recommendations | Recommendations Received file: writer's name, company, text, date | Count them and note the newest date. LinkedIn lets members hide a received recommendation, and its help does not say whether the file includes hidden ones, so ask the person whether they hid any. Ask the person how they worked with each writer: manager, peer, someone they managed, client, another team. In `audit.md`, describe each writer by that relationship. Name the writer's company only when it is one of the person's own employers, as in "manager at Contoso Logistics". A client's name fails the front-page test. The texts and the writers' names stay in the export. |
| Open to Work, partly | Job Seeker Preferences file, when present | LinkedIn describes it only as the member's chosen job preferences. Inference: it may hold what LinkedIn's API lists for the same data: job types, locations, industries, company sizes, dream companies, job titles and activity level. That list has no visibility field, so the Open to Work screenshot is still needed. |
| No checklist item | Profile Summary file, larger archive only | LinkedIn's AI-written summaries of the profile, which it may show members when it suggests the person as a connection. Compare them with the targets when the person has the file. |

Four checks before you move on:

- **Missing files.** A missing file usually means an empty section, since LinkedIn sends only the categories that apply. When the section matters for the audit, confirm with the person: they may not have selected it.
- **Broken characters.** LinkedIn says its CSV export of connections does not support all characters, and names Chinese, Japanese and Hebrew. Inference: profile files may share the limit. Where text in another script looks broken, ask the person to paste that section.
- **A second-language profile.** Ask whether the person keeps a profile in another language. LinkedIn does not say whether the download includes it. Ask them to paste it when the audit should cover it.
- **Names in the current text.** The current About or a position description may name a client, a colleague or an internal system. Flag each such text in the audit, and describe it in `audit.md` without the name.

List every checklist item the files leave uncovered. Step 5 covers most of them. Whatever is still uncovered after step 5 goes on the "Sections the inputs did not cover" line of `audit.md`.

Done when you know, for every audit checklist item, which file and columns hold its input, or that it needs step 5.

## 5. Screenshots of what the download leaves out

LinkedIn lists no download category for the profile photo, the cover image or the Featured section, and the settings the audit checks come from the screen too. Ask the person for the screenshots below. They take them and attach them to the conversation. In full mode they can instead save them in a folder and give you its path. Ask them to crop each one to the part the table names. That leaves out other people's names and photos, for example in side panels, and any pay expectations.

| Screen | How to get there | What the audit reads | Checklist item |
|---|---|---|---|
| Top of the profile | "Me" → "View Profile" | photo and cover image, the headline as shown, current position, location, the #OpenToWork frame or the Open to Work box | Headline; Photo and cover image; Location; Open to Work |
| About | the About section of the profile, before clicking "see more" | the opening that readers see; Top skills, if the section shows them | About; Skills |
| Featured | the Featured section of the profile, every item in view | each item's type and title | Featured |
| Experience | the Experience section, the last two or three positions | any skills shown under each position; career break entries | Each position; Gaps |
| Public profile & URL | "Me" → "View Profile" → Edit next to "Public profile & URL" | the custom URL, under "Edit your custom URL"; the public profile settings | Custom profile URL and public profile |
| Open to Work | "Jobs" → "Preferences" → "Open to work", or Edit on the Open to Work box of the profile | job titles, location types, locations, start date, employment types, visibility | Open to Work |
| Job seeking preferences | "Me" → "Settings & Privacy" → "Data privacy" → "Job seeking preferences" | every setting on the screen and its state, such as "Share your profile when you click Apply for a job" | Account, privacy and job-search settings |
| Share profile updates | "Me" → "Settings & Privacy" → "Visibility" → "Visibility of your LinkedIn activity" → "Share profile updates" | on or off | Account, privacy and job-search settings |

- **No screen to take.** LinkedIn hides an empty Featured section. When the person says Open to Work is off, record that. Record both for the audit; they need no screenshot.
- **The photo.** The screenshot shows the photo as the person sees it, and a visibility setting can hide it from viewers outside a chosen group. Ask whether they limited who can see it. LinkedIn offers 1st-degree connections only, your network, all LinkedIn members and anyone, and the default is anyone. Ask roughly when the photo was taken, for the recency check. Check only what the `photo-` rules name, as [audit](audit.md) step 3 lists them; the person's appearance is never assessed.
- **About before "see more".** LinkedIn does not document how much of About shows before "see more". The screenshot shows where the person's own screen cuts it.
- **Not an audit item.** LinkedIn says it trains its generative AI models on profile data, such as positions, education, skills and recommendations. Its setting "Data for Generative AI Improvement" stops that use going forward, not training already done. Some regions, the UK among them, have their own rules. Mention it once while the person is in their settings; the choice is theirs.

Done when the person has sent each screenshot, or has told you that a screen does not apply or that they skip it. Every item left without input is `can't tell` in the audit.

## 6. Fallbacks without the download

Use these when the person cannot wait for the download or cannot get it. Then take the screenshots in step 5 as usual.

**Save to PDF.** On a computer, the person goes to "Me" → "View Profile", clicks "More" or "Resources" in the introduction section, and selects "Save to PDF". LinkedIn sets these limits:

- it is not in the LinkedIn mobile app;
- it is available only when the profile language is English;
- it works correctly only when the language setting is English too, and it supports only English characters;
- it allows 200 PDF downloads a month, the person's own profile and other members' together;
- LinkedIn warns it may not be accessible to all members.

LinkedIn calls the PDF the entire profile in a resume format, but lists no sections. Read the PDF, note which sections it holds, and list the rest as not covered. For a profile in another language, or names in another script, use the download or pasted text instead.

**Pasted text.** The person copies each section from their profile and pastes it into the conversation: headline, About, the last two or three positions with title, company, dates and description, then skills, education, certifications and languages. For recommendations, the count, the newest date and each writer's relationship are enough.

The skill leaves two other routes aside:

- LinkedIn's Member Data Portability API is open only to members whose profile location is in the EU, EEA or Switzerland, and it needs a developer app and an access token. The download covers the same profile categories without either.
- LinkedIn's Resume Builder is not available to all members, LinkedIn says, and its help article returned "not found" on 2026-10-30.

Done when every section the audit covers has its input in the PDF, pasted text or a screenshot, or is listed as not covered.

## Sources

LinkedIn pages, checked on 2026-10-30. A relative "Last updated" date is counted back from that day.

- [Download your data](https://www.linkedin.com/help/linkedin/answer/a1339364), updated ≈2026-10. Steps 2 to 5.
- [Export connections from LinkedIn](https://www.linkedin.com/help/linkedin/answer/a566336/export-connections-from-linkedin), updated ≈2025-10. Steps 2 and 4.
- [Manage your email address](https://www.linkedin.com/help/linkedin/answer/a519904), updated ≈2026-09. Step 2.
- [Troubleshoot LinkedIn emails not received](https://www.linkedin.com/help/linkedin/answer/a522629), updated ≈2026-10. Step 2.
- [User Agreement](https://www.linkedin.com/legal/user-agreement), effective 2025-11-03. Step 2.
- [Privacy Policy](https://www.linkedin.com/legal/privacy-policy), effective 2025-11-03. Step 1.
- [Member Snapshot API](https://learn.microsoft.com/en-us/linkedin/dma/member-data-portability/shared/member-snapshot-api), LinkedIn API documentation, updated 2026-06-24. Step 4.
- [Member Snapshot Domains](https://learn.microsoft.com/en-us/linkedin/dma/member-data-portability/shared/snapshot-domain), LinkedIn API documentation, updated 2026-08-26. Step 4.
- [Profile Position Reference Schema](https://learn.microsoft.com/en-us/linkedin/shared/references/v2/profile/position), LinkedIn API documentation, updated 2026-04-30. Step 4.
- [Recommendations on LinkedIn](https://www.linkedin.com/help/linkedin/answer/a541653), updated ≈2023-10. Step 4.
- [Edit the introduction section on your profile](https://www.linkedin.com/help/linkedin/answer/a547248), updated ≈2026-02. Step 5.
- [Why It's Important to List Skills on Your LinkedIn Profile](https://www.linkedin.com/business/talent/blog/talent-acquisition/skills-on-linkedin-profile), LinkedIn Talent Blog, 2024-04-04. Step 5.
- [Featured section on your profile FAQs](https://www.linkedin.com/help/linkedin/answer/a552452/featured-section-on-your-profile-faqs), updated ≈2026-02. Step 5.
- [Add Career Breaks to Your Profile](https://www.linkedin.com/help/linkedin/answer/a597655/add-career-breaks-to-your-profile), updated ≈2021-10. Step 5.
- [Manage your public profile URL](https://www.linkedin.com/help/linkedin/answer/a542685), updated ≈2026-10. Step 5.
- [Control your public LinkedIn profile](https://www.linkedin.com/help/linkedin/answer/a528138), updated ≈2026-09. Step 5.
- [Let recruiters know you're Open to Work](https://www.linkedin.com/help/linkedin/answer/a507508/let-recruiters-know-you-re-open-to-work), updated ≈2026-10. Step 5.
- [Sharing your full profile with job posters on LinkedIn](https://www.linkedin.com/help/linkedin/answer/a512339/sharing-your-full-profile-with-job-posters-on-linkedin), updated ≈2023-10. Step 5.
- [Share profile updates](https://www.linkedin.com/help/linkedin/answer/a529062/share-profile-updates-with-your-network), updated ≈2026-08. Step 5.
- [Settings for profile photo visibility](https://www.linkedin.com/help/linkedin/answer/a545557/settings-for-profile-photo-visibility), updated ≈2024-10. Step 5.
- [Updates to LinkedIn navigation](https://www.linkedin.com/help/linkedin/answer/a11028010), updated ≈2026-10. Step 2.
- [LinkedIn and generative AI (GAI) FAQs](https://www.linkedin.com/help/linkedin/answer/a5538339), updated ≈2026-07. Step 5.
- [Save a profile as a PDF](https://www.linkedin.com/help/linkedin/answer/a541960), updated ≈2026-10. Step 6.
- [Upload your resume to LinkedIn](https://www.linkedin.com/help/linkedin/answer/a510363), updated ≈2026-03. Step 6.
- [Member portability APIs](https://www.linkedin.com/help/linkedin/answer/a6214075), updated ≈2023-10. Step 6.
- [Member Data Portability (Member)](https://learn.microsoft.com/en-us/linkedin/dma/member-data-portability/member-data-portability-member), LinkedIn API documentation, updated 2026-04-15. Step 6.
