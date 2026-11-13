# Checking a staged page

Use this once the user has approved a staging publish, when canvas snapshots fail, or when a check needs published output.

## 1. Confirm the build is current

Compare the site's Last Published time with the page's `lastUpdated`, and fetch the page with a cache-busting query (`?v=<timestamp>`). Continue only when the staged build is newer than the last edit.

## 2. Measure and click through

In headless Chrome, with a timeout on every run, load the page at each of the four breakpoints. Scroll each section into view before measuring, since lazy-loaded images report collapsed heights until then. Measure against the acceptance checks, click through every interaction and state, and tab through the keyboard order.

When Figma node data exists, compare numbers before pictures. Dump every staged element's box (x, y from its section's top, width, height) and computed font in one script run, and set that list beside the Figma node positions. Done when each Figma node in scope has a staged counterpart within a few pixels, or a logged gap. Read screenshots only for what numbers cannot show: colour, shape and imagery.

Check in the published HTML what API readback cannot prove, listed under Publishing in [common-issues.md](common-issues.md).

## 3. Test a fix before publishing

To try a markup or script fix without another publish, intercept the page request with the Chrome DevTools Protocol (`Fetch.enable`, then `Fetch.fulfillRequest` with the edited HTML) and re-run step 2 on the swapped page. Then make the fix in Designer, and stage again only with approval.
