# The AI-Ready Webflow Site Scorecard

Score your Webflow site in 5 minutes, before you point an AI tool at it.

AI builds on whatever your site already has. A site with clear building blocks gets pages that match. A site with a mess gets a bigger mess, faster. This scorecard shows you which one you have.

## How to score

Open your site in the Webflow Designer with whoever knows it best. Rate each of the five categories from 1 to 5, using the descriptions for 1, 3 and 5 as anchors. A 2 or a 4 is fine when you land between two. Add the five numbers for a total out of 25.

---

## 1. Class naming

Open the Style Manager and read the list of class names.

| Score | What it looks like |
|---|---|
| 1 | No system. Classes have names like "Div Block 47" or "new-section-copy-copy," and nobody knows which ones are safe to change. |
| 3 | There is a loose system, and about half the classes follow it. |
| 5 | Every class follows one written naming convention. A new developer could open the project and read the structure. |

**Why AI cares:** an agent copies the naming it finds. With no pattern to copy, it invents a new class for every element it builds.

**Score: ___ / 5**

## 2. CMS structure

Open the CMS panel and look at your collections and their fields.

| Score | What it looks like |
|---|---|
| 1 | Collections overlap or are misused. Content that belongs in the CMS is typed into static pages, and half the fields are empty. |
| 3 | The CMS works, with some unused fields and collections that do the same job. Adding a new content type is awkward. |
| 5 | Each collection has one clear job and plainly named fields. Adding a blog post or a case study takes a marketer a few minutes. |

**Why AI cares:** an agent fills the fields it is given. Vague fields get vague content, and a confusing collection gets items put in the wrong place.

**Score: ___ / 5**

## 3. Component reuse

Open the Components panel, then compare two pages that share a similar section.

| Score | What it looks like |
|---|---|
| 1 | Every section is built from scratch. Sections that look the same are separate copies, so changing one changes nothing else. |
| 3 | The navbar, footer and a few sections are components. Most others are duplicated by hand. |
| 5 | Common sections (heroes, CTAs, feature grids, cards) are components with clear names. Update one and it changes everywhere. |

**Why AI cares:** this is the category that matters most. An agent with a component library assembles pages from approved pieces. An agent without one draws every section fresh, and each one comes out a little different.

**Score: ___ / 5**

## 4. Editing safety

Ask the marketers on your team how they feel about editing the site.

| Score | What it looks like |
|---|---|
| 1 | The team is afraid to touch the site. A text edit sometimes breaks a layout, so every change goes to a developer. |
| 3 | The team makes basic text and image edits. Adding a page or a section still needs a developer. |
| 5 | The team edits content, adds CMS items and launches landing pages from existing sections without help, and reviews changes on a draft page before they go live. |

**Why AI cares:** a site that breaks when a careful person edits it will break when an agent edits it. The review habit is also the one that catches an agent's mistakes.

**Score: ___ / 5**

## 5. Custom code

Check the site settings, the page settings and any embed blocks for custom code.

| Score | What it looks like |
|---|---|
| 1 | Code is scattered across site settings, page settings and embeds. Nobody knows what it all does, and removing any of it feels dangerous. |
| 3 | The code mostly works and nothing is written down. When something breaks, it takes a while to find out why. |
| 5 | There is very little custom code, each piece has a note saying what it does, and there is a backup outside Webflow. |

**Why AI cares:** an agent cannot see what a script does to a page it is editing. Undocumented code is where an AI change breaks something three pages away.

**Score: ___ / 5**

---

## Your total: ___ / 25

| Total | What it means | What I'd do next |
|---|---|---|
| 21 to 25 | **Ready.** Your site has the building blocks AI needs. | Connect the Webflow MCP, add the `AGENTS.md` rules from this kit, and start with one landing page on a draft page. |
| 14 to 20 | **Fix a few things first.** AI will work in the strong categories and make a mess in the weak ones. | Fix your lowest category before AI builds anything new. If components scored lowest, start there. |
| 5 to 13 | **Not yet.** AI will multiply the problems your team already works around. | Restructure the site first. The work pays for itself whether or not you ever use AI, because your team gets a site it can edit. |

---

## Before AI touches the site

Five yes or no questions. These are not part of your score. A "no" on any of them is worth fixing this week, whatever your total is.

1. **Is your AI tool connected to this one site only?** A shared, account-wide Webflow login is how an agent ends up editing the wrong site.
2. **Does the site have a Style Guide page** showing its colors, type, buttons and components? This is the first thing a well-set-up agent reads.
3. **Are your rules written down** in a file the AI reads at the start of every session? The `AGENTS.md` template in this kit is that file.
4. **Does AI build on a draft page first**, never on a live page?
5. **Does a person look at every AI change before it is published?**

---

## Want a second pair of eyes?

If you would like me to run the full audit and set your team up, that is the [AI-Ready Webflow Sprint](https://www.armstrong.so/ai-ready-sprint): two weeks, working directly with me.

Emmett Armstrong, Webflow Premium Enterprise Partner
