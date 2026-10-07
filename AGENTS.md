# Repository guidance

Rules for anyone, human or agent, changing this repository. The skill list is in [README.md](README.md).

## Structure

- Keep skills compatible with the open Agent Skills format (`skills/<name>/SKILL.md`).
- Each skill is one `SKILL.md` plus only the files that skill must ship.
- Shared material (framework grammar, MCP/Designer quirks) lives once, in `wf-reference`. Never copy it into another skill. Skills that need it load `wf-reference` and stop with the install command if it is missing.
- First step of any skill that names classes: load `wf-reference` and follow its convention check.
- Instructions only. No required scripts or crawler dependencies.

## Content

- Discover Webflow MCP tool names in-session. Don't freeze tool names; official Webflow MCP docs cover mechanics.
- Never publish a Webflow site from these skills unless the user explicitly asks.
- Keep workflow out of grammar files. A grammar file describes naming and structure for one convention.
- Link to third-party docs rather than copying substantial third-party text.

## Adding to `common-issues.md`

Add a bullet only when:

1. The mistake cost real time on a real job.
2. It is about platform, MCP, or Designer behavior, not one site's design system.
3. It fits in one short bullet. Link to official docs when they exist.

## Privacy

This repository is public. Never include client names, screenshots, extracted tokens, site IDs, or evaluation artifacts.

## License

Original material is CC0.
