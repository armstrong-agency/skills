# Finsweet Attributes: List

Behavior of Finsweet Attributes List (`fs-list-*`) that its docs leave out. The source of truth is the package source at `packages/list/src` in [finsweet/attributes](https://github.com/finsweet/attributes); read it when these notes don't cover a case.

- `fs-list-combine` goes on the receiving list and names the source instance.
- Pagination needs a page count element, or later pages never load.
- `fs-list-load="more"` loads every item up front and reveals them in steps.
- Filters see only loaded items.
- Hooks for custom code: `addHook('start' | 'sort')`, `item.collectFields()`, `list.itemsPerPage` and `list.initialItemsPerPage`.
