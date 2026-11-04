#!/usr/bin/env python3
"""Summarize the person's Claude Code data on this computer, for the harvest phase.

Usage:
    python3 claude_history.py [--root DIR] [--summary] [--project TEXT]
                              [--since YYYY-MM-DD] [--until YYYY-MM-DD] [--prompt-chars N]
    python3 claude_history.py --show FILE

DIR is the Claude Code folder: $CLAUDE_CONFIG_DIR when it is set, otherwise
~/.claude.

Prints four lists to the terminal and writes nothing to disk:
  1. memory files (projects/*/memory/, sub-folders included) with size and date;
  2. personal skills (skills/*/SKILL.md, and skills/synced/*/SKILL.md for skills
     synced from claude.ai) with their descriptions, marking symlinked and
     synced ones, which are often installed from elsewhere;
  3. per project folder, the sessions that still have a transcript: their
     number, the prompts in them, the first and last date, and each
     session's opening request;
  4. from the prompt history (history.jsonl), per project path, the sessions
     that no longer have a transcript: their date and first prompt. Prompts
     saved without a session ID are grouped by day, and a day is left out
     when a transcript of that project covers it. Claude Code deletes old
     transcripts (by default after 30 days without use; on v2.1.248 or later
     it keeps sessions from Claude Desktop or Cowork at any age) but keeps the
     prompt history, except under the HIPAA configuration.
Each project in lists 3 and 4 starts with a line
  -- <folder or path>: N sessions, M prompts, FIRST to LAST
and each session follows as  DATE  opening request.

A session's opening request is the first thing the person typed. When a
session opens with a slash command that has arguments and Claude answers it,
such as /build-page <ticket>, the command and its arguments are the opening;
a command that only sets up the session, such as /model opus, gives way to
the request typed after it.

Options that narrow the output:
  --summary        lists 3 and 4 with the project lines only: no requests
  --project TEXT   only the project folders and paths that contain TEXT,
                   ignoring letter case and the characters between words
                   (contoso/ledger matches -Users-me-contoso-ledger); leaves
                   out the skills list
  --since, --until only sessions active on or after, and on or before, a
                   date; they do not narrow the memory files or skills
A long history reads best as --summary first, then --project for one project
at a time, with --since and --until for a stretch of a long employment.

--show FILE prints one file instead of the lists, with secrets masked: a
transcript (.jsonl) as the user and assistant text, each message under a
line "== DATE user" or "== DATE assistant"; any other file, such as a memory
file or a claude.ai export, as it is, JSON indented one value per line.

Requests, prompts and skill descriptions are shortened, with secrets masked.
A line the script cannot read is skipped, and so is a file, with a note.

The output is raw material for the conversation only. It is not clean text:
project folder names, paths, requests and prompts can name the employer's
systems and clients.

Standard library only; Python 3.8 or newer.
"""

import argparse
import datetime
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scan_text import mask_secrets  # noqa: E402

TAG_BLOCK = re.compile(r"<([a-z][a-z0-9_-]*)[^>]*>.*?</\1>", re.DOTALL)
TAG = re.compile(r"</?[a-z][a-z0-9_-]*[^>]*>")
# How Claude Code records a slash command the person typed.
COMMAND = re.compile(r"<command-name>\s*(/[^<\s]*)\s*</command-name>")
COMMAND_ARGS = re.compile(r"<command-args>(.*?)</command-args>", re.DOTALL)
# A slash command without arguments (/clear, /resume) says nothing about the work.
BARE_COMMAND = re.compile(r"^/\S*$")
# Claude Code adds this when the person stops a reply; they did not type it.
INTERRUPTED = re.compile(r"^\[Request interrupted by user")
# Claude Code names a project's folder after its path, with every character
# other than a letter or digit turned into "-".
NOT_ALPHANUMERIC = re.compile(r"[^A-Za-z0-9]")
# No value, or a YAML block indicator (>, |, >-, |+): the text follows on indented lines.
BLOCK_SCALAR = re.compile(r"^(?:[>|][+-]?\d*[+-]?)?$")
# What a malformed line can raise; one bad line must not stop the run.
LINE_ERRORS = (AttributeError, KeyError, TypeError, ValueError, RecursionError)


def default_root():
    return os.path.expanduser(os.environ.get("CLAUDE_CONFIG_DIR") or "~/.claude")


def iso_date(value):
    if not isinstance(value, str) or not value:
        return None
    try:
        return datetime.datetime.fromisoformat(value.replace("Z", "+00:00")).date()
    except ValueError:
        pass
    # Older Pythons reject some time formats; the date part is enough.
    try:
        return datetime.date.fromisoformat(value[:10])
    except ValueError:
        return None


def stamp_date(value):
    """Return the date of a prompt-history timestamp: epoch milliseconds, epoch seconds or ISO text."""
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        seconds = value / 1000.0 if value > 1e11 else value
        try:
            return datetime.date.fromtimestamp(seconds)
        except (OverflowError, OSError, ValueError):
            return None
    if isinstance(value, str):
        return iso_date(value)
    return None


def file_date(path):
    return datetime.date.fromtimestamp(os.path.getmtime(path))


def shorten(text, limit):
    text = mask_secrets(text)
    if len(text) > limit:
        text = text[: limit - 3].rstrip() + "..."
    return text


def count(number, word):
    return "%d %s%s" % (number, word, "" if number == 1 else "s")


def parse_line(raw):
    """Return one JSON line as a dict, or None."""
    try:
        entry = json.loads(raw)
    except (ValueError, RecursionError):
        return None
    return entry if isinstance(entry, dict) else None


def raw_text(entry):
    """Return a transcript line's message text (string content or text parts), or None."""
    message = entry.get("message")
    content = message.get("content") if isinstance(message, dict) else None
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        if any(isinstance(part, dict) and part.get("type") == "tool_result" for part in content):
            return None
        texts = [part.get("text") for part in content if isinstance(part, dict) and part.get("type") == "text"]
        return "\n".join(text for text in texts if isinstance(text, str))
    return None


def typed_by_person(entry):
    """True for a user line the person typed: not meta, not a subagent's, not a summary."""
    return (
        entry.get("type") == "user"
        and not entry.get("isMeta")
        and not entry.get("isSidechain")
        and not entry.get("isCompactSummary")
    )


def message_text(entry, collapse=True):
    """Return the person's own text from a transcript line, or None.

    collapse joins the text into one line; otherwise its line breaks stay.
    """
    if not typed_by_person(entry):
        return None
    text = raw_text(entry)
    if not text:
        return None
    text = TAG.sub(" ", TAG_BLOCK.sub(" ", text))
    text = " ".join(text.split()) if collapse else text.strip()
    if not text or INTERRUPTED.match(text):
        return None
    return text


def command_text(entry):
    """Return "/name args" for a line where the person typed a slash command with arguments, or None."""
    if not typed_by_person(entry):
        return None
    text = raw_text(entry)
    if not text:
        return None
    name = COMMAND.search(text)
    args = COMMAND_ARGS.search(text)
    if not name or not args or not args.group(1).strip():
        return None
    return "%s %s" % (name.group(1), " ".join(args.group(1).split()))


def summarize_session(path):
    """Return (first date, last date, opening request, prompts) for a transcript, or None if it cannot be read."""
    first_date = last_date = None
    opening = command = None
    prompts = 0
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            for raw in handle:
                entry = parse_line(raw)
                if entry is None:
                    continue
                try:
                    stamp = stamp_date(entry.get("timestamp"))
                    if stamp:
                        first_date = min(first_date, stamp) if first_date else stamp
                        last_date = max(last_date, stamp) if last_date else stamp
                    text = message_text(entry)
                    typed = command_text(entry)
                    if text or typed:
                        prompts += 1
                    if opening is None:
                        # A command Claude answers (a skill, /review) opens the session; one that only
                        # sets it up (/model opus) gets no answer before the next request.
                        if command and entry.get("type") == "assistant":
                            opening = command
                        else:
                            command = typed or command
                            opening = text
                except LINE_ERRORS:
                    continue
        fallback = file_date(path)
    except OSError:
        return None
    return first_date or fallback, last_date or fallback, opening or command, prompts


def matches(name, wanted):
    """True when a project folder or path contains the --project text; None matches all."""
    if wanted is None:
        return True
    return wanted in NOT_ALPHANUMERIC.sub("-", name).lower()


def active(first, last, since, until):
    """True when a session active from first to last overlaps the --since/--until window."""
    return not (since and last < since) and not (until and first > until)


def list_memory(projects, wanted):
    print("== Memory files")
    pattern = os.path.join(glob.escape(projects), "*", "memory", "**", "*.md")
    shown = False
    for path in sorted(glob.glob(pattern, recursive=True)):
        if not matches(os.path.relpath(path, projects).split(os.sep)[0], wanted):
            continue
        shown = True
        try:
            print("%s  %s  %d bytes" % (file_date(path), path, os.path.getsize(path)))
        except OSError:
            print("(cannot read)  %s" % path)
    if not shown:
        print("(none)")
    return shown


def skill_files(skills_dir):
    """Yield (name, path of SKILL.md, origin note) for personal and synced skills."""
    for path in sorted(glob.glob(os.path.join(glob.escape(skills_dir), "*", "SKILL.md"))):
        folder = os.path.dirname(path)
        origin = " (symlink to %s)" % os.path.realpath(folder) if os.path.islink(folder) else ""
        yield os.path.basename(folder), path, origin
    for path in sorted(glob.glob(os.path.join(glob.escape(skills_dir), "synced", "*", "SKILL.md"))):
        yield os.path.basename(os.path.dirname(path)), path, " (synced from claude.ai)"


def skill_description(path):
    """Return the description from a SKILL.md, joined into one line with secrets masked."""
    parts = []
    found = False
    with open(path, encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if not found:
                if line.startswith("description:"):
                    found = True
                    value = line.split(":", 1)[1].strip()
                    if not BLOCK_SCALAR.match(value):
                        parts.append(value)
                continue
            # A block value (>-, |) or a long plain value goes on in the indented lines that follow.
            if not line.strip():
                continue
            if not line[0].isspace():
                break
            parts.append(line.strip())
    return mask_secrets(" ".join(parts))[:200]


def list_skills(skills_dir):
    print("\n== Personal skills")
    found = False
    for name, path, origin in skill_files(skills_dir):
        found = True
        try:
            description = skill_description(path)
        except OSError:
            description = "(cannot read SKILL.md)"
        print("%s%s: %s" % (name, origin, description))
    if not found:
        print("(none)")


def read_transcripts(projects):
    """Return ({project folder name: [(session ID, first date, last date, opening, prompts)]}, unreadable count)."""
    found = {}
    unreadable = 0
    for folder in sorted(glob.glob(os.path.join(glob.escape(projects), "*"))):
        if not os.path.isdir(folder):
            continue
        for path in sorted(glob.glob(os.path.join(glob.escape(folder), "*.jsonl"))):
            summary = summarize_session(path)
            if summary is None:
                unreadable += 1
                continue
            first, last, opening, prompts = summary
            session = os.path.splitext(os.path.basename(path))[0]
            found.setdefault(os.path.basename(folder), []).append((session, first, last, opening, prompts))
    return found, unreadable


def list_sessions(transcripts, unreadable, options):
    print("\n== Sessions with a transcript, by project folder")
    shown = False
    for folder in sorted(transcripts):
        if not matches(folder, options.wanted):
            continue
        sessions = [item for item in transcripts[folder] if active(item[1], item[2], options.since, options.until)]
        if not sessions:
            continue
        shown = True
        sessions.sort(key=lambda item: item[1])
        header = "-- %s: %s, %s, %s to %s" % (
            folder,
            count(len(sessions), "session"),
            count(sum(item[4] for item in sessions), "prompt"),
            sessions[0][1],
            max(item[2] for item in sessions),
        )
        if options.summary:
            print(header)
            continue
        print("\n" + header)
        for _, first, _, opening, _ in sessions:
            print("  %s  %s" % (first, shorten(opening or "(no request text)", options.prompt_chars)))
    if not shown:
        print("(none)")
    if unreadable:
        print("(could not read %s)" % count(unreadable, "transcript"))
    return shown


def history_entries(path, stats):
    """Yield (project path, session ID or None, date, prompt text) from history.jsonl.

    Counts the non-empty lines in stats["lines"] and the lines read in stats["read"].
    """
    with open(path, encoding="utf-8", errors="replace") as handle:
        for raw in handle:
            if not raw.strip():
                continue
            stats["lines"] += 1
            entry = parse_line(raw)
            if entry is None or not isinstance(entry.get("display"), str):
                continue
            stamp = stamp_date(entry.get("timestamp"))
            if stamp is None:
                continue
            stats["read"] += 1
            text = " ".join(entry["display"].split())
            if not text:
                continue
            project = entry.get("project")
            session = entry.get("sessionId")
            yield (
                project if isinstance(project, str) and project else "(no project path)",
                session if isinstance(session, str) and session else None,
                stamp,
                text,
            )


def covered_by_transcript(project, day, transcripts):
    """True when a transcript in the project's folder spans the given day."""
    sessions = transcripts.get(NOT_ALPHANUMERIC.sub("-", project), [])
    return any(first <= day <= last for _, first, last, _, _ in sessions)


def list_history(history, transcripts, options):
    print("\n== Older sessions from the prompt history, by project path")
    if not os.path.isfile(history):
        print("(no prompt history)")
        return False
    with_transcript = {item[0] for sessions in transcripts.values() for item in sessions}
    stats = {"lines": 0, "read": 0}
    projects = {}
    try:
        for project, session, stamp, text in history_entries(history, stats):
            if not matches(project, options.wanted):
                continue
            # An entry without a session ID joins its project's group for that day, which stands in for a session.
            key = session or stamp.isoformat()
            groups = projects.setdefault(project, {})
            group = groups.get(key)
            if group is None:
                group = groups[key] = {"first": stamp, "last": stamp, "prompts": 0, "opening": None, "dated": not session}
            group["first"] = min(group["first"], stamp)
            group["last"] = max(group["last"], stamp)
            group["prompts"] += 1
            if group["opening"] is None and not BARE_COMMAND.match(text):
                group["opening"] = text
    except OSError as error:
        print("(cannot read history.jsonl: %s)" % error)
        return False
    if stats["lines"] and not stats["read"]:
        print("(history.jsonl has %s, none in a format this script reads)" % count(stats["lines"], "line"))
        return False
    left_out = 0
    kept = {}
    for project, groups in projects.items():
        for key, group in groups.items():
            dated_and_covered = group["dated"] and covered_by_transcript(project, group["first"], transcripts)
            if key in with_transcript or dated_and_covered:
                left_out += 1
            elif group["opening"] and active(group["first"], group["last"], options.since, options.until):
                kept.setdefault(project, []).append(group)
    if left_out:
        print("(left out because they still have a transcript: %s)" % count(left_out, "session"))
    for project in sorted(kept):
        sessions = kept[project]
        sessions.sort(key=lambda group: group["first"])
        header = "-- %s: %s, %s, %s to %s" % (
            project,
            count(len(sessions), "session"),
            count(sum(group["prompts"] for group in sessions), "prompt"),
            sessions[0]["first"],
            max(group["last"] for group in sessions),
        )
        if options.summary:
            print(header)
            continue
        print("\n" + header)
        for group in sessions:
            print("  %s  %s" % (group["first"], shorten(group["opening"], options.prompt_chars)))
    if not kept:
        print("(none)")
    return bool(kept)


def show_transcript(path):
    """Print a transcript's user and assistant text; return False when the file holds no transcript lines."""
    transcript = printed = False
    with open(path, encoding="utf-8", errors="replace") as handle:
        for raw in handle:
            entry = parse_line(raw)
            if entry is None:
                continue
            try:
                kind = entry.get("type")
                if kind not in ("user", "assistant"):
                    continue
                transcript = True
                if kind == "user":
                    text = command_text(entry) or message_text(entry, collapse=False)
                elif entry.get("isSidechain"):
                    text = None
                else:
                    text = (raw_text(entry) or "").strip()
                if not text:
                    continue
                print("== %s %s" % (stamp_date(entry.get("timestamp")) or "(no date)", kind))
                for line in text.split("\n"):
                    print(mask_secrets(line))
                printed = True
            except LINE_ERRORS:
                continue
    if transcript and not printed:
        print("(no user or assistant text)")
    return transcript


def show_file(path):
    """Print one file with secrets masked: a transcript as its user and assistant text, anything else as it is."""
    if not os.path.isfile(path):
        print("claude_history: --show needs a file: %s" % path, file=sys.stderr)
        return 2
    try:
        if path.lower().endswith(".jsonl") and show_transcript(path):
            return 0
        with open(path, encoding="utf-8", errors="replace") as handle:
            text = handle.read()
    except OSError as error:
        print("claude_history: cannot read %s: %s" % (path, error), file=sys.stderr)
        return 2
    if path.lower().endswith(".json"):
        # An export is often one long line; indented, it can be read in parts.
        try:
            text = json.dumps(json.loads(text), indent=1, ensure_ascii=False)
        except (ValueError, RecursionError):
            pass
    if text.endswith("\n"):
        text = text[:-1]
    for line in text.split("\n"):
        print(mask_secrets(line))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--root",
        default=default_root(),
        metavar="DIR",
        help="Claude Code folder (default: $CLAUDE_CONFIG_DIR if set, else ~/.claude)",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="one line per project folder or path (sessions, prompts, first and last date), no requests",
    )
    parser.add_argument(
        "--project",
        metavar="TEXT",
        help="only project folders and paths that contain TEXT; leaves out the skills list",
    )
    parser.add_argument("--since", metavar="YYYY-MM-DD", help="only sessions active on or after this date")
    parser.add_argument("--until", metavar="YYYY-MM-DD", help="only sessions active on or before this date")
    parser.add_argument(
        "--prompt-chars",
        type=int,
        default=160,
        metavar="N",
        help="shorten requests and prompts to N characters (default 160, at least 20)",
    )
    parser.add_argument("--show", metavar="FILE", help="print this file with secrets masked, instead of the lists")
    args = parser.parse_args(argv)

    if args.show:
        return show_file(args.show)

    dates = {}
    for option in ("since", "until"):
        value = getattr(args, option)
        try:
            dates[option] = datetime.date.fromisoformat(value) if value else None
        except ValueError:
            print("claude_history: --%s must be YYYY-MM-DD" % option, file=sys.stderr)
            return 2
    if dates["since"] and dates["until"] and dates["since"] > dates["until"]:
        print("claude_history: --since is after --until", file=sys.stderr)
        return 2
    if args.prompt_chars < 20:
        print("claude_history: --prompt-chars must be at least 20", file=sys.stderr)
        return 2
    options = argparse.Namespace(
        summary=args.summary,
        wanted=NOT_ALPHANUMERIC.sub("-", args.project).lower() if args.project is not None else None,
        since=dates["since"],
        until=dates["until"],
        prompt_chars=args.prompt_chars,
    )

    root = os.path.expanduser(args.root)
    projects = os.path.join(root, "projects")
    history = os.path.join(root, "history.jsonl")
    if not os.path.isdir(projects) and not os.path.isfile(history):
        print(
            "claude_history: no Claude Code data at %s (no projects folder, no history.jsonl)" % root,
            file=sys.stderr,
        )
        return 2

    transcripts, unreadable = read_transcripts(projects)
    shown = list_memory(projects, options.wanted)
    if options.wanted is None:
        list_skills(os.path.join(root, "skills"))
    shown = list_sessions(transcripts, unreadable, options) or shown
    shown = list_history(history, transcripts, options) or shown
    if args.project is not None and not shown:
        print("claude_history: no project folder or path contains %r in these dates" % args.project, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
