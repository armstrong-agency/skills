# Armstrong Agency Skills

Free, reusable agent skills for Webflow work over MCP.

These complement [Webflow's official skills](https://github.com/webflow/webflow-skills) (platform operations, MCP tools, publishing, CMS). This repo is implementation judgment plus framework grammar.

## Layout

```text
skills/                    Active tools (Agent Skills)
  wf-mcp-setup/            Connect MCP (Pi, Claude Code, Cursor local + Cloud; not Codex)
    references/            cursor-local.md, cursor-cloud.md (Cursor surfaces differ)
  wf-audit/                Read-only site/style-guide/naming check
  wf-design-system/        Token catalog → DESIGN.md (no Webflow writes)
  wf-plan/                 Scope, reuse, destination — then stop
  wf-prototype/            Assemble on an unpublished draft page
  wf-build/                Implement in Webflow, one section at a time
  */references/            Packaged copy of shared quirks when that skill cites them
framework-grammar/         Not skills — naming lookups the tools read
  client-first.md
  mast.md
references/                Shared MCP/Designer footguns (edit here, copy into skills)
```

Each skill is **version 0.1.0, work in progress**.

## Skills

### `wf-mcp-setup`

Project-scoped Webflow MCP so each repo keeps its own workspace authorization. Pi, Claude Code, and Cursor. Not Codex.

**Cursor local and Cursor Cloud Agents are separate.** Local uses `.cursor/mcp.json`. Cloud does not load project MCP files — register HTTP MCP on [cursor.com/agents](https://cursor.com/agents) (`+` → MCP Servers → Add MCP). See `skills/wf-mcp-setup/references/cursor-local.md` and `cursor-cloud.md`.

### `wf-audit`

Read-only: is there a Style Guide, is there a naming convention, connected/public-site issues. Does not extract tokens (`wf-design-system`) or mutate.

### `wf-design-system`

Catalog colors, type, spacing, radii, and control states into `DESIGN.md`. Markdown only — no Webflow writes.

### `wf-plan`

What to build, reuse vs new, draft vs staging vs production. No Webflow writes.

### `wf-prototype`

Assemble on a new unpublished draft/sandbox page using existing classes only. Do not invent system classes.

### `wf-build`

Implement in Webflow. One section at a time. Never publish unless asked.

## Framework grammar

Not skills. After the convention is known, the tools read `framework-grammar/client-first.md` or `mast.md`. Copy this folder into the client project, or keep a checkout of this repo visible to the agent.

## Install

```bash
npx skills add armstrong-agency/skills
# or
skilldeck install-group webflow --global
```

Copy `framework-grammar/` into the project (or clone this repo) so the tools can load naming files.

## Working model

Audit → design-system (if tokens needed) → plan → prototype (draft page) → build. You can skip steps; ask more questions if context is missing.

Never publish a Webflow site unless the user explicitly asks.

## License

Original material is [CC0 1.0 Universal](LICENSE). Third-party names (Webflow, Finsweet, Client-First, Mast, Lumos, No-Code Supply Co.) belong to their owners. This is an independent Armstrong Agency project.
