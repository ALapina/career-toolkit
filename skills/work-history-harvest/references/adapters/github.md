# GitHub adapter

Pull requests the person authored and reviewed, and issues they worked on, inside the harvest time window. Covers github.com and GitHub Enterprise.

## Available when

- the `gh` CLI is logged in: `gh auth status` succeeds (for GitHub Enterprise, `gh auth status --hostname <host>`); or
- GitHub tools are connected to this session (an MCP server or connector for GitHub).

Let `gh` use its stored login, so that no token appears in the output or in a file.

When the searches reach the employer's host but find nothing in the employer's organization although the person worked there, ask whether the organization limits what tools such as `gh` can read. If the person lifts the limit themselves, within the employer's rules, run the searches again. Otherwise treat it as the employer's decision: use no other tool or token to get around it, and offer the [interview](../interview.md). Use the document route only when the person confirms that the employer allows AI tools to read this data. Report the refusal in clean words, with no host or site name, so that harvest records the source as skipped with the reason.

Without any of these routes, ask for a document: the person can search `type:pr author:@me` on GitHub and save the result list into `local-only/`, or paste it.

## Collect

`<start>` and `<last>` are the first and last day of the time window, as `YYYY-MM-DD`. GitHub search writes a date range as `<start>..<last>`.

```bash
# pull requests the person authored that were merged in the window
gh search prs "merged:<start>..<last>" --author=@me --limit 1000 \
  --json title,body,repository,labels,createdAt,closedAt,url

# pull requests the person reviewed
gh search prs "created:<start>..<last>" --reviewed-by=@me --limit 1000 \
  --json title,body,repository,labels,createdAt,closedAt,url

# issues the person created, and issues assigned to them
gh search issues "created:<start>..<last>" --author=@me --limit 1000 \
  --json title,body,repository,labels,createdAt,closedAt,state
gh search issues "created:<start>..<last>" --assignee=@me --limit 1000 \
  --json title,body,repository,labels,createdAt,closedAt,state
```

- Add `--owner=<organization>` to stay inside the employer's organization.
- The sources do not say how `gh search` picks a GitHub Enterprise host. On GitHub Enterprise, check that the results come from the employer's host. When they do not, ask the person which repositories they worked in and list each one with `gh pr list` as below, or use the document route.
- Use `--reviewed-by` for the person's review history. A requested reviewer drops out of `--review-requested` results once they have reviewed.
- GitHub's search documentation lists no qualifier for who approved a pull request: `review:approved` matches pull requests that a reviewer has approved. Count reviews only.
- `--limit` defaults to 30. GitHub's REST search API returns at most 1,000 results for each search, and the gh manual does not say whether `gh search` shares that cap. When a query returns 1,000 items, split the window into shorter ranges and run the query once per range.
- GitHub's REST search API allows a signed-in user 30 requests a minute. When `gh` reports a rate limit, wait a minute and run the query again.

`gh search prs` returns no merge date. When a theme needs exact merge dates, list the person's merged pull requests in that repository with `gh pr list`, which works on one repository at a time. On GitHub Enterprise, write the repository as `<host>/<owner>/<repo>`.

```bash
gh pr list --repo <owner>/<repo> --author "@me" --state merged --limit 1000 \
  --json title,mergedAt,url
```

This adapter only reads. Use connected GitHub tools only to read. For a raw API call, pass `--method GET` to `gh api` when you add `-f` fields. Without it, `gh` sends the fields in a POST.

Keep from each item: title, the first lines of the body, repository, labels, dates. Leave the diffs: they are code.

Done when every query has run over the whole window, in shorter ranges where one returned 1,000 items, or has failed and is reported with the themes. On the document route, done when the document is read or the person skips the source.

## Turn into themes

- Group by repository, then by topic within it (recurring words in titles and labels, bursts of related work).
- For each theme: what the work was, the period, pull requests authored and reviewed, outcomes visible in the bodies.
- Role signals: authoring most of a theme's pull requests suggests `built`, a share of them `contributed`, mostly reviewing `supported`. The searches return only the person's own pull requests, so the share is the person's to confirm; leading comes from the interview.

## Public or private

Work in public repositories on github.com that anyone can open without signing in is public (on GitHub Enterprise Server, a "public" repository is visible only inside the employer): name the project and keep the link, which a profile or a CV can show. Work in the employer's private repositories follows the confidentiality rules: no repository names, numbers or links.

## Sources

GitHub documentation, checked 2026-10-30. None of these pages shows a date.

- [gh search prs](https://cli.github.com/manual/gh_search_prs)
- [gh search issues](https://cli.github.com/manual/gh_search_issues)
- [gh pr list](https://cli.github.com/manual/gh_pr_list)
- [gh api](https://cli.github.com/manual/gh_api)
- [Searching issues and pull requests](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests)
- [Understanding the search syntax](https://docs.github.com/en/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax)
- [REST API endpoints for search](https://docs.github.com/en/rest/search/search), which names API version 2026-03-10
