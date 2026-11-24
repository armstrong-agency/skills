---
name: wf-scorecard
description: Score a Webflow site out of 25 for how ready it is for AI agents to build on, with evidence read from the site over the MCP. Use when the user asks whether their Webflow site is ready for AI, wants a site audit or scorecard, or before the first build on an unfamiliar site.
---

# Webflow site scorecard

An agent builds on whatever a site already has. A site with clear building blocks gets pages that match, and a site with a mess gets a bigger mess, faster. The **scorecard** rates five categories from 1 to 5, for a total out of 25, so the user knows which one they have before an agent builds anything.

This skill reads the site and changes nothing: no elements, no styles, no CMS items, no publishing.

## 1. Check context

Done when you can state:

- **Connection:** the MCP reaches the intended workspace, using the tool names this session exposes. If it is missing, run `wf-mcp-setup`.
- **Target:** the site, confirmed by the user from the name and ID you read back.

## 2. Read the site

Collect evidence for each category before scoring any of them. Sample when the site is large, and say what you sampled.

- **Class naming:** the style list. Look for one naming convention, auto-generated names such as "Div Block 47", and copies such as "-copy".
- **CMS structure:** the collections and their fields. Look for collections that overlap, empty or unused fields, and vague field names.
- **Component reuse:** the component list and two or three pages that share a similar section. Look for whether common sections are components with clear names, or copies built by hand.
- **Custom code:** the site and page head and footer code, registered scripts, and embeds on the sampled pages. Look for how much there is, whether each piece says what it does, and whether a backup exists outside Webflow.

**Editing safety** cannot be read from the site. Ask the user one question: how do the marketers on the team feel about editing the site, and what still goes to a developer?

Done when every category has evidence, or a stated reason it could not be read.

## 3. Score

Rate each category from 1 to 5 against these anchors. Use 2 or 4 when the evidence lands between two.

| Category | 1 | 3 | 5 |
| --- | --- | --- | --- |
| Class naming | No system, and nobody knows which classes are safe to change. | A loose system that about half the classes follow. | Every class follows one written convention. |
| CMS structure | Collections overlap or are misused, and content that belongs in the CMS is typed into static pages. | The CMS works, with unused fields and collections that do the same job. | Each collection has one clear job and plainly named fields. |
| Component reuse | Every section is built from scratch, and lookalike sections are separate copies. | The navbar, footer and a few sections are components. Most others are duplicated by hand. | Common sections are components with clear names. |
| Editing safety | The team is afraid to touch the site, and every change goes to a developer. | The team makes text and image edits. A new page or section still needs a developer. | The team adds CMS items and launches pages from existing sections, and reviews changes on a draft page before they go live. |
| Custom code | Code is scattered, nobody knows what it all does, and removing any of it feels dangerous. | The code mostly works and nothing is written down. | There is very little custom code, each piece has a note, and there is a backup outside Webflow. |

Component reuse matters most: an agent with a component library assembles pages from approved pieces, and an agent without one draws every section fresh.

## 4. Check the setup

Answer five yes or no questions. They are not part of the score.

1. Is the agent connected to this one site only, through a project-scoped server?
2. Does the site have a Style Guide page showing its colors, type, buttons and components?
3. Are the site's rules written down where an agent reads them at the start of every session?
4. Does the agent build on a draft page first, never on a live page?
5. Does a person look at every change before it is published?

Ask the user for any you cannot verify.

## 5. Report

Lead with the total and what it means:

| Total | Meaning | Next step |
| --- | --- | --- |
| 21 to 25 | Ready. | Run `wf-folder-setup`, then build one page on a draft page with `wf-build`. |
| 14 to 20 | Fix a few things first. | Fix the lowest category before an agent builds anything new. Start with components when they score lowest. |
| 5 to 13 | Not yet. | Restructure the site first. An agent will multiply the problems the team already works around. |

Then give, in this order:

1. Each category's score with the evidence behind it, naming real classes, collections, components or scripts from the site.
2. The five setup answers, with the fix for each "no".
3. The three changes that would raise the score most.
4. Anything you could not read, and what you sampled.

Label a score as a guess when the evidence for it was thin.
