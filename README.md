# Webflow agent skills

Agent skills for building Webflow sites with an AI coding agent over the [Webflow MCP server](https://developers.webflow.com/mcp). They encode the judgment a careful Webflow developer applies: reuse the existing system before inventing, style only through native Designer controls, follow the site's naming convention, prototype on a draft page, and never publish without being asked.

They complement [Webflow's official skills](https://github.com/webflow/webflow-skills), which cover platform operations such as MCP tool mechanics, publishing, and CMS.

The skills use the open [Agent Skills](https://agentskills.io) format, so they work in any agent that supports it.

## Install

```bash
npx skills add armstrong-agency/skills
```

You also need the Webflow MCP server connected to your project. `wf-mcp-setup` walks your agent through it.

## Skills

| Skill | What it does | Writes to Webflow |
| --- | --- | --- |
| `wf-mcp-setup` | Connects a project-scoped Webflow MCP server, so each project stays pinned to its own workspace. | No |
| `wf-build` | Takes a job from context check to reviewed sections: agrees a brief, builds one section at a time on a sandbox page, tunes interactions, and sets up a Style Guide when the site has none. Grammar files for [Client-First](https://finsweet.com/client-first/docs/intro) and [Mast](https://www.nocodesupply.co/mast/docs) ship inside it. | Yes, after review |

## Workflow

`wf-build` reads the site, agrees a brief with you, and stops for your review of each section. The Webflow site is the record: nothing depends on a separate context file, and no new class is created until you approve it.

No skill publishes a site unless you explicitly ask it to.

## Contributing

Issues and pull requests are welcome, especially new Designer or MCP quirks and grammar files for other conventions. Read [AGENTS.md](AGENTS.md) first; it holds the repository rules for people and agents.

## License

Original material is [CC0 1.0 Universal](LICENSE). Webflow, Finsweet, Client-First, Mast, Lumos, and No-Code Supply Co. are the property of their owners. This is an independent project by Armstrong Agency and is not affiliated with Webflow.
