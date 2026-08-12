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

### `webflow-marketer`

Assemble and update pages using only approved components, templates, classes,
variables, CMS fields, content, and assets. Missing system capabilities are
handed to the Designer instead of being patched with one-off styles.

### `webflow-designer`

Design, extend, and refactor Webflow systems. This skill covers small component
boundaries, compounding approvals, shared-component safety, progressive custom
behavior, troubleshooting, and complete QA before work is presented.

## Runtime-specific setup

Claude Code and Codex use different project configuration and authentication
flows, so their Webflow MCP setup skills remain separate:

- `skills/claude-code/webflow-mcp-setup`
- `skills/codex/webflow-mcp-setup`

The three core skills are runtime-neutral.

## Supporting notes

These folders are repository documentation, not installable skills:

- `knowledge/` — hard-won Webflow platform facts and conventions the skills stand on (quirks catalogue, verified platform facts, Client-First naming grammar, Marketer vs Designer roles).
- `skills/webflow-designer/references/` — deeper Designer workflows for Figma-to-Webflow implementation and Preview/runtime/publication evidence.

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

Webflow, Finsweet, Client-First, and other product names and trademarks belong
to their respective owners. This repository is an independent Armstrong
Agency project and does not imply endorsement by those companies.
