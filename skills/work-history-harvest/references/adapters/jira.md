# Jira adapter

Issues the person was assigned, reported or resolved, inside the harvest time window.

## Available when

- Atlassian tools are connected to this session (the Atlassian MCP server or connector), with a tool that searches Jira with JQL: `searchJiraIssuesUsingJql` on the Atlassian MCP server; or
- in full mode only, the person has an Atlassian API token and exports it in their own shell. Use it from the environment only: refer to it by its variable name in commands, never print it, and never write it to a file.

The Atlassian MCP server's address is `https://mcp.atlassian.com/v2/mcp`. The server acts with the person's own permissions. When it is not connected, connecting it is the person's decision, within the employer's rules. Give them the steps: the person runs every command and sign-in, and you never change their configuration yourself. In Claude Code, they add the server with `claude mcp add --transport http atlassian https://mcp.atlassian.com/v2/mcp` and then sign in with their work account. Atlassian stopped supporting the old address `https://mcp.atlassian.com/v1/sse` after 2026-06-30, so the person replaces it with the v2 address wherever a configuration still names it. A connection to `/v1/mcp` starts using the v2 tools on its own on 2027-03-01. Moving a Claude Code connection from v1 to v2 needs a new sign-in, because v1 credentials do not carry over.

The employer's Atlassian admin decides which AI tools may connect, whether API tokens work with the MCP server, and which IP addresses may connect. A blocked address sees "You don't have permission to connect from this IP address." Treat a refusal that points to the admin or to the IP address as the employer's decision: stop using Atlassian tools for this source, use no other tool or token, suggest no way around the block, and offer the [interview](../interview.md). Use the document route only when the person confirms that the employer allows AI tools to read this data. Report the refusal in clean words, with no host or site name, so that harvest records the source as skipped with the reason.

Without any of these routes, ask for a document: the person can run the JQL below in Jira's issue search, choose the columns listed under Collect, and export the result as CSV into `local-only/`. The queries with `currentUser()` need no accountId. On a self-hosted Jira (Data Center), the person's username takes the place of `<accountId>`.

## Collect

With the Atlassian MCP:

1. **Pick the site.** Call `getAccessibleAtlassianResources` first in every session. Every other call needs a `cloudId`, and this tool lists the sites the person can reach with their `cloudId` values. When it lists more than one site, ask the person which one is the employer's. Pass its `cloudId` in every later call.
2. **Identify the person.** Jira Cloud JQL names people by accountId, never by username. Call `atlassianUserInfo` and take the person's accountId from the result. When the result holds none, use `getJiraCurrentUser`.
3. **Search** with `searchJiraIssuesUsingJql`. Take its parameter names (fields, page size, next page) from the tool's schema, and page until no next page is left.

This adapter only reads. Call a tool directly when it is in your tool list. Find any other tool, such as `getJiraCurrentUser` or `listJiraIssueComments`, with `discover`, and run it with `executeRead`, never with `executeWrite` or `executeDestructive`.

JQL, with `<start>` the first day of the time window and `<end>` the day after its last day, both as `yyyy/MM/dd` in quotes:

```
assignee WAS "<accountId>" DURING ("<start>","<end>") ORDER BY created ASC
reporter = currentUser() AND created >= "<start>" AND created < "<end>" ORDER BY created ASC
```

The first finds issues the person was assigned at any time in the window; the second, issues they raised (bug reports, proposals). Request only these fields: summary, issue type, status, resolution, resolution date, created, labels, components, parent (epic), priority, assignee. Page through all results; large result sets are normal.

`WAS` and `CHANGED` take the accountId: Jira's documentation lists them among the operators that `currentUser()` does not support. That documentation, which also covers `updatedBy()` below, is for Jira Data Center, and Jira Cloud may reject these history forms. Run the history query first. When Jira rejects it or it returns nothing, run this plain clause instead; it finds only the issues still assigned to the person:

```
assignee = currentUser() AND updated >= "<start>" AND created < "<end>" ORDER BY created ASC
```

Two more history queries, for work that shows less in assignments:

- Testers and analysts who move issues through the workflow: `status CHANGED BY "<accountId>" DURING ("<start>","<end>")`.
- People who mostly review and advise in comments: `issuekey IN updatedBy("<accountId>", "<start>", "<end>")`. It matches every kind of edit. JQL's `comment` field cannot narrow it, because it searches comment text, not authors. Count an issue only after `listJiraIssueComments` shows a comment by the person.

When one of these fails, skip it and report it with the themes.

`getWorkActivity` (beta) lists activity across the work sources it supports. Without a date filter it covers only the last seven days, and it returns counts and limited item previews. If you use it for an overview of the person's own activity, pass the time window as its date filter, and take the themes from the query results.

With the REST API: `GET https://<site>.atlassian.net/rest/api/3/search/jql?jql=<url-encoded JQL>&fields=<comma-separated fields>&maxResults=100`, following `nextPageToken`. `GET https://<site>.atlassian.net/rest/api/3/myself` returns the person's accountId. The sources below do not cover this search endpoint or its paging, so check the first response, and use the document route when it fails.

Done when the site and the person are identified, and every query has run over the whole window or has failed and is reported with the themes. On the document route, done when the export is read or the person skips the source.

## Turn into themes

- Group by parent epic first, then by component and label. Epics are often named after the initiative, which makes them the natural theme.
- For each theme: what the initiative was, the period, counts by issue type (stories delivered, bugs fixed, spikes), with issues resolved while the person was the assignee (compare the assignee's accountId) kept apart from issues they worked on and passed on, and the resolutions.
- Role signals: issues assigned and resolved mean `built` or `contributed` depending on the share of the epic, which these queries do not show, so the person confirms it; raising many bugs in an area is quality work; being the assignee of the epic itself hints at `led`; confirm in the interview.

## Leave out

Issue keys, project keys, links, assignee and reporter names, and summaries copied word for word: summaries often name clients or internal systems. Describe the work in your own clean words.

## Sources

Checked 2026-10-30. Dates are the pages' own.

- [REST API migration guide and deprecation notice - removal of username and userkey](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/), last updated 2026-10-30
- [Advanced searching - fields reference (Jira Software Data Center 11.3)](https://confluence.atlassian.com/jirasoftwareserver/advanced-searching-fields-reference-939938743.html), undated
- [Advanced searching - operators reference (Jira Software Data Center 11.3)](https://confluence.atlassian.com/jirasoftwareserver/advanced-searching-operators-reference-939938745.html), last modified 2023-03-08
- [Advanced searching - functions reference (Jira Software Data Center 11.3)](https://confluence.atlassian.com/jirasoftwareserver/advanced-searching-functions-reference-939938746.html), last modified 2023-10-12
- [Get started with the Atlassian MCP server](https://support.atlassian.com/atlassian-ai-gateway/docs/get-started-with-the-atlassian-remote-mcp-server/), undated
- [Supported tools](https://support.atlassian.com/atlassian-ai-gateway/docs/supported-tools/), undated
- [How to upgrade from Atlassian MCP v1 to Atlassian MCP v2](https://support.atlassian.com/atlassian-ai-gateway/docs/how-to-upgrade-from-atlassian-mcp-v1-to-atlassian-mcp-v2/), undated
- [Control Atlassian MCP server settings](https://support.atlassian.com/security-and-access-policies/docs/control-atlassian-rovo-mcp-server-settings/), undated
- [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server), README, undated
