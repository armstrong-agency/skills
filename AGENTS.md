# Repository guidance

- Keep every published skill compatible with the open Agent Skills format.
- Keep `SKILL.md` focused on orchestration and route detailed guidance into `references/`.
- This repository is instructions-only. Do not add required scripts, runtimes, or proprietary crawler dependencies.
- Use capability-oriented Webflow MCP instructions. Discover the currently exposed tool and action names instead of assuming one client presents them identically.
- Preserve the distinction between a public source-site audit and authenticated Webflow destination writes.
- Never publish a Webflow site from these skills. Publishing requires a separate, explicit user request.
- Never include private client screenshots, extracted tokens, site IDs, or evaluation artifacts in the public repository.
- Treat persisted Webflow state, visual QA, and publishing as separate checkpoints.
- Original repository material is CC0. Link to third-party documentation rather than copying substantial third-party text.

## Working model

- Use `webflow-build` for how to build: reuse ladder, native styling, completion gates, confirmation checkpoints, and full review loop only when inventing new system decisions.
- Use `framework/client-first` or `framework/mast` for grammar only (class naming, structure, taxonomy).
- Official Webflow skills remain complementary for platform operations (MCP tools, publishing workflows, CMS operations, technical audits).
- Never publish unless the user explicitly requests publication.
