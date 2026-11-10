# career-toolkit

A set of Claude skills that help you keep a complete, organized history of your work and then use it for your LinkedIn profile and your CV.

Collecting your own work history is hard. Your work is spread across tickets, pages, merge requests, reviews and chats, and nobody remembers every year of it. `work-history-harvest` gathers it from those places, asks you about the rest, and organizes it into one document per employer that you check and keep. Every time you update your LinkedIn profile or tailor your CV to a job description, you start from real facts in that document.

Run `work-history-harvest` once a year, even when you are not looking for a job. It is a good moment to reflect on what you achieved, while your memory is still fresh enough to fill in the details.

## The skills

| Skill | What it does | Status |
|---|---|---|
| **work-history-harvest** | Collects your work at one employer into one document you keep, `work-history-<employer>.md`. It is built to respect your NDA: the document holds only general descriptions of your own work, and you review every word of it. | ready |
| **linkedin-profile-coach** | Checks your LinkedIn profile and drafts new texts from that document. You paste them in yourself. | ready |
| **cv-tailor** | Will write a CV for a specific job from the same document. | planned |

### work-history-harvest

Start here, before your access to work systems ends.

- **Reads** what you allow it to read: Jira, Confluence, GitLab, GitHub, your Claude history, performance reviews, an old CV, certificates.
- **Asks you** about what the systems cannot show, such as results, numbers and your own part.
- **Writes** one English document per employer, whatever language you chat in. Each record says what backs it: something in a work system, or only your word.
- **Leaves out** client and colleague names, internal systems, ticket numbers, code and company figures.
- **Updates** once a year. It adds only the new period and updates records for work that continued.

The document explains itself at the top, so any AI assistant can use it a year from now, with or without this toolkit.

### linkedin-profile-coach

- Reads your work history documents and your LinkedIn data download.
- Audits your profile against sourced LinkedIn rules and the jobs you want.
- Drafts a headline, an About section, experience entries, skills and recommendation requests.
- Never touches LinkedIn. You paste every text and change every setting yourself, because LinkedIn's User Agreement forbids software that automates the site.

Each rule it applies names its source: LinkedIn's own pages or hiring research that states its method. The rules live in [best-practices.md](skills/linkedin-profile-coach/references/best-practices.md).

## Where to run

**Claude Code.** Files save to your computer and the helper scripts run. GitLab and GitHub work through their command-line tools, `glab` and `gh`. The scripts need Python 3.8 or newer.

**claude.ai.** Easier if you have never used a terminal. After each step you download the work as a ZIP file and upload it again next time, because a chat keeps nothing for the next one. Jira and Confluence work through connectors.

Your claude.ai chat history reaches both places through the claude.ai data export. On a work account, an admin may have turned the export off.

The skills talk in your language. They work best on the strongest model available.

## Install

### Claude Code

Add the repository as a plugin marketplace, then install the plugin. Claude Code needs `git` for this.

```text
/plugin marketplace add ALapina/career-toolkit
/plugin install career-toolkit@career-toolkit
```

The skills then run as `/career-toolkit:work-history-harvest` and `/career-toolkit:linkedin-profile-coach`. You can also just ask, for example "help me save my work history before I leave".

To update, choose **Update now** for the plugin under `/plugin` > Installed, then run `/reload-plugins`. A new copy arrives only when the plugin's version number changes.

### claude.ai

Each skill is a separate ZIP file.

1. **Turn on code execution.** Skills need it. Look under Settings > Capabilities for **Code execution and file creation**, called **Create and edit files** in the newer layout. On Team and Enterprise plans, an Owner controls it under Organization settings > Plugins & skills.
2. **Build the ZIPs.** Download the repository and open its `skills` folder in a terminal. Then run:

   ```bash
   for s in work-history-harvest linkedin-profile-coach; do rm -f "$s.zip"; zip -r "$s.zip" "$s/" -x '*.DS_Store' '*__pycache__*'; done
   ```

   Each ZIP must hold the skill folder itself at the top, not the files inside it. Without a terminal, compress each skill folder with your file manager.
3. **Upload each ZIP.** Open Customize > Skills, click **+**, then **+ Create skill** > **Upload a skill**.

To update, build the ZIPs again from the newer repository and upload them the same way.

If you also use Claude Code 2.1.273 or later with the same Claude account, it loads the skills you turned on in claude.ai. Then skip the Claude Code install.

## Your data and your NDA

- **Your contract decides what you may keep.** The skills keep only general descriptions of your own work. You still know your obligations better than any tool. This is not legal advice.
- **You can give the skill your NDA.** It can also take the confidentiality section of your contract or your exit agreement. Give only the clauses it needs, without salary or personal data. Before you upload them, check your company's AI policy if you use a work account. On a personal account, check whether your chats are used to train models. The clauses stay in `local-only/`. The skill turns them into general rules at the top of your document and asks you to confirm each one.
- **Read the whole document yourself.** The skill makes mistakes. The line "Reviewed by owner" stays `no` until you tell the skill you have read all of it. Check it against your contract before you copy it off a work computer.
- **`local-only/` stays behind.** This folder holds your list of names that must never appear, your NDA clauses and the employer documents you gathered. Before you copy anything to personal storage, ask the skill for its final check, then copy only the files it lists: your work history documents, `progress.md` and your own certificates.
- **Raw data stays where it was read.** Claude Code keeps session transcripts as plain text under `~/.claude/projects/` on the computer you use. In claude.ai, files you upload stay in the chat until you delete it.
- **Some sources expire.** Claude Code deletes transcripts after 30 days without use by default. Performance reviews and work chats often disappear with your account. The harvest starts with what to save first.
- **Passwords stay with you.** The skills never ask for a password, token or API key. They only read work systems, with your own access. When your employer blocks a connection, they stop and ask you instead.

This project is not affiliated with LinkedIn, Atlassian, GitLab or GitHub.

## Development

```text
skills/work-history-harvest/     the harvest skill
skills/linkedin-profile-coach/   the LinkedIn skill
evals/<skill>/<case>/            eval cases, all fictional
tests/                           script and repository tests
```

- **Format copies.** Each skill keeps its own copy of the document format in `references/document-format.md`. The copies must be identical. So must the two copies of `scripts/scan_text.py`.
- **Tests.** Run `python3 -m unittest discover -s tests` in the repository root. They check the scripts, the format copies, and that every link and rule ID inside a skill resolves.
- **Evals.** Use Claude Code v2.1.269 or later and run `claude plugin eval . --scaffold --allow-tools Write Edit Bash`, as [Test plugins with evals](https://code.claude.com/docs/en/plugin-evals) describes. `--case <name>` runs one case. Everything in the cases is fictional, including the planted instruction the skills must ignore and the password they must not keep.

## License

[MIT](LICENSE)
