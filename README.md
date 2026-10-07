![Awesome Obsidian — Plugins, Themes, AI and Workflows](assets/banners/awesome-obsidian.png)

# Awesome Obsidian

A community guide to Obsidian resources, use cases and workflows. Read this catalog directly on GitHub or in a Markdown reader; the website adds search, filters and easier browsing.

[简体中文](README.zh-CN.md) · [Contributing](CONTRIBUTING.md)


<!-- catalog:start -->
232 entries · 15 illustrated themes · 7 workflow guides

## Start with a task

| I want to… | Start here |
| --- | --- |
| Start using Obsidian | [Obsidian Help](#resource-obsidian-help) · [kepano’s Obsidian vault](#resource-kepano-vault) |
| Collect reading notes | [Obsidian Web Clipper](#resource-web-clipper) · [From a saved article to a usable note](#resource-reading-workflow) |
| Research a topic | [From a question to a sourced answer](#resource-research-workflow) · [Zotero Integration](#resource-zotero-integration) · [Dataview](#resource-dataview) · [Dataview Example Vault](#resource-dataview-example-vault) |
| Plan projects | [From a project goal to next actions](#resource-projects-workflow) · [Tasks](#resource-tasks) · [Kanban](#resource-kanban) · [LifeOS](#resource-lifeos) |
| Write and find Chinese notes | [Easy Typing](#resource-easy-typing) · [Fuzzy Chinese Pinyin](#resource-fuzzy-chinese) · [PKMer](#resource-pkmer) |
| Use AI with your notes | [Use AI with a focused set of notes](#resource-ai-workflow) · [Local GPT](#resource-local-gpt) · [LLM Workspace](#resource-llm-workspace) · [Obsidian Skills](#resource-obsidian-skills) |
| Publish a knowledge garden | [Obsidian Publish](#resource-obsidian-publish) · [Quartz](#resource-quartz) · [Digital Garden](#resource-digital-garden) |
| Customize the look | [Minimal](#resource-minimal) · [Things](#resource-things) · [Modular CSS Layout](#resource-modular-css) |
| Finish a draft | [From linked notes to a finished draft](#resource-writing-workflow) |
| Learn and review | [From course notes to usable knowledge](#resource-learning-workflow) |
| Sync, back up and recover | [From device sync to recoverable backups](#resource-sync-backup-workflow) · [Sync your notes across devices](#resource-sync-methods-guide) · [Back up your Obsidian files](#resource-backup-guide) · [Obsidian Sync](#resource-obsidian-sync) · [Obsidian Git](#resource-obsidian-git) |

## Contents

- [Official & core](#category-official) · 22
- [Plugins](#category-plugins) · 75
- [Themes & appearance](#category-appearance) · 21
- [Templates & vaults](#category-templates) · 18
- [AI & automation](#category-ai) · 32
- [Tools & integrations](#category-integrations) · 22
- [Workflows](#category-workflows) · 7
- [Methods](#category-methods) · 10
- [Learning & community](#category-learning) · 12
- [Development](#category-development) · 13

<a id="category-official"></a>

## Official & core

[Start here](#topic-official-start) · [Core features & services](#topic-official-core) · [Links & discovery](#topic-official-linking) · [Writing & structure](#topic-official-writing) · [Workspace & app links](#topic-official-workspace)

<a id="topic-official-start"></a>

### Start here

- <a id="resource-obsidian-home"></a>[Obsidian](https://obsidian.md/) — Download Obsidian and explore its local Markdown notes, links and extensions.
- <a id="resource-obsidian-help"></a>[Obsidian Help](https://obsidian.md/help/) — Look up setup instructions, core features and everyday operations in the official help.
- <a id="resource-obsidian-community"></a>[Obsidian Community](https://community.obsidian.md/) — Browse the official directory of community plugins and themes.

<a id="topic-official-core"></a>

### Core features & services

- <a id="resource-obsidian-bases"></a>[Bases](https://obsidian.md/help/bases) — Create database-style views of notes with property filters, sorting and formulas.
- <a id="resource-obsidian-canvas"></a>[Canvas](https://obsidian.md/canvas) — Arrange notes, images and web pages on an infinite canvas for visual thinking.
- <a id="resource-obsidian-cli"></a>[Obsidian CLI](https://obsidian.md/cli) — Control Obsidian from the terminal to read, create and search notes in scripts.
- <a id="resource-obsidian-sync"></a>[Obsidian Sync](https://obsidian.md/sync) — Sync vaults across devices with the official service, selective syncing and version history. · Paid
  Useful when you want less sync configuration; file changes propagate, so keep a separate backup.
  Requires a subscription; storage and history retention depend on the plan.
- <a id="resource-obsidian-publish"></a>[Obsidian Publish](https://obsidian.md/publish) — Publish selected notes as an online knowledge base, wiki or digital garden. · Paid
  Useful for publishing selected notes directly; check whether their attachments and links are suitable for public access.

<a id="topic-official-linking"></a>

### Links & discovery

- <a id="resource-obsidian-backlinks"></a>[Backlinks](https://help.obsidian.md/Plugins/Backlinks) — Find notes that link to the current note and mentions that could become links.
- <a id="resource-obsidian-search"></a>[Search](https://help.obsidian.md/Plugins/Search) — Combine text, path, tag and property searches to find notes.
- <a id="resource-obsidian-graph-view"></a>[Graph View](https://help.obsidian.md/Plugins/Graph+view) — Explore connections across the vault or around a single note.
- <a id="resource-obsidian-internal-links"></a>[Internal Links](https://help.obsidian.md/Linking+notes+and+files/Internal+links) — Link to notes, headings and blocks to connect ideas precisely.
- <a id="resource-obsidian-embed-files"></a>[Embed Files](https://help.obsidian.md/Linking+notes+and+files/Embed+files) — Show notes, images and other attachments inside a note.

<a id="topic-official-writing"></a>

### Writing & structure

- <a id="resource-obsidian-properties"></a>[Properties](https://help.obsidian.md/Editing+and+formatting/Properties) — Store status, dates, numbers and links as structured note data for consistent filtering.
  Useful for queryable project, book or source collections; a property name shares one type throughout a vault, so choose names consistently.
- <a id="resource-obsidian-templates"></a>[Templates](https://help.obsidian.md/Plugins/Templates) — Insert a reusable note structure into the current file, with title, date and time variables.
  A starting point for meeting, reading and review formats without adding a scripted template plugin.
- <a id="resource-obsidian-daily-notes"></a>[Daily Notes](https://help.obsidian.md/Plugins/Daily+notes) — Create dated notes for daily logs, capture and reflection.
- <a id="resource-obsidian-note-composer"></a>[Note Composer](https://help.obsidian.md/Plugins/Note+composer) — Extract selected text into another note or merge notes together.
- <a id="resource-obsidian-callouts"></a>[Callouts](https://help.obsidian.md/Editing+and+formatting/Callouts) — Use labeled blocks to distinguish examples, questions and summaries.
- <a id="resource-obsidian-markdown-syntax"></a>[Markdown Syntax](https://help.obsidian.md/Editing+and+formatting/Basic+formatting+syntax) — Learn the headings, lists, tables and formatting supported in notes.

<a id="topic-official-workspace"></a>

### Workspace & app links

- <a id="resource-obsidian-bookmarks"></a>[Bookmarks](https://help.obsidian.md/Plugins/Bookmarks) — Keep frequently used notes, searches and headings within reach.
- <a id="resource-obsidian-workspaces"></a>[Workspaces](https://help.obsidian.md/Plugins/Workspaces) — Save and restore layouts for different kinds of work.
- <a id="resource-obsidian-uri"></a>[Obsidian URI](https://help.obsidian.md/Extending+Obsidian/Obsidian+URI) — Open or create notes through links from other applications.


<a id="category-plugins"></a>

## Plugins

Grouped by primary purpose; see also [AI & automation](#category-ai) and [Tools & integrations](#category-integrations) for other plugins.

[Capture & templates](#topic-plugins-capture) · [Tasks & daily planning](#topic-plugins-tasks) · [Search & navigation](#topic-plugins-search) · [Writing & formatting](#topic-plugins-editing) · [Queries & visual thinking](#topic-plugins-visual) · [Research & review](#topic-plugins-study) · [Tables & properties](#topic-plugins-tables) · [Long writing & language](#topic-plugins-writing) · [Links & organization](#topic-plugins-knowledge) · [Images, audio & attachments](#topic-plugins-media) · [Vault maintenance](#topic-plugins-maintenance) · [Workspace & controls](#topic-plugins-interface)

<a id="topic-plugins-capture"></a>

### Capture & templates

- <a id="resource-quickadd"></a>[QuickAdd](https://github.com/chhoumann/quickadd) — Create template notes, append captured text or combine actions into macros from a shortcut.
  Useful for repeated capture, such as sending ideas to an inbox; configure the destination before adding automation.
  [Usage & choosing](content/en/quickadd.md)
- <a id="resource-templater"></a>[Templater](https://github.com/SilentVoid13/Templater) — Combine dates, prompts and scripts in templates to create meeting, daily or project notes.
  Use it when fixed text templates are insufficient; the core Templates plugin may suffice for titles and dates.
  [Usage & choosing](content/en/templater.md)
- <a id="resource-natural-language-dates"></a>[Natural Language Dates](https://github.com/argenos/nldates-obsidian) — Turn natural-language date expressions into dates and links to daily notes.
- <a id="resource-obsidian-auto-link-title"></a>[Auto Link Title](https://github.com/zolrath/obsidian-auto-link-title) — Fetch a pasted web address’s title to create a readable link.

<a id="topic-plugins-tasks"></a>

### Tasks & daily planning

- <a id="resource-tasks"></a>[Tasks](https://github.com/obsidian-tasks-group/obsidian-tasks) — Query tasks across notes, organize them by dates and conditions, and update completion from an aggregated view.
  Useful when tasks live in meeting, project and daily notes; agree on date and capture conventions first.
  [Usage & choosing](content/en/tasks.md)
- <a id="resource-kanban"></a>[Kanban](https://github.com/community-archive/obsidian-kanban) — Organize tasks on boards stored as Markdown notes.
  Useful for stage-based work such as to-do, doing and done; pair with Tasks for due-date queries across notes.
- <a id="resource-calendar"></a>[Calendar](https://github.com/liamcain/obsidian-calendar-plugin) — Open and create daily notes from a calendar in the sidebar.
- <a id="resource-periodic-notes"></a>[Periodic Notes](https://github.com/liamcain/obsidian-periodic-notes) — Create daily, weekly and monthly notes with separate templates and folders.
- <a id="resource-obsidian-day-planner"></a>[Day Planner](https://github.com/ivan-lednev/obsidian-day-planner) — Schedule tasks as time blocks on an editable timeline and track time spent.
- <a id="resource-obsidian-full-calendar"></a>[Full Calendar](https://github.com/obsidian-community/obsidian-full-calendar) — Manage events in calendar views with each local event stored as a note.
- <a id="resource-obsidian-reminder-plugin"></a>[Reminder](https://github.com/uphy/obsidian-reminder) — Add date-and-time reminders to Markdown task items.
- <a id="resource-pomodoro-timer"></a>[Pomodoro Timer](https://github.com/eatgrass/obsidian-pomodoro-timer) — Run adjustable work and break intervals to structure focused sessions.
- <a id="resource-obsidian-checklist-plugin"></a>[Checklist](https://github.com/delashum/obsidian-checklist-plugin) — Collect checklists from multiple notes into a single sidebar.

<a id="topic-plugins-search"></a>

### Search & navigation

- <a id="resource-omnisearch"></a>[Omnisearch](https://github.com/scambier/obsidian-omnisearch) — Find notes with relevance-ranked search and optional PDF and image text indexing.
- <a id="resource-fuzzy-chinese"></a>[Fuzzy Chinese Pinyin](https://github.com/lazyloong/obsidian-fuzzy-chinese) — Find Chinese notes, headings and commands using pinyin or initials.
- <a id="resource-quiet-outline"></a>[Quiet Outline](https://github.com/guopenghui/obsidian-quiet-outline) — Search headings and control outline expansion to navigate long notes.
- <a id="resource-homepage"></a>[Homepage](https://github.com/mirnovov/obsidian-homepage) — Open a chosen note, canvas, base or workspace when the vault starts.
- <a id="resource-file-tree-alternative"></a>[File Tree Alternative](https://github.com/ozntel/file-tree-alternative) — Browse folders and files in separate panes instead of one file tree.
- <a id="resource-notebook-navigator"></a>[Notebook Navigator](https://github.com/johansan/notebook-navigator) — Browse notes with a two-pane file navigator, previews and a calendar.
- <a id="resource-darlal-switcher-plus"></a>[Quick Switcher++](https://github.com/darlal/obsidian-switcher-plus) — Find open tabs, headings and other symbols through an extended quick switcher.
- <a id="resource-obsidian-another-quick-switcher"></a>[Another Quick Switcher](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher) — Use configurable search commands to switch between notes and headings.
- <a id="resource-recent-files-obsidian"></a>[Recent Files](https://github.com/tgrosinger/recent-files-obsidian) — Reopen recently viewed notes from a sidebar list.

<a id="topic-plugins-editing"></a>

### Writing & formatting

- <a id="resource-easy-typing"></a>[Easy Typing](https://github.com/Yaozhuwa/easy-typing-obsidian) — Format mixed Chinese and English text with automatic spacing, punctuation and paired symbols.
- <a id="resource-linter"></a>[Linter](https://github.com/platers/obsidian-linter) — Apply configurable formatting rules to Markdown text and note properties.
- <a id="resource-outliner"></a>[Outliner](https://github.com/vslinko/obsidian-outliner) — Edit nested lists with outliner-style movement, indentation and folding.
- <a id="resource-any-block"></a>[AnyBlock](https://github.com/any-block/any-block) — Render lists and other Markdown blocks as tables, cards and alternative views.
- <a id="resource-editing-toolbar"></a>[Editing Toolbar](https://github.com/pkm-er/obsidian-editing-toolbar) — Apply formatting and custom editing commands from a configurable toolbar.
- <a id="resource-various-complements"></a>[Various Complements](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin) — Complete words and links from your notes as you type.
- <a id="resource-url-into-selection"></a>[Paste URL into selection](https://github.com/denolehov/obsidian-url-into-selection) — Turn selected text into a Markdown link by pasting a URL over it.
- <a id="resource-obsidian-footnotes"></a>[Footnote Shortcut](https://github.com/michabrugger/obsidian-footnotes) — Create, navigate and edit footnotes with keyboard commands.
- <a id="resource-lapel"></a>[Lapel](https://github.com/liamcain/obsidian-lapel) — Show heading levels in the editor gutter to inspect document structure.
- <a id="resource-obsidian-admonition"></a>[Admonition](https://github.com/ebullient/obsidian-admonition) — Create styled information blocks with configurable icons and appearance.
- <a id="resource-callout-manager"></a>[Callout Manager](https://github.com/eth-p/obsidian-callout-manager) — Browse, create and customize callout styles from one settings interface.
- <a id="resource-number-headings-obsidian"></a>[Number Headings](https://github.com/onlyafly/number-headings-obsidian) — Add or update hierarchical numbering across document headings.
- <a id="resource-obsidian-plugin-toc"></a>[Table of Contents](https://github.com/hipstersmoothie/obsidian-plugin-toc) — Generate a linked table of contents from the headings in a note.
- <a id="resource-obsidian-smart-typography"></a>[Smart Typography](https://github.com/mgmeyers/obsidian-smart-typography) — Convert typed quotes, dashes and dots into typographic punctuation.

<a id="topic-plugins-visual"></a>

### Queries & visual thinking

- <a id="resource-dataview"></a>[Dataview](https://github.com/blacksmithgu/obsidian-dataview) — Turn properties across notes into live lists and tables, such as reading queues, project indexes and research catalogs.
  Useful when you maintain consistent fields and want less manual aggregation; queries use indexed data, not semantic search over all prose.
  [Usage & choosing](content/en/dataview.md)
- <a id="resource-excalidraw"></a>[Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin) — Draw diagrams and visual notes with Excalidraw inside your vault.
  Useful for concept sketches, meeting whiteboards and visual notes; compare core Canvas when you only need to arrange existing notes.
- <a id="resource-excalibrain"></a>[ExcaliBrain](https://github.com/zsviczian/excalibrain) — Navigate note relationships through an interactive graph built with Excalidraw.
- <a id="resource-obsidian-tracker"></a>[Tracker](https://github.com/pyrochlore/obsidian-tracker) — Collect values from notes and plot habits, progress or other personal metrics.
- <a id="resource-obsidian-charts"></a>[Charts](https://github.com/phibr0/obsidian-charts) — Render interactive charts from data written in your notes.
- <a id="resource-heatmap-calendar"></a>[Heatmap Calendar](https://github.com/richardsl/heatmap-calendar-obsidian) — Display daily activity as a year-long heatmap using DataviewJS data.

<a id="topic-plugins-study"></a>

### Research & review

- <a id="resource-zotero-integration"></a>[Zotero Integration](https://github.com/community-archive/obsidian-zotero-integration) — Import Zotero citations, bibliographies and PDF annotations into research notes.
- <a id="resource-spaced-repetition"></a>[Spaced Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) — Review flashcards and notes on a spaced-repetition schedule inside Obsidian.
- <a id="resource-pdf-plus"></a>[PDF++](https://github.com/ryotaushio/obsidian-pdf-plus) — Annotate PDFs and link notes to passages or regions inside a document.
- <a id="resource-obsidian-annotator"></a>[Annotator](https://github.com/elias-sundqvist/obsidian-annotator) — Read and annotate PDF and EPUB documents inside Obsidian.
- <a id="resource-zotlit"></a>[ZotLit](https://github.com/aidenlx/zotlit) — Create literature notes and bring citations and annotations from Zotero into the vault.
- <a id="resource-obsidian-citation-plugin"></a>[Citations](https://github.com/hans/obsidian-citation-plugin) — Search BibTeX or CSL-JSON bibliographies and insert citations into notes.
- <a id="resource-obsidian-book-search-plugin"></a>[Book Search](https://github.com/anpigon/obsidian-book-search-plugin) — Create book notes from title, author or ISBN searches and fetched metadata.
- <a id="resource-flashcards-obsidian"></a>[Flashcards](https://github.com/reuseman/flashcards-obsidian) — Turn note content into Anki flashcards through Anki integration.

<a id="topic-plugins-tables"></a>

### Tables & properties

- <a id="resource-table-editor-obsidian"></a>[Advanced Tables](https://github.com/tgrosinger/advanced-tables-obsidian) — Move between Markdown table cells and align rows while editing.
- <a id="resource-metadata-menu"></a>[Metadata Menu](https://github.com/mdelobelle/metadatamenu) — Edit note metadata through field controls and reusable field definitions.
- <a id="resource-obsidian-meta-bind-plugin"></a>[Meta Bind](https://github.com/mprojectscode/obsidian-meta-bind-plugin) — Add property inputs, calculated displays and clickable buttons inside notes.

<a id="topic-plugins-writing"></a>

### Long writing & language

- <a id="resource-better-word-count"></a>[Better Word Count](https://github.com/lukeleppan/better-word-count) — Count words in selected text while editing a draft.
- <a id="resource-languagetool"></a>[LanguageTool](https://github.com/wrenger/obsidian-languagetool) — Check spelling and grammar through a LanguageTool server or service. · Optional payment
- <a id="resource-longform"></a>[Longform](https://github.com/kevboh/longform) — Arrange scene notes into a manuscript and compile long writing projects.
- <a id="resource-obsidian-word-sprint"></a>[Word Sprint](https://github.com/kinabalu/obsidian-word-sprint) — Run timed writing sprints and track words produced during each session.
- <a id="resource-writing-goals"></a>[Writing Goals](https://github.com/lynchjames/obsidian-writing-goals) — Set writing targets for individual notes or folders and track progress.

<a id="topic-plugins-knowledge"></a>

### Links & organization

- <a id="resource-tag-wrangler"></a>[Tag Wrangler](https://github.com/pjeby/tag-wrangler) — Rename or merge tags across notes from the tag pane.
- <a id="resource-folder-note-plugin"></a>[Folder Note](https://github.com/xpgo/obsidian-folder-note-plugin) — Attach an overview note to a folder and show its contents as cards.
- <a id="resource-waypoint"></a>[Waypoint](https://github.com/idreesinc/Waypoint) — Maintain folder-based maps of content that update as files change.
- <a id="resource-breadcrumbs"></a>[Breadcrumbs](https://github.com/michaelpporter/breadcrumbs) — Navigate typed relationships such as parent, child, next and previous notes.
- <a id="resource-note-refactor-obsidian"></a>[Note Refactor](https://github.com/lynchjames/note-refactor-obsidian) — Extract selected content into a new note or split a long note into smaller ones.

<a id="topic-plugins-media"></a>

### Images, audio & attachments

- <a id="resource-image-converter"></a>[Image Converter](https://github.com/xryul/obsidian-image-converter) — Convert, resize and compress images inside your vault.
- <a id="resource-obsidian-image-toolkit"></a>[Image Toolkit](https://github.com/obsidian-community/obsidian-image-toolkit) — Open images in a viewer with zoom, rotation and other viewing controls.
- <a id="resource-image-captions"></a>[Image Captions](https://github.com/alangrainger/obsidian-image-captions) — Display Markdown-compatible captions beneath embedded images.
- <a id="resource-attachment-management"></a>[Attachment Management](https://github.com/trganda/obsidian-attachment-management) — Organize attachment locations and filenames using configurable variables.
- <a id="resource-media-extended"></a>[Media Extended](https://github.com/aidenlx/media-extended) — Take timestamped notes while playing audio and video inside Obsidian.

<a id="topic-plugins-maintenance"></a>

### Vault maintenance

- <a id="resource-oz-clear-unused-images"></a>[Clear Unused Images](https://github.com/ozntel/oz-clear-unused-images-obsidian) — Find and remove images no longer referenced by Markdown notes.
- <a id="resource-auto-note-mover"></a>[Auto Note Mover](https://github.com/farux/obsidian-auto-note-mover) — Move notes to folders according to rules based on tags or titles.
- <a id="resource-obsidian-file-cleaner"></a>[File Cleaner](https://github.com/johnsonhong997/obsidian-file-cleaner) — Locate empty notes and unused attachments for vault cleanup.

<a id="topic-plugins-interface"></a>

### Workspace & controls

- <a id="resource-cmdr"></a>[Commander](https://github.com/jsmorabito/obsidian-commander) — Place frequently used commands in toolbars, menus and other interface locations.
- <a id="resource-obsidian-hover-editor"></a>[Hover Editor](https://github.com/nothingislost/obsidian-hover-editor) — Edit linked notes in floating preview windows without leaving the current note.
- <a id="resource-pane-relief"></a>[Pane Relief](https://github.com/pjeby/pane-relief) — Navigate tab history and move between panes using keyboard shortcuts.
- <a id="resource-iconic"></a>[Iconic](https://github.com/gfxholo/iconic) — Choose icons and colors for files, tags, tabs and other interface elements.


<a id="category-appearance"></a>

## Themes & appearance

[Theme gallery](#topic-appearance-themes) · [CSS snippets & layouts](#topic-appearance-css)

<a id="topic-appearance-themes"></a>

### Theme gallery

- <a id="resource-anuppuccin"></a>[AnuPpuccin](https://github.com/AnubisNekhet/AnuPpuccin) — Customize palettes, layouts and colorful folders through Style Settings.

![AnuPpuccin theme](assets/themes/anuppuccin/preview.webp)

- <a id="resource-blue-topaz"></a>[Blue Topaz](https://github.com/PKM-er/Blue-Topaz_Obsidian-css) — A blue-accented theme with configurable layouts and visual styles.

![Blue Topaz theme](assets/themes/blue-topaz/preview.png)

- <a id="resource-catppuccin"></a>[Catppuccin](https://github.com/catppuccin/obsidian) — A pastel theme with one light and three dark color palettes.

![Catppuccin theme](assets/themes/catppuccin/preview.png)

- <a id="resource-dracula"></a>[Dracula](https://github.com/dracula/obsidian) — A dark theme with the Dracula palette and contrasting syntax colors.

![Dracula theme](assets/themes/dracula/preview.png)

- <a id="resource-its-theme"></a>[ITS Theme](https://github.com/SlRvb/Obsidian--ITS-Theme) — A customizable theme with light and dark modes and detailed reading styles.

![ITS Theme theme](assets/themes/its-theme/preview.png)

- <a id="resource-minimal"></a>[Minimal](https://github.com/kepano/obsidian-minimal) — A restrained reading and writing interface with configurable colors, typography and layouts.
  Useful for a quiet interface with room for customization; begin with defaults before adjusting companion settings.

![Minimal theme](assets/themes/minimal/preview.png)

- <a id="resource-primary"></a>[Primary](https://github.com/primary-theme/obsidian) — A warm, playful theme with light and dark modes and carefully styled interface details.

![Primary theme](assets/themes/primary/preview.png)

- <a id="resource-things"></a>[Things](https://github.com/colineckert/obsidian-things) — A Things-inspired theme with light and dark modes and custom checkbox styles.

![Things theme](assets/themes/things/preview.png)

- <a id="resource-everforest"></a>[Everforest](https://github.com/0xglitchbyte/obsidian_everforest) — Use a forest-inspired palette with muted greens.

![Everforest theme](assets/themes/everforest/preview.png)

- <a id="resource-shimmering-focus"></a>[Shimmering Focus](https://github.com/chrisgrieser/shimmering-focus) — Reduce interface chrome to focus on reading and writing.

![Shimmering Focus theme](assets/themes/shimmering-focus/preview.webp)

- <a id="resource-prism"></a>[Prism](https://github.com/damiankorcz/Prism-Theme) — Customize light and dark layouts with multiple color schemes.

![Prism theme](assets/themes/prism/preview.png)

- <a id="resource-border"></a>[Border](https://github.com/akifyss/obsidian-border) — Separate workspace panels with clear boundaries and adjustable styling.

![Border theme](assets/themes/border/preview.png)

- <a id="resource-maple"></a>[Maple](https://github.com/subframe7536/obsidian-theme-maple) — Combine restrained colors with readable note typography.

![Maple theme](assets/themes/maple/preview.png)

- <a id="resource-vanilla-amoled"></a>[Vanilla AMOLED](https://github.com/sakuraisayeki/vanilla-amoled-theme) — Use a black-background variation of the default interface.

![Vanilla AMOLED theme](assets/themes/vanilla-amoled/preview.png)

- <a id="resource-rose-pine"></a>[Rose Pine](https://github.com/rose-pine/obsidian) — Write with warm, subdued colors inspired by the Rosé Pine palette.

![Rose Pine theme](assets/themes/rose-pine/preview.png)


<a id="topic-appearance-css"></a>

### CSS snippets & layouts

- <a id="resource-style-settings"></a>[Style Settings](https://github.com/community-archive/obsidian-style-settings) — Adjust supported theme, plugin and CSS snippet options from a settings panel.
  Useful for fine-tuning a chosen theme; available controls depend on compatible themes, plugins or snippets.
- <a id="resource-modular-css"></a>[Modular CSS Layout](https://github.com/efemkay/obsidian-modular-css-layout) — Use CSS snippets to add multi-column notes, wide views and gallery cards.
- <a id="resource-css-snippets"></a>[Obsidian CSS Snippets](https://github.com/r-u-s-h-i-k-e-s-h/Obsidian-CSS-Snippets) — Pick individual CSS snippets to customize interface elements and note presentation.
- <a id="resource-sailkite-snippets"></a>[sailKite's Snippets and Demos](https://github.com/sailKiteV/Obsidian-Snippets-and-Demos) — Adapt CSS snippets and Markdown demonstrations for custom note layouts.
- <a id="resource-minimal-snippets"></a>[Minimal Theme CSS Snippets](https://github.com/replete/obsidian-minimal-theme-css-snippets) — Fine-tune Minimal with targeted interface and typography snippets.
- <a id="resource-flexoki"></a>[Flexoki](https://stephango.com/flexoki) — Explore an ink-and-paper color palette available in themes such as Minimal.


<a id="category-templates"></a>

## Templates & vaults

[Personal vault starters](#topic-templates-personal) · [Research & query examples](#topic-templates-examples) · [Note & clipping templates](#topic-templates-notes)

<a id="topic-templates-personal"></a>

### Personal vault starters

- <a id="resource-kepano-vault"></a>[kepano’s Obsidian vault](https://github.com/kepano/kepano-obsidian) — A personal vault template with example notes, categories and reusable templates.
  Useful for studying how a real vault is organized; adopt useful structures before moving your own notes.
- <a id="resource-lifeos"></a>[LifeOS](https://github.com/quanru/obsidian-example-lifeos) — Start a personal management vault with PARA folders and periodic-note templates.
- <a id="resource-bramses-vault"></a>[Bramses’ Highly Opinionated Vault](https://github.com/bramses/bramses-highly-opinionated-vault-2023) — Explore a Zettelkasten-oriented vault with project workflows, templates and tutorials.
- <a id="resource-cyanvoxel-vault"></a>[CyanVoxel’s Vault Template](https://github.com/CyanVoxel/Obsidian-Vault-Template) — Explore a personal vault layout with coordinated CSS snippets and a companion video tour.
- <a id="resource-dashboard-plus-plus"></a>[Dashboard++](https://github.com/TfTHacker/DashboardPlusPlus) — Build a home dashboard with linked sections and multi-column layouts.
- <a id="resource-zk-starter-kit"></a>[Zettelkasten Starter Kit](https://github.com/groepl/Obsidian-Zettelkasten-Starter-Kit) — Start a linked-note system with example notes and a ready-made vault structure.
- <a id="resource-obsidian-jg-method"></a>[JG Method](https://github.com/joshwingreene/obsidian-jg-method) — Explore a starter vault organized around goals, tasks and development work.
- <a id="resource-ideaverse-lite"></a>[Ideaverse Lite](https://www.linkingyourthinking.com/ideaverse-for-obsidian/onboarding-ideaverse) — Explore a free linked-note starter vault with maps and example notes.

<a id="topic-templates-examples"></a>

### Research & query examples

- <a id="resource-starter-templates"></a>[Obsidian Starter Templates](https://github.com/masonlr/obsidian-starter-templates) — Explore research-project and technology-radar vaults built around linked notes.
- <a id="resource-dataview-example-vault"></a>[Dataview Example Vault](https://github.com/s-blu/obsidian_dataview_example_vault) — Learn Dataview with sample data, basic queries and JavaScript examples in a downloadable vault.
  Useful for modifying queries alongside their results; understand the required fields before copying examples into your vault.
- <a id="resource-dataview-snippets"></a>[Dataview Snippets](https://github.com/Aetherinox/obsidian-dataview-snippets) — Adapt reusable Dataview queries for indexes, lists and galleries.
- <a id="resource-blue-topaz-vault"></a>[Blue Topaz Example Vault](https://github.com/cumany/Blue-topaz-examples) — Explore a Chinese example vault combining dashboards, plugins and theme layouts.

<a id="topic-templates-notes"></a>

### Note & clipping templates

- <a id="resource-zettelkasten-templates"></a>[Obsidian Templates for Zettelkasten](https://github.com/groepl/Obsidian-Templates) — Reuse note templates for books, quotes, concepts and other parts of a Zettelkasten.
  Useful as a consistent starting point; keep fields that support ideas and source links rather than copying every convention.
- <a id="resource-clipper-templates"></a>[Web Clipper Templates](https://github.com/kepano/clipper-templates) — Capture structured references from sites such as arXiv, Goodreads and Wikipedia.
  Useful for customizing capture fields for frequently read sites; check titles, source URLs and extracted text after importing.
- <a id="resource-dashboard-gallery"></a>[Obsidian Dashboard Gallery](https://github.com/InlitX/Obsidian-Dashboard-Gallery) — Reuse dashboard layouts and queries for a visual vault homepage.
- <a id="resource-meeting-note-template"></a>[Meeting decisions and actions](content/en/meeting-note-template.md) — Keep agenda, decisions, owners and next actions in one note for follow-up.
  An original lightweight template from this project. Copy its template sections into your template folder and insert them with core Templates; no community plugin is required.
  [Usage & choosing](content/en/meeting-note-template.md)
- <a id="resource-reading-note-template"></a>[Reading sources and ideas](content/en/reading-note-template.md) — Separate source claims, your interpretation and open questions while retaining a path to the original.
  An original lightweight template from this project. Copy its template sections into your template folder and insert them with core Templates; no community plugin is required.
  [Usage & choosing](content/en/reading-note-template.md)
- <a id="resource-project-review-template"></a>[Project review](content/en/project-review-template.md) — Compare goals with results, reasons and next changes rather than only logging events.
  An original lightweight template from this project. Copy its template sections into your template folder and insert them with core Templates; no community plugin is required.
  [Usage & choosing](content/en/project-review-template.md)


<a id="category-ai"></a>

## AI & automation

Model APIs, subscriptions and cloud services may have separate costs.

[Chat & writing](#topic-ai-chat) · [Local models & note retrieval](#topic-ai-retrieval) · [Skills & visual automation](#topic-ai-agents) · [Classification & conversation archives](#topic-ai-organize) · [Audio & learning](#topic-ai-audio-study)

<a id="topic-ai-chat"></a>

### Chat & writing

- <a id="resource-copilot"></a>[Copilot](https://github.com/logancyang/obsidian-copilot) — Chat with note context inside Obsidian, or connect agents such as Codex and Claude Code. · Optional payment
  Useful for AI work within the note interface; agent backends run local processes and are desktop features, while mobile has a different feature set.
  Use your own agent account, model key or local model; provider charges are separate, and hosted models or some features require a paid plan.
  [Usage & choosing](content/en/copilot.md)
- <a id="resource-chatgpt-md"></a>[ChatGPT MD](https://github.com/bramses/chatgpt-md) — Keep AI conversations in Markdown notes using cloud providers, Ollama or LM Studio.
- <a id="resource-text-generator"></a>[Text Generator](https://github.com/nhaouari/obsidian-textgenerator-plugin) — Use prompt templates with cloud or local models for repeated note generation and rewriting tasks.
  Useful for tasks with a defined input and output, such as turning points into a draft; compare generated text with the source.
  The plugin is free; cloud models follow provider pricing, and local models require a local runtime.
- <a id="resource-bmo-chatbot"></a>[BMO Chatbot](https://github.com/longy2k/obsidian-bmo-chatbot) — Chat with configurable AI personas using local or cloud model providers.
- <a id="resource-companion"></a>[Companion](https://github.com/rizerphe/obsidian-companion) — Suggest inline text completions using the surrounding note as context.
- <a id="resource-tars"></a>[Tars](https://github.com/tarslab/obsidian-tars) — Generate text through tag-triggered prompts with multiple model providers.
- <a id="resource-smart-composer"></a>[Smart Composer](https://github.com/glowingjade/obsidian-smart-composer) — Ask questions with note context and apply suggested edits to the vault.
- <a id="resource-copilot-auto-completion"></a>[Copilot auto completion](https://github.com/j0rd1smit/obsidian-copilot-auto-completion) — Show configurable AI text completions beside the cursor as you write.

<a id="topic-ai-retrieval"></a>

### Local models & note retrieval

- <a id="resource-local-gpt"></a>[Local GPT](https://github.com/pfrankov/obsidian-local-gpt) — Summarize or rewrite selected text using configurable AI actions and local model support.
  Useful for focused actions on selected text; whether processing is local depends on the configured model endpoint.
- <a id="resource-smart-connections"></a>[Smart Connections](https://github.com/brianpetro/obsidian-smart-connections) — Surface semantically related notes and excerpts with local embeddings. · Optional payment
- <a id="resource-llm-workspace"></a>[LLM Workspace](https://github.com/ofalvai/obsidian-llm-workspace) — Chat with a manually selected set of notes and inspect the sources used for retrieval.
- <a id="resource-ollama-chat"></a>[Ollama Chat](https://github.com/brumik/obsidian-ollama-chat) — Ask questions about your notes using Ollama and a local retrieval setup.

<a id="topic-ai-agents"></a>

### Skills & visual automation

- <a id="resource-obsidian-skills"></a>[Obsidian Skills](https://github.com/kepano/obsidian-skills) — Provide compatible AI agents with instructions for Obsidian formats and CLI tasks, including Markdown, Bases and Canvas.
  This is a skill collection rather than a standalone Obsidian plugin; choose skills for the task and configure an agent.
  Skill files are free; the selected agent or model service may charge separately.
  [Usage & choosing](content/en/obsidian-skills.md)
- <a id="resource-cannoli"></a>[Cannoli](https://github.com/DeabLabs/cannoli) — Build executable AI workflows with cards and arrows in Obsidian Canvas.
- <a id="resource-loom"></a>[Loom](https://github.com/cosmicoptima/loom) — Explore alternative continuations of a text through branching AI generations.
- <a id="resource-chat-stream"></a>[Chat Stream](https://github.com/rpggio/obsidian-chat-stream) — Branch AI conversations on Canvas while choosing which ancestor notes provide context.
- <a id="resource-smart-templates"></a>[Smart Templates](https://github.com/brianpetro/obsidian-smart-templates) — Combine Markdown templates and selected vault context into repeatable AI prompts. · Optional payment
- <a id="resource-ai-templater"></a>[AI for Templater](https://github.com/tfthacker/obsidian-ai-templater) — Call OpenAI-compatible language models from Templater scripts.
- <a id="resource-skill-obsidian-markdown"></a>[Obsidian Markdown Skill](https://github.com/kepano/obsidian-skills/blob/main/skills/obsidian-markdown/SKILL.md) — Create and edit notes with wikilinks, embeds, callouts and properties.
  Useful when an agent edits note syntax; it is not a control interface for the running app.
  Skill files are free; agent or model usage may have separate charges.
- <a id="resource-skill-obsidian-bases"></a>[Obsidian Bases Skill](https://github.com/kepano/obsidian-skills/blob/main/skills/obsidian-bases/SKILL.md) — Guide an agent in creating and editing Bases views, filters and formulas.
  Useful for generating views over structured notes; standardize properties before checking filter results.
  Skill files are free; agent or model usage may have separate charges.
- <a id="resource-skill-json-canvas"></a>[JSON Canvas Skill](https://github.com/kepano/obsidian-skills/blob/main/skills/json-canvas/SKILL.md) — Guide an agent in building Canvas files with nodes, edges and groups.
  Useful for turning known relationships into a canvas; inspect layout and connection meaning after generation.
  Skill files are free; agent or model usage may have separate charges.
- <a id="resource-skill-obsidian-cli"></a>[Obsidian CLI Skill](https://github.com/kepano/obsidian-skills/blob/main/skills/obsidian-cli/SKILL.md) — Guide an agent in interacting with a vault through the CLI and checking available commands.
  Useful for app operations beyond file editing; requires Obsidian running with its CLI enabled.
  Skill files are free; agent or model usage may have separate charges.

<a id="topic-ai-organize"></a>

### Classification & conversation archives

- <a id="resource-auto-classifier"></a>[Auto Classifier](https://github.com/HyeonseoNam/auto-classifier) — Suggest note tags using OpenAI-compatible models or Jina AI classification.
- <a id="resource-nexus-ai-importer"></a>[Nexus AI Chat Importer](https://github.com/Superkikim/nexus-ai-chat-importer) — Import ChatGPT, Claude and other exported AI conversations as local Markdown notes.
- <a id="resource-ai-tagger"></a>[AI Tagger](https://github.com/lucagrippa/obsidian-ai-tagger) — Suggest tags from your existing vocabulary using a language model.
- <a id="resource-ai-summarize"></a>[AI Summarize](https://github.com/ravenwits/obsidian-ai-summarize) — Create note summaries and folder digests with an OpenAI model.
- <a id="resource-packup4ai"></a>[packUp4AI](https://github.com/shuxueshuxue/PackUp4AI) — Bundle linked notes and backlinks into focused context for external AI tools.

<a id="topic-ai-audio-study"></a>

### Audio & learning

- <a id="resource-aloud"></a>[Aloud](https://github.com/adrianlyjak/obsidian-aloud-tts) — Read notes aloud and export audio through a configured speech-generation service.
- <a id="resource-quiz-generator"></a>[Quiz Generator](https://github.com/ECuiDev/obsidian-quiz-generator) — Turn selected notes into interactive practice questions with an AI model.
- <a id="resource-whisper"></a>[Whisper](https://github.com/nikdanilov/whisper-obsidian-plugin) — Transcribe recorded or uploaded audio through a Whisper-compatible API.
- <a id="resource-ai-latex-generator"></a>[AI LaTeX Generator](https://github.com/aaaaayushh/ai-latex-generator) — Convert a selected natural-language formula description into LaTeX using Ollama.
- <a id="resource-voicenotes-sync"></a>[Voicenotes Sync](https://github.com/voicenotes-community/voicenotes-sync) — Import recordings, transcripts and generated summaries from a Voicenotes account. · Optional payment


<a id="category-integrations"></a>

## Tools & integrations

[Reading & migration](#topic-integrations-collect) · [Publishing & digital gardens](#topic-integrations-publish) · [App launchers, APIs & MCP](#topic-integrations-connect) · [Export & conversion](#topic-integrations-export) · [Sync & storage](#topic-integrations-sync)

<a id="topic-integrations-collect"></a>

### Reading & migration

- <a id="resource-importer"></a>[Importer](https://github.com/obsidianmd/obsidian-importer) — Convert notes from apps such as Notion, Evernote and OneNote into Markdown.
- <a id="resource-web-clipper"></a>[Obsidian Web Clipper](https://obsidian.md/clipper) — Save web pages and highlights to Obsidian, with optional AI processing.
  Useful for capturing pages before making reading notes; add your own summary and purpose so the vault is more than copied pages.
- <a id="resource-readwise-reader"></a>[Readwise Reader](https://readwise.io/read) — Read articles and PDFs, then export highlights to Obsidian through Readwise. · Paid
- <a id="resource-yarle"></a>[YARLE](https://github.com/akosbalasko/yarle) — Convert Evernote exports to Markdown while preserving attachments, metadata and note links.
- <a id="resource-obsidian-read-it-later"></a>[ReadItLater](https://github.com/dominikpieper/obsidian-ReadItLater) — Save web content as notes using templates tailored to different source types.
- <a id="resource-obsidian-weread-plugin"></a>[Weread](https://github.com/zhaohongxuan/obsidian-weread-plugin) — Sync highlights and annotations from WeRead into reading notes.
- <a id="resource-markdownload"></a>[MarkDownload](https://github.com/deathau/markdownload) — Save browser pages as Markdown files for your vault.
- <a id="resource-keep-it-markdown"></a>[Keep It Markdown](https://github.com/djsudduth/keep-it-markdown) — Export Google Keep notes into Markdown for migration and archiving.

<a id="topic-integrations-publish"></a>

### Publishing & digital gardens

- <a id="resource-quartz"></a>[Quartz](https://github.com/jackyzha0/quartz) — Turn Markdown notes into a website with backlinks, search and a graph view.
  Useful when you want control over publishing and site styling; expect to configure builds and hosting.
- <a id="resource-digital-garden"></a>[Digital Garden](https://github.com/oleeskild/obsidian-digital-garden) — Publish selected Obsidian notes to a digital garden using a configurable site template.
- <a id="resource-perlite"></a>[Perlite](https://github.com/secure-77/Perlite) — Browse a Markdown vault through a self-hosted web interface.
- <a id="resource-flowershow"></a>[Flowershow](https://github.com/flowershow/flowershow) — Publish Markdown as a website with hosted plans and an open-source codebase. · Optional payment

<a id="topic-integrations-connect"></a>

### App launchers, APIs & MCP

- <a id="resource-advanced-uri"></a>[Advanced URI](https://github.com/Vinzent03/obsidian-advanced-uri) — Trigger Obsidian actions from links in shortcuts and other applications.
- <a id="resource-local-rest-api"></a>[Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) — Connect scripts and agents to your vault through a local REST API and MCP server.
- <a id="resource-shell-commands"></a>[Shell commands](https://github.com/Taitava/obsidian-shellcommands) — Run configured terminal commands with note variables and insert their output into notes.
- <a id="resource-shimmering-obsidian"></a>[Shimmering Obsidian](https://github.com/chrisgrieser/shimmering-obsidian) — Search and create Obsidian notes from Alfred on macOS; requires Alfred Powerpack. · Paid

<a id="topic-integrations-export"></a>

### Export & conversion

- <a id="resource-obsidian-kindle-export"></a>[Kindle](https://github.com/simeonlukas/obsidian-kindle-export) — Export notes and embedded content as EPUB through a configured conversion backend.
- <a id="resource-obsidian-pandoc"></a>[Pandoc Plugin](https://github.com/oliverbalfour/obsidian-pandoc) — Export notes to DOCX, EPUB and other formats through an installed Pandoc converter.

<a id="topic-integrations-sync"></a>

### Sync & storage

- <a id="resource-obsidian-git"></a>[Obsidian Git](https://github.com/Vinzent03/obsidian-git) — Inspect changes, commit versions and sync with a remote Git repository from your vault.
  Best suited to desktop users familiar with Git; substantial mobile limitations make it a poor default for cross-device sync.
  [Usage & choosing](content/en/obsidian-git.md)
- <a id="resource-obsidian-livesync"></a>[Self-hosted LiveSync](https://github.com/vrtmrz/obsidian-livesync) — Sync vaults through a self-hosted CouchDB or supported object-storage backend.
- <a id="resource-remotely-save"></a>[Remotely Save](https://github.com/remotely-save/remotely-save) — Sync notes with supported cloud storage, with optional paid sync features. · Optional payment
- <a id="resource-s3-attachments-storage"></a>[S3 attachments storage](https://github.com/ttax00/obsidian-s3) — Store and retrieve media attachments through S3-compatible object storage.


<a id="category-workflows"></a>

## Workflows

- <a id="resource-reading-workflow"></a>[From a saved article to a usable note](content/en/reading-workflow.md) — Turn a saved article into a linked note you can find and reuse.
- <a id="resource-research-workflow"></a>[From a question to a sourced answer](content/en/research-workflow.md) — Compare sources and connect each conclusion to its evidence.
- <a id="resource-writing-workflow"></a>[From linked notes to a finished draft](content/en/writing-workflow.md) — Turn source notes into an outline, draft and exportable article.
- <a id="resource-learning-workflow"></a>[From course notes to usable knowledge](content/en/learning-workflow.md) — Practice recall, record mistakes and apply concepts in a small task.
- <a id="resource-projects-workflow"></a>[From a project goal to next actions](content/en/projects-workflow.md) — Connect outcomes, tasks and weekly reviews in a project note.
- <a id="resource-ai-workflow"></a>[Use AI with a focused set of notes](content/en/ai-workflow.md) — Ask source-based questions and review proposed note changes before applying them.
- <a id="resource-sync-backup-workflow"></a>[From device sync to recoverable backups](content/en/sync-backup-workflow.md) — Choose a sync method, keep independent backups and verify them with a restore exercise.
  Use when adding devices, migrating a vault or changing sync methods.


<a id="category-methods"></a>

## Methods

[Organizing & connecting ideas](#topic-methods-principles) · [Note design & publishing](#topic-methods-design)

<a id="topic-methods-principles"></a>

### Organizing & connecting ideas

- <a id="resource-zettelkasten-introduction"></a>[Zettelkasten: getting started](https://zettelkasten.de/overview/) — Learn how to connect notes into a Zettelkasten for reading and writing.
- <a id="resource-evergreen-notes"></a>[Evergreen notes](https://notes.andymatuschak.org/Evergreen_notes) — Learn to develop connected, concept-focused notes through repeated revision.
- <a id="resource-para"></a>[The PARA Method](https://fortelabs.com/blog/para/) — Organize notes into Projects, Areas, Resources and Archives around actionable work.
- <a id="resource-file-over-app"></a>[File over app](https://stephango.com/file-over-app) — Understand why durable, controllable files matter when choosing a note-taking system.
- <a id="resource-johnnydecimal"></a>[Johnny.Decimal](https://johnnydecimal.com/documentation/introduction) — Use numbered areas and categories to give files and notes predictable locations.

<a id="topic-methods-design"></a>

### Note design & publishing

- <a id="resource-steph-evergreen"></a>[Evergreen Notes — Steph Ango](https://stephango.com/evergreen-notes) — Write reusable ideas as notes that can develop and connect over time.
- <a id="resource-garden-history"></a>[A Brief History & Ethos of the Digital Garden](https://maggieappleton.com/garden-history) — Understand digital gardens as evolving, connected collections of public notes.
- <a id="resource-progressive-summarization"></a>[Progressive Summarization](https://fortelabs.com/blog/progressive-summarization-a-practical-technique-for-designing-discoverable-notes/) — Layer highlights and summaries to make useful passages easier to rediscover.
- <a id="resource-atomic-notes"></a>[Evergreen Notes Should Be Atomic](https://notes.andymatuschak.org/Evergreen_notes_should_be_atomic) — Keep a note focused on one idea so it can be reused in different contexts.
- <a id="resource-concept-notes"></a>[Evergreen Notes Should Be Concept-Oriented](https://notes.andymatuschak.org/Evergreen_notes_should_be_concept-oriented) — Organize reusable notes around concepts rather than the source that introduced them.


<a id="category-learning"></a>

## Learning & community

[Communities & directories](#topic-learning-community) · [Courses & author resources](#topic-learning-learn) · [Articles & practical tutorials](#topic-learning-tutorials)

<a id="topic-learning-community"></a>

### Communities & directories

- <a id="resource-obsidian-forum"></a>[Obsidian Forum](https://forum.obsidian.md/) — Find answers, share workflows and discuss plugins with the Obsidian community.
- <a id="resource-obsidian-forum-zh"></a>[Obsidian Chinese Forum](https://forum-zh.obsidian.md/) — Discuss plugins, note-taking methods and troubleshooting in Chinese.
- <a id="resource-obsidian-hub"></a>[Obsidian Hub](https://github.com/obsidian-community/obsidian-hub) — Browse community knowledge online or download the shared vault to explore it in Obsidian.
- <a id="resource-pkmer"></a>[PKMer](https://pkmer.cn/) — Find Chinese Obsidian tutorials, plugin guides and knowledge-management resources. · Optional payment

<a id="topic-learning-learn"></a>

### Courses & author resources

- <a id="resource-linking-your-thinking"></a>[Linking Your Thinking](https://www.linkingyourthinking.com/) — Explore Nick Milo’s linked-note workflows, learning resources and workshops. · Optional payment
- <a id="resource-obsidian-blog"></a>[Obsidian Blog](https://obsidian.md/blog/) — Follow official feature announcements, product updates and community highlights.
- <a id="resource-building-second-brain"></a>[Building a Second Brain](https://www.buildingasecondbrain.com/) — Explore books, resources and courses about organizing knowledge for creative work. · Optional payment

<a id="topic-learning-tutorials"></a>

### Articles & practical tutorials

- <a id="resource-how-i-use-obsidian"></a>[How I use Obsidian](https://stephango.com/vault) — See how Steph Ango uses categories, properties, templates and links in a personal vault.
  Useful for examining the author’s organizational choices; compare your own inputs and outputs instead of copying the entire workflow.
- <a id="resource-obsidian-rocks"></a>[Obsidian Rocks](https://obsidian.rocks/) — Read practical tutorials on Obsidian features, plugins and everyday workflows.
- <a id="resource-backup-guide"></a>[Back up your Obsidian files](https://help.obsidian.md/backup) — Explains the difference between sync and backup and how to keep recoverable vault copies.
  Read before adding devices or migrating; the goal is restoring an earlier state, not merely seeing the same files elsewhere.
- <a id="resource-sync-methods-guide"></a>[Sync your notes across devices](https://help.obsidian.md/sync-notes) — Compare official sync, cloud drives and other methods with their device-specific setup differences.
  Filter by your device combination before following setup steps; desktop support does not imply equivalent mobile support.
- <a id="resource-plugin-security-guide"></a>[Community plugin security](https://help.obsidian.md/Extending+Obsidian/Plugin+security) — Understand community plugin capabilities and the role of Restricted Mode.
  Read before installing plugins or connecting AI to a vault; directory inclusion does not provide fine-grained permission isolation.


<a id="category-development"></a>

## Development

[Build plugins & tools](#topic-development-build) · [Development & testing tools](#topic-development-testing)

<a id="topic-development-build"></a>

### Build plugins & tools

- <a id="resource-developer-docs"></a>[Obsidian Developer Docs](https://docs.obsidian.md/) — Read official guides for building plugins and themes and working with the API.
- <a id="resource-sample-plugin"></a>[Obsidian Sample Plugin](https://github.com/obsidianmd/obsidian-sample-plugin) — The official starter template for building Obsidian community plugins.
- <a id="resource-obsidian-api"></a>[Obsidian API](https://github.com/obsidianmd/obsidian-api) — Use the official TypeScript definitions when developing Obsidian plugins.
- <a id="resource-json-canvas"></a>[JSON Canvas](https://jsoncanvas.org/) — Use the open canvas format to exchange nodes, edges and groups between tools.
- <a id="resource-obsidian-sample-theme"></a>[Obsidian Sample Theme](https://github.com/obsidianmd/obsidian-sample-theme) — Use the official starter files to create and submit an Obsidian theme.
- <a id="resource-obsidian-releases"></a>[Obsidian Releases](https://github.com/obsidianmd/obsidian-releases) — Find the official registries used to distribute community plugins and themes.
- <a id="resource-obsidian-translations"></a>[Obsidian Translations](https://github.com/obsidianmd/obsidian-translations) — Contribute translations for Obsidian's interface.
- <a id="resource-obsidian-typings"></a>[Obsidian Typings](https://github.com/obsidian-typings/obsidian-typings) — Explore community TypeScript definitions that extend the official API types.

<a id="topic-development-testing"></a>

### Development & testing tools

- <a id="resource-execute-code"></a>[Execute Code](https://github.com/twibiral/obsidian-execute-code) — Run supported code blocks locally and display their output beneath the code.
- <a id="resource-obsidian42-brat"></a>[BRAT](https://github.com/tfthacker/obsidian42-brat) — Install and update beta plugins or themes directly from their repositories.
- <a id="resource-hot-reload"></a>[Hot Reload](https://github.com/pjeby/hot-reload) — Reload plugins under development when their files change.
- <a id="resource-plugin-reloader"></a>[Plugin Reloader](https://github.com/benature/obsidian-plugin-reloader) — Reload a selected plugin from a command or hotkey during development.
- <a id="resource-obsidian-linter-rules"></a>[Obsidian ESLint Plugin](https://github.com/obsidianmd/eslint-plugin) — Check plugin code against Obsidian-specific API and development rules.
<!-- catalog:end -->

[Image credits](assets/README.md)

## Acknowledgements

Thanks to these community lists for resource leads and ideas for organizing the catalog:

- [kmaasrud/awesome-obsidian](https://github.com/kmaasrud/awesome-obsidian)
- [obsidian-pkm-vault/awesome-obsidian-vault](https://github.com/obsidian-pkm-vault/awesome-obsidian-vault)
- [PKM-er/awesome-obsidian-zh](https://github.com/PKM-er/awesome-obsidian-zh)
- [awesome-obsidian/awesome-obsidian](https://github.com/awesome-obsidian/awesome-obsidian)
- [danielrosehill/Awesome-Obsidian-AI-Tools](https://github.com/danielrosehill/Awesome-Obsidian-AI-Tools)
