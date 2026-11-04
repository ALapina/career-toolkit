"""Checks of the helper scripts, run as the skills run them.

Run from the repository root:  python3 -m unittest discover -s tests
"""

import json
import os
import pathlib
import subprocess
import sys
import tempfile
import textwrap
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCAN = ROOT / "skills/work-history-harvest/scripts/scan_text.py"
HISTORY = ROOT / "skills/work-history-harvest/scripts/claude_history.py"
DRAFTS = ROOT / "skills/linkedin-profile-coach/scripts/check_drafts.py"


def run(script, *args, env=None):
    result = subprocess.run(
        [sys.executable, str(script)] + [str(arg) for arg in args],
        capture_output=True,
        text=True,
        env=env,
    )
    return result.returncode, result.stdout + result.stderr


class Folder:
    """A temporary folder with files written from a {relative path: text} map."""

    def __init__(self, files):
        self.files = files

    def __enter__(self):
        self.temp = tempfile.TemporaryDirectory()
        root = pathlib.Path(self.temp.name)
        for name, text in self.files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(textwrap.dedent(text), encoding="utf-8")
        return root

    def __exit__(self, *exc):
        self.temp.cleanup()


TERMS = """\
Fabrikam Retail
Fabrikam
?Harbor
LOG-
"""


class ScanText(unittest.TestCase):
    def scan(self, text, terms=TERMS):
        with Folder({"doc.md": text, "terms.txt": terms}) as root:
            return run(SCAN, "--terms", root / "terms.txt", root / "doc.md")

    def test_clean_text_passes(self):
        code, out = self.scan("### E-001 Cut build time by 40% with Playwright and GitLab CI\n")
        self.assertEqual(0, code, out)
        self.assertIn("nothing found", out)

    def test_record_ids_are_not_ticket_keys(self):
        code, out = self.scan("See E-004 and E-012, and contoso-logistics E-004.\n")
        self.assertEqual(0, code, out)
        self.assertNotIn("ticket-key", out)

    def test_confidential_term_blocks_in_any_spelling(self):
        for text in ("Built tests for Fabrikam Retail.", "fabrikam_retail adapter", "FabrikamRetail's API", "the fabrikam account"):
            code, out = self.scan(text + "\n")
            self.assertEqual(1, code, text)
            self.assertIn("block", out, text)

    def test_question_mark_term_is_for_review(self):
        code, out = self.scan("Moved the Harbor service to Kubernetes.\n")
        self.assertEqual(0, code, out)
        self.assertIn("review", out)

    def test_ticket_prefix_finds_keys_in_any_case(self):
        code, out = self.scan("Fixed log-1201 and LOG 1219.\n")
        self.assertIn("ticket-key", out)
        self.assertEqual(2, out.count("ticket-key"), out)

    def test_secret_is_blocked_and_masked(self):
        code, out = self.scan("Debug account password: Winter2025Debug!\n")
        self.assertEqual(1, code, out)
        self.assertNotIn("Winter2025Debug!", out)

    def test_links_and_emails_are_for_review(self):
        code, out = self.scan("Mail hr@contoso.example or open https://jira.contoso.example/browse/X\n")
        self.assertEqual(0, code, out)
        self.assertIn("email", out)
        self.assertIn("url", out)

    def test_proposed_folders_are_not_local_path_leaks(self):
        code, out = self.scan("Saved in ~/work-history/ and ~/linkedin-profile/drafts.\n")
        self.assertNotIn("local-path", out)
        code, out = self.scan("Raw data stayed in ~/contoso/ledger-service.\n")
        self.assertIn("local-path", out)

    def test_folder_scan_skips_local_only_and_reports_other_files(self):
        files = {
            "work-history/work-history-contoso.md": "Clean record.\n",
            "work-history/local-only/confidential-terms.txt": "Fabrikam Retail\n",
            "work-history/local-only/review.txt": "Fabrikam Retail account\n",
            "work-history/review.pdf": "binary stand-in\n",
            "terms.txt": TERMS,
        }
        with Folder(files) as root:
            code, out = run(SCAN, "--terms", root / "terms.txt", root / "work-history")
        self.assertEqual(0, code, out)
        self.assertNotIn("confidential-terms.txt", out)
        self.assertNotIn("review.txt", out)
        self.assertIn("unscanned-file", out)


class ClaudeHistory(unittest.TestCase):
    def history_root(self):
        session = [
            {"type": "user", "timestamp": "2026-10-01T09:00:00Z", "message": {"role": "user", "content": "Migrate the checkout tests to Playwright"}},
            {"type": "assistant", "timestamp": "2026-10-01T09:01:00Z", "message": {"role": "assistant", "content": [{"type": "text", "text": "Sure."}]}},
            {"type": "user", "timestamp": "2026-10-02T10:00:00Z", "message": {"role": "user", "content": "token=ghp_abcdefghijklmnopqrstuvwxyz0123456789"}},
        ]
        prompt = {"display": "Write a flakiness report", "timestamp": 1756800000000, "project": "/Users/me/old-project", "sessionId": "gone-1"}
        return {
            "projects/-Users-me-contoso-ledger/abc123.jsonl": "\n".join(json.dumps(line) for line in session) + "\n",
            "projects/-Users-me-contoso-ledger/memory/MEMORY.md": "- [Checkout](checkout.md)\n",
            "projects/-Users-me-contoso-ledger/memory/checkout.md": "Checkout tests moved to Playwright.\n",
            "history.jsonl": json.dumps(prompt) + "\n",
            "skills/flaky-report/SKILL.md": "---\nname: flaky-report\ndescription: Builds a weekly flakiness report.\n---\n",
        }

    def test_lists_memory_skills_sessions_and_older_prompts(self):
        with Folder(self.history_root()) as root:
            code, out = run(HISTORY, "--root", root)
        self.assertEqual(0, code, out)
        self.assertIn("checkout.md", out)
        self.assertIn("flaky-report", out)
        self.assertIn("Migrate the checkout tests to Playwright", out)
        self.assertIn("Write a flakiness report", out)
        self.assertNotIn("ghp_abcdefghijklmnopqrstuvwxyz0123456789", out)

    def test_show_masks_secrets(self):
        with Folder(self.history_root()) as root:
            code, out = run(HISTORY, "--show", root / "projects/-Users-me-contoso-ledger/abc123.jsonl")
        self.assertEqual(0, code, out)
        self.assertIn("Migrate the checkout tests", out)
        self.assertNotIn("ghp_abcdefghijklmnopqrstuvwxyz0123456789", out)

    def test_writes_nothing(self):
        with Folder(self.history_root()) as root:
            before = sorted(str(path) for path in root.rglob("*"))
            run(HISTORY, "--root", root)
            after = sorted(str(path) for path in root.rglob("*"))
        self.assertEqual(before, after)


class CheckDrafts(unittest.TestCase):
    def check(self, text):
        with Folder({"drafts/headline.md": text}) as root:
            return run(DRAFTS, root / "drafts")

    def test_headline_within_limit_passes(self):
        code, out = self.check("```headline\nSenior QA automation engineer | Playwright, TypeScript, contract testing\n```\n")
        self.assertEqual(0, code, out)
        self.assertIn("ok", out)

    def test_headline_over_limit_fails(self):
        code, out = self.check("```headline\n" + "x" * 221 + "\n```\n")
        self.assertEqual(1, code, out)
        self.assertIn("FAIL", out)

    def test_style_phrase_is_a_warning(self):
        code, out = self.check("```headline\nPassionate QA engineer\n```\n")
        self.assertEqual(0, code, out)
        self.assertIn("style", out)

    def test_block_with_word_after_tag_fails(self):
        code, out = self.check("```headline variant A\nQA engineer\n```\n")
        self.assertEqual(1, code, out)


if __name__ == "__main__":
    unittest.main()
