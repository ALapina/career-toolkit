"""Checks that keep the skills in this repository consistent with each other.

Run from the repository root:  python3 -m unittest discover -s tests
"""

import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
SKILL_DIRS = sorted(path.parent for path in SKILLS.glob("*/SKILL.md"))

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
# A rule ID in backticks, such as `headline-1` or `career-break-4`.
RULE_REF = re.compile(r"`([a-z]+(?:-[a-z]+)*-\d+)`")
RULE_DEF = re.compile(r"^(?:- |\| )`([a-z]+(?:-[a-z]+)*-\d+)`", re.MULTILINE)


def markdown_files(folder):
    return sorted(path for path in folder.rglob("*.md") if path.is_file())


def without_fences(text):
    """Return the lines outside fenced code blocks, with their line numbers."""
    inside = False
    for number, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line):
            inside = not inside
            continue
        if not inside:
            yield number, line


def slug(heading):
    """GitHub's anchor for a heading: lowercase, punctuation dropped, spaces to hyphens."""
    text = re.sub(r"[`*_]", "", heading).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path):
    found = set()
    counts = {}
    for _, line in without_fences(path.read_text(encoding="utf-8")):
        match = HEADING.match(line)
        if match:
            base = slug(match.group(2))
            number = counts.get(base, 0)
            counts[base] = number + 1
            found.add(base if number == 0 else "%s-%d" % (base, number))
    return found


def opening_block(text):
    """Return the text of the '## How to read this document' section, up to the next heading of level 2."""
    match = re.search(r"^## How to read this document\n\n(.*?)\n+## ", text, re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else None


class FormatCopies(unittest.TestCase):
    def test_each_skill_keeps_an_identical_document_format(self):
        copies = sorted(SKILLS.glob("*/references/document-format.md"))
        self.assertGreaterEqual(len(copies), 2, "expected a copy in each skill that uses the document")
        first = copies[0].read_text(encoding="utf-8")
        for copy in copies[1:]:
            self.assertEqual(first, copy.read_text(encoding="utf-8"), "%s differs from %s" % (copy, copies[0]))

    def test_template_opening_block_matches_the_format(self):
        format_text = (SKILLS / "work-history-harvest/references/document-format.md").read_text(encoding="utf-8")
        match = re.search(r"holds exactly this text:\n\n```markdown\n(.*?)\n```", format_text, re.DOTALL)
        self.assertIsNotNone(match, "document-format.md lost its opening block")
        template = (SKILLS / "work-history-harvest/templates/work-history.md").read_text(encoding="utf-8")
        self.assertEqual(match.group(1).strip(), opening_block(template))

    def test_eval_fixtures_use_the_current_opening_block(self):
        template = (SKILLS / "work-history-harvest/templates/work-history.md").read_text(encoding="utf-8")
        expected = opening_block(template)
        fixtures = sorted((ROOT / "evals").rglob("work-history-*.md"))
        self.assertTrue(fixtures, "no work history document among the eval fixtures")
        for fixture in fixtures:
            self.assertEqual(expected, opening_block(fixture.read_text(encoding="utf-8")), str(fixture))

    def test_scanner_copies_are_identical(self):
        copies = sorted(SKILLS.glob("*/scripts/scan_text.py"))
        self.assertGreaterEqual(len(copies), 2)
        first = copies[0].read_bytes()
        for copy in copies[1:]:
            self.assertEqual(first, copy.read_bytes(), "%s differs from %s" % (copy, copies[0]))


class SkillLinks(unittest.TestCase):
    def test_links_resolve_inside_their_skill(self):
        problems = []
        for skill in SKILL_DIRS:
            for path in markdown_files(skill):
                for number, line in without_fences(path.read_text(encoding="utf-8")):
                    for target in LINK.findall(line):
                        if re.match(r"[a-z][a-z0-9+.-]*:", target):
                            continue
                        file_part, _, anchor = target.partition("#")
                        destination = (path.parent / file_part).resolve() if file_part else path
                        where = "%s:%d: %s" % (path.relative_to(ROOT), number, target)
                        if skill.resolve() not in destination.parents and destination != skill.resolve():
                            problems.append(where + " (leaves the skill folder)")
                        elif not destination.exists():
                            problems.append(where + " (no such file)")
                        elif anchor and destination.suffix == ".md" and anchor not in anchors(destination):
                            problems.append(where + " (no such heading)")
        self.assertEqual([], problems)

    def test_rule_ids_resolve_inside_their_skill(self):
        files = {skill: markdown_files(skill) + sorted(skill.rglob("*.py")) for skill in SKILL_DIRS}
        defined = {skill: set() for skill in SKILL_DIRS}
        for skill, paths in files.items():
            for path in paths:
                defined[skill].update(RULE_DEF.findall(path.read_text(encoding="utf-8")))
        # An ID counts as a rule reference when any skill defines rules of its area (`log-1201` is a ticket example).
        areas = {rule.rsplit("-", 1)[0] for rules in defined.values() for rule in rules}
        self.assertTrue(areas, "found no rule definitions at all")
        problems = []
        for skill, paths in files.items():
            for path in paths:
                for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                    for rule in RULE_REF.findall(line):
                        if rule.rsplit("-", 1)[0] in areas and rule not in defined[skill]:
                            problems.append("%s:%d: %s" % (path.relative_to(ROOT), number, rule))
        self.assertEqual([], problems)


class Manifests(unittest.TestCase):
    def test_plugin_and_marketplace_are_career_toolkit(self):
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual("career-toolkit", plugin["name"])
        self.assertEqual("career-toolkit", marketplace["name"])
        self.assertEqual(["career-toolkit"], [entry["name"] for entry in marketplace["plugins"]])

    def test_skill_names_match_their_folders(self):
        for skill in SKILL_DIRS:
            text = (skill / "SKILL.md").read_text(encoding="utf-8")
            front = text.split("---", 2)[1]
            name = re.search(r"^name:\s*(\S+)\s*$", front, re.MULTILINE)
            description = re.search(r"^description:\s*(.+)$", front, re.MULTILINE)
            self.assertIsNotNone(name, skill)
            self.assertEqual(skill.name, name.group(1))
            self.assertIsNotNone(description, skill)
            self.assertLessEqual(len(description.group(1)), 1024, skill)


if __name__ == "__main__":
    unittest.main()
