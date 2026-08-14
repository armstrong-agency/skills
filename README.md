# Armstrong Agency Skills

Free, reusable agent skills for high-quality Webflow work.

These skills complement
[Webflow's official skills](https://github.com/webflow/webflow-skills).
Webflow's repository covers platform operations, MCP tools, publishing, CMS
workflows, and standardized technical audits. Armstrong's skills focus on
implementation judgment: preserving an existing design system, working within
the right role, and completing the relevant quality checks before returning
work.

## Core skills

### `client-first`

Apply Finsweet Client-First rules to Webflow structure, class naming,
utilities, components, responsive behavior, and Navigator organization.

Supporting references:
- `references/conventions.md` -- detailed naming rules, token mapping, and migration cautions

### `mast`

Apply No-Code Supply Co. Mast rules to Webflow structure, class naming,
utilities, components, variables, Build Mode, and Navigator organization.

Supporting references:
- `references/conventions.md` -- naming, class types, variables, management rules
- `references/layout-and-grid.md` -- page structure and 12-column system
- `references/components.md` -- component inventory and Build Mode notes

### `webflow-marketer`

Assemble and update pages using only approved components, templates, classes,
variables, CMS fields, content, and assets. Missing system capabilities are
handed to the Designer instead of being patched with one-off styles.

### `webflow-designer`

Design, extend, and refactor Webflow systems. This skill covers small component
boundaries, compounding approvals, shared-component safety, progressive custom
behavior, troubleshooting, and complete QA before work is presented.

Supporting references:
- `references/native-styling.md` -- Designer-native style fields; no embed or custom-property workarounds
- `references/figma-to-webflow.md` -- Figma implementation judgment
- `references/preview-and-state.md` -- Designer Preview, runtime custom behavior, and publication-state evidence
- `references/platform-facts.md` -- verified Webflow platform capabilities, Shadow DOM behavior, and Code Component facts
- `references/headless-quirks.md` -- MCP tool edge cases, workarounds, and time-sensitive observations
- `references/roles.md` -- Marketer vs Designer authority boundaries and when to switch roles

## Runtime-specific setup

### Claude Code

`skills/claude-code/webflow-mcp-setup` -- Webflow MCP connection setup for Claude Code.

### Codex (removed)

The Codex Webflow MCP setup skill was removed because it doesn't work.

For Codex users needing Webflow access, use the **webflow-bridge** approach.
This repository does not include webflow-bridge setup instructions; consult
the webflow-bridge documentation or your team's internal setup guides.

## Install

Install the repository with the Skills CLI:

```bash
npx skills add armstrong-agency/skills
```

Or copy an individual directory from `skills/` into the skills directory used
by your agent.

## Working model

- Use `client-first` when the project follows Client-First or a documented
  Client-First-derived system.
- Use `mast` when the project follows Mast or a documented Mast-derived
  system.
- Use `webflow-marketer` when the requested work can be assembled entirely
  from the approved system.
- Use `webflow-designer` when the work requires a new or changed reusable
  decision.
- Treat persisted Webflow state, Designer appearance, runtime behavior, and
  publication state as separate evidence.
- Never publish a Webflow site unless the user explicitly requests that
  publication.

## License

Original material in this repository is dedicated to the public domain under
[CC0 1.0 Universal](LICENSE). Third-party material and trademarks retain their
respective rights.

Webflow, Finsweet, Client-First, Mast, No-Code Supply Co., and other product names and trademarks belong
to their respective owners. This repository is an independent Armstrong
Agency project and does not imply endorsement by those companies.
