# Review the built page

Follow this when every section in the brief exists on the page. Review runs twice, one section at a time: you first, then the user.

## 1. Agent review

Review each section in order against the brief and its design source, fix what fails, and re-check until it passes. Dispatch a reviewer subagent per section when the harness allows, so the read is fresh. Give it the brief, the section's design source and the page, and fix what it finds. When canvas snapshots fail or a check needs published output, follow [staging-check.md](staging-check.md).

A section passes when:

- **Complete:** every element, state and interaction in its design source exists, and nothing outside the brief was added.
- **Faithful:** Canvas and Preview match the acceptance checks at the four breakpoints, from Figma node data where it exists.
- **Working:** states, interactions and keyboard order behave where they exist.
- **Persisted:** readback matches the intended structure.

Done when every section passes, or each remaining gap is logged with the reason it cannot close.

## 2. Human review

Present each section in order at desktop and mobile, with its agent-review result and any logged gaps, and stop until the user approves it. Apply requested changes and re-run the agent review on that section before presenting it again.

After approval:

- Suggest converting the section to a component if it is not one, named and described per [components.md](components.md).
- When the section introduced a reusable piece, such as a variable, utility or base class meant for other sections, propose adding it to the Style Guide. Classes that belong to one section stay on that section.

Approval covers the sandbox page only. Overwriting page content and moving work onto a real page each need their own explicit yes. Publishing follows the publishing levels in the project's `AGENTS.md`, and where it has none, each publish needs its own explicit yes.

Done when the user has approved every section.
