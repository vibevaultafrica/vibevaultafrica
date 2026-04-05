# WEBSITE-FIXES — Targeted bug fixes only

These are emergency fixes for 3 bugs introduced by the previous edit session.
Do NOT rebuild or restructure anything. Open each file, find the specific issue, fix only that.

---

## FIX 1 — Blank / invisible content sections on V1, V2, V3, V4

**Symptom:** After the hero image, all content sections appear blank (dark empty space). The sections exist in the DOM but content is invisible.

**What to do:**
Open v1.html, v2.html, v3.html, v4.html one at a time.

For each file, find every `.topo-overlay` element or SVG element that was added as a topographic overlay. Check its CSS. Fix as follows:

The topo overlay SVG elements must have:
```css
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
z-index: 0;
pointer-events: none;
opacity: 0.08;
```

The PARENT container of each topo overlay must have:
```css
position: relative;
```

All TEXT CONTENT and inner divs inside a section that contains a topo overlay must have:
```css
position: relative;
z-index: 1;
```

Without `z-index: 1` on the text content, the topo SVG (even at z-index 0) can sit on top of content if the content has no z-index set.

**Check also:** If any section has `overflow: hidden` that was not there before — remove it unless it was intentional for a specific image container. `overflow: hidden` on a section with `position: relative` can clip absolutely positioned children.

**Check also:** If the hero section or any section was given `min-height: 100vh` where it did not have it before, this may be creating enormous blank gaps. Restore the original height values.

---

## FIX 2 — Hero image on V2 (The Inevitable) has white gaps on left and right sides

**Symptom:** The hero image on v2.html appears with white/grey borders on each side instead of filling the full width.

**What to do:**
Open v2.html. Find the hero section's background image container. Ensure it has:
```css
background-size: cover;
background-position: center;
background-repeat: no-repeat;
width: 100%;
```

If the image is an `<img>` tag instead of a background-image:
```css
width: 100%;
height: 100%;
object-fit: cover;
object-position: center;
display: block;
```

Also check that the parent container does not have `max-width` set, or that `max-width` is set to `100%` or `none` for the hero section.

Apply the same check to v3.html and v4.html hero images.

---

## FIX 3 — Topographic SVG lines not visible on any page

**Symptom:** The topo overlay SVGs were added but are completely invisible — no lines appear.

**What to do:**
Check that each topo SVG element:
1. Has `opacity` set to at least `0.06` (teal: `0.08`, white ghost: `0.05`, amber: `0.07`)
2. Has `stroke` set to the correct colour (not `transparent` or matching the background)
3. Is actually inside the HTML — not accidentally placed outside the `<body>` tag
4. Has `fill: none` and `stroke-width: 1` (or similar visible value)

The topo SVG for each version should use these stroke colours:
- V1: `#40E0D0` (teal)
- V2: `#ffffff` (white)
- V3: `#40E0D0` (teal)
- V4: `#C8A96E` (amber/gold)

If the SVG paths are there but using `stroke: currentColor` without a color set on the parent, they will inherit the background color and be invisible. Set stroke explicitly on the SVG or `<path>` elements.

---

## After all fixes: commit and push to main

Once all three fixes are made across all pages, commit with message:
"Fix blank sections, image cover, and topo SVG visibility"

Then push to main so the live site updates.

---

## Verification checklist
- [ ] V1: Scroll through entire page — all sections have visible text content
- [ ] V2: Hero image fills full width edge to edge, no gaps
- [ ] V3: Scroll through — all sections visible
- [ ] V4: Scroll through — all sections visible
- [ ] At least one page shows faint topographic contour lines in the hero area
- [ ] No new blank sections introduced
