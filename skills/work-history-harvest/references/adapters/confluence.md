# Confluence adapter

Pages and blog posts the person created or edited, inside the harvest time window.

## Available when

- Atlassian tools are connected to this session (the Atlassian MCP server or connector), with a tool that searches Confluence with CQL: `searchConfluence` on the Atlassian MCP server; or
- in full mode only, the person has an Atlassian API token and exports it in their own shell. Use it from the environment only: refer to it by its variable name in commands, never print it, and never write it to a file.

The Atlassian MCP server's address is `https://mcp.atlassian.com/v2/mcp`. The server acts with the person's own permissions. When it is not connected, connecting it is the person's decision, within the employer's rules. Give them the steps: the person runs every command and sign-in, and you never change their configuration yourself. In Claude Code, they add the server with `claude mcp add --transport http atlassian https://mcp.atlassian.com/v2/mcp` and then sign in with their work account. Atlassian stopped supporting the old address `https://mcp.atlassian.com/v1/sse` after 2026-06-30, so the person replaces it with the v2 address wherever a configuration still names it. A connection to `/v1/mcp` starts using the v2 tools on its own on 2027-03-01. Moving a Claude Code connection from v1 to v2 needs a new sign-in, because v1 credentials do not carry over.

The employer's Atlassian admin decides which AI tools may connect, whether API tokens work with the MCP server, and which IP addresses may connect. A blocked address sees "You don't have permission to connect from this IP address." Treat a refusal that points to the admin or to the IP address as the employer's decision: stop using Atlassian tools for this source, use no other tool or token, suggest no way around the block, and offer the [interview](../interview.md). Use the document route only when the person confirms that the employer allows AI tools to read this data. Report the refusal in clean words, with no host or site name, so that harvest records the source as skipped with the reason.

Without any of these routes, ask for a document: a list of the person's pages, from their Confluence profile or a saved search, pasted or saved as PDF into `local-only/`.

## Collect

With the Atlassian MCP:

1. **Pick the site.** Call `getAccessibleAtlassianResources` first in every session. Every other call needs a `cloudId`, and this tool lists the sites the person can reach with their `cloudId` values. When it lists more than one site, ask the person which one is the employer's. Pass its `cloudId` in every later call.
2. **Search** with `searchConfluence`. Take its parameter names (limit, next page) from the tool's schema, and page until no next page is left.

This adapter only reads. Call a tool directly when it is in your tool list. Find any other tool with `discover`, and run it with `executeRead`, never with `executeWrite` or `executeDestructive`.

CQL, with `<start>` the first day of the time window and `<end>` the day after its last day, both as `yyyy-MM-dd`:

```
type IN (page, blogpost) AND creator = currentUser() AND created >= "<start>" AND created < "<end>" ORDER BY created ASC
type IN (page, blogpost) AND contributor = currentUser() AND lastmodified >= "<start>" ORDER BY lastmodified DESC
```

The first finds pages and blog posts the person wrote. The second finds everything they created or edited, so it repeats the first: count each page once. Keep: title, space name, labels, created and last-modified dates, and for pages the person wrote, the opening paragraph, enough to know what the page is for.

Inference: `lastmodified` is the date of the latest edit by anyone, not of the person's own edit. Date a theme by the pages the person created, and treat the period of pages they only edited as approximate.

`getWorkActivity` (beta) lists activity across the work sources it supports. Without a date filter it covers only the last seven days, and it returns counts and limited item previews. If you use it for an overview of the person's own activity, pass the time window as its date filter, and take the themes from the query results.

With the REST API: `GET https://<site>.atlassian.net/wiki/rest/api/content/search?cql=<url-encoded CQL>&limit=50`, following the `next` link. Search without `expand`, then read the opening paragraph of each page the person wrote. With `expand=body.storage.value`, a search returns at most 50 results per request whatever the limit, and the response does not mention the cut. The sources below do not cover how this endpoint pages, so check the first response, and use the document route when it fails.

Done when the site is picked, and both queries have run over the whole window or have failed and are reported with the themes. On the document route, done when the document is read or the person skips the source.

## Turn into themes

- Group by purpose: guides and how-tos, architecture decisions, research and comparisons, incident reviews, onboarding material, process documentation, meeting or planning pages.
- For each theme: what the documents were for, how many, the period, and who used them (by function: "the frontend team", "new joiners"), only when the page or the person says so.
- Pages the person wrote are evidence of technical writing and knowledge sharing. A decision record shows that the person wrote the decision up; whether they led it is a question for the interview.

## Leave out

Page and space names when they are internal, links, page content beyond the purpose, and names of people mentioned on the pages.

## Sources

Checked 2026-10-30. Dates are the pages' own.

- [CQL fields](https://developer.atlassian.com/cloud/confluence/cql-fields/), last updated 2026-10-30
- [CQL functions](https://developer.atlassian.com/cloud/confluence/cql-functions/), last updated 2026-10-30
- [Advanced searching using CQL](https://developer.atlassian.com/cloud/confluence/advanced-searching-using-cql/), last updated 2026-10-30
- [Get started with the Atlassian MCP server](https://support.atlassian.com/atlassian-ai-gateway/docs/get-started-with-the-atlassian-remote-mcp-server/), undated
- [Supported tools](https://support.atlassian.com/atlassian-ai-gateway/docs/supported-tools/), undated
- [How to upgrade from Atlassian MCP v1 to Atlassian MCP v2](https://support.atlassian.com/atlassian-ai-gateway/docs/how-to-upgrade-from-atlassian-mcp-v1-to-atlassian-mcp-v2/), undated
- [Control Atlassian MCP server settings](https://support.atlassian.com/security-and-access-policies/docs/control-atlassian-rovo-mcp-server-settings/), undated
- [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server), README, undated
