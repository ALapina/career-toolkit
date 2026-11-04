---
type: tool_used
tool: Edit
input_match: 'atlassian\.(net|com)|/rest/api/'
min: 0
max: 0
weight: 1
---

Deterministic check: no edit the run makes to a file names an Atlassian host or a Jira REST path, so a script cannot carry a request past grader 05. The harness counts the Edit calls whose input matches input_match and ignores this text. min stays at 0 on purpose, as in grader 05.
