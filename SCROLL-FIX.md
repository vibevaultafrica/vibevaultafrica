# SCROLL-FIX — Emergency fixes for post-edit breakage

CRITICAL: Do NOT rebuild or restructure. Open each file, diagnose, fix only what is broken.
Read ALL of this file before touching anything.

---

## ROOT CAUSE — WHY PAGES LOOK BLANK

The site uses a scroll reveal animation system:
- Every content section has class `rv` which starts at `opacity: 0; transform: translateY(24px)`
- An IntersectionObserver script adds class `in` to each element as it scrolls into view
- `rv.in` sets `opacity: 1; transform: none` — making content visible
- HERO elements are triggered separately on `DOMContentLoaded` (which is why the hero image shows)
- ALL other sections rely entirely on the IntersectionObserver

If that observer script is broken, missing, duplicated, or interfered with — every section below the hero stays at `opacity: 0` permanently. This is exactly what is happening.

---

## FIX 1 — Restore and verify the IntersectionObserver (applies to ALL pages)

Open v1.html, v2.html, v3.html, v4.html one at a time.

### Step 1a: Find and audit the scroll reveal CSS

In the `<style>` block, verify these rules exist exactly as follows. If they are missing, add them. If they are different, correct them:

```css
.rv { opacity: 0; transform: translateY(24px); transition: opacity 0.65s ease, transform 0.65s ease; }
.rv.in { opacity: 1; transform: none; }
.d1 { transition-delay: 0.08s; }
.d2 { transition-delay: 0.16s; }
.d3 { transition-delay: 0.24s; }
```

### Step 1b: Find and audit the IntersectionObserver script

Near the bottom of each file, before `</body>`, there must be ONE (and only one) IntersectionObserver script. Find it and verify it reads exactly:

```javascript
var io = new IntersectionObserver(function(entries) {
  entries.forEach(function(e) {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, { threshold: 0.08, rootMargin: '0px 0px -28px 0px' });
document.querySelectorAll('.rv').forEach(function(el) { io.observe(el); });
```

If this script is missing — add it.
If it appears more than once — remove duplicates, keep only one.
If there is a JavaScript syntax error near it — fix it.

### Step 1c: Find and audit the hero DOMContentLoaded script

Also near the bottom of each file, verify this exists:

```javascript
window.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.hero .rv').forEach(function(el, i) {
    setTimeout(function() { el.classList.add('in'); }, 100 + i * 120);
  });
});
```

### Step 1d: Add a safety fallback

Immediately after the IntersectionObserver script, add this failsafe — it forces ALL rv elements visible after 800ms in case the observer fails:

```javascript
setTimeout(function() {
  document.querySelectorAll('.rv').forEach(function(el) { el.classList.add('in'); });
}, 800);
```

### Step 1e: Check for overflow:hidden on section containers

If any wrapper divs were added around sections for the topographic overlay (e.g. with `position: relative; overflow: hidden`), check whether those wrappers contain elements with the `rv` class.

If a wrapper has `overflow: hidden` AND contains child elements with `rv`, the IntersectionObserver may not detect visibility correctly in all browsers. Fix by either:
- Moving `overflow: hidden` to a specific inner image container (not the whole section wrapper), or
- Removing `overflow: hidden` from section wrappers entirely — use `overflow: visible` instead

---

## FIX 2 — Topographic SVG overlay z-index (applies to ALL pages)

Any topographic SVG overlay element must:
1. Have `position: absolute; top: 0; left: 0; width: 100%; height: 100%`
2. Have `z-index: 0; pointer-events: none`
3. Be inside a parent container with `position: relative`

All actual text content and inner divs inside sections that contain a topo overlay must have:
```css
position: relative;
z-index: 1;
```

Topo overlay stroke colours per version:
- V1: `stroke="#40E0D0"` opacity `0.08`
- V2: `stroke="#ffffff"` opacity `0.05`
- V3: `stroke="#40E0D0"` opacity `0.08`
- V4: `stroke="#C8A96E"` opacity `0.07`

Each SVG must also have `fill="none"` and visible `stroke-width` (e.g. `0.5` or `1`).

---

## FIX 3 — V2 hero image not filling full width

Open v2.html. Find the hero section background image container. Apply:

```css
background-size: cover;
background-position: center;
background-repeat: no-repeat;
width: 100%;
```

If the image is an `<img>` tag:
```css
width: 100%;
height: 100%;
object-fit: cover;
object-position: center;
display: block;
```

Check that no `max-width` or `margin: auto` is constraining the container to less than full width. Apply the same check to v3.html and v4.html hero images.

---

## FIX 4 — Sanity check: verify nothing else was accidentally changed

After fixing the above, do a quick check on each file:

1. Brand colours are still correct: primary teal `#40E0D0`, deep navy `#0D1B2A`, near-black `#080E18`
2. Font stack is still: `-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', system-ui, sans-serif`
3. No Google Fonts or external font CDNs were introduced
4. Contact details still correct: `dasha@vibevaultafrica.co.za` / `+27 73 012 9314`
5. Language switcher script still present and working
6. `translations.js` still referenced in the `<head>` of each page

---

## After all fixes: commit and push DIRECTLY to main — no PR

```
git add v1.html v2.html v3.html v4.html
git commit -m "Fix scroll reveal, z-index, and image cover"
git push origin main
```

Do NOT create a branch. Do NOT create a PR. Push straight to main.

---

## Verification checklist
- [ ] V1: Scroll down — all content sections animate in and are fully visible
- [ ] V2: Hero image fills full width edge to edge, no gaps. Content visible on scroll
- [ ] V3: All content sections visible on scroll
- [ ] V4: All content sections visible on scroll
- [ ] All pages: Faint topographic contour lines visible in hero areas
- [ ] All pages: Language switcher still works
- [ ] No blank dark sections anywhere on any page
