# Contributing

This is a community guide, not an official Obsidian product. Read the catalog directly in either README; the website adds convenient browsing.

## Suggest or correct a resource

Provide the original URL, the Obsidian task it helps with, a concrete reason to include it, known limitations, and any relationship to the author. English and Chinese submissions are welcome. A source and a clear explanation are enough to start a discussion; you do not need to prepare JSON first.

Paid resources are welcome. Payment never buys inclusion or placement. Donations do not turn a free tool into a paid tool. Separate the tool's price from external model or service costs.

## Edit a record

1. Update `data/resources/<id>.json` and its sources. Use the enums in `data/catalog-contract.json`.
2. Edit `content/en/<id>.md` and `content/zh-cn/<id>.md`. Keep claims and limitations equivalent. If you cannot translate, mark the other locale stale and ask for translation review; do not pretend it is current.
3. Increment `revision` for substantive changes. Set each reviewed locale's `based_on_revision` and `content_sha256` to its actual content. A hash is not editorial approval.
4. Run `python3 scripts/catalog.py check` and `python3 scripts/catalog.py build`. Browse the generated pages before proposing the change.

The English and Chinese READMEs are independently readable catalogs, not website landing pages. Use a direct source link and one sentence explaining what each resource does. Include a paid label when needed and keep theme images available in Markdown. Longer guides are optional, not an entry requirement. The website is an optional browsing enhancement.

Shared metadata is stored once. Link related resources by ID and use same-locale Markdown links in prose. Edit README introductions outside the catalog markers; the marked sections are generated from the same metadata and prose as the site. Never edit generated files in `site/preview` or the generated sample catalogs directly.

## Sources

Describe the concrete purpose from primary documentation. Keep maintenance and verification records in metadata; do not render process notes or review statuses in reader-facing copy. Avoid unsupported superlatives.

Theme images need an original source, credit, rights information and descriptive alt text. Do not submit private vault screenshots. Summarize articles in your own words and link to the original.

The root MIT license remains unchanged during this design stage. The proposed future content/code license split is documented in the editorial policy and is not yet applied. Third-party assets retain their own notices. Licensing terms must be clarified before opening the production contribution workflow.

See [design and review documents](docs/README.md) for the current scope and acceptance boundaries.

## Navigation

Add each resource to exactly one primary group in `data/navigation.json`. Use task routes for cross-category discovery without duplicating entries. Keep group labels and route descriptions bilingual. Add Chinese-language resources based on their concrete use, not the author’s nationality. Distinguish a reusable vault, note templates and a published website in the one-line description.

## Release build

Run `python3 scripts/catalog.py check --release`, the test suite and `python3 scripts/catalog.py build --release`. The static output is `site/dist`; commit generated README and catalog changes with the source changes. Python 3.10+ is required. The GitHub workflow checks the same commands without deploying.
