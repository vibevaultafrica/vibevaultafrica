# WEBSITE-EDITS.md — VibeVault Africa
# Claude Code reads this file alongside CLAUDE.md.
# These are targeted edits to the LIVE site. Do NOT rebuild from scratch.
# Repo: github.com/vibevaultafrica/vibevaultafrica
# Live: vibevaultafrica.co.za

---

## BEFORE YOU START

Read every section of this file before touching a single file.
Work through edits in the order listed. Each section is self-contained.
After completing all edits, run through the VERIFICATION CHECKLIST at the bottom.

---

## IMAGES — MANUAL STEP REQUIRED BEFORE EDITING HTML

The following images must be placed in the `images/` folder of the repo by the user
before Claude Code references them. Do NOT proceed with image edits until confirmed.

Expected filenames in `images/`:
- `IMG_5158.JPG` → replaces V4 hero background
- `IMG_5163.JPG` → replaces V3 hero background
- `IMG_5179.JPG` → replaces V2 hero background
- `IMG_5153.JPG` → replaces V2 "The Tension" section image

---

## EDIT 1 — "FIND YOUR VIBEVAULT" BUTTON (V1, V3, V4)

### What exists already
V2 already has a "← Find your VibeVault" link near the top that returns users to index.html.
Replicate this exact button on V1, V3, and V4 — at BOTH the top (below nav) AND the bottom
(above the footer) of each page.

### Behaviour
- Links to: `index.html`
- This reloads the entry game from Screen 1 (language selection)
- Do NOT use `href="#"` — use `href="index.html"` explicitly

### HTML structure (match V2's existing implementation exactly)
```html
<a href="index.html" class="back-game" data-i18n="fyv">← Find your VibeVault</a>
```

### Styling
Match V2's existing `.back-game` style. If that class doesn't exist in V2, use:
```css
.back-game {
  display: inline-block;
  color: rgba(255,255,255,0.62);
  text-decoration: none;
  font-size: 0.875rem;
  letter-spacing: 0.02em;
  padding: 0.5rem 0;
  transition: color 0.2s ease;
}
.back-game:hover { color: #40E0D0; }
```

### Translation key to ADD to translations.js
Add `fyv` key to the `shared` object (or per-version if shared doesn't exist) in every
language in translations.js. Also add `fyv` to the embedded translations object in index.html.

Full translations for `fyv` across all 26 languages:

```javascript
// Add to VV_WEB[lang].shared (or at page level) in translations.js
// AND add to T[lang] in index.html if the back button appears on index.html screens

en:  { fyv: '← Find your VibeVault' },
af:  { fyv: '← Vind jou VibeVault' },
zu:  { fyv: '← Thola i-VibeVault yakho' },
xh:  { fyv: '← Fumana i-VibeVault yakho' },
st:  { fyv: '← Fumana VibeVault ya hao' },
tn:  { fyv: '← Bona VibeVault ya gago' },
ve:  { fyv: '← Wana VibeVault yaṋu' },       // ⚠️ Verify with native speaker
de:  { fyv: '← Finde dein VibeVault' },
'de-CH': { fyv: '← Finde dein VibeVault' },
fr:  { fyv: '← Trouvez votre VibeVault' },
es:  { fyv: '← Encuentra tu VibeVault' },
pt:  { fyv: '← Encontre o seu VibeVault' },
it:  { fyv: '← Trova il tuo VibeVault' },
nl:  { fyv: '← Vind jouw VibeVault' },
sv:  { fyv: '← Hitta ditt VibeVault' },
el:  { fyv: '← Βρείτε το VibeVault σας' },
ru:  { fyv: '← Найдите ваш VibeVault' },
ar:  { fyv: 'ابحث عن VibeVault الخاص بك ←' },   // RTL — arrow on right
ur:  { fyv: 'اپنا VibeVault تلاش کریں ←' },      // RTL — arrow on right
zh:  { fyv: '← 找到你的 VibeVault' },
'zh-TW': { fyv: '← 找到你的 VibeVault' },
yue: { fyv: '← 搵返你嘅 VibeVault' },
ja:  { fyv: '← あなたの VibeVault を見つける' },
ko:  { fyv: '← 나의 VibeVault 찾기' },
sw:  { fyv: '← Pata VibeVault yako' },
yo:  { fyv: '← Wa VibeVault rẹ' },              // ⚠️ Verify with native speaker
```

For RTL languages (ar, ur): ensure the arrow displays on the correct side using CSS
`direction: rtl` context inherited from the `<html dir="rtl">` attribute.

---

## EDIT 2 — V1: WHITE TEXT FOR EMAIL AND PHONE IN GET IN TOUCH SECTION

In `v1.html`, find the "Get In Touch" section.
The email address `dasha@vibevaultafrica.co.za` and phone number `+27 73 012 9314`
must have explicit white text colour.

Find these elements and add/update their style:
```css
color: #FFFFFF;
```

If they are inside an `<a>` tag (anchor/link), apply to the anchor:
```css
a[href^="mailto"], a[href^="tel"] {
  color: #FFFFFF !important;
  text-decoration: none;
}
a[href^="mailto"]:hover, a[href^="tel"]:hover {
  color: #40E0D0;
  text-decoration: underline;
}
```

Apply this scoped to the Get In Touch section only (e.g., `.contact a` or `#contact a`)
to avoid affecting other anchor colours across the page.

---

## EDIT 3 — V1: RENAME "GET VIBEVAULT" BUTTON

In `v1.html`, find the button or CTA that currently reads "Get VibeVault".
Replace the text with: **"Register your interest"**

This implies nothing transactional — it positions VibeVault honestly as a project
in development that welcomes people into its orbit.

Add/update the translation key `cta_v1` in translations.js for all 26 languages:

```javascript
en:  'Register your interest',
af:  'Registreer jou belangstelling',
zu:  'Bhalisa intshisekelo yakho',           // ⚠️ Verify with native speaker
xh:  'Bhalisela umdla wakho',                // ⚠️ Verify with native speaker
st:  'Ngodisa kgahlehelo ya hao',            // ⚠️ Verify with native speaker
tn:  'Rejistara kgatlhego ya gago',          // ⚠️ Verify with native speaker
ve:  'Ṅwalisa vhuṱoḓea haṋu',               // ⚠️ Verify with native speaker
de:  'Interesse anmelden',
'de-CH': 'Interesse anmelden',
fr:  'Enregistrer votre intérêt',
es:  'Registra tu interés',
pt:  'Registar o seu interesse',
it:  'Registra il tuo interesse',
nl:  'Registreer je interesse',
sv:  'Registrera ditt intresse',
el:  'Δηλώστε το ενδιαφέρον σας',
ru:  'Зарегистрировать интерес',
ar:  'سجّل اهتمامك',
ur:  'اپنی دلچسپی درج کریں',
zh:  '登记您的兴趣',
'zh-TW': '登記您的興趣',
yue: '登記你嘅興趣',
ja:  '興味を登録する',
ko:  '관심 등록하기',
sw:  'Sajili nia yako',
yo:  'Forúkọ ìfẹ́ rẹ',                      // ⚠️ Verify with native speaker
```

Add `data-i18n="cta_v1"` to the button element so it updates with language selection.

---

## EDIT 4 — V2 AND V3: ADD "INFRASTRUCTURE CASE" LINK BUTTON

Both V2 (v2.html) and V3 (v3.html) need a link button in their Connect/bottom section
that matches the one already present in V1.

### Button text and link
```html
<a href="v4.html" class="infra-link" data-i18n="infra_cta">
  Looking to invest or partner? See the infrastructure case →
</a>
```

### Placement
At the bottom of the page, inside the Connect section, ABOVE the form/contact area —
same position and styling as the equivalent button in v1.html.

### Styling — match V1's version exactly
If V1 uses a specific class for this link, replicate the same class in V2 and V3.
If no dedicated class exists, use:
```css
.infra-link {
  display: inline-block;
  color: rgba(255,255,255,0.72);
  border: 1px solid rgba(255,255,255,0.24);
  border-radius: 4px;
  padding: 0.75rem 1.25rem;
  font-size: 0.9rem;
  text-decoration: none;
  letter-spacing: 0.015em;
  transition: color 0.2s ease, border-color 0.2s ease;
  margin-top: 1.5rem;
}
.infra-link:hover {
  color: #40E0D0;
  border-color: #40E0D0;
}
```

### Translation key `infra_cta` — add to translations.js
```javascript
en:  'Looking to invest or partner? See the infrastructure case →',
af:  'Wil jy belê of vennoot? Sien die infrastruktuurssaak →',
zu:  'Ufuna ukutshala izimali noma ukuba mlingani? Bona icala lengqalasizinda →',  // ⚠️ Verify
xh:  'Ufuna ukutshala imali okanye ukuba njengomlingane? Bona ityala lengqalasizinda →', // ⚠️ Verify
st:  'Na o batla ho peela tjhelete kapa ho ba setho? Bona nyewe ya meralo →',     // ⚠️ Verify
tn:  'A o batla go tshala madi kana go nna motlhankedi? Bona nyewe ya meraka →',  // ⚠️ Verify
ve:  'Ni toda u ita peḽe kana vhushaka? Vhona nyito ya meralo →',                // ⚠️ Verify
de:  'Investieren oder Partner werden? Zur Infrastruktur-Analyse →',
'de-CH': 'Investieren oder Partner werden? Zur Infrastruktur-Analyse →',
fr:  'Investir ou devenir partenaire? Voir le dossier infrastructure →',
es:  '¿Invertir o asociarse? Ver el caso de infraestructura →',
pt:  'Investir ou tornar-se parceiro? Ver o caso de infraestrutura →',
it:  'Investire o diventare partner? Vedi il caso infrastrutturale →',
nl:  'Investeren of partner worden? Bekijk het infrastructuurrapport →',
sv:  'Investera eller bli partner? Se infrastrukturanalysen →',
el:  'Θέλετε να επενδύσετε ή να συνεργαστείτε; Δείτε την υποδομή →',
ru:  'Инвестировать или стать партнёром? Изучить инфраструктурный кейс →',
ar:  'هل تريد الاستثمار أو الشراكة؟ اطّلع على قضية البنية التحتية ←',   // RTL
ur:  'سرمایہ کاری یا شراکت داری؟ انفراسٹرکچر کیس دیکھیں ←',               // RTL
zh:  '想投资或合作？了解基础设施案例 →',
'zh-TW': '想投資或合作？了解基礎設施案例 →',
yue: '想投資或合作？了解基礎設施案例 →',
ja:  '投資またはパートナーシップをお考えですか？インフラケースを見る →',
ko:  '투자 또는 파트너십에 관심 있으신가요? 인프라 케이스 보기 →',
sw:  'Taka kuwekeza au kushirikiana? Angalia kesi ya miundombinu →',
yo:  'Fẹ́ lati fòwó kọlé tàbí ṣe àjọṣepọ̀? Wo ọ̀ràn amayederun →',        // ⚠️ Verify
```

---

## EDIT 5 — IMAGE REPLACEMENTS

IMPORTANT: All hero image containers MUST use `background-size: cover;
background-position: center center; background-repeat: no-repeat;` with NO gaps.
If any `<img>` tag is used instead of background-image, switch it to:
```css
img { width: 100%; height: 100%; object-fit: cover; object-position: center; display: block; }
```
The screenshot provided shows the current issue: images have visible borders where they
cut into the dark background. This must not exist on any image across any page.
All hero containers should also have a subtle dark overlay for text legibility:
```css
.hero::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    rgba(8,14,24,0.45) 0%,
    rgba(8,14,24,0.15) 40%,
    rgba(8,14,24,0.55) 100%
  );
  pointer-events: none;
}
```

### 5a — V4 hero background
File: `v4.html`
Replace current hero background image with: `images/IMG_5158.JPG`
This is the row of solar-canopied locker banks at a fiery orange-red sunset, sea visible.
CSS: `background-image: url('images/IMG_5158.JPG'); background-size: cover; background-position: center;`

### 5b — V3 hero background
File: `v3.html`
Replace current hero background image with: `images/IMG_5163.JPG`
This is the teal locker bank with glowing circular seating area at dusk.
CSS: `background-image: url('images/IMG_5163.JPG'); background-size: cover; background-position: center;`

### 5c — V2 hero background
File: `v2.html`
Replace current hero background image with: `images/IMG_5179.JPG`
This is the teal illuminated circular pod unit at blue-hour dusk by the sea.
CSS: `background-image: url('images/IMG_5179.JPG'); background-size: cover; background-position: center top;`
Use `background-position: center top` to keep the pod structure in frame.

### 5d — V2 "The Tension" section image
File: `v2.html`
Find the section that contains the text "The Tension" (eyebrow or heading).
Replace its associated image with: `images/IMG_5153.JPG`

Image description: A hand holds a smartphone displaying the VibeVault subscription app
(showing Premium R299/month, Lower Tier R50/month, Student Discount R40/month tiers).
In the background, a glowing teal VibeVault pod stands illuminated at night. The image
shows both the digital interface and the physical pod in a single frame — ideal for
illustrating the seamless connection between the app and the infrastructure.

Placement: This image works best displayed as a contained image (not a full-bleed
background) — approximately 50% width on desktop, full width on mobile, with rounded
corners (`border-radius: 12px`) and a subtle glow shadow:
```css
box-shadow: 0 0 40px rgba(64,224,208,0.15);
border-radius: 12px;
overflow: hidden;
```
Apply `object-fit: cover; object-position: center;` and ensure no border gaps.

### Audit ALL other images across all pages
After the above replacements, audit every other image on every page (v1, v2, v3, v4, brief):
- Any `<img>` must have `object-fit: cover; width: 100%; height: 100%; display: block;`
- Any background-image must have `background-size: cover; background-position: center;`
- No image should have a visible border against the dark page background
- Each image container should have `overflow: hidden` and `position: relative`

---

## EDIT 6 — TOPOGRAPHIC LINEWORK ACROSS ALL PAGES

The entry page (index.html) already has SVG topo contour lines. Extend this design
element throughout v1.html, v2.html, v3.html, and v4.html.

### Shared SVG pattern
Create a reusable topo SVG function. Add the following to each page (or to a shared
CSS/JS include). The lines should be organic, irregular closed loops — NOT perfect circles
or grids. Reference the index.html implementation for the existing style.

```css
/* Topo overlay — applies to all pages */
.topo-overlay {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  pointer-events: none;
  overflow: hidden;
  z-index: 0;
}
.topo-overlay svg {
  width: 100%; height: 100%;
  opacity: 1;
}
```

### Placement per page

**V1 (Your Vault)** — warm, human, present
- Place one topo overlay in the hero section background (behind text, before image overlay)
- Place one in the transition zone between the "features/pillars" section and the
  "Get In Touch" section
- Line colour: `rgba(64,224,208,0.05)` to `rgba(64,224,208,0.10)` (slight teal warmth)

**V2 (The Inevitable)** — elegant, seamless, invisible
- Place topo overlays in the hero AND across the full page as a very subtle page-wide
  background layer (this fits perfectly — it IS the invisible infrastructure metaphor)
- Line colour: `rgba(255,255,255,0.03)` to `rgba(255,255,255,0.08)` (pure white, ghostlike)
- V2 should feel like topo lines are woven INTO the page, not placed on top

**V3 (The Explorer)** — open, free, for everyone
- Place at the hero section and at the transition into the "Who we're for" persona section
- Line colour: `rgba(64,224,208,0.06)` to `rgba(64,224,208,0.12)` (more visible, energetic)

**V4 (Infrastructure Case)** — institutional, investment-grade
- Place at the hero section (subtle) and at the statistics/credentials strip section
- Line colour: `rgba(201,168,76,0.04)` to `rgba(201,168,76,0.09)` (amber tones, V4 accent colour)

### SVG pattern to use (adapt from index.html, or generate a new variant)
Each topo overlay should have 6–9 nested irregular closed paths. Vary the shapes per page
so they don't look identical. Use the same core approach as index.html:
- Nested loops getting slightly smaller toward the centre
- Irregular, organic curves — think topographic map, not UI circles
- Stroke width: 0.8–1.2px
- No fill, stroke only
- Paths should be roughly centred in the container but offset organically

---

## EDIT 7 — DISCLAIMER COPY (add near the bottom of each page, above the footer)

Add a disclaimer section to V1, V2, V3, V4, and brief.html.
Use the class `.vv-disclaimer` for consistent styling.

### Styling
```css
.vv-disclaimer {
  border-top: 1px solid rgba(255,255,255,0.08);
  padding: 2rem 1.5rem;
  max-width: 780px;
  margin: 0 auto;
  text-align: center;
}
.vv-disclaimer p {
  font-size: 0.78rem;
  line-height: 1.65;
  color: rgba(255,255,255,0.38);
  letter-spacing: 0.01em;
}
/* V4 amber accent for disclaimer */
.v4-page .vv-disclaimer {
  border-top-color: rgba(201,168,76,0.15);
}
/* brief.html print styles */
@media print {
  .vv-disclaimer { color: #555; border-top-color: #ccc; }
}
```

### Disclaimer text per version

**V1 — Your Vault** (`data-i18n="disclaimer_v1"`)
```
All imagery is AI-generated for concept purposes. VibeVault is currently in development —
locations, features and partnerships shown represent the vision, not confirmed reality.
If something here resonates with you, your interest might be exactly what helps make it real.
```

**V2 — The Inevitable** (`data-i18n="disclaimer_v2"`)
```
All imagery is AI-generated for illustrative purposes. Deployment locations, integrations
and partnerships shown are part of the intended model and have not been confirmed.
VibeVault is in development. Belief in what a city could be is how it gets built.
```

**V3 — The Explorer** (`data-i18n="disclaimer_v3"`)
```
All imagery is AI-generated for illustrative purposes. Locations, services and features shown
represent the vision for VibeVault — none are yet confirmed. We are actively building.
Your curiosity, support or connection could be part of what brings this to life.
```

**V4 — Infrastructure Case** (`data-i18n="disclaimer_v4"`)
```
All renderings and imagery are AI-generated concept illustrations. Projected deployment
locations, referenced partnerships and financial projections are indicative only and do not
constitute confirmed agreements or guaranteed outcomes. VibeVault Africa (PTY) Ltd is an
early-stage company currently in pre-seed development. This page does not constitute a
formal investment offering. Investment partnerships, city co-operation agreements and
crowdfunding interest are actively welcomed.
```

**brief.html** — add at the very end, before `</body>`, styled for print:
```html
<div class="vv-disclaimer brief-disclaimer">
  <p>
    This document is for informational purposes only and does not constitute a formal
    financial offering or investment advice. All imagery is AI-generated concept illustration.
    Projected figures, locations and partnerships are indicative only and subject to change
    without notice. VibeVault Africa (PTY) Ltd (Enterprise No. 2025/958585/07) is an
    early-stage company in pre-seed development. The company is actively seeking its first
    investment partners, city co-operation agreements and crowdfunding supporters to bring
    the first VibeVault pod to market.
  </p>
</div>
```

### Translation
Add `disclaimer_v1`, `disclaimer_v2`, `disclaimer_v3`, `disclaimer_v4` to translations.js.
Translate each accurately into all 26 languages. The tone for V1–V3 should be warm and
honest; V4 should read as formal but accessible.

For the brief, disclaimer stays in English only (it is a formal legal/investor document).

---

## EDIT 8 — SEO: SEARCH ENGINE VISIBILITY

Add to the `<head>` of EVERY page (index.html, v1.html, v2.html, v3.html, v4.html, brief.html).

### Meta tags (per page)

**index.html**
```html
<meta name="description" content="VibeVault Africa — Cape Town's smart urban pod network. Secure storage, phone charging, emergency assistance and safe rides, available across Cape Town's most vibrant locations.">
<meta name="keywords" content="VibeVault Africa, Cape Town safety, urban pods, secure storage Cape Town, phone charging Cape Town, safe city infrastructure, nightlife safety Cape Town, Cape Town tourism, V&A Waterfront">
<meta name="robots" content="index, follow">
<meta property="og:title" content="VibeVault Africa — Find Your VibeVault">
<meta property="og:description" content="A city where going out is just going out. VibeVault pods across Cape Town — storage, charge, rides, care.">
<meta property="og:image" content="https://vibevaultafrica.co.za/images/hero-pod.jpg">
<meta property="og:url" content="https://vibevaultafrica.co.za/">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_ZA">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="VibeVault Africa">
<meta name="twitter:description" content="Cape Town's urban pod network. Storage, charge, rides, care.">
<meta name="twitter:image" content="https://vibevaultafrica.co.za/images/hero-pod.jpg">
<link rel="canonical" href="https://vibevaultafrica.co.za/">
```

**v1.html**
```html
<meta name="description" content="Your Vault — VibeVault Africa's warm, human companion for Cape Town nights. Secure your bag, charge your phone, get home safe. For everyone.">
<meta name="keywords" content="VibeVault Your Vault, Cape Town nightlife safety, secure locker Cape Town, phone charging V&A Waterfront, safe night out Cape Town">
<meta property="og:title" content="Your Vault — VibeVault Africa">
<meta property="og:description" content="The friend who carries what you shouldn't have to. Storage, charge, rides — your whole night covered.">
<meta property="og:image" content="https://vibevaultafrica.co.za/images/hero-pod.jpg">
<meta property="og:url" content="https://vibevaultafrica.co.za/v1.html">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Your Vault — VibeVault Africa">
<meta name="twitter:description" content="Drop your bag. Go live. VibeVault carries the load.">
<meta name="twitter:image" content="https://vibevaultafrica.co.za/images/hero-pod.jpg">
<link rel="canonical" href="https://vibevaultafrica.co.za/v1.html">
<meta name="robots" content="index, follow">
```

**v2.html**
```html
<meta name="description" content="The Inevitable — VibeVault Africa. A city where safety never becomes a thought. Seamless urban infrastructure for Cape Town.">
<meta name="keywords" content="VibeVault The Inevitable, Cape Town urban infrastructure, invisible safety Cape Town, smart city Cape Town, seamless city safety">
<meta property="og:title" content="The Inevitable — VibeVault Africa">
<meta property="og:description" content="A city where safety never becomes a thought. Cape Town's next infrastructure layer.">
<meta property="og:image" content="https://vibevaultafrica.co.za/images/IMG_5179.JPG">
<meta property="og:url" content="https://vibevaultafrica.co.za/v2.html">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="The Inevitable — VibeVault Africa">
<meta name="twitter:description" content="Safety as something you never think about again. VibeVault Africa.">
<meta name="twitter:image" content="https://vibevaultafrica.co.za/images/IMG_5179.JPG">
<link rel="canonical" href="https://vibevaultafrica.co.za/v2.html">
<meta name="robots" content="index, follow">
```

**v3.html**
```html
<meta name="description" content="The Explorer — VibeVault Africa. Cape Town belongs to everyone in it. Storage, rides, care and safety for tourists, students, families and locals.">
<meta name="keywords" content="VibeVault Explorer, Cape Town for everyone, tourist safety Cape Town, student safety Cape Town, Camps Bay, V&A Waterfront, Cape Town explorer">
<meta property="og:title" content="The Explorer — VibeVault Africa">
<meta property="og:description" content="Cape Town belongs to everyone in it. VibeVault moves when you move.">
<meta property="og:image" content="https://vibevaultafrica.co.za/images/IMG_5163.JPG">
<meta property="og:url" content="https://vibevaultafrica.co.za/v3.html">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="The Explorer — VibeVault Africa">
<meta name="twitter:description" content="For everyone out in this city. VibeVault Africa.">
<meta name="twitter:image" content="https://vibevaultafrica.co.za/images/IMG_5163.JPG">
<link rel="canonical" href="https://vibevaultafrica.co.za/v3.html">
<meta name="robots" content="index, follow">
```

**v4.html**
```html
<meta name="description" content="VibeVault Africa Infrastructure Case — Cape Town's R24.5bn tourism economy deserves infrastructure that matches its ambition. Investment and partnership opportunities.">
<meta name="keywords" content="VibeVault invest, Cape Town infrastructure investment, urban pod network South Africa, B-BBEE Level 1 investment, Cape Town smart city investment, VibeVault Africa investor">
<meta property="og:title" content="Infrastructure Case — VibeVault Africa">
<meta property="og:description" content="The infrastructure Cape Town has been building toward. R24.5bn economy. B-BBEE Level 1. 100% Black Woman Owned.">
<meta property="og:image" content="https://vibevaultafrica.co.za/images/IMG_5158.JPG">
<meta property="og:url" content="https://vibevaultafrica.co.za/v4.html">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Infrastructure Case — VibeVault Africa">
<meta name="twitter:description" content="Investment and partnership opportunities. Cape Town urban infrastructure.">
<meta name="twitter:image" content="https://vibevaultafrica.co.za/images/IMG_5158.JPG">
<link rel="canonical" href="https://vibevaultafrica.co.za/v4.html">
<meta name="robots" content="index, follow">
```

**brief.html**
```html
<meta name="description" content="VibeVault Africa Investor Brief 2026 — Cape Town urban pod infrastructure. Pre-seed investment opportunity. B-BBEE Level 1, 100% Black Woman Owned.">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="https://vibevaultafrica.co.za/brief.html">
```

Note: `noindex` on brief.html is intentional — investor documents should not be
publicly indexed by search engines.

### JSON-LD Structured Data
Add to `<head>` of index.html:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "VibeVault Africa",
  "alternateName": "VibeVault Africa (PTY) Ltd",
  "url": "https://vibevaultafrica.co.za",
  "logo": "https://vibevaultafrica.co.za/images/hero-pod.jpg",
  "description": "Cape Town's smart urban pod network — secure storage, phone charging, emergency assistance and safe rides.",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Cape Town",
    "addressCountry": "ZA"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+27730129314",
    "email": "dasha@vibevaultafrica.co.za",
    "contactType": "General Enquiries"
  },
  "foundingDate": "2025",
  "founder": {
    "@type": "Person",
    "name": "Dasha Mohlala"
  },
  "areaServed": {
    "@type": "City",
    "name": "Cape Town"
  },
  "sameAs": []
}
</script>
```

### Create sitemap.xml (place at root of repo)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://vibevaultafrica.co.za/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://vibevaultafrica.co.za/v1.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://vibevaultafrica.co.za/v2.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://vibevaultafrica.co.za/v3.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://vibevaultafrica.co.za/v4.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
</urlset>
```

### Create robots.txt (place at root of repo)
```
User-agent: *
Allow: /
Disallow: /brief.html

Sitemap: https://vibevaultafrica.co.za/sitemap.xml
```

### hreflang tags (add to <head> of all pages for multilingual SEO)
```html
<link rel="alternate" hreflang="en" href="https://vibevaultafrica.co.za/v1.html?lang=en" />
<link rel="alternate" hreflang="af" href="https://vibevaultafrica.co.za/v1.html?lang=af" />
<link rel="alternate" hreflang="fr" href="https://vibevaultafrica.co.za/v1.html?lang=fr" />
<link rel="alternate" hreflang="de" href="https://vibevaultafrica.co.za/v1.html?lang=de" />
<link rel="alternate" hreflang="es" href="https://vibevaultafrica.co.za/v1.html?lang=es" />
<link rel="alternate" hreflang="pt" href="https://vibevaultafrica.co.za/v1.html?lang=pt" />
<link rel="alternate" hreflang="zh" href="https://vibevaultafrica.co.za/v1.html?lang=zh" />
<link rel="alternate" hreflang="ar" href="https://vibevaultafrica.co.za/v1.html?lang=ar" />
<link rel="alternate" hreflang="ru" href="https://vibevaultafrica.co.za/v1.html?lang=ru" />
<link rel="alternate" hreflang="ja" href="https://vibevaultafrica.co.za/v1.html?lang=ja" />
<link rel="alternate" hreflang="ko" href="https://vibevaultafrica.co.za/v1.html?lang=ko" />
<link rel="alternate" hreflang="x-default" href="https://vibevaultafrica.co.za/" />
```
Adjust page path (v1, v2, v3, v4) for each respective page's `<head>`.

---

## EDIT 9 — FIX LANGUAGE TRANSLATION GAPS (text that stays in English)

This is the final and most detailed audit task.

### Root cause
Text that stays in English regardless of language selection is caused by one or more of:
1. Missing `data-i18n` attribute on an HTML element
2. The element is dynamically generated in JS without translation applied
3. A translation key exists in translations.js but the element isn't queried on load
4. The translation JS runs before the DOM is ready

### Fix approach — apply to v1.html, v2.html, v3.html, v4.html

**Step 1:** Audit every visible text node in each HTML file.
For any text that is hardcoded in English (not dynamically inserted), ensure its
parent element has a `data-i18n="key_name"` attribute pointing to a valid key
in translations.js for that version.

**Step 2:** For dynamically generated text (generated via JS innerHTML), ensure the
translation function is called AFTER the element is added to the DOM.

**Step 3:** Verify the translation initialisation script runs inside:
```javascript
document.addEventListener('DOMContentLoaded', function() {
  // language detection + VV_WEB application
});
```
NOT at the top level of a `<script>` tag where the DOM may not be ready.

**Step 4:** Common elements frequently missing translation:
- Navigation link labels
- Form placeholder text (use `data-placeholder` and apply via JS:
  `el.setAttribute('placeholder', VV_WEB[lang].shared.form_placeholder_name)`)
- Button text inside dynamically rendered components
- Footer legal text
- Stat card labels and source notes
- Tier/pricing section labels
- Error/confirmation messages from the Formspree form

**Step 5:** After making fixes, test by:
1. Opening each page in a browser
2. Appending `?lang=fr` to the URL
3. Every visible text element should render in French
4. Repeat with `?lang=ar` — page should switch to RTL layout, all text in Arabic
5. Repeat with `?lang=zu` — all available Zulu translations should show

**Step 6:** For any text where a translation is genuinely missing in translations.js,
add the missing key and translate it for all 26 languages. Use your training knowledge
and mark uncertain African language translations with `// ⚠️ Verify with native speaker`.

---

## VERIFICATION CHECKLIST

After all edits are complete, verify the following before committing:

- [ ] "← Find your VibeVault" button appears at top AND bottom of V1, V3, V4
- [ ] Clicking the button on any version takes the user to index.html (game Screen 1)
- [ ] V1: email and phone number in Get In Touch section display in white
- [ ] V1: "Get VibeVault" button now reads "Register your interest"
- [ ] V2 and V3 both have "Looking to invest or partner?" link at the bottom
- [ ] V4 hero shows IMG_5158.JPG with no gaps or borders visible
- [ ] V3 hero shows IMG_5163.JPG with no gaps or borders visible
- [ ] V2 hero shows IMG_5179.JPG with no gaps or borders visible
- [ ] V2 "The Tension" section shows IMG_5153.JPG correctly
- [ ] No image on any page has a visible edge/border against the dark background
- [ ] Topographic SVG linework appears on V1, V2, V3, V4 (different placements)
- [ ] Disclaimer appears on all 4 versions and on brief.html
- [ ] All pages have correct `<meta>` SEO tags and Open Graph tags
- [ ] sitemap.xml exists at root
- [ ] robots.txt exists at root and blocks brief.html from indexing
- [ ] JSON-LD structured data exists in index.html `<head>`
- [ ] Selecting French (`?lang=fr`) on any page shows no English text leaking through
- [ ] Selecting Arabic (`?lang=ar`) applies RTL layout correctly
- [ ] All changes work in mobile viewport (375px width minimum)
- [ ] No JavaScript console errors on any page

---

END OF EDITS
