---
type: tool_used
tool: Bash
input_match: 'atlassian\.(net|com)|/rest/api/'
min: 0
max: 0
weight: 1
---

Deterministic check, so it also sees the middle of the run that an llm judge of the trace never sees: no Bash command names an Atlassian host or a Jira REST path. The harness counts the Bash calls whose input matches input_match and ignores this text. min stays at 0 on purpose: without it the harness requires at least one call, and max 0 could never pass. Graders 06 and 07 cover a request that a script file carries, written with Write or Edit and run from Bash.
