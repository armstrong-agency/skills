---
name: wf-reference
description: Shared reference for the wf-* Webflow skills — how to identify a site's class-naming convention, Client-First and Mast grammar, and known Webflow MCP/Designer quirks. Load when another wf-* skill asks for it, or when the user asks how to name classes or structure a page in Client-First or Mast.
---

# Webflow Reference

Lookups for the other `wf-*` skills. This skill has no workflow of its own: the skill that loaded it decides what happens next.

## Files

- [client-first.md](client-first.md) — Finsweet Client-First
- [mast.md](mast.md) — No-Code Supply Co. Mast
- [common-issues.md](common-issues.md) — Webflow MCP and Designer quirks

## Identify the convention

Do this before naming, choosing, or judging any class:

1. Inspect the Style Guide, existing classes, and project instructions. On a public site, use the rendered class names.
2. Name the convention: Client-First, Mast, mixed, or none. Do not assume.
3. Read the matching grammar file now. Do not write or pick class names from memory or from a different grammar.
4. If the convention is unclear, say so and wait. Do not pick a grammar because a file for it exists.
5. If the site follows a convention with no file here (Lumos, an in-house system, or none), say so. Follow the site's style guide and existing class names; do not force Client-First or Mast onto it.

**Style guide wins over framework on class names.** If they disagree, follow the style guide and tell the user.

Use the grammar files first. Use the framework's official docs as a secondary source.

## Adding a grammar

Add `<name>.md` here and list it under Files. Keep workflow out of grammar files.
