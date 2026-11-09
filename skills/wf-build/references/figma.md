# Reading a Figma source

Figma MCP calls are a budget: a section-level `get_metadata` can run to about 800k characters, and the plan's call limit can run out mid-job. Spend calls only on what an export cannot prove.

## 1. Ask for exports first

Before the first Figma call, ask the user for exports of the frames in scope, saved to a folder you can read:

- **One page or a few sections:** each section's frame as PNG at 1x, one per breakpoint the design covers.
- **The whole file:** File → Export frames to PDF, or select every top-level frame and export them as PNG at 1x in one batch.
- **Notes:** any developer notes or interaction notes, pasted as text, since exports drop annotations.

A 1x export has known scale, so it needs no calibration. Exports prove layout, order, imagery and visual hierarchy.

## 2. Read node data one section at a time

Call `get_design_context` once per section, scoped to that section's node, and read every annotation in it (`data-annotations` and `data-interaction-annotations`). Developer notes appear only there, not in `get_metadata` or image exports. Take from it what exports cannot prove: exact measurements, text styles, variables and the notes.

Search large dumps that spill to a file by layer name instead of reading them whole.

## 3. When Figma runs out

When access is gone or the call limit is close, stop calling and ask the user for the remaining exports and notes. Mark values taken from a raster as approximate in the brief.
