# Claude Code adapter

What the person worked on with Claude Code and claude.ai: memory files, their own skills, prompt history and session transcripts on this computer, and claude.ai chats and memory. Besides the topics of their work, this source shows how the person uses AI tools, which many employers now ask about.

## Available when

- **Claude Code:** full mode, and the Claude Code folder exists on this computer. That is `~/.claude/` (`%USERPROFILE%\.claude` on Windows), or the folder named by the `CLAUDE_CONFIG_DIR` environment variable.
- **claude.ai:** the person can still sign in to the account they used for work. See [claude.ai](#claudeai).
- **Light mode:** ask the person to paste their claude.ai memory and to describe their projects.

## Where Claude Code keeps its files

Paths are inside the Claude Code folder.

| What | Where | Kept |
|---|---|---|
| Session transcripts | `projects/<project>/<session-id>.jsonl` | by default 30 days without use; [Retention](#retention) has the exceptions |
| Memory files | `projects/<project>/memory/`: a `MEMORY.md` index and one markdown file per memory | until the person or Claude deletes them |
| Prompt history | `history.jsonl`: the prompts the person typed, with time and project path | until the person deletes it |
| Personal skills | `skills/<name>/SKILL.md`. When Claude Code v2.1.273 or later is signed in to the person's Claude account, the skills they enabled in claude.ai sync into `skills/synced/`. | until removed |

- `<project>` is the path of the folder Claude Code ran in, with every character other than a letter or digit turned into `-`. For memory, `<project>` comes from the git repository instead, so all worktrees and sub-folders of one repository share one memory folder.
- Auto memory is on by default in local sessions. If the script lists no memory files, ask the person to run `/memory` in Claude Code: it lists the memory files and opens the auto memory folder. The `autoMemoryDirectory` setting can move that folder, and auto memory can be turned off.
- Memory is machine-local: Claude Code does not share it across machines or cloud environments. Inference: on a computer that goes back to the employer, the memory goes back with it.
- Transcripts and the prompt history are plain text and not encrypted at rest; file permissions are their only protection. A transcript holds whatever passed through a tool: file contents, command output, pasted text, and any credential a tool read or a command printed.

## Retention

Transcripts expire by default. Memory files and the prompt history stay.

- **Default:** Claude Code deletes a transcript after 30 days without use. The `cleanupPeriodDays` setting holds the period, and its default is 30.
- **Claude Desktop and Cowork:** on Claude Code v2.1.248 or later, transcripts of sessions started or last continued in Claude Desktop or Cowork are kept at any age by default. The `desktopSessionCleanupPeriodDays` setting can give them an age limit. They follow `cleanupPeriodDays` after all when the employer's managed settings set it or the HIPAA configuration applies. Earlier versions delete them after `cleanupPeriodDays` like the rest. `claude --version` shows the version.
- **How it happens:** a background sweep runs after each session starts and deletes the expired transcripts without a message. Those sessions also disappear from `/resume`. Each new session can remove more.
- **Prompt history** has no age limit, except under the HIPAA configuration: there, each sweep removes the entries older than `cleanupPeriodDays`.
- **Memory files** are exempt from the sweep. Before v2.1.228, the sweep could still delete old files in sub-folders of a memory folder.

## Keeping transcripts longer

This is the person's decision, within their employer's rules. Explain the steps; the person edits their own settings. Never edit a settings file yourself.

- The person sets `cleanupPeriodDays` in `settings.json` in the Claude Code folder (`~/.claude/settings.json` by default). The value is a whole number of days, at least 1; 0 fails validation. Claude Code's documentation suggests a large value such as 3650, about ten years, for long retention. A new file holds `{"cleanupPeriodDays": 3650}`. In an existing file, the person adds `"cleanupPeriodDays": 3650` inside the outer braces, with a comma between it and the other settings.
- Inference: the next session that starts under the old setting deletes every transcript past the old limit, so the change has to come before that session starts.
- A longer period also keeps the raw data of this harvest on the computer for longer. Suggest setting it back once the harvest is done.
- What the employer controls: managed settings deployed by the organization take precedence over every settings file of the person, and a `cleanupPeriodDays` set there cannot be overridden. The "Setting sources" line of `/status` names the managed source that applies, but not which file supplied each key.

Done when the person has decided whether to change the setting.

## Collect from Claude Code

Run the summary script; it prints to the conversation and writes nothing. Start with one line per project, then list one project at a time within the time window:

```bash
python3 <skill>/scripts/claude_history.py --summary --since <YYYY-MM-DD> --until <YYYY-MM-DD>
python3 <skill>/scripts/claude_history.py --project <part of the project's path> --since <YYYY-MM-DD> --until <YYYY-MM-DD>
```

It reads the Claude Code folder (`--root <folder>` names another one). A project run lists four things:

1. **Memory files.** Read them next with `--show <file>`, which masks secrets: they are short notes Claude Code kept about the person's projects, decisions and findings, often the best summary of their work there is.
2. **Personal skills.** A skill the person wrote is evidence of building AI tooling. Symlinked and synced skills are often installed from someone else: ask the person which ones they wrote.
3. **Sessions with a transcript**, per project folder, with the number of sessions and prompts, dates and each session's opening request, which can be a slash command such as `/review-pr`. Use them for the kinds of work (investigations, migrations, reviews, documentation, tooling) and how often; open a transcript with `--show <file>` only to confirm a theme, and then read only the parts you need.
4. **Older sessions from the prompt history**, per project path: sessions whose transcript is gone, with the date and the first prompt. Prompts saved without a session ID are grouped by day. Read them like the sessions in item 3. They often reach back before the oldest transcript.

Claude Code does not document the entries in either file. The transcript format is internal and changes between versions: when recent sessions show no request text, it has probably changed, so work from the memory files and the prompt history. When the script says it cannot read `history.jsonl`, work from the memory files and the transcripts.

Read old sessions as files. Resuming one to ask for a summary (`claude -p --resume <session-id>`) adds a turn to it, and each session start runs the retention sweep.

## claude.ai

Chats and memory from claude.ai, for the work the person did there. Save every export in `local-only/`: chats about work hold the employer's material.

### Personal account

- **Export.** Individual users on the Free, Pro, Max and Ultra plans can export their data. In the web app or Claude Desktop, the path is Settings > Privacy > Export data; the iOS and Android apps cannot export. Claude emails a download link. It works only while the person is signed in, and it expires 24 hours after delivery; after that, the person runs the export again. The export holds conversation data and account data.
- **Private chats.** The export holds the account's conversations, so private chats come with the work ones. Suggest the export when the person used this account for work. On an employer's computer, suggest that the person delete the export once its themes are in the document.
- **Memory.** Settings > Your Claude, then "Manage" next to Your memory, shows the memory as Claude sees it. In the older layout the path is Settings > Capabilities > "View and manage memory". The person keeps a copy by pasting it into a file in `local-only/`. They can also ask in a chat: "Write out your memories of me verbatim, exactly as they appear in your memory."

### Work account (Team or Enterprise)

The employer decides what leaves a work account: the organization's Primary Owner manages the work account and all its data.

- A member can export their own data only after an owner turns on "Allow members to export their own data". The member then follows the same steps as above. The export holds the member's own chats, without the contents of the files they uploaded.
- When the "Export data" button is missing, the person can ask an owner whether the setting is on. With the setting off, only the Primary Owner can export, and only for the whole organization; the person can ask them for their own chats.
- Removing a member from the organization deletes neither their account nor their data. The help page does not say what a removed member can still open: export before the last day.
- The memory help page does not say whether memory differs on work accounts. Try the same memory view.

### Read an export

The file format is not documented: look at what arrives before reading it, and list only the conversation titles and dates first (for example by searching the file for `"name"`); `--show` on the whole export would print private chats too. If it lists conversation titles and dates, start there. Agree with the person which chats are about work, and leave the others unread. Group the work chats into themes, and open a conversation only to confirm a theme. When an export is large and you can start subagents, give it its own, as [harvest](../harvest.md) does for large sources.

Done when the work chats and the memory are grouped into themes, or the person has decided to skip claude.ai.

## Turn into themes

- Group by project folder or project path, then by kind of work. Memory notes usually name the outcome; sessions and the prompt history show the volume and the period.
- Treat claude.ai chats like sessions, and claude.ai memory like memory notes.
- Look for these themes in particular: investigations that ended in a decision or a fix, tooling or automation the person built, documentation they produced, and the practice of AI-assisted development itself (custom skills, multi-step workflows, review automation).
- Role signals: sessions show work the person did with an AI assistant, so most themes here are `built`. `led` needs evidence that the person directed other people's work, from another source or the interview.
- Basis: memory notes (written by Claude) and sessions show the topic, the period and the volume. An outcome or figure is verified only when a measurement in a transcript or another artifact, such as a merged merge request, shows it. Whether the result shipped is the person's answer, so the record is `mixed` or `self-reported` and names that part.

## Leave out

Everything raw: folder names and project paths (they hold local paths with employer and repository names), session and chat text, prompts, conversation titles, file paths, commands, ticket numbers and the names in memory notes. The script masks the secrets it recognizes; treat the rest of its output as raw as well. Write only clean themes.

## Sources

Checked 2026-10-30. Claude Code docs pages show no date; Claude Help Center dates are as the pages showed them that day.

- [Manage sessions](https://code.claude.com/docs/en/sessions.md), Claude Code docs, no page date, checked 2026-10-30
- [Data usage](https://code.claude.com/docs/en/data-usage), Claude Code docs, no page date, checked 2026-10-30
- [All settings](https://code.claude.com/docs/en/settings-reference.md), Claude Code docs, no page date, checked 2026-10-30
- [Settings files and precedence](https://code.claude.com/docs/en/settings.md), Claude Code docs, no page date, checked 2026-10-30
- [Explore the .claude directory](https://code.claude.com/docs/en/claude-directory), Claude Code docs, no page date, checked 2026-10-30
- [How Claude remembers your project](https://code.claude.com/docs/en/memory.md), Claude Code docs, no page date, checked 2026-10-30
- [Extend Claude with skills](https://code.claude.com/docs/en/skills), Claude Code docs, no page date, checked 2026-10-30
- [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude), Claude Help Center, "Updated this week" on 2026-10-30
- [Export your Claude data](https://support.claude.com/en/articles/9450526-export-your-claude-data), Claude Help Center, "Updated over 2 weeks ago" on 2026-10-30
- [Export your organization's data](https://support.claude.com/en/articles/13346720-export-your-organization-s-data), Claude Help Center, "Updated this week" on 2026-10-30
- [What happens to a user's data when they are removed from a Team or Enterprise organization?](https://support.claude.com/en/articles/12053672-what-happens-to-a-user-s-data-when-they-are-removed-from-a-team-or-enterprise-organization), Claude Help Center, "Updated this week" on 2026-10-30
- [Who owns and manages the data of my team?](https://support.claude.com/en/articles/9265372-who-owns-and-manages-the-data-of-my-team), Claude Help Center, dated 2026-03-16, checked 2026-10-30
- [Import and export your memory from Claude](https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude), Claude Help Center, "Updated this week" on 2026-10-30
