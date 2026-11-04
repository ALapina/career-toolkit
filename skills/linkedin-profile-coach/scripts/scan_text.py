#!/usr/bin/env python3
"""Find text that must not appear in clean workspace files.

Usage:
    python3 scan_text.py [--terms FILE] PATH [PATH ...]

PATH is a file or a folder. Folders are scanned recursively for .md,
.markdown, .txt, .csv, .tsv, .json, .jsonl, .yaml, .yml and .log files.
Directly under each folder passed, the sub-folders local-only,
linkedin-export and .git are skipped (pass a file inside them explicitly to
scan it anyway); deeper down, folders with those names are scanned like any
other. What a folder scan cannot read is reported as a review finding on
line 0 and counted in the summary: each file of another type
(unscanned-file), each symlinked sub-folder, each .git folder further down
and each folder without read access (unscanned-folder). .DS_Store, Thumbs.db
and desktop.ini are ignored.

--terms names a file with one confidential term per line (clients, partners,
internal code names). Blank lines and lines starting with # are ignored, and
so is a " # comment" after a term. It matches each name in any letter case,
with any punctuation or none between its words, and at the start of
identifiers such as FabrikamClient or falcon2. It also matches a name across
a line break and with a plural -s or -es: "Fabrikam Retail" also matches
fabrikam_retail, FabrikamRetail and Fabrikam-Retail's. A short form needs a
line of its own. Two more kinds of line:
  ?Harbor   a name that is also an ordinary word or a public product: it
            gives review findings instead of block findings
  LOG-      a ticket prefix (ends in -): LOG-1201, log-1201, LOG_1201 and
            LOG 1201 give ticket-key review findings
A term that holds , ; : = / | ( ) [ ] { } < >, a backslash, a tab, two or
more spaces in a row, an arrow, a double quotation mark of any style
(straight, curly, low or angle) or a dash between spaces may never match,
so the scan warns about its line on stderr. It warns too about a term that
starts with a list bullet or number (* Fabrikam, 1. Fabrikam); a hyphen
bullet (- Fabrikam) still matches.

Each finding prints as  path:line: severity: category: excerpt
  block   secrets (credentials in links, password and token assignments,
          known key formats) and confidential terms; always fix
  review  ticket keys, merge-request numbers, links with or without a
          scheme, e-mail addresses, host names, IP addresses, local paths
          (other than the ~/linkedin-profile and ~/work-history folders the
          skills propose), @handles, terms marked ?, terms inside an
          identifier (getFabrikamOrders), and what a folder scan cannot
          read; fix unless public and wanted
Secrets are masked in every line of the output. The summary line reads
  scan_text: B block, R review findings in F of N files[; not scanned: ...][; cannot read: ...][; terms: T names, P ticket prefixes]
or, with no finding,
  scan_text: nothing found in N files[; cannot read: ...][; terms: ...]
The terms part comes with --terms and counts what the terms file holds.

Exit status: 2 on usage errors, when the terms file holds no names or ticket
prefixes, or when a file cannot be read (the other files are still scanned);
otherwise 1 if there is any block finding, else 0.
Standard library only; Python 3.8 or newer.
"""

import argparse
import bisect
import os
import re
import sys

TEXT_SUFFIXES = (".md", ".markdown", ".txt", ".csv", ".tsv", ".json", ".jsonl", ".yaml", ".yml", ".log")
# Skipped only directly under a folder passed on the command line.
SKIP_DIRS = {"local-only", "linkedin-export", ".git"}
# Files the operating system writes; they hold no text of the person's.
IGNORED_FILES = {".DS_Store", "Thumbs.db", "desktop.ini"}
UNSCANNED = {
    "file": "unscanned-file: not a text file the scanner reads; open it, or move it to local-only/",
    "symlink": "unscanned-folder: symlinked folder, not followed; scan its target, or move it to local-only/",
    "git": "unscanned-folder: a git repository's data; move the repository out of the workspace or to local-only/",
    "unreadable": "unscanned-folder: cannot be read; check its permissions",
}

# Key names that hold a secret; a name may end in one (DB_PASSWORD, "api_key", SECRET_KEY_BASE).
SECRET_NAME = (
    r"(?:password|passwd|pwd|passphrase|secret|token|api[_-]?key|access[_-]?key|private[_-]?key|client[_-]?secret)"
    r"(?:[_-](?:key|base|value))*"
)

SECRET_PATTERNS = [
    ("aws-access-key", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("github-token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}\b|\bgithub_pat_[A-Za-z0-9_]{40,}\b")),
    ("gitlab-token", re.compile(r"\bgl(?:pat|dt|rt|cbt|ptt|ft|imt|oas)-[A-Za-z0-9_-]{20,}")),
    ("slack-token", re.compile(r"\bxox[abposr]-[A-Za-z0-9-]{10,}")),
    ("atlassian-token", re.compile(r"\bATATT[A-Za-z0-9_=-]{20,}")),
    ("anthropic-key", re.compile(r"\bsk-ant-[A-Za-z0-9_-]{20,}")),
    ("openai-key", re.compile(r"\bsk-(?:proj-|svcacct-)?[A-Za-z0-9]{20}[A-Za-z0-9_-]{12,}")),
    ("google-api-key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("stripe-key", re.compile(r"\b[rs]k_(?:live|test)_[A-Za-z0-9]{16,}")),
    ("npm-token", re.compile(r"\bnpm_[A-Za-z0-9]{36}\b")),
    ("private-key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}")),
    ("bearer-token", re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~+/-]{20,}=*")),
    # user:password@ in a link, such as postgres://app:secret@db.example.com
    ("url-credentials", re.compile(r"(?i)\b[a-z][a-z0-9+.-]{0,30}://[^\s/:@]*:[^\s/@]+@")),
    (
        # A value that only names a variable or a placeholder ($TOKEN, %TOKEN%, <token>, {{ token }}) is not a secret.
        "secret-assignment",
        re.compile(r"(?i)(?<![a-z0-9])" + SECRET_NAME + r"['\"]?\s*[:=]\s*['\"]?(?!\$\{?[A-Za-z_]\w*\}?(?:[\s'\"`]|$)|%\w+%|<[^>\s]+>|\{\{)[^\s'\"`]{6,}"),
    ),
    # "The password is X": the value needs a digit or a symbol, so "the password was leaked" stays clean.
    ("password-in-text", re.compile(r"(?i)\bpass(?:word|phrase)\s+(?:is|was)\s+(?=\S*[\d!@#$%^&*])\S{6,}")),
]

REVIEW_PATTERNS = [
    ("ticket-key", re.compile(r"\b[A-Z][A-Z0-9]{1,9}-\d{1,6}\b")),
    ("merge-request-ref", re.compile(r"(?<![\w&!])![0-9]{2,7}\b|(?i:\b(?:MR|PR|merge request|pull request)\s*[!#]?\d{1,7}\b)")),
    ("issue-ref", re.compile(r"(?<![\w&#])#\d{3,7}\b")),
    ("url", re.compile(r"(?i)\b[a-z][a-z0-9+.-]{0,30}://[^\s<>()\[\]\"'`]+")),
    # A link without a scheme: a domain and a path, such as gitlab.com/group/repo.
    # A last label of js (Vue.js/React) names a library, not a domain.
    ("link", re.compile(r"(?<![\w./@:-])(?:[A-Za-z0-9-]+\.)+(?!js\b)[a-z]{2,24}(?:/[^\s/<>()\[\]\"'`]+)+")),
    ("email", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("ip-address", re.compile(r"\b(?:25[0-5]|2[0-4]\d|1?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|1?\d?\d)){3}\b")),
    (
        "host-name",
        re.compile(
            r"(?i)\b[a-z0-9-]+(?:\.[a-z0-9-]+)*\.(?:internal|local|corp|lan|intranet)\b"
            r"|\b[a-z0-9-]+\.atlassian\.net\b"
            r"|\b(?:gitlab|jira|confluence|wiki|git|ci|jenkins|grafana|kibana)\.[a-z0-9-]+\.[a-z]{2,}\b"
        ),
    ),
    # Home-folder paths, and the folder names Claude Code makes from them (-Users-alex-work-repo).
    (
        "local-path",
        re.compile(
            r"(?<![\w.~-])/(?:Users|home)/[^\s/<>()\[\]\"'`]+(?:/[^\s<>()\[\]\"'`]*)?"
            r"|(?<![\w/])~/[^\s<>()\[\]\"'`]+"
            r"|(?i:\b[a-z]:\\users\\[^\s<>()\[\]\"'`]+)"
            r"|(?<![\w-])-(?:Users|home)-[A-Za-z0-9][A-Za-z0-9-]*"
            r"|\b[A-Za-z]--Users-[A-Za-z0-9][A-Za-z0-9-]*"
        ),
    ),
    ("handle", re.compile(r"(?<![\w.@/])@[A-Za-z][A-Za-z0-9_.-]{1,38}")),
]

# Public standards and time labels that look like ticket keys.
NOT_TICKETS = re.compile(
    r"^(?:UTF|ISO|SHA|COVID|ES|ECMA|RFC|TLS|SSL|HTTP|WCAG|IEC|IEEE|OWASP|PCI|SOC|EN|BS|ISBN|IPV|GPT|PSD|IFRS)-\d+$"
    r"|^(?:Q[1-4]|H[12])-\d{2,4}$"
)
# The folders the skills propose (~/linkedin-profile/, ~/work-history/) and paths inside them are not a leak.
WORKSPACE_PATH = re.compile(
    r"^(?:~|/(?:Users|home)/[^/]+|[A-Za-z]:\\Users\\[^\\]+)[/\\](?:linkedin-profile|work-history)(?:[/\\]|[.,;:]?$)"
    r"|-(?:linkedin-profile|work-history)$",
    re.IGNORECASE,
)

# A term's words: split at separators and where the letter case changes (ShipmentApi, APIGateway).
TERM_WORDS = re.compile(r"[\s_.\-]+|(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")
# Where a term ends, after an optional plural: before anything but a letter or digit, or where an
# identifier goes on with a digit after a letter (falcon2), with a capital after a lowercase letter
# (FabrikamClient, fabrikamAPI), or with a capital that starts a word, or V and a digit (FALCONGateway,
# ShipmentAPIV2). Not inside an all-caps word or its plural, even with a version after it: NORDIC is
# clean for Nord, FALCONRY for Falcon, SAML, SAML2 and SAMLv2 for Sam, ALBs and ALBv2 for Al.
TERM_END = r"(?:e?s)?(?:(?![^\W_])|(?<=[^\W\d_])(?=\d)|(?-i:(?<=[a-z])(?=[A-Z])|(?=V\d|[A-Z](?!s(?![^\W_])|v\d)[a-z])))"
# A term of one or two letters or digits, such as Al or Ed, does not end before a digit, even after a
# plural, as many public codes start with one: AL2023, Ed25519, LIS3DH for Li.
SHORT_TERM_END = r"(?!(?:e?s)?\d)" + TERM_END
# Where a term starts a capitalized word inside an identifier: after a lowercase letter or a digit
# (getFabrikamOrders, PeregrineFalcon), or after a capital (IFabrikamClient). Such a match is a review
# finding, because the identifier may name something else (GitHub for Hub, TypeScript for Script).
TERM_INSIDE = r"(?-i:(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z]))"
# A note, a second name or quotation marks written into a terms line: Fabrikam Retail (client),
# Fabrikam Retail - client, Fabrikam Retail<TAB>client, Northwind [partner], Wingtip -> client (or
# an arrow character, U+2190 to U+21FF), Project Falcon / Falcon, or a name in double quotation marks
# of any style; or a list bullet or number and a space at the start (* Wingtip, + Wingtip, 1. Wingtip;
# the bullet may also be an en or em dash, U+2022, U+2023, U+2043, U+00B7 or a shape from U+25A0 to
# U+25FF). Such a term matches only text that holds the same note, marks or bullet, so it may never
# match. Two spaces in a row warn as well: a stray double space inside a name still matches, but a
# note after a column gap (Fabrikam Retail  client) never does. A hyphen bullet (- Contoso Pharma)
# gets no warning, as the hyphen is a separator and the name still matches, and neither does a single
# quotation mark, which names hold as an apostrophe (O'Brien).
TERM_NOTE = re.compile(
    r"[,;:()\[\]{}<>=/|\\\t\"\u201c\u201d\u201e\u201f\u00ab\u00bb\u2190-\u21ff]|\s[-\u2013\u2014]+\s|\s{2,}"
    r"|^(?:[*+\u2013\u2014\u2022\u2023\u2043\u00b7\u25a0-\u25ff]|\d{1,3}\.)\s"
)
TERM_COMMENT = re.compile(r"\s+#.*$")
NEWLINE = re.compile(r"\n")


def mask(value):
    value = value.strip()
    return "%s... (%d chars)" % (value[:4], len(value))


def mask_secrets(text):
    """Return text with every secret-looking match replaced by a masked stub.

    Overlapping matches merge into one stub, so a key inside an assignment is masked once.
    """
    spans = sorted(match.span() for _, pattern in SECRET_PATTERNS for match in pattern.finditer(text))
    merged = []
    for start, end in spans:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    for start, end in reversed(merged):
        text = text[:start] + "[secret " + mask(text[start:end]) + "]" + text[end:]
    return text


def term_patterns(term):
    """Return (pattern, inside) for a term, or None for a term without a letter or digit.

    Both match the term in any letter case, with any punctuation or none between its words and a
    plural -s or -es, and let it end where TERM_END says, or SHORT_TERM_END for a term of one or two
    letters or digits. pattern matches where no letter or digit comes before the term, so also at the
    start of an identifier (FabrikamClient, falcon2); inside matches where the term starts a
    capitalized word inside an identifier (getFabrikamOrders).
    """
    if not re.search(r"[^\W_]", term):
        return None
    words = [word for word in TERM_WORDS.split(term) if word]
    body = r"[\W_]*".join(re.escape(word) for word in words)
    # The lookahead for the first character changes no match, but most positions then fail before the
    # slower lookbehinds: the scan runs about three times faster.
    first = "(?=" + re.escape(words[0][0]) + ")"
    end = TERM_END if len(re.findall(r"[^\W_]", term)) > 2 else SHORT_TERM_END
    return (
        re.compile(first + r"(?<![^\W_])" + body + end, re.IGNORECASE),
        re.compile(first + TERM_INSIDE + body + end, re.IGNORECASE),
    )


def load_terms(path):
    """Return (terms, ticket prefixes, noted lines) from a terms file.

    terms holds (term, severity, patterns); a line starting with ? gives review findings.
    ticket prefixes holds patterns; a line ending in - names one, such as LOG-.
    noted lines holds the numbers of the lines whose term holds a note (TERM_NOTE).
    """
    terms = []
    tickets = []
    noted = []
    # utf-8-sig drops the byte-order mark some editors write at the start.
    with open(path, encoding="utf-8-sig") as handle:
        for number, raw in enumerate(handle, start=1):
            term = TERM_COMMENT.sub("", raw).strip()
            if not term or term.startswith("#"):
                continue
            severity = "block"
            if term.startswith("?"):
                severity, term = "review", term[1:].strip()
            if TERM_NOTE.search(term):
                noted.append(number)
            if term.endswith("-"):
                prefix = term.rstrip("-").strip()
                if prefix:
                    tickets.append(re.compile(r"(?<![^\W_])" + re.escape(prefix) + r"[-_ ]?\d+", re.IGNORECASE))
                continue
            patterns = term_patterns(term)
            if patterns:
                terms.append((term, severity, patterns))
    return terms, tickets, noted


def iter_files(paths, unscanned):
    """Yield the files to scan; add (path, kind) to unscanned for what a folder walk cannot read."""

    def unreadable(error):
        unscanned.append((error.filename, "unreadable"))

    for path in paths:
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path, onerror=unreadable):
                kept = []
                for name in sorted(dirs):
                    full = os.path.join(root, name)
                    if root == path and name in SKIP_DIRS:
                        continue
                    if name == ".git":
                        unscanned.append((full, "git"))
                    elif os.path.islink(full):
                        unscanned.append((full, "symlink"))
                    else:
                        kept.append(name)
                dirs[:] = kept
                for name in sorted(files):
                    full = os.path.join(root, name)
                    if name.lower().endswith(TEXT_SUFFIXES):
                        yield full
                    elif name not in IGNORED_FILES:
                        unscanned.append((full, "file"))
        elif os.path.isfile(path):
            yield path
        else:
            raise FileNotFoundError(path)


def find_terms(content, terms):
    """Return {line number: [(severity, term)]} for a file's text; a term may wrap onto the next line.

    A term inside an identifier gives a review finding. A line reports each term once, as a block
    finding when any of its matches there is one.
    """
    found = {}
    starts = None
    for term, severity, (pattern, inside) in terms:
        for kind, regex in ((severity, pattern), ("review", inside)):
            for match in regex.finditer(content):
                if starts is None:
                    starts = [0] + [newline.end() for newline in NEWLINE.finditer(content)]
                hits = found.setdefault(bisect.bisect_right(starts, match.start()), {})
                if hits.get(term) != "block":
                    hits[term] = kind
    return {number: [(kind, term) for term, kind in hits.items()] for number, hits in found.items()}


def scan_line(line, line_terms, tickets):
    """Yield (severity, category, excerpt) for one line: secrets, then terms, then review findings."""
    for category, pattern in SECRET_PATTERNS:
        for match in pattern.finditer(line):
            yield "block", category, mask(match.group(0))
    for severity, term in line_terms:
        yield severity, "confidential-term", term
    # Review patterns read the line with its secrets masked, so no secret reaches the output.
    masked = mask_secrets(line)
    keys = []
    for category, pattern in REVIEW_PATTERNS:
        for match in pattern.finditer(masked):
            value = match.group(0)
            if category == "ticket-key":
                if NOT_TICKETS.match(value):
                    continue
                keys.append(match.span())
            if category == "local-path" and WORKSPACE_PATH.search(value):
                continue
            yield "review", category, value[:80]
    for pattern in tickets:
        for match in pattern.finditer(masked):
            start, end = match.span()
            if not any(start < key_end and key_start < end for key_start, key_end in keys):
                yield "review", "ticket-key", match.group(0)[:80]


def plural(number, word, words=None):
    return "%d %s" % (number, word if number == 1 else words or word + "s")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--terms", metavar="FILE", help="file with one confidential term per line")
    parser.add_argument("paths", nargs="+", metavar="PATH", help="files or folders to scan")
    args = parser.parse_args(argv)

    terms, tickets = [], []
    unscanned = []
    try:
        if args.terms:
            terms, tickets, noted = load_terms(args.terms)
            for number in noted:
                print(
                    'scan_text: %s line %d may never match: one name per line, a note only after " # "' % (args.terms, number),
                    file=sys.stderr,
                )
            # An empty terms file would make the scan look clean with no name checked.
            if not terms and not tickets:
                print("scan_text: %s holds no names or ticket prefixes" % args.terms, file=sys.stderr)
                return 2
        files = list(iter_files(args.paths, unscanned))
    except (OSError, UnicodeDecodeError) as error:
        print("scan_text: cannot read %s" % error, file=sys.stderr)
        return 2

    counts = {"block": 0, "review": 0}
    files_with_findings = set()
    unreadable = 0
    for path in files:
        try:
            with open(path, encoding="utf-8", errors="replace") as handle:
                content = handle.read()
        except OSError as error:
            print("scan_text: cannot read %s: %s" % (path, error), file=sys.stderr)
            unreadable += 1
            continue
        term_lines = find_terms(content, terms)
        for number, line in enumerate(content.split("\n"), start=1):
            for severity, category, excerpt in scan_line(line, term_lines.get(number, ()), tickets):
                counts[severity] += 1
                files_with_findings.add(path)
                print("%s:%d: %s: %s: %s" % (path, number, severity, category, excerpt))
    for path, kind in unscanned:
        counts["review"] += 1
        print("%s:0: review: %s" % (path, UNSCANNED[kind]))

    scanned = len(files) - unreadable
    if counts["block"] or counts["review"]:
        summary = "scan_text: %d block, %d review findings in %d of %d files" % (
            counts["block"],
            counts["review"],
            len(files_with_findings),
            scanned,
        )
    else:
        summary = "scan_text: nothing found in %d files" % scanned
    if unscanned:
        folders = sum(1 for _, kind in unscanned if kind != "file")
        parts = [plural(number, word) for number, word in ((len(unscanned) - folders, "file"), (folders, "folder")) if number]
        summary += "; not scanned: %s" % ", ".join(parts)
    if unreadable:
        summary += "; cannot read: %s" % plural(unreadable, "file")
    if args.terms:
        summary += "; terms: %s, %s" % (plural(len(terms), "name"), plural(len(tickets), "ticket prefix", "ticket prefixes"))
    print(summary)
    if unreadable:
        return 2
    return 1 if counts["block"] else 0


if __name__ == "__main__":
    sys.exit(main())
