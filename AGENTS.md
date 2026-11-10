# Repository guidance

Rules for anyone, human or agent, changing this repository. The skill list is in [README.md](README.md).

## Structure

- Keep skills compatible with the open Agent Skills format (`skills/<name>/SKILL.md`).
- Each skill is one `SKILL.md` plus only the files that skill must ship.
- `wf-build` is the main skill. Grammar files, MCP/Designer quirks and branch-only steps live in `skills/wf-build/references/`, each meaning stated once.
- The Webflow site is the record. Skills read context from it and require no per-site context files.
- Instructions only. No required scripts or crawler dependencies.

## Content

- Discover Webflow MCP tool names in-session. Don't freeze tool names; official Webflow MCP docs cover mechanics.
- Never publish a Webflow site from these skills unless the user explicitly asks.
- Keep workflow out of grammar files. A grammar file describes naming and structure for one convention, and ends with a Docs section linking its style guide and cloneable starter.
- To add a grammar, add `<name>.md` to `references/` and a row to `references/grammars.md`. Within skills, name specific grammars only in those files.
- Link to third-party docs rather than copying substantial third-party text.
- End each harness reference in `wf-mcp-setup` with a dated, sanitized _Tested_ note, so a later edit can tell verified steps from untested ones.

## Adding to `common-issues.md`

Add a bullet only when:

1. The mistake cost real time on a real job.
2. It is about platform, MCP, or Designer behavior, not one site's design system.
3. It fits in one short bullet. Link to official docs when they exist.

## Privacy

This repository is public. Never include client names, screenshots, extracted tokens, site IDs, or evaluation artifacts.

Run `python3 .github/scripts/check.py` before committing. CI runs it on every pull request; it catches ID-shaped strings, local paths, invalid TOML or JSON blocks and broken relative links, but not client names.

## License

Original material is CC0.
