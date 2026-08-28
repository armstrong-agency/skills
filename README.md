# Armstrong Agency Skills

Free, reusable agent skills for Webflow work over MCP.

These complement [Webflow's official skills](https://github.com/webflow/webflow-skills) (platform operations, MCP tools, publishing, CMS). This repo is implementation judgment plus framework grammar.

## Layout

```text
skills/                    Active tools (Agent Skills)
  wf-mcp-setup/            Connect MCP (Claude Code or Cursor, not Codex)
  wf-audit/                Style guide, colors, classes → webflow-context.md
  wf-plan/                 Talk through the job, classes, destination
  wf-prototype/            HTML for one section (not Webflow)
  wf-build/                Put it in Webflow, one section at a time
framework-grammar/         Not skills — naming lookups the tools read
  client-first.md
  mast.md
```

Each skill is **version 0.1.0, work in progress**.

A fuller design-system catalog skill is planned. `wf-audit` covers style guide, colors, and classes for now.

## Skills

### `wf-mcp-setup`

Project-scoped Webflow MCP so each repo keeps its own workspace authorization. Claude Code and Cursor. Not Codex.

### `wf-audit`

Style guide, colors, classes. Writes `webflow-context.md` for the other skills.

### `wf-plan`

What to build, mobile, reuse vs new classes, draft vs staging vs production. No Webflow writes.

### `wf-prototype`

Standalone HTML for one section (layout, mobile, motion). Faster than Webflow MCP.

### `wf-build`

Implements in Webflow. Better with audit + plan (+ prototype) already in `webflow-context.md`. One section at a time. Never publish unless asked.

## Framework grammar

Not skills. After the convention is known, the tools read `framework-grammar/client-first.md` or `mast.md`. Copy this folder into the client project, or keep a checkout of this repo visible to the agent.

## Install

```bash
npx skills add armstrong-agency/skills
```

Copy `framework-grammar/` into the project (or clone this repo) so the tools can load naming files.

## Working model

Audit → plan → prototype (HTML) → build (Webflow). You can skip to build; ask more questions if context is missing.

Never publish a Webflow site unless the user explicitly asks.

## License

Original material is [CC0 1.0 Universal](LICENSE). Third-party names (Webflow, Finsweet, Client-First, Mast, Lumos, No-Code Supply Co.) belong to their owners. This is an independent Armstrong Agency project.
