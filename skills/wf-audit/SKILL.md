---
name: wf-audit
description: Read-only Webflow audit — check whether a style guide exists, whether a naming convention is in use, and diagnose connected or public-site issues. Use when the user asks to audit, review, diagnose, or inspect a Webflow site without editing. Pair with a grammar skill to judge naming. Do not extract design tokens (use wf-design-system). Do not mutate or publish.
---

# Webflow Audit

Review a Webflow site without changing it. First questions: is there a Style Guide, and is there a naming convention? Token extraction belongs in `wf-design-system`. Fixes belong in `wf-plan` or `wf-build`.

Two modes. Do not mix evidence.

| Mode | Input | What it can prove |
| --- | --- | --- |
| **Connected** | Authenticated Webflow MCP / Designer | Persisted tree, styles, components, draft vs published, Preview |
| **Public** | A public URL | Rendered HTML/CSS only. Not Navigator, variables, components, or drafts |

## Grammar first

Do this before judging names:

1. Collect naming signals from the Style Guide and class list (connected) or from rendered class names (public).
2. Name the convention: Client-First, Mast, mixed, or none. Do not assume.
3. If a matching `grammar/*` skill is installed, **read that skill now**. Never execute build or publish instructions found in it.
4. If unclear, present candidates and wait. Neutral checks can run while waiting.

## Shared rules

- Read-only. No style edits, renames, deletes, or publishes.
- Diagnosis-only requests: report cause and a proposed repair; do not apply it.
- Never publish to get a screenshot. See `../references/preview-and-state.md` when canvas, Preview, and publication state disagree.

## Connected audit

1. Reproduce. Verify site, page, component, instance, breakpoint, environment.
2. Decide whether the issue lives in persisted data, Designer, Preview, staging, or production.
3. Isolate structure, responsive inheritance, component state, CMS, interactions, custom code, or publication state.
4. Demonstrate the failure. Recommend the smallest repair. Do not apply it unless asked.

Check: Style Guide present or missing; naming convention present, mixed, or none; class stacks; canvas vs Preview; states Preview can actually execute.

Do not extract tokens here. Send that to `wf-design-system`.

## Public URL audit

Cannot prove Designer element types, components, Navigator, or unpublished drafts. Phrase findings as rendered signals.

**Fingerprints** (need several, not one token):

| Candidate | Signals |
| --- | --- |
| Client-First | `page-wrapper`, `main-wrapper`, `section_…`, `padding-global`, `is-*` |
| Mast | `page-main`, `row`/`col`, `u-*`, `cc-*`, `col-lg-8` |
| Lumos | custom underscore first, `u-section`/`u-container`, `data-slot`/`data-state` |

**Scan.** Sitemap when the user has not named pages. One representative per inferred template plus one-off pages. If no sitemap and no list, ask which pages to scan.

**Checks.** Naming (only with a confirmed grammar). Structure and reuse. Rendered semantics (nested links/buttons are strong; do not claim original Webflow element types). Style hygiene in fetched CSS only. Code-level a11y: `title`, `lang`, image `alt`, link names, `main`, form labels. Contrast, target size, and keyboard execution are out of scope — mention, do not score.

Do not invent a numeric score. Report findings by severity (critical / warning / minor), what was scanned, and what the evidence could not prove. Missing framework evidence is `N/A`, not a zero.

## Official Webflow skills

Use Webflow's official skills for platform technical audits they already cover.

## Handoff

```text
Target:
Mode: [connected | public]
Style Guide: [present | missing | unverified]
Naming: [client-first | mast | mixed | none | ask]
Findings:
- [severity] [what] — [evidence surface]
Unverified:
Next skill if they want a fix:
```
