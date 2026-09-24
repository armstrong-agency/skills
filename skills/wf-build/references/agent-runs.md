# Running a build through a coding agent

Use this when a Webflow build runs as a long-lived agent (a cloud VM or a local worker) instead of an interactive session. Every follow-up re-sends the whole context, so run shape matters more than prompt length.

## Before launch (whoever briefs the agent)
- Resolve IDs first: site, page, section root element, components, design-source nodes. The agent should never have to search for them.
- List what is frozen and must not change, and what the agent is allowed to edit.
- Write acceptance checks as numbers (heights, gaps, widths, contrast) at 1920, 991, 768 and 390.
- Scope: one section per agent, or two if they are small and share components.
- Say whether the agent may publish, and to which target. The default is no publish.

## Brief template
Goal / IDs / Allowed edits / Frozen / Naming grammar file / Acceptance checks / Budget / Publish rule / Report format.

## Turn budget
- Launch turn: build, verify, write HANDOFF.md.
- At most 3 follow-ups. Batch all feedback into each one; never send single fixes one at a time.
- After 3 follow-ups, or once a run passes roughly 150 tool calls, stop. Update HANDOFF.md and continue with a fresh agent seeded from it.

## HANDOFF.md (always kept current)
- An ID map of every element, class and component touched.
- What is verified, with the measurements.
- What is left, and anything blocked by shared components.
- Input shapes that worked for each MCP tool used in this run.

## Reading the site
- Read the page tree once, at the start, scoped to the section root. Record the IDs in HANDOFF.md and don't re-read the whole page.
- Read elements and styles by ID or name. Never list every style or every element on a page.
- Verify with scoped snapshots or screenshots of the section, not whole-page dumps.
- If a read returns more than you need, narrow the query rather than paging through it.

## Tool calls
- Before the first call to any MCP tool in a run, read its input schema. Reuse the shapes recorded in HANDOFF.md.
- If a call fails validation, fix it from the schema. Do not retry with guessed variations. After two failures, record it and move on.
- Put a timeout on every render, screenshot or terminal command (60s by default). Kill a hung command and log it; don't wait on it.
