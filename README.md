# Armstrong Agency Skills

Free, reusable agent skills for high-quality Webflow work.

These skills complement [Webflow's official skills](https://github.com/webflow/webflow-skills). Webflow's repository covers platform operations, MCP tools, publishing, CMS workflows, and standardized technical audits. Armstrong's skills focus on implementation judgment: build workflow, framework grammar, reuse discipline, and completion gates.

## Core skills

### `webflow-build`

How to build in Webflow: section-based workflow, reuse ladder (existing component → class → combo → new class → custom code), native Designer styling, completion QA, and hard confirmation gates (never overwrite live pages or publish without explicit approval).

Use for any Webflow implementation work—assembling pages with approved components or creating new design-system decisions.

Supporting references:
- `references/native-styling.md` — Designer-native style fields; no embed or custom-property workarounds
- `references/figma-to-webflow.md` — Figma implementation judgment
- `references/preview-and-state.md` — Designer Preview, runtime custom behavior, and publication-state evidence
- `references/platform-facts.md` — verified Webflow platform capabilities, Shadow DOM behavior, and Code Component facts
- `references/headless-quirks.md` — MCP tool edge cases, workarounds, and time-sensitive observations

### Framework grammar

Framework skills provide naming and structure conventions only. Pair them with `webflow-build` for the implementation workflow.

#### `framework/client-first`

Apply Finsweet Client-First rules to Webflow structure, class naming, utilities, components, responsive behavior, and Navigator organization.

Supporting references:
- `references/conventions.md` — detailed naming rules, token mapping, and migration cautions

#### `framework/mast`

Apply No-Code Supply Co. Mast rules to Webflow structure, class naming, utilities, components, variables, Build Mode, and Navigator organization.

Supporting references:
- `references/conventions.md` — naming, class types, variables, management rules
- `references/layout-and-grid.md` — page structure and 12-column system
- `references/components.md` — component inventory and Build Mode notes

Additional frameworks can be added later as `skills/framework/<name>/`.

## Runtime-specific setup

### Claude Code

`skills/claude-code/webflow-mcp-setup` — Webflow MCP connection setup for Claude Code.

### Codex (removed)

The Codex Webflow MCP setup skill was removed because it doesn't work.

For Codex users needing Webflow access, use the **webflow-bridge** approach. This repository does not include webflow-bridge setup instructions; consult the webflow-bridge documentation or your team's internal setup guides.

## Install

Install the repository with the Skills CLI:

```bash
npx skills add armstrong-agency/skills
```

Or copy an individual directory from `skills/` into the skills directory used by your agent.

## Working model

- Use `webflow-build` for how to build: reuse ladder, native styling, completion gates, and confirmation checkpoints.
- Use `framework/client-first` when the project follows Client-First or a documented Client-First-derived system.
- Use `framework/mast` when the project follows Mast or a documented Mast-derived system.
- Framework skills provide grammar only; `webflow-build` provides the workflow.
- Treat persisted Webflow state, Designer appearance, runtime behavior, and publication state as separate evidence.
- Never publish a Webflow site unless the user explicitly requests that publication.

## License

Original material in this repository is dedicated to the public domain under [CC0 1.0 Universal](LICENSE). Third-party material and trademarks retain their respective rights.

Webflow, Finsweet, Client-First, Mast, No-Code Supply Co., and other product names and trademarks belong to their respective owners. This repository is an independent Armstrong Agency project and does not imply endorsement by those companies.
