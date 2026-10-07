# Webflow agent skills

Agent skills for building Webflow sites with an AI coding agent over the [Webflow MCP server](https://developers.webflow.com/mcp). They encode the judgment a careful Webflow developer applies: reuse the existing system before inventing, style only through native Designer controls, follow the site's naming convention, prototype on a draft page, and never publish without being asked.

They complement [Webflow's official skills](https://github.com/webflow/webflow-skills), which cover platform operations such as MCP tool mechanics, publishing, and CMS.

The skills use the open [Agent Skills](https://agentskills.io) format, so they work in any agent that supports it.

## Install

```bash
npx skills add armstrong-agency/skills
```

To install only some skills, name them, and include `wf-reference` with any skill that names classes:

```bash
npx skills add armstrong-agency/skills --skill wf-plan --skill wf-reference
```

You also need the Webflow MCP server connected to your project. `wf-mcp-setup` walks your agent through it.

## Skills

| Skill | What it does | Writes to Webflow |
| --- | --- | --- |
| `wf-mcp-setup` | Connects a project-scoped Webflow MCP server, so each project stays pinned to its own workspace. | No |
| `wf-audit` | Reviews a connected or public site: style guide, naming convention, structure, rendered semantics. | No |
| `wf-design-system` | Catalogs colors, type, spacing, radii, and control states into `DESIGN.md`. | No |
| `wf-plan` | Inventories sections, finds what can be reused, and justifies anything new before it is built. | No |
| `wf-prototype` | Assembles a layout on an unpublished draft page from existing components and classes only. | Draft page only |
| `wf-build` | Implements one section at a time with a reuse ladder, approval gates, and a completion checklist. | Yes, after confirmation |
| `wf-reference` | Shared lookups the other skills load: how to identify a site's naming convention, [Client-First](https://finsweet.com/client-first/docs/intro) and [Mast](https://www.nocodesupply.co/mast/docs) grammar, and known MCP and Designer quirks. | No |

## Workflow

A typical job runs audit → design-system (if you need tokens) → plan → prototype → build. Each step is optional; ask for the one you need, such as "audit this site" or "plan the pricing page."

No skill publishes a site unless you explicitly ask it to.

## Contributing

Issues and pull requests are welcome, especially new Designer or MCP quirks and grammar files for other conventions. Read [AGENTS.md](AGENTS.md) first; it holds the repository rules for people and agents.

## License

Original material is [CC0 1.0 Universal](LICENSE). Webflow, Finsweet, Client-First, Mast, Lumos, and No-Code Supply Co. are the property of their owners. This is an independent project by Armstrong Agency and is not affiliated with Webflow.
