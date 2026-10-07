# Contributing

This is a community guide, not an official Obsidian product. Read the catalog directly in either README; the website adds convenient browsing.

## Suggest or correct a resource

Provide the original URL, the Obsidian task it helps with, a concrete reason to include it, known limitations, and any relationship to the author. English and Chinese submissions are welcome. A source and a clear explanation are enough to start a discussion; you do not need to prepare JSON first.

Paid resources are welcome. Payment never buys inclusion or placement. Donations do not turn a free tool into a paid tool. Separate the tool's price from external model or service costs.

## Community workflow / 社区贡献流程

1. Search the catalog and open/closed issues for the same resource or problem. Add useful evidence to an existing discussion when appropriate.
2. Choose [suggest a resource](https://github.com/mansucache/awesome-obsidian/issues/new?template=resource.yml), [correct an entry](https://github.com/mansucache/awesome-obsidian/issues/new?template=correction.yml), or [catalog feedback](https://github.com/mansucache/awesome-obsidian/issues/new?template=feedback.yml). A PR is also welcome without a preceding issue.
3. Maintainers check scope, duplication, primary sources, costs and material limitations. Missing information can be clarified in the discussion; submission does not guarantee inclusion.
4. Before merging, maintainers ensure applicable checks, generated files and affected English/Chinese content are ready. Accepted changes are linked back to the discussion; declined or deferred suggestions receive a brief reason.

先搜索目录及已有 Issue，再选择推荐资源、修正条目或目录反馈，也可以直接提交 PR。维护者核验收录范围、重复项、原始来源、费用和重要限制，必要时补问；收录后提供对应修改链接，暂缓或不收录时简要说明原因。

English or Chinese alone is enough to start an issue or PR. Resource suggestions need a name, original link, use case/reason and relationship disclosure, not JSON or technical checks. Known costs and limitations help; unknown facts may remain unknown until review. Self-recommendations are welcome and follow the same criteria.

Issue 或 PR 中英文任选一种即可。推荐资源只需名称、原始链接、用途与推荐理由、关联关系；不要求提交者准备 JSON、双语内容或运行技术检查。欢迎自荐，适用相同收录标准。维护者在合并前补齐所需翻译和核验。

Use catalog feedback for missing categories, navigation, README or website display problems. Report a plugin's own malfunction to its upstream project; an inaccurate catalog claim still belongs here. Share only public or redacted examples.

分类缺口、导航和显示问题使用目录反馈；插件自身故障到上游反馈，目录介绍有误则仍在这里修正。只提供公开或已脱敏的示例。

## PR scope and checks / PR 范围与检查

Keep changes focused. Apply only relevant template checks: a text typo does not require image-license or resource-cost review. Report actual checks and any missing work honestly; unchecked work is a review task, not a reason to claim success. Maintainers complete the applicable checks before merging. Catalog data changes use the checks below; code changes also need relevant tests. Existing CI remains the merge validation baseline.

让每个 PR 聚焦一个明确问题，按修改类型填写检查项；修正错字无需填写图片许可或费用核验。未完成翻译或未运行检查时直接说明，由维护者在合并前补齐。目录数据变更运行下方目录检查，代码变更补充相关测试；现有 CI 继续承担合并前验证。

## Edit a record

1. Update the resource record, its primary sources and affected English/Chinese prose. The contract is in `data/catalog-contract.json`.
2. Write enough for a reader to choose: purpose, a concrete use case and any material constraint. Use an optional short context paragraph; longer usage notes are useful when they add a starting point or a meaningful comparison. Keep essential conditions in the README, not only on the website.
3. After actually reviewing both locales, run `python3 scripts/review_record.py <id> --bump --reviewed en zh-cn`. This updates revision and hashes; it does not verify claims or update source-check dates.
4. If only one locale is ready, review that locale and keep the record as `draft`. Run `python3 scripts/catalog.py check --draft`. After reviewing the other locale without another revision bump, explicitly set publication to `listed`. Drafts are suitable for discussion but cannot pass release checks.
5. Run the applicable checks below and inspect affected generated Markdown and site pages. If you cannot run them, note that in the PR; maintainers complete them before merging.

English and Chinese READMEs are independently readable catalogs. Names link to the original resource; local original templates and workflows link to their Markdown pages. Theme previews remain available in Markdown. See the [writing policy](docs/editorial-policy.zh-cn.md) for type-specific guidance.

Shared metadata is stored once. Link related resources by ID and use same-locale Markdown links in prose. Edit README introductions outside the catalog markers; the marked sections are generated from the same metadata and prose as the site. Never edit generated files in `site/preview` or the generated sample catalogs directly.

## Sources

Describe the concrete purpose from primary documentation. Keep maintenance and verification records in metadata; do not render process notes or review statuses in reader-facing copy. Avoid unsupported superlatives.

Theme images need an original source, credit, rights information and descriptive alt text. Do not submit private vault screenshots. Summarize articles in your own words and link to the original.

Original content and code use the root MIT license. Third-party assets retain their own notices. Open-source labels require a recorded license and a traceable upstream source.

See [design and review documents](docs/README.md) for the current scope and acceptance boundaries.

## Navigation

Add each resource to exactly one primary group in `data/navigation.json`. Use task routes for cross-category discovery without duplicating entries. Keep group labels and route descriptions bilingual. Add Chinese-language resources based on their concrete use, not the author’s nationality. Distinguish a reusable vault, note templates and a published website in the one-line description.

## Release build

Run `python3 scripts/catalog.py check --release`, `python3 -m unittest discover -s scripts -p 'test_*.py'` and `python3 scripts/catalog.py build --release`. The static output is `site/dist`; commit generated README and catalog changes with the source changes. Python 3.10+ is required. The GitHub workflow checks the same commands without deploying.

## Maintenance and retirement

Use `python3 scripts/catalog.py report` for the editorial queue. Weekly link checks run independently from PR checks and write review signals to the Actions summary. A timeout, rate limit or quiet commit history does not automatically remove an entry.

A `needs-review` entry stays discoverable while it is investigated. Confirmed `archived` or `unavailable` entries require a dated, bilingual reason under `maintenance`; they leave normal discovery but retain historical README and detail links. Recovery requires new evidence and another review. See the [maintenance guide](docs/maintenance.zh-cn.md).

Release checks enforce integrity and translation readiness, not minimum catalog counts. Remove obsolete resources when appropriate; do not add filler to replace them.
