# Use AI with a focused set of notes

## Goal

Ask source-based questions and review proposed note changes before applying them.

## Steps

- Choose a bounded task, such as comparing three meeting notes. Select only the notes needed and check which model or service will receive their contents.
- Start with a read-only request: Compare these notes, cite the filename for each finding, distinguish agreement from disagreement, and list missing information. Do not edit files.
- Open the cited notes and verify each finding. Ask for the exact supporting passage when a conclusion is too broad or a citation is missing.
- Ask for proposed edits as a separate step. Review filenames, changes to meaning and links; use version history or a backup before applying accepted changes.
- Inspect the resulting files, open affected links and record unresolved questions. Keep original source material available for later checks.

## Acceptance

- Every accepted finding can be traced to a supplied note.
- Applied edits match the reviewed proposal and preserve working links.

## Optional extensions

Use [LLM Workspace](llm-workspace.md) to select context, [Local GPT](local-gpt.md) for configurable model actions, or [Obsidian Skills](obsidian-skills.md) with a coding agent.
