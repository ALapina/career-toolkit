#!/usr/bin/env python3
"""Check paste-ready blocks in draft files against LinkedIn's limits and the house style.

A paste-ready block is a fenced code block whose info string names a field:

    ```headline
    QA automation engineer | Playwright and TypeScript | Logistics
    ```

Fields: headline, about, position-title, position-description, skills (one
skill per line). Open each block with ```<field> at the start of a line, with
nothing after the tag, and close it with ``` at the start of a line. A field
block written any other way (indented, fenced with ~~~ or more backticks, a
word after the tag, never closed) is not checked and fails the run. Blocks
with other tags are ignored.

The documented limits below come from the platform facts in
references/best-practices.md; keep the two in step. LinkedIn documents no
limit for position titles and descriptions, so for those the script reports
the length only.

Characters are counted the way a browser counts them (UTF-16 code units), so
most emoji count as two and a line break counts as one. LinkedIn's own counter
has the last word.

Usage:
    python3 check_drafts.py PATH [PATH ...]    draft files or folders of .md files

Each block prints one line, path:line: field: then one of
  ok, N/LIMIT characters        (headline, about)
  ok, N characters (LinkedIn documents no limit; the counter in its edit form decides)
  ok, N skills
  FAIL: ...                     empty, over a documented limit, or not checked
followed by a line  path:line: field: style: ...  for each house-style finding.
The last line reads  check_drafts: N blocks, F failed, W warnings.

Exit status: 2 on usage errors or when a file cannot be read (the other files
are still checked); otherwise 1 if a block is empty, over a documented limit
or not checked, else 0. Style findings are warnings and do not change the
exit status. Standard library only; Python 3.8 or newer.
"""

import os
import re
import sys

# Documented by LinkedIn: a block over its limit fails.
LIMITS = {
    "headline": 220,
    "about": 2600,
}
SKILLS_MAX = 100
# LinkedIn documents no limit for these fields (experience-9): report the length only.
NO_DOCUMENTED_LIMIT = ("position-title", "position-description")

# House style (best-practices.md, area style-): phrases that read as filler or machine-written.
STYLE_PHRASES = [
    "passionate",
    "results-driven",
    "results driven",
    "dynamic",
    "seasoned",
    "leverage",
    "leveraging",
    "spearheaded",
    "synergy",
    "cutting-edge",
    "proven track record",
    "detail-oriented",
    "team player",
    "go-getter",
    "think outside the box",
    "fast-paced environment",
    "self-starter",
    "ninja",
    "rockstar",
    "guru",
    "wizard",
    "delve",
    "tapestry",
    "testament",
    "showcase",
    "showcasing",
    "fostering",
    "pivotal",
    "seamless",
    "robust",
    "innovative",
    "visionary",
    "thought leader",
    "highly motivated",
    "hard-working",
    "extensive experience",
]
STYLE_PATTERNS = [
    ("em dash", re.compile("—")),
    ("en dash used as a dash", re.compile(r"\s–\s")),
    # Emoji code points only: pictographs, flags, keycaps and the emoji in the symbol blocks,
    # not arrows, bullets or keyboard symbols such as ⌘ and ⏎.
    (
        "emoji",
        re.compile(
            "[\U0001F000-\U0001FAFF⌚⌛⏩-⏳⏸-⏺☀-➿"
            "⬅-⬇⬛⬜⭐⭕⃣️]"
        ),
    ),
    ("hashtag", re.compile(r"(?<![\w&])#[A-Za-z]\w+")),
    ("'not just X but Y'", re.compile(r"(?i)\bnot (?:just|only|merely)\b[^.\n]{0,80}\bbut\b")),
]
PHRASE_PATTERNS = [(phrase, re.compile(r"(?<![\w-])" + re.escape(phrase) + r"(?![\w-])", re.IGNORECASE)) for phrase in STYLE_PHRASES]

FIELDS = ("headline", "about", "position-title", "position-description", "skills")
BLOCK = re.compile(r"^```([A-Za-z-]+)[ \t]*\n(.*?)^```[ \t]*$", re.MULTILINE | re.DOTALL)
# Any fence that opens a field block, also the ones BLOCK cannot read.
FIELD_FENCE = re.compile(
    r"^[ \t]*(?:`{3,}|~{3,})[ \t]*(" + "|".join(FIELDS) + r")(?![\w-])",
    re.MULTILINE | re.IGNORECASE,
)


def length(text):
    return len(text.encode("utf-16-le")) // 2


def iter_files(paths):
    for path in paths:
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                dirs.sort()
                for name in sorted(files):
                    if name.lower().endswith(".md"):
                        yield os.path.join(root, name)
        elif os.path.isfile(path):
            yield path
        else:
            raise FileNotFoundError(path)


def style_findings(text):
    for phrase, pattern in PHRASE_PATTERNS:
        if pattern.search(text):
            yield "'%s'" % phrase
    for name, pattern in STYLE_PATTERNS:
        if pattern.search(text):
            yield name


def check_block(field, body):
    """Return (problems, info) for one block; problems make the run fail."""
    text = body.rstrip("\n")
    if not text.strip():
        return ["empty"], ""
    if field == "skills":
        skills = [line.strip() for line in text.splitlines() if line.strip()]
        problems = []
        if len(skills) > SKILLS_MAX:
            problems.append("%d skills, LinkedIn allows %d" % (len(skills), SKILLS_MAX))
        return problems, "%d skills" % len(skills)
    count = length(text)
    if field in NO_DOCUMENTED_LIMIT:
        return [], "%d characters (LinkedIn documents no limit; the counter in its edit form decides)" % count
    limit = LIMITS[field]
    if count > limit:
        return ["%d/%d characters, over by %d" % (count, limit, count - limit)], ""
    return [], "%d/%d characters" % (count, limit)


def main(argv=None):
    paths = sys.argv[1:] if argv is None else argv
    if not paths or paths[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    try:
        files = list(iter_files(paths))
    except FileNotFoundError as error:
        print("check_drafts: no such file or folder: %s" % error, file=sys.stderr)
        return 2

    blocks = failures = warnings = 0
    unreadable = False
    for path in files:
        try:
            with open(path, encoding="utf-8", errors="replace") as handle:
                content = handle.read()
        except OSError as error:
            print("check_drafts: cannot read %s: %s" % (path, error), file=sys.stderr)
            unreadable = True
            continue
        results = []  # (offset, output lines) per block, printed in file order
        for match in BLOCK.finditer(content):
            field, body = match.group(1).lower(), match.group(2)
            if field not in FIELDS:
                continue
            blocks += 1
            line = content.count("\n", 0, match.start()) + 1
            problems, info = check_block(field, body)
            if problems:
                failures += 1
                output = ["%s:%d: %s: FAIL: %s" % (path, line, field, "; ".join(problems))]
            else:
                output = ["%s:%d: %s: ok, %s" % (path, line, field, info)]
            for finding in style_findings(body):
                warnings += 1
                output.append("%s:%d: %s: style: %s" % (path, line, field, finding))
            results.append((match.start(), output))
        # A field block that BLOCK cannot read would otherwise pass without a word.
        checked = {offset for offset, _ in results}
        for match in FIELD_FENCE.finditer(content):
            if match.start() in checked:
                continue
            blocks += 1
            failures += 1
            field = match.group(1).lower()
            line = content.count("\n", 0, match.start()) + 1
            output = (
                "%s:%d: %s: FAIL: not checked; open the block with ```%s at the start of a line, "
                "nothing after the tag, and close it with ``` at the start of a line" % (path, line, field, field)
            )
            results.append((match.start(), [output]))
        for _, output in sorted(results, key=lambda item: item[0]):
            print("\n".join(output))

    print("check_drafts: %d blocks, %d failed, %d warnings" % (blocks, failures, warnings))
    if not blocks:
        print("check_drafts: no tagged blocks found; tag paste-ready text as ```headline, ```about, ...")
    if unreadable:
        return 2
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
