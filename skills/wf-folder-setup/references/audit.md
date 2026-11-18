# Audit an existing working folder

Compare the folder with the standard in [SKILL.md](../SKILL.md) and [agents-template.md](agents-template.md). The audit reads only. Changes come after the user approves them, item by item.

## 1. Read

Read every instruction file, config file and the root listing, and read the site through the working folder's MCP server when it connects. Run these six checks in order:

1. **Secrets:** passwords, API keys or tokens in tracked files. Report the file and line, and leave the value out of the report.
2. **Instruction files:** which exist and whether they agree. The standard is one `AGENTS.md` and a `CLAUDE.md` holding the single line `@AGENTS.md`. Where two real files exist, list what each says that the other lacks.
3. **Missing facts:** the MCP pin, the site ID, the two publishing levels.
4. **Inventories:** page lists, class or variable tables, component IDs and anything else that copies what the site holds. Compare a sample with the live site and say where it has gone stale.
5. **Loose root files:** handoffs, one-off HTML, exports, screenshots. For each, propose a `work/YYYY-MM-<name>/` folder dated from its git history, or `snippets/` when it is custom code that lives in Webflow.
6. **`.gitignore` gaps:** against the list in SKILL.md, plus any tracked machine-specific settings.

Done when every file at the root and every instruction file is accounted for under one of the six checks or named as already meeting the standard.

## 2. Report

Present the findings in the same order, as a numbered list of proposed changes. Each item names the file, the change and the reason. Ask for the two publishing levels and any other missing fact here, as stage 3 of SKILL.md does. Then stop until the user approves items by number.

## 3. Apply

Apply the approved items only. Move tracked files with `git mv` so their history follows them. Merge instruction files into `AGENTS.md` using the template's sections, and show the merged file before replacing either original. A secret needs more than a deletion: tell the user it remains in git history and should be changed at its source.

Commit the reshape on its own, apart from any job in progress.

Done when every approved item is applied, every unapproved item is untouched, and you have listed both for the user.
