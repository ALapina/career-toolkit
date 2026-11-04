# GitLab adapter

Merge requests the person authored, reviewed and approved, and issues they worked on, inside the harvest time window.

## Available when

- the `glab` CLI is logged in: `glab auth status` succeeds (for a self-managed GitLab, `glab auth status --hostname <host>`); or
- GitLab tools are connected to this session (an MCP server or connector for GitLab); or
- in full mode only, the person has a personal access token and exports it in their own shell as `GITLAB_TOKEN`. Ask for the `read_api` scope only: GitLab accepts it for read requests (GET and HEAD) on most endpoints, and every call in this adapter is a read. Use the token from the environment only: write `$GITLAB_TOKEN` in commands, never print its value, and never write it to a file.

A `401` response means the token is missing or invalid. A `403` response with `insufficient_scope` lists the scopes the call needs. Skip a call that needs more than `read_api`. When calls keep failing although the login or token is valid, ask whether the employer restricts API access. If it does, treat it as the employer's decision: use no other tool or token to get around it, and offer the [interview](../interview.md). Use the document route only when the person confirms that the employer allows AI tools to read this data. Report the refusal in clean words, with no host or site name, so that harvest records the source as skipped with the reason.

Without any of these routes, ask for a document: the person can filter the merge request list by author in the GitLab web interface and save the page as PDF into `local-only/`, or paste the list.

## Collect

Use `glab api`: it lists merge requests and issues across every project the person can see. `glab mr list` and `glab issue list` cover one project, or one group with `--group`. Both show only open items by default: `glab mr list` needs `--merged` or `--all` to include merged ones, and `glab issue list` needs `--all` to include closed ones.

`<start>` is the first day of the time window and `<end>` the day after its last day, both `YYYY-MM-DD`. The approvals query needs the person's username: `glab api user` returns it in the field `username`.

```bash
# merge requests the person authored that were merged
glab api --method GET merge_requests --paginate -f scope=created_by_me -f state=merged \
  -f created_after=<start>T00:00:00Z -f created_before=<end>T00:00:00Z -f per_page=100

# merge requests that list the person as a reviewer
glab api --method GET merge_requests --paginate -f scope=reviews_for_me \
  -f created_after=<start>T00:00:00Z -f created_before=<end>T00:00:00Z -f per_page=100

# merge requests the person approved
glab api --method GET merge_requests --paginate -f scope=all -f "approved_by_usernames[]=<username>" \
  -f created_after=<start>T00:00:00Z -f created_before=<end>T00:00:00Z -f per_page=100

# issues the person created, and issues assigned to them
glab api --method GET issues --paginate -f scope=created_by_me \
  -f created_after=<start>T00:00:00Z -f created_before=<end>T00:00:00Z -f per_page=100
glab api --method GET issues --paginate -f scope=assigned_to_me \
  -f created_after=<start>T00:00:00Z -f created_before=<end>T00:00:00Z -f per_page=100
```

- This adapter only reads. Keep `--method GET`: with `-f` fields and no method, `glab api` sends a POST. Use connected GitLab tools only to read.
- For a self-managed GitLab, add `--hostname <host>` to every call. Outside a Git directory, `glab api` talks to gitlab.com.
- The date filters take ISO 8601 date-times, as shown.
- A page holds at most 100 items, and `--paginate` fetches every page.
- Inference: the approvals query needs `scope=all` because, by default, the endpoint returns only merge requests the person created.
- `reviews_for_me` lists merge requests the person was asked to review, whether or not they did. Count approvals as reviews, each merge request once, and report the other reviewer assignments as review requests.
- For issues, use `created_by_me` and `assigned_to_me`: on GitLab.com, `scope=all` can return `400 Bad Request`. Inference: `assigned_to_me` matches only the current assignee, so issues later passed to someone else do not appear.

With `curl`, send the same parameters as a query string to `https://<gitlab-host>/api/v4/<endpoint>`, with the header `PRIVATE-TOKEN: $GITLAB_TOKEN`. Write the bracketed name as `approved_by_usernames%5B%5D`. Each response's `Link` header gives the next page as `rel="next"`; follow it until it is gone. Above 10,000 results, GitLab leaves out the total-count headers and the `rel="last"` link, so page by `rel="next"` only.

Take merge requests and issues from these lists for the whole window. Activity events (`GET /events`) reach back only 3 years, because GitLab removes older ones. The events API also returns no merge request events.

Keep from each item: title, the first lines of the description, labels, milestone, project ID, created and merged dates, state. Leave the diffs: they are code.

Done when every query has run over the whole window, or has failed and is reported with the themes. On the document route, done when the document is read or the person skips the source.

## Turn into themes

- Group by project, then by topic within a project: words that recur in titles and labels (migration, upgrade, performance, test, documentation), milestones, bursts of related work in the same weeks.
- For each theme: what the work was, the period, the number of merge requests authored and reviewed, and outcomes visible in descriptions (what changed, what got faster or simpler).
- Role signals: many merged merge requests in an area suggest `built` or `contributed`; the queries return only the person's own merge requests, so the person confirms which. Mostly reviewing in an area means `supported`; leading is rarely visible here, so ask about it in the interview.

## Leave out

Project and group paths, merge request and issue numbers, links, branch names, colleagues' usernames, and any title that names a client. Project names serve for grouping in the conversation only.

## Sources

GitLab documentation, checked 2026-10-30. None of these pages shows a date.

- [Merge requests API](https://docs.gitlab.com/api/merge_requests/), which mentions GitLab 19.0
- [Issues API](https://docs.gitlab.com/api/issues/)
- [REST API](https://docs.gitlab.com/api/rest/)
- [REST API authentication](https://docs.gitlab.com/api/rest/authentication/)
- [Events API](https://docs.gitlab.com/api/events/)
- [Contributions calendar](https://docs.gitlab.com/user/profile/contributions_calendar/)
- [glab api](https://docs.gitlab.com/cli/api/)
- [glab mr list](https://docs.gitlab.com/cli/mr/list/)
- [glab issue list](https://docs.gitlab.com/cli/issue/list/)
