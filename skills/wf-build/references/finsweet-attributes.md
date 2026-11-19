# Finsweet Attributes

[Finsweet Attributes](https://finsweet.com/attributes) adds behavior to native Webflow elements through custom attributes and one script. Reach for it when a section needs something Webflow cannot do natively:

- **Lists:** filtering, sorting, load more, infinite scroll or pagination that keeps filters, combining several Collection Lists into one, and nesting past Webflow's limits.
- **CMS into native elements:** a Slider, Tabs or a select field filled from a Collection List.
- **Forms and UI:** custom selects, range sliders, input counters, accessible modals and accordions, a table of contents, copy to clipboard and social share.

Propose it in the brief, naming the solution and the behavior it adds, because it loads a script on the site. Read that solution's page on the Finsweet site before building, and use the current version: v1 is discontinued.

## List

Behavior of Attributes List (`fs-list-*`) that its docs leave out. The source of truth is the package source at `packages/list/src` in [finsweet/attributes](https://github.com/finsweet/attributes); read it when these notes don't cover a case.

- `fs-list-combine` goes on the receiving list and names the source instance.
- Pagination needs a page count element, or later pages never load.
- `fs-list-load="more"` loads every item up front and reveals them in steps.
- Filters see only loaded items.
- Hooks for custom code: `addHook('start' | 'sort')`, `item.collectFields()`, `list.itemsPerPage` and `list.initialItemsPerPage`.
