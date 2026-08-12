# Designer Preview, runtime, and publication state

Use this workflow when Webflow completion depends on visual evidence, responsive
behavior, custom code, third-party attributes, interactions, or publication
state.

## Evidence surfaces

Treat each surface as a separate claim:

| Surface | What it can prove | What it cannot prove alone |
| --- | --- | --- |
| Persisted Webflow readback | Element tree, styles, variables, attributes, properties, assets, and sibling order | Actual canvas appearance or runtime behavior |
| Designer canvas | Native presentation and editability in the current breakpoint | Runtime custom code and published output |
| Designer Preview | The current Designer state, responsive layout, native interactions, custom code, and third-party behavior when execution is enabled | Persisted-save proof or production deployment state |
| Staging or published URL | The last content delivered to that environment | Unsaved or unpublished Designer changes |

A connected Designer browser or Bridge is useful for canvas-aware inspection
and Preview control. It is not permission to publish, and publication is not a
prerequisite for saved-draft visual QA.

## Visual QA without publication

Use the normal Designer canvas first, then Preview for the relevant behavior
checks. Preview can show the current Designer state without publishing it to a
public environment. Use persisted readback—not Preview alone—to prove that the
intended state was saved.

Never publish merely to obtain a screenshot, inspect responsive layout, or
test a behavior that Preview can execute. If a dependency genuinely requires a
deployed URL, report that limitation and request separate publication authority.

## Custom-code compilation failures

When Preview remains stuck compiling custom code:

1. Confirm the correct site, page, session, and Preview state.
2. Wait only a bounded period and avoid repeated reload loops.
3. It is acceptable to disable custom-code execution temporarily to isolate
   native structure and visual presentation.
4. Record that this proves static visual behavior only.
5. Restore execution when practical before testing runtime behavior.
6. Do not publish as a workaround for a broken Preview compiler.

When code execution is disabled or unavailable, do not report Finsweet
Attributes, custom interactions, active states, scroll offsets, or other
runtime contracts as passed. “Custom code was not changed” is not equivalent
to “custom behavior passed.”

## Third-party attribute contracts

Persisted attributes are necessary but not sufficient evidence. Test the
complete runtime contract in Preview with custom code enabled.

For a table of contents or similar scroll-linked integration, verify:

- source headings and generated or configured links map correctly;
- the active or selected state changes while scrolling in both directions;
- visual active styling matches the approved design;
- click and keyboard activation reach the intended section;
- the requested scroll offset is measured in the rendered page and accounts
  for sticky navigation or other fixed UI;
- history or fragment behavior does not create unexpected jumps;
- desktop and mobile layouts preserve readable order and usable targets.

Keep exact attribute names and offset values in the project brief or current
vendor guidance. Shared skills should require verification without freezing a
site-specific value or a vendor API that may change.

## Persisted and publication evidence

When the platform exposes timestamps or environment metadata:

1. Read the target and publication state before mutation.
2. Read back the intended definition, instance, settings, and order after
   mutation.
3. Read the target and publication state again.
4. Report saved, staged, Webflow subdomain, and production state separately.

`lastUpdated` and `lastPublished` are useful boundary evidence, but timestamps
do not replace target-specific readback.

## Handoff

Use a compact evidence handoff:

- Target:
- Reused:
- Created or changed:
- Persisted readback:
- Designer canvas:
- Preview/runtime:
- Custom code enabled during runtime QA:
- Staging or published:
- Still unverified:
