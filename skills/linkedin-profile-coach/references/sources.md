# Source policy

Which sources may back a rule in [best practices](best-practices.md) and its area files in `best-practices/`. The [refresh procedure](refresh-reference.md) searches only here.

## Tier 1: LinkedIn's own material

The only authority on how LinkedIn works and what it allows.

- LinkedIn Help Center, Recruiter Help included: `linkedin.com/help/`
- LinkedIn legal pages (User Agreement, Privacy Policy, Professional Community Policies): `linkedin.com/legal/`
- LinkedIn's business sites and blogs, such as Talent Solutions, the Talent Blog and Sales Solutions: `business.linkedin.com/`, `linkedin.com/business/`
- LinkedIn's API documentation on Microsoft Learn: `learn.microsoft.com/en-us/linkedin/`
- LinkedIn's economic research, formerly the Economic Graph: `economicgraph.linkedin.com`, which redirected to `pulse.linkedin.com` on 2026-10-30
- LinkedIn's newsroom and official blogs: `news.linkedin.com`, `linkedin.com/blog/`
- LinkedIn Engineering blog, where it explains search, ranking or how recruiting tools read profiles: `linkedin.com/blog/engineering/`
- Articles on `linkedin.com/pulse/` only when the page names a LinkedIn account, such as LinkedIn News, as the publisher

For tool and file-format facts (Claude Code, claude.ai, GitLab, GitHub, Jira, Confluence, Leapsome, Lattice, Culture Amp), tier 1 is the vendor's own documentation, including the README of a repository the vendor publishes itself, such as `github.com/atlassian/atlassian-mcp-server`.

## Tier 2: research with a stated method

Studies of hiring and job search, such as how recruiters and hiring managers read profiles and resumes or how employers respond to applicants, that publish who was studied, how many, and how it was measured: peer-reviewed papers, working papers from research institutes, field experiments, eye-tracking studies, surveys with a published sample. A study qualifies only when its method can be found.

Research by a vendor, such as a recruiting platform, an interview-practice service or a career service, is tier 2 only when it states its method and its sample. A vendor's marketing posts never count, whatever figures they quote.

The refresh searches for tier 2 studies only on these domains: `nber.org`, `aeaweb.org`, `iza.org`, `academic.oup.com`, `link.springer.com`, `sciencedirect.com`, `journals.sagepub.com`, `onlinelibrary.wiley.com`, `tandfonline.com`, `nature.com`, `papers.ssrn.com`, and the sites of universities and public research institutes. A vendor's study counts only from the vendor's own research page.

## Age of a source

- A figure that states no method, such as a share LinkedIn reports from its own data, backs a rule for five years from the date of the page that reports it. After that, the refresh proposes removing it.
- A figure from a source that states its method can be older. The rule gives its year.
- Advice and facts from an older page can still back a rule. The Source line shows the page's date, the rule names the year of old advice, and the refresh checks the oldest pages first.

## Not accepted

Posts that individuals publish themselves, such as influencer posts and articles on `linkedin.com/pulse/` under the author's own name, even when the author works at LinkedIn; "N tips" lists from anyone but LinkedIn itself; career-coach and SEO blogs; vendor marketing; and anything that cannot be traced to its origin. A rule that only such sources support stays out of the reference.

## How a rule is recorded

The index, [best practices](best-practices.md), says how a rule is written and holds the date of the last full check. Each rule's Source line gives the title, publisher and URL, the source's own date and its tier. A rule needs at least one tier 1 or tier 2 source, and "Inference:" marks reasoning beyond what its sources say. A choice that no such source supports is either one of this skill's own conventions (area `style-`, in the index) or left out.
