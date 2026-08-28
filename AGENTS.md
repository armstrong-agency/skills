# Repository guidance

- Keep published skills compatible with the open Agent Skills format (`skills/*/SKILL.md`).
- `framework-grammar/` is not a skill. Skills read those files for class names. Don't copy workflow into grammar.
- Each skill is one `SKILL.md`. Don't add per-skill reference folders.
- Instructions only. No required scripts or crawler dependencies.
- Discover Webflow MCP tool names in-session. Don't freeze tool names here; official Webflow MCP docs cover mechanics.
- First step of any skill that names classes: identify the convention and read `framework-grammar/client-first.md` or `mast.md`.
- Never publish a Webflow site from these skills unless the user explicitly asks.
- Never include private client screenshots, extracted tokens, site IDs, or evaluation artifacts in this public repository.
- Original material is CC0. Link to third-party docs rather than copying substantial third-party text.

## Working model

- `wf-mcp-setup` — project-scoped MCP (Claude Code or Cursor, not Codex).
- `wf-audit` — style guide, colors, classes → `webflow-context.md`.
- `wf-plan` — talk through the job; no Webflow writes.
- `wf-prototype` — HTML for one section; no Webflow MCP.
- `wf-build` — implement in Webflow, one section at a time.
- `framework-grammar/` — Client-First and Mast naming.
- Official Webflow skills remain complementary for platform operations.
