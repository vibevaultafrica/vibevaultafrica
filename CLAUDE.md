# CLAUDE.md — VibeVault Africa Complete Build Spec
# Claude Code reads this file first before touching anything.

---

## WHO THIS IS FOR
Dasha Mohlala, founder of VIBEVAULT AFRICA (PTY) LTD.
You are building her live website at vibevaultafrica.co.za, hosted on GitHub Pages.
The repository is at github.com/vibevaultafrica/vibevaultafrica.

---

## WHAT IS LIVE NOW (the old site — replace everything)
The current index.html is titled "Safe by Design" with teal branding, one page,
old copy, and zero multilingual support. Replace it completely.

---

## WHAT TO BUILD — COMPLETE FILE LIST

Build EVERY file below. Do not skip any. Do not stop until all exist and are complete.

```
/
├── index.html          ← game entry experience (the first thing users see)
├── v1.html             ← Your Vault (warm, human, friend)
├── v2.html             ← The Inevitable (elegant, poetic, invisible)
├── v3.html             ← The Explorer (open, free, for everyone)
├── v4.html             ← Infrastructure Case (investor/institutional)
├── brief.html          ← downloadable investor brief (V4 CTA downloads this)
├── translations.js     ← ALL 26 language translations for websites
├── images/
│   ├── hero-pod.jpg       ← (slot: rename IMG_5175.jpeg when user uploads)
│   ├── hero-promenade.jpg ← (slot: rename IMG_5160.jpeg)
│   ├── hero-solar.jpg     ← (slot: rename IMG_5179.jpeg)
│   ├── hero-row.jpg       ← (slot: rename IMG_5176.jpeg)
│   ├── seating.jpg        ← (slot: rename IMG_5162.jpeg)
│   └── stranded-screen.jpg← (slot: rename IMG_5163.jpeg)
└── CLAUDE.md           ← this file (do not delete)
```

---

## BRAND RULES — NEVER BREAK THESE

**Logo**: "Vibe" = white (#FFFFFF), "Vault" = teal (#40E0D0). Never invert. Never gold. Never both white.
**Font**: ONLY `-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', system-ui, sans-serif`
  — No Google Fonts. No Cormorant Garamond. No serif. No exceptions.
**Colors**:
  - Primary teal: #40E0D0
  - Deep teal: #00CED1
  - Midnight navy: #0D1B2A
  - Near-black: #080E18
  - Surface: #0D1824
  - Card: #111F30
  - Warm amber: #C9A84C (V4 / investor accents only)
  - Light grey: #E5E5E5
**Contact number**: +27730129314 — display as +27 73 012 9314
**Email**: dasha@vibevaultafrica.co.za
**Company**: VIBEVAULT AFRICA (PTY) LTD
**Enterprise No.**: 2025/958585/07
**B-BBEE**: Level 1, 100% Black Woman Owned
**SARS Tax Ref**: 9332914259

---

## LANGUAGE SYSTEM — HOW IT WORKS

### 26 Languages
| Code    | Name                   | RTL | Welcome word           | Notes                                   |
|---------|------------------------|-----|------------------------|-----------------------------------------|
| en      | English                | no  | Welcome                |                                         |
| af      | Afrikaans              | no  | Welkom                 |                                         |
| zu      | isiZulu                | no  | Sawubona               |                                         |
| xh      | isiXhosa               | no  | Wamkelekile            |                                         |
| st      | SeSotho                | no  | Amoheloa               |                                         |
| tn      | SeTswana               | no  | Amogetsegile           |                                         |
| ve      | TshiVenda              | no  | Ndi maswali            | ⚠️ Flag in code: needs native review    |
| de      | Deutsch                | no  | Willkommen             |                                         |
| de-CH   | Schweizerdeutsch       | no  | Willkommen             | Uses Standard Hochdeutsch formally      |
| fr      | Français               | no  | Bienvenue              |                                         |
| es      | Español                | no  | Bienvenido             |                                         |
| pt      | Português              | no  | Bem-vindo              |                                         |
| it      | Italiano               | no  | Benvenuto              |                                         |
| nl      | Nederlands             | no  | Welkom                 |                                         |
| sv      | Svenska                | no  | Välkommen              |                                         |
| el      | Ελληνικά               | no  | Καλώς ήλθατε           |                                         |
| ru      | Русский                | no  | Добро пожаловать       |                                         |
| ar      | العربية                | YES | أهلاً وسهلاً           | Apply dir="rtl" to container            |
| ur      | اردو                   | YES | خوش آمدید              | Apply dir="rtl" to container            |
| zh      | 中文 (Mandarin)        | no  | 欢迎                   | Simplified characters                   |
| zh-TW   | 繁體中文 (Taiwanese)   | no  | 歡迎                   | Traditional characters, Taiwan usage    |
| yue     | 廣東話 (Cantonese)     | no  | 歡迎                   | Traditional chars, Cantonese vocabulary |
| ja      | 日本語                 | no  | ようこそ               |                                         |
| ko      | 한국어                 | no  | 어서 오세요            |                                         |
| sw      | Kiswahili              | no  | Karibu                 |                                         |
| yo      | Yorùbá                 | no  | Ẹ káàbọ̀              |                                         |

### Language Flow
1. User lands on index.html (the game)
2. Selects language — ALL game text updates immediately to that language
3. Clicks "Enter this version" — site stores lang in localStorage key `vv-lang`
4. Each website version (v1.html etc.) reads localStorage on load and applies translations
5. Also reads `?lang=` URL parameter as override (e.g. vibevaultafrica.co.za/v1.html?lang=fr)
6. Falls back to browser language, then English

### RTL Handling
For `ar` and `ur`: apply `dir="rtl"` to the `<html>` tag and `text-align: right` where needed.

### What stays in English regardless of language
- "VibeVault" (always, in every language)
- All legal text (company registration, B-BBEE, enterprise number, SARS ref)
- Dasha Mohlala (her name)
- dasha@vibevaultafrica.co.za
- +27 73 012 9314
- vibevaultafrica.co.za
- R24.5 billion / R24.5 bn / R99 / R299 etc. (currency amounts stay as Rand)
- Cape Town (proper noun, stays as is)

---

## FILE 1: index.html — THE GAME (ENTRY EXPERIENCE)

### Purpose
This is the first page users see at vibevaultafrica.co.za. It IS the entry experience.
After the game, users are routed to v1.html, v2.html, v3.html, or v4.html.

### Structure: 5 screens (CSS display:none / display:flex toggling)

**Screen 1 — Language Selection**
- Logo: <span style="color:#fff">Vibe</span><span style="color:#40E0D0">Vault</span>
- "Welcome" word cycles through all 26 languages — Apple-style pace: visible 3.4 seconds, fade out over 720ms, fade in new language
- When user selects a language, word stops on that language's welcome
- Grid of 26 language buttons (all text must be visible: white or teal on dark background)
- "Continue →" button (teal background, dark text — ALWAYS VISIBLE)
- Small note: "Your full experience continues in your chosen language"
- ALL elements use <div> not <button> to prevent host CSS override

**Screen 2 — Intro**
- "Before you enter" eyebrow
- Headline: "Three questions. Your VibeVault."
- Sub: "Answer instinctively — thinking gets in the way."
- "Begin →" div button (teal, dark text, always visible)
- Skip option: "skip the quiz — see all versions" (visible, white underlined text)
- Note: "we respect your autonomy around here"

**Screen 3 — Browse All (opt-out)**
- "All roads lead here."
- Grid of 4 version cards (each clickable, teal border on hover)
- Back to game link

**Screen 4 — Game (3 questions)**
- Progress dots (3 dots, current is white/enlarged)
- Question text
- 4 answer divs (dark card background, white text, teal border on hover)
- NEVER use <button> tags for answers

**Screen 5 — Reveal**
- Golden ratio spiral (φ = 1.618) drawn on canvas
- Version name, tag, description
- "← Try again" and "Enter this version ↗" divs

### Game Logic (Golden Ratio Routing)
Each answer carries weights for v1/v2/v3/v4. Sum across 3 questions, highest wins.

Questions and weights:
```
Q1: "Cape Town, midnight. What matters most right now?"
  A: "Who I'm with"              → {v1:2, v2:0, v3:0, v4:0}
  B: "That nothing can interrupt this" → {v1:0, v2:2, v3:0, v4:0}
  C: "Where I haven't explored yet"   → {v1:0, v2:0, v3:2, v4:0}
  D: "What this city could become"    → {v1:0, v2:0, v3:0, v4:2}

Q2: "At its best, safety should feel like..."
  A: "Someone who genuinely has you"  → {v1:2, v2:1, v3:0, v4:0}
  B: "Something you never think about"→ {v1:0, v2:2, v3:1, v4:0}
  C: "Something that never slows us down" → {v1:0, v2:1, v3:2, v4:0}
  D: "Infrastructure that simply works"  → {v1:0, v2:0, v3:0, v4:2}

Q3: "A city that truly cares gives us..."
  A: "Somewhere we belong"          → {v1:2, v2:0, v3:0, v4:1}
  B: "A night without a single worry"→ {v1:0, v2:2, v3:1, v4:0}
  C: "Every reason to keep exploring"→ {v1:0, v2:0, v3:2, v4:1}
  D: "Infrastructure that outlasts its founders" → {v1:0, v2:1, v3:0, v4:2}
```

### Game Translations
The COMPLETE translations object must be embedded in index.html (cannot use external file because the game runs first).

For each language, translate these keys:
```
lp   = langPrompt         "Select your language"
ct   = continue           "Continue →"
ln   = lnote              "Your full experience continues in your chosen language"
eb   = eyBefore           "Before you enter"
tg   = titleGame          "Three questions. Your VibeVault."  (use \n for line break)
sg   = subGame            "Answer instinctively — thinking gets in the way."
bg   = begin              "Begin →"
sk   = skip               "skip the quiz — see all versions"
sn   = skipNote           "we respect your autonomy around here"
ec   = eyCall             "Your call, entirely"
ar2  = allRoads           "All roads lead here."
bs   = browseSub          "Four versions of VibeVault. One of them is unmistakably you."
ev   = enterVer           "Enter this version →"
bk   = backGame           "← actually, I'm curious about the game"
qo   = qOf                "Question {n} of 3"   ← replace {n} with number in JS
yv   = yourVault          "Your VibeVault"
ta   = tryAgain           "← Try again"
et   = enterThis          "Enter this version ↗"
q1   = question 1 text
q1a-q1d = 4 answers
q2   = question 2 text
q2a-q2d = 4 answers
q3   = question 3 text
q3a-q3d = 4 answers
v1n, v1t, v1d = V1 name/tag/desc (browse screen)
v2n, v2t, v2d = V2 name/tag/desc
v3n, v3t, v3d = V3 name/tag/desc
v4n, v4t, v4d = V4 name/tag/desc
r1n, r1t, r1d = V1 result name/tag/desc (reveal screen)
r2n, r2t, r2d = V2 result
r3n, r3t, r3d = V3 result
r4n, r4t, r4d = V4 result
```

### COMPLETE GAME TRANSLATIONS — All 26 Languages
Implement ALL of these accurately. Claude Code: use your training knowledge for accuracy.
For languages where you have lower confidence, add a comment `// ⚠️ Verify with native speaker`.

```javascript
// ENGLISH
en: {
  lp:'Select your language', ct:'Continue →', ln:'Your full experience continues in your chosen language',
  eb:'Before you enter', tg:'Three questions.\nYour VibeVault.', sg:'Answer instinctively — thinking gets in the way.',
  bg:'Begin →', sk:'skip the quiz — see all versions', sn:'we respect your autonomy around here',
  ec:'Your call, entirely', ar2:'All roads lead here.',
  bs:'Four versions of VibeVault. One of them is unmistakably you.',
  ev:'Enter this version →', bk:'← actually, I\'m curious about the game',
  qo:'Question {n} of 3', yv:'Your VibeVault', ta:'← Try again', et:'Enter this version ↗',
  q1:'Cape Town, midnight. What matters most right now?',
  q1a:'Who I\'m with', q1b:'That this moment is untouchable',
  q1c:'Where I haven\'t explored yet', q1d:'What this city could become',
  q2:'At its best, safety should feel like...',
  q2a:'Someone who genuinely has you', q2b:'Something you never think about',
  q2c:'Something that never slows us down', q2d:'Infrastructure that simply works',
  q3:'A city that truly cares gives us...',
  q3a:'Somewhere we belong', q3b:'A night without a single worry',
  q3c:'Every reason to keep exploring', q3d:'Infrastructure that outlasts its founders',
  v1n:'Your Vault', v1t:'The Friend. Warm, human, present.',
  v1d:'VibeVault is there before you think to ask — bag held, phone charged, ride home sorted. For everyone who wants a night with nothing in the way.',
  v2n:'The Inevitable', v2t:'Elegant, seamless, invisible.',
  v2d:'Safety as something you never think about again. A city that has already taken care of it.',
  v3n:'The Explorer', v3t:'Open, free, for everyone.',
  v3d:'For everyone moving through this city, for any reason, at any time.',
  v4n:'Infrastructure Case', v4t:'Institutional, investment-grade.',
  v4d:'The civic case for Cape Town\'s R24.5bn economy. For investors and city partners.',
  r1n:'Your Vault', r1t:'The city\'s most prepared friend.',
  r1d:'VibeVault for you is the friend who thought of everything before you thought to ask — bag held, phone charged, ride home sorted. The one who never makes you feel like you should have planned better. You just get to be present.',
  r2n:'The Inevitable', r2t:'Safety, without the word.',
  r2d:'VibeVault for you is what Cape Town feels like when it\'s working exactly as it should — safety not as something you hold onto, but as the air. Already there.',
  r3n:'The Explorer Edition', r3t:'The city, fully yours.',
  r3d:'VibeVault for you moves when you move — storage, rides, safety and care woven into every corner.',
  r4n:'The Infrastructure Case', r4t:'Cape Town\'s defining civic moment.',
  r4d:'VibeVault for you is the investment thesis a R24.5 billion economy has been building toward.'
},

// AFRIKAANS
af: {
  lp:'Kies jou taal', ct:'Aanhou →', ln:'Jou volledige ervaring gaan voort in jou gekose taal',
  eb:'Voordat jy ingaan', tg:'Drie vrae.\nJou VibeVault.', sg:'Antwoord instinktief — om te dink staan in die pad.',
  bg:'Begin →', sk:'slaan die vaag oor — sien alle weergawes', sn:'ons respekteer jou outonomie hier',
  ec:'Jou keuse, heeltemal', ar2:'Alle paaie lei hierheen.',
  bs:'Vier weergawes van VibeVault. Een van hulle is onmiskenbaar jy.',
  ev:'Gaan na hierdie weergawe →', bk:'← eintlik, ek is nuuskierig oor die spel',
  qo:'Vraag {n} van 3', yv:'Jou VibeVault', ta:'← Probeer weer', et:'Gaan na hierdie weergawe ↗',
  q1:'Kaapstad, middernag. Wat is nou die belangrikste?',
  q1a:'Met wie ek is', q1b:'Dat hierdie oomblik onaantasbaar is',
  q1c:'Waar ek nog nie was nie', q1d:'Wat hierdie stad kan word',
  q2:'Op sy beste moet veiligheid voel soos...',
  q2a:'Iemand wat regtig vir jou omgee', q2b:'Iets waaraan jy nooit dink nie',
  q2c:'Iets wat ons nooit vertraag nie', q2d:'Infrastruktuur wat eenvoudig werk',
  q3:'\'n Stad wat werklik omgee gee vir ons...',
  q3a:'\'n Plek waar ons hoort', q3b:'\'n Nag sonder enige bekommernis',
  q3c:'Elke rede om aan te hou verken', q3d:'Infrastruktuur wat sy stigters oorleef',
  v1n:'Jou Vault', v1t:'Die Vriend. Warm, menslik, teenwoordig.',
  v1d:'VibeVault is daar voordat jy om te vra — tas gehou, foon opgeladen, ritje huis toe gesorteer. Vir almal wat \'n aand wil hê met niks in die pad.',
  v2n:'Die Onvermydelike', v2t:'Elegant, naatloos, onsigbaar.',
  v2d:'Veiligheid as iets waaraan jy nooit weer dink nie. \'n Stad wat al klaar daarvoor gesorg het.',
  v3n:'Die Ontdekker', v3t:'Oop, vry, vir almal.',
  v3d:'Vir almal wat deur hierdie stad beweeg, vir enige rede, enige tyd.',
  v4n:'Infrastruktuurssaak', v4t:'Institusioneel, beleggingsgraad.',
  v4d:'Die burgerlike saak vir Kaapstad se R24.5bn ekonomie. Vir beleggers en stadsvennote.',
  r1n:'Jou Vault', r1t:'Die stad se gereedste vriend.',
  r1d:'VibeVault vir jou is die vriend wat van alles gedink het voordat jy om te vra — tas gehou, foon opgeladen, ritje huis toe gesorteer. Die een wat jou nooit voel soos jy beter moes beplan het nie. Jy kry net om teenwoordig te wees.',
  r2n:'Die Onvermydelike', r2t:'Veiligheid, sonder die woord.',
  r2d:'VibeVault vir jou is wat Kaapstad voel soos wanneer dit presies werk — veiligheid nie as iets wat jy vashou nie, maar as die lug. Al daar.',
  r3n:'Die Ontdekker Uitgawe', r3t:'Die stad, heeltemal joune.',
  r3d:'VibeVault vir jou beweeg wanneer jy beweeg — bergplek, ritte, veiligheid en sorg geweef in elke hoek.',
  r4n:'Die Infrastruktuurssaak', r4t:'Kaapstad se bepalende burgerlike oomblik.',
  r4d:'VibeVault vir jou is die beleggingstese wat \'n R24.5 miljard ekonomie na gebou het.'
},

// ISIZULU
zu: {
  lp:'Khetha ulimi lwakho', ct:'Qhubeka →', ln:'Ulwazi lwakho oluphelele luqhubeka ngolimi lwakho olukhethiwe',
  eb:'Ngaphambi kokungena', tg:'Imibuzo emithathu.\nI-VibeVault yakho.', sg:'Phendula ngokwemvelo — ukucabanga kuphazamisa.',
  bg:'Qala →', sk:'langisa i-quiz — bona zonke izinguqulo', sn:'siyakuhlonipha inkululeko yakho lapha', // ⚠️ Verify with native speaker
  ec:'Ukhetha kwakho, ngokuphelele', ar2:'Yonke imigwaqo iya lapha.',
  bs:'Izinguqulo ezine ze-VibeVault. Eyodwa yalzo ayikhakhaleki.',
  ev:'Ngena kule nguqulo →', bk:'← empeleni, ngifuna ukudlala umdlalo',
  qo:'Umbuzo {n} ku-3', yv:'I-VibeVault yakho', ta:'← Zama futhi', et:'Ngena kule nguqulo ↗',
  q1:'iKapa, phakathi kobusuku. Yini ebaluleke kakhulu manje?',
  q1a:'Engikanaye', q1b:'Ukuthi lomzuzu awukhathazekile',
  q1c:'Lapho angikayihloli khona', q1d:'Ukuthi le dolobha ingaba yini',
  q2:'Ekuhle kwayo, ukuphepha kufanele kuzizwe njenge...',
  q2a:'Umuntu okunakekelayo ngokweqiniso', q2b:'Okungacabangwayo',
  q2c:'Okungasiyephi ngedla phansi', q2d:'Ingqalasizinda esebenzayo',
  q3:'Idolobha elinakekela ngokweqiniso lisinike...',
  q3a:'Indawo esohlela kuyo', q3b:'Ubusuku obungenalo ixhala',
  q3c:'Zonke izizathu zokuqhubeka nokuhlola', q3d:'Ingqalasizinda edlula abasunguleli bayo',
  v1n:'I-Vault yakho', v1t:'Umngane. Fudumele, ngokomuntu, ukhona.',
  v1d:'I-VibeVault ikhona ngaphambi kokuba ucele — ibhegi ilibanjwe, ifoni ilichajwe, uhambo olwandle lwalulandelwa. Kubo bonke abafuna ubusuku ongeno okusiphazamisa.',
  v2n:'Okungagwenywa', v2t:'Elihle, luteketiso, alubonakali.',
  v2d:'Ukuphepha njengehco ongacabanga ngalo futhi. Idolobha eseliqapha.',
  v3n:'Umhloli', v3t:'Vulekile, ngokukhululeka, kubo bonke.',
  v3d:'Kulo lonke uhamba kulo idolobha, nganoma iyiphi isizathu, nanoma inini.',
  v4n:'Icala Lengqalasizinda', v4t:'Yesikhungo, izinga lokutshala imali.',
  v4d:'Icala lobumphakathi le-R24.5bn ye-economy yaseKapa. Labatshali bezimali nabalingani bedolobha.',
  r1n:'I-Vault yakho', r1t:'Umngane okulungiselele kakhulu wendolobha.',
  r1d:'I-VibeVault yakho yumngane owacabanga ngakho konke ngaphambi kokuba ucele — ibhegi ilibanjwe, ifoni ilichajwe, uhambo olwandle lwalulandelwa. Yile eyokukhala ukuthi akudingeki ukubephethe kuhle. Nje nje ukhona.',
  r2n:'Okungagwenywa', r2t:'Ukuphepha, ngaphandle kwegama.',
  r2d:'I-VibeVault yakho yingkutshane ye-Cape Town iyuma ngokunembile — ukuphepha hhayi njengelinto oyibambayo, kodwa njengokhoya. Ivele',
  r3n:'Inguqulo Yomhloli', r3t:'Idolobha, eyakho ngokuphelele.',
  r3d:'I-VibeVault yakho ihamba lapho uhamba — ukugcina, ukugibela, ukuphepha nokukhathala kuguqulelwa emkhoneni ngomkhono.',
  r4n:'Icala Lengqalasizinda', r4t:'Umzuzu omqoka wobumphakathi baseKapa.',
  r4d:'I-VibeVault yakho icala lokutshala imali i-economy ye-R24.5 billion eyakhele kulo.'
},

// ISIXHOSA
xh: {
  lp:'Khetha ulwimi lwakho', ct:'Qhubeka →', ln:'Ulwazi lwakho olupheleleyo luqhubeka ngolwimi lwakho olukhethileyo',
  eb:'Ngaphambi kokungena', tg:'Imibuzo emithathu.\nI-VibeVault yakho.', sg:'Phendula ngokwemvelo — ukucinga kuyaphazamisa.',
  bg:'Qala →', sk:'langisa i-quiz — jonga zonke iinguqulo', sn:'siyahlonipha inyaniso yakho apha', // ⚠️ Verify with native speaker
  ec:'Ukhetha kwakho, ngokupheleleyo', ar2:'Yonke iindlela ziya apha.',
  bs:'Iinguqulo ezine ze-VibeVault. Enye yayo ayikhakhaleki.',
  ev:'Ngena kwinguqulo yaba →', bk:'← ngokwenene, ndinombuzo ngomdlalo',
  qo:'Umbuzo {n} ku-3', yv:'I-VibeVault yakho', ta:'← Zama kwakhona', et:'Ngena kwinguqulo yaba ↗',
  q1:'iKapa, phakathi kwamabusuku. Yintoni ebalulekileyo ngoku?',
  q1a:'Lowo ndikuye', q1b:'Ukuba lo mzuzu awunamakhulukelwano',
  q1c:'Apho ndingakayihloli khona', q1d:'Ukuba le dolophu inokuphenduka ntoni',
  q2:'Ubuhle bayo, ukhuseleko bufanele buzive njenge...',
  q2a:'Umntu onovelwano ngokwenyaniso', q2b:'Into ongazicingeli yona',
  q2c:'Into engasoze isiphuphume', q2d:'Ingqalasizinda esebenzayo nje',
  q3:'Idolophu enyaniso enakekela isinika...',
  q3a:'Indawo esiyileyo', q3b:'Ubusuku obungenaxhala',
  q3c:'Yonke imizekelo yokuqhubeka nokhwelo', q3d:'Ingqalasizinda eyidlulayo abayimisileyo',
  v1n:'I-Vault yakho', v1t:'Umhlobo. Fudumele, nomntu, ukhona.',
  v1d:'I-VibeVault ikhona ngaphambi kokubuza — ibhagi ibambile, ifowuni ilichajwe, uhambo wesitaxi lulungile. Kubo bonke abafuna ubusuku engekho into eyimangalelo.',
  v2n:'Okungamelwe', v2t:'Elihle, luteketiso, alubonakali.',
  v2d:'Ukhuseleko njengehco ongacingelisisi futhi. Idolophu esolele ngalo.',
  v3n:'Umkhangeli', v3t:'Vulekile, ngokukhululeka, kubo bonke.',
  v3d:'Kubo bonke abahambi kulo mzi, nangasiphi na isizathu, nanini na.',
  v4n:'Ityala Lengqalasizinda', v4t:'Yesikhungo, izinga lokutshala imali.',
  v4d:'Ityala lobuluntu le-R24.5bn ye-economy yaseKapa. Labatshali-mali nabalinganisi belo dolophu.',
  r1n:'I-Vault yakho', r1t:'Umhlobo okulungisile kakhulu wedolophu.',
  r1d:'I-VibeVault yakho ngumhlobo ocinga ngakho konke ngaphambi kokubuza — ibhagi ibambile, ifowuni ilichajwe, uhambo wesitaxi lulungile. Olo oyokukhala ukuthi akufuneki ukucinga ngawe. Nje ubheke.',
  r2n:'Okungamelwe', r2t:'Ukhuseleko, ngaphandle kwelizwi.',
  r2d:'I-VibeVault yakho yiyo iKapa njengoko ifana xa ikhulula kuqo — ukhuseleko hhayi njengento oyibambayo, kodwa njengomoya. Ivele ikhona.',
  r3n:'Inguqulo Yomkhangeli', r3t:'Idolophu, eyakho ngokupheleleyo.',
  r3d:'I-VibeVault yakho ihambe nawe — ukugcina, ukugibela, ukhuseleko nenkathalo kuguqulelwa emkhokhweni ngomkhokho.',
  r4n:'Ityala Lengqalasizinda', r4t:'Umzuzu omqoka wobuluntu baseKapa.',
  r4d:'I-VibeVault yakho ityala lokutshala imali i-economy ye-R24.5 billion eyakhele kulo.'
},

// SESOTHO
st: {
  lp:'Khetha puo ya hao', ct:'Tswela pele →', ln:'Boiphihlelo ba hao botlalo bo tswela pele ka puo eo o e khethileng',
  eb:'Pele o kenella', tg:'Dipotso tse tharo.\nI-VibeVault ya hao.', sg:'Araba ka tlhaho — ho nahana ho a sitisa.',
  bg:'Qala →', sk:'qeta papadi — bolela kaofela', sn:'re hlonephela kgetsi ya gago ka mo', // ⚠️ Verify with native speaker
  ec:'Khetho ya hao, ka botlalo', ar2:'Ditsela tsohle di ya mona.',
  bs:'Mefuta e mene ya VibeVault. E nngwe ya tsone ke wena.',
  ev:'Kena ho phetolelo ena →', bk:'← hantle, ke mahloko ka papadi',
  qo:'Potso {n} ho tse 3', yv:'I-VibeVault ya hao', ta:'← Leka hape', et:'Kena ho phetolelo ena ↗',
  q1:'Kapa, bosiu bo bong hara bona. Ke eng e bohlokwa ka ho fetisisa jwale?',
  q1a:'Motho eo ke nayo', q1b:'Hore metsotso eo e se ka ho lakatswa',
  q1c:'Moo ke eso ke hlahle', q1d:'Motse ona o ka ba eng',
  q2:'Ka botlalo ba ona, ts\'ireletso e lokela ho ikutlwa jwalo ka...',
  q2a:'Motho ya tshepahala ho wena', q2b:'Ntho eo o seke o nahane ka yona',
  q2c:'Ntho e sa re sitiseng', q2d:'Meralo e sebetsang feela',
  q3:'Motse o tlhokomelang ka nnete o re nea...',
  q3a:'Moo re amohelehang teng', q3b:'Bosiu bo sa nang mathata',
  q3c:'Mabaka ohle a ho tswela pele ho lekola', q3d:'Meralo e phelang ho feta ba e theeng',
  v1n:'Vault ya hao', v1t:'Moratwi. Ho futhumala, motho, o nang teng.',
  v1d:'I-VibeVault e nteng pele o kopa — mokotlane o babatswe, eseme e bataleng, oka ba hae e amohuoa. Bakeng sa bohle ba ba ratang bosiu bo se nang letho le le sitisang.',
  v2n:'Se se Neng Se Tla Eba Jwalo', v2t:'E ntle, e tshwana, e sa bonahale.',
  v2d:'Ts\'ireletso e le ntho eo o seke wa e nahana hape. Motse o se o hlokometse.',
  v3n:'Mohlahlobi', v3t:'E buleha, e lokoloha, ho bohle.',
  v3d:'Ho bohle ba tsamayang motse ona, ka mabaka afe kapa afe, nako efe kapa efe.',
  v4n:'Nyewe ya Meralo', v4t:'Ya setheo, la pelaelo.',
  v4d:'Nyewe ya mmuso bakeng sa moruo wa R24.5bn wa Kapa. Bakeng sa bapehi-tsa-tjhelete le bahanyetsi ba motse.',
  r1n:'Vault ya hao', r1t:'Moratwi o itokisetseng ka ho fetisisa wa motse.',
  r1d:'I-VibeVault ya hao ke moratwi ya nahane ka ho ofela pele o kopa — mokotlane o babatswe, eseme e bataleng, oka ba hae e amohuoa. O e nngwe e sa o thabe o be o ka lokela ho beakanya hantle. O fela o dumel.',
  r2n:'Se Se Neng Se Tla Eba Jwalo', r2t:'Ts\'ireletso, ntle le lentsu.',
  r2d:'I-VibeVault ya hao ke seo Kapa se nang teng ha se sebetsa hantle — ts\'ireletso e se le ntho eo o e bapiyang, empa e le moea. E se e nang teng.',
  r3n:'Phetolelo ya Mohlahlobi', r3t:'Motse, wa hao ka botlalo.',
  r3d:'I-VibeVault ya hao e tsamaya ha o tsamaya — ho boloka, ho palama, ts\'ireletso le tlhokomelo.',
  r4n:'Nyewe ya Meralo', r4t:'Metsotso e hlokomelehang ea Kapa.',
  r4d:'I-VibeVault ya hao ke morero wa pelaelo eo moruo wa R24.5 billion o keng o haha.'
},

// SETSWANA
tn: {
  lp:'Tlhopha puo ya gago', ct:'Tswelela →', ln:'Boitekanelo jwa gago jotlhe bo tswelela mo puong eo o e tlhophileng',
  eb:'Pele ga go tsena', tg:'Dipotso tse tharo.\nVibeVault ya gago.', sg:'Araba ka tlholego — go nagana go a thibela.',
  bg:'Simolola →', sk:'qeta papadi — mpolele tsotlhe', sn:'re ikemisetsa loratanelo wa gago kano', // ⚠️ Verify with native speaker
  ec:'Tlhopho ya gago, gotlhe', ar2:'Ditsela tsotlhe di ya fa.',
  bs:'Mefuta e mene ya VibeVault. E nngwe ya ona e le wena.',
  ev:'Tsena mo phetolelong e →', bk:'← kwa boikemong, ke rata go ralala papadi',
  qo:'Potso {n} ya 3', yv:'VibeVault ya gago', ta:'← Leka gape', et:'Tsena mo phetolelong e ↗',
  q1:'Kapa, bogare jwa bosigo. Ke eng yo o botlhokwa go gaisa jaanong?',
  q1a:'Yo ke naye', q1b:'Gore go se kgone go go phakamisa nako eo',
  q1c:'Moo ke ose ke ya teng', q1d:'Motse o o ka nna eng',
  q2:'Fa e le botoka jwa yona, polokego e tshwanetse go ikutlwa jaaka...',
  q2a:'Motho yo o go tlhokomelang ka boammaaruri', q2b:'Sengwe se o sa nahaneng ka sona',
  q2c:'Sengwe se se sa re kgobetseng', q2d:'Meraka e e dirang fela',
  q3:'Motse yo o tlhokomelang ka nnete o re naya...',
  q3a:'Lefelo le re amogelwang mo', q3b:'Bosigo jo bo sa nang matshwenyego',
  q3c:'Mabaka otlhe a go tswelela go lekola', q3d:'Meraka e e phelang go feta baakakanyi ba yona',
  v1n:'Vault ya gago', v1t:'Moratwi. Go oketsa, motho, o teng.',
  v1d:'VibeVault e teng pele o kopa — mokotlane o babalwa, mogala o batle, oka ba gae o ipagile. Go lefapelo la bohle ba ba ratang bosigo bo se nang letho le le sitisang.',
  v2n:'Se se Neng se Tla Nna', v2t:'E ntle, e tlhagisang, ga e bonale.',
  v2d:'Polokego jaaka sengwe se o sa nahaneng ka sona gape. Motse o sena o tlhokomela.',
  v3n:'Mowatle', v3t:'E bulegileng, go gololesegile, go botlhe.',
  v3d:'Go botlhe ba ba tsamayang mo motseng, ka mabaka afe, nako efe kapa efe.',
  v4n:'Nyewe ya Meraka', v4t:'Ya setheo, bogolo jwa peeletso.',
  v4d:'Nyewe ya mmuso ya moruo wa R24.5bn wa Kapa. Go bapeeli-tšhelete le bareetsi ba motse.',
  r1n:'Vault ya gago', r1t:'Moratwi o itokisetseng go gaisa la motse.',
  r1d:'VibeVault ya gago ke moratwi ya nahana ka ofela pele o kopa — mokotlane o babalwa, mogala o batle, oka ba gae o ipagile. Yele e yo gago e lo gontsha go gona o ka lokela go nahana sentle. Gano feela o na.',
  r2n:'Se se Neng se Tla Nna', r2t:'Polokego, kwa ntle ga lentsu.',
  r2d:'VibeVault ya gago ke seo Kapa se nang teng ha se bereka sentle — polokego e se le sengwe se o se e bapiyang, empa e le mowa. E se e teng.',
  r3n:'Phetolelo ya Mowatle', r3t:'Motse, wa gago gotlhe.',
  r3d:'VibeVault ya gago e tsamaya o tsamaya — poloko, go palama, polokego le tlhokomelo.',
  r4n:'Nyewe ya Meraka', r4t:'Metsotso e tlhokwang ya Kapa.',
  r4d:'VibeVault ya gago ke khanoformo ya peeletso moruo wa R24.5 billion o neng o haha.'
},

// TSHIVENDA — ⚠️ Verify with native speaker
ve: {
  lp:'Nwalela luambo lwau', ct:'Bvela phanda →', ln:'Tshenetsho yaṋu yoṱhe i bvela phanda nga luambo lwo nwalaho',
  eb:'Hu si na u dzhena', tg:'Mbudziso ṱharu.\nVibeVault yaṋu.', sg:'Fhindula nga nḓila ya mbilu — u humbula zwi a fhindula.',
  bg:'Thoma →', sk:'shuma ikhwishiri — nthoniseni zwiravho zwoṱhe', sn:'ri do lushea kuitele kha muno', // ⚠️ Verify with native speaker
  ec:'Zwine na zwi nanga, nga ṱhoḓo', ar2:'Nḓila dzoṱhe dzi ya afho.',
  bs:'Mihumbulo ina ya VibeVault. Iyo ṋwe yayo ndi naṋu.',
  ev:'Dzhena kha iyi mihumbulo →', bk:'← hone, ndi a takalela muvhigo',
  qo:'Mbudziso {n} kha 3', yv:'VibeVault yaṋu', ta:'← Linga hafhu', et:'Dzhena kha iyi mihumbulo ↗',
  q1:'Kapa, vhusiku. Ndi nnyi ane a vha wa ndeme zwino?',
  q1a:'Vhathu vhane ndi na vhone', q1b:'Uri thaidulu iyi i si kone u phazamisa',
  q1c:'Hune nda si si tshimbila', q1d:'Uri muta uyu u nga vha mini',
  q2:'Hu tshi ri zwa ndeme yawo, vhukhethelo vhu fanela u ḓivhiwa sa...',
  q2a:'Muthu ane a ni ṱhogomela nga nnete', q2b:'Thinyelwa hune ha sa humbulwi',
  q2c:'Zwe zwi si ngo ri longa', q2d:'Zwishumiswa zwa tshilimo zwo timelaho',
  q3:'Muta une wa ṱhogomela nga nnete u ri nea...',
  q3a:'Fhethu hune ra khou kovhekana', q3b:'Vhusiku vhu si na mangoho',
  q3c:'Zwifhio zwoṱhe u tshimbila ḓivhazwakale', q3d:'Zwishumiswa zwi tshilaho vhugala ha vhasunguli',
  v1n:'Vault yaṋu', v1t:'Murangaphanda. Lufuno, muthu, u na.',
  v1d:'VibeVault i na u si vho budziswa — bhagi i halangwe, foni i balanywe, oka hayani i shumele. Kha vhathu vhoṱhe vhane vha khou rata vhusiku a hu na nthihi i stopakanya.',
  v2n:'Zwo fanelaho', v2t:'Zwo nakala, zwi holefhedzano, a zwi bonali.',
  v2d:'Vhukhethelo sa thinyelwa hune wa sa humbula hafhu. Muta wo tou ṱhogomela.',
  v3n:'Muphandi', v3t:'Zwi vuleaho, zwo guleaho, zwa vhathu vhoṱhe.',
  v3d:'Kha vhathu vhoṱhe vhane vha khou tshimbila mutani uyu, lwa hune ha vha, nthihi na nthihi.',
  v4n:'Ṱhoho ya Zwishumiswa', v4t:'Ya istitsheni, vhuvhili ha u vhea tshelede.',
  v4d:'Ṱhoho ya lushaka ya moralo wa R24.5bn wa Kapa. Kha vhavhei-tshelede na vharangaphanda vha muta.',
  r1n:'Vault yaṋu', r1t:'Murangaphanda o itokisetseng kha fhasi muta.',
  r1d:'VibeVault yaṋu ndi murangaphanda ana a nahana ka vhale pele o vho budziswa — bhagi i halangwe, foni i balanywe, oka hayani i shumele. Iyo na ine i ngo kuvhiya u bo ndi u vho sumbedza mina. Nje u na.',
  r2n:'Zwo fanelaho', r2t:'Vhukhethelo, ntha ha lintshi.',
  r2d:'VibeVault yaṋu ndi seo Cape Town se hwali ha se bereka zwa ayo — vhukhethelo ha si thinyelwa iyo o e bambile, emba e lufuno. I sa na.',
  r3n:'Mihumbulo ya Muphandi', r3t:'Muta, waṋu nga ṱhoḓo.',
  r3d:'VibeVault yaṋu i tshimbila na ṋu tshimbilaho — u vhona, u dzhena, vhukhethelo na ṱhogomelo.',
  r4n:'Ṱhoho ya Zwishumiswa', r4t:'Tshifhinga tsho nangaho tsha lushaka lwa Kapa.',
  r4d:'VibeVault yaṋu ndi ṱhoho ya u vhea tshelede iyo moralo wa R24.5 bilioni wo akhaho.'
},

// DEUTSCH
de: {
  lp:'Wählen Sie Ihre Sprache', ct:'Weiter →', ln:'Ihre vollständige Erfahrung wird in Ihrer gewählten Sprache fortgesetzt',
  eb:'Bevor Sie eintreten', tg:'Drei Fragen.\nIhr VibeVault.', sg:'Antworten Sie instinktiv — Nachdenken bremst.',
  bg:'Beginnen →', sk:'Quiz überspringen — alle Versionen anzeigen', sn:'wir respektieren deine Entscheidungsfreiheit hier',
  ec:'Ihre Entscheidung, vollständig', ar2:'Alle Wege führen hierher.',
  bs:'Vier Versionen von VibeVault. Eine davon ist unverkennbar Sie.',
  ev:'Diese Version betreten →', bk:'← eigentlich bin ich neugierig auf das Spiel',
  qo:'Frage {n} von 3', yv:'Ihr VibeVault', ta:'← Noch einmal versuchen', et:'Diese Version betreten ↗',
  q1:'Kapstadt, Mitternacht. Was ist jetzt am wichtigsten?',
  q1a:'Mit wem ich zusammen bin', q1b:'Dass dieser Moment unantastbar ist',
  q1c:'Wo ich noch nicht war', q1d:'Was diese Stadt werden kann',
  q2:'Im besten Fall sollte Sicherheit sich anfühlen wie...',
  q2a:'Jemand, der wirklich für mich da ist', q2b:'Etwas, an das man nie denkt',
  q2c:'Etwas, das uns nie aufhält', q2d:'Infrastruktur, die einfach funktioniert',
  q3:'Eine Stadt, die wirklich sorgt, gibt uns...',
  q3a:'Einen Ort, wo wir hingehören', q3b:'Eine Nacht ohne jede Sorge',
  q3c:'Jeden Grund, weiterzuforschen', q3d:'Infrastruktur, die ihre Gründer überlebt',
  v1n:'Ihr Vault', v1t:'Der Freund. Warm, menschlich, präsent.',
  v1d:'VibeVault ist da, bevor Sie fragen — Tasche gehalten, Handy geladen, Heimfahrt geregelt. Für alle, die einen Abend ohne Ablenkung wollen.',
  v2n:'Das Unvermeidliche', v2t:'Elegant, nahtlos, unsichtbar.',
  v2d:'Sicherheit als etwas, an das man nie wieder denkt. Eine Stadt, die bereits dafür gesorgt hat.',
  v3n:'Der Entdecker', v3t:'Offen, frei, für alle.',
  v3d:'Für alle, die diese Stadt durchqueren, aus welchem Grund auch immer, jederzeit.',
  v4n:'Infrastrukturfall', v4t:'Institutionell, investitionsgeeignet.',
  v4d:'Der bürgerliche Fall für Kapstadts R24,5-Mrd.-Wirtschaft. Für Investoren und Stadtpartner.',
  r1n:'Ihr Vault', r1t:'Der zuverlässigste Freund der Stadt.',
  r1d:'VibeVault für Sie ist der Freund, der an alles gedacht hat, bevor Sie fragen — Tasche gehalten, Handy geladen, Heimfahrt geregelt. Der, der Sie nie das Gefühl gibt, besser hätten planen sollen. Sie sind einfach dabei.',
  r2n:'Das Unvermeidliche', r2t:'Sicherheit, ohne das Wort.',
  r2d:'VibeVault für Sie ist das, was Kapstadt fühlt, wenn es genau funktioniert — Sicherheit nicht als etwas, das Sie festhalten, sondern als die Luft. Einfach da.',
  r3n:'Die Entdecker-Edition', r3t:'Die Stadt, vollständig Ihre.',
  r3d:'VibeVault bewegt sich, wenn Sie sich bewegen — Lagerung, Fahrten, Sicherheit und Fürsorge.',
  r4n:'Der Infrastrukturfall', r4t:'Kapstadts prägender bürgerlicher Moment.',
  r4d:'VibeVault ist die Investitionsthese, auf die eine R24,5-Milliarden-Wirtschaft hingearbeitet hat.'
},

// SCHWEIZERDEUTSCH (de-CH) — same content as de; formal Swiss German = Hochdeutsch
'de-CH': null,  // JS: if lang === 'de-CH', use T['de']

// FRANÇAIS
fr: {
  lp:'Choisissez votre langue', ct:'Continuer →', ln:'Votre expérience complète continue dans la langue choisie',
  eb:'Avant d\'entrer', tg:'Trois questions.\nVotre VibeVault.', sg:'Répondez instinctivement — la réflexion fait obstacle.',
  bg:'Commencer →', sk:'passer le quiz — montrer toutes les versions', sn:'nous respectons ta liberté de choix ici',
  ec:'Votre choix, entièrement', ar2:'Tous les chemins mènent ici.',
  bs:'Quatre versions de VibeVault. L\'une d\'elles est incontestablement vous.',
  ev:'Accéder à cette version →', bk:'← en fait, le jeu m\'intéresse',
  qo:'Question {n} sur 3', yv:'Votre VibeVault', ta:'← Recommencer', et:'Accéder à cette version ↗',
  q1:'Le Cap, minuit. Qu\'est-ce qui compte le plus maintenant ?',
  q1a:'Avec qui je suis', q1b:'Que ce moment soit intouchable',
  q1c:'Là où je n\'ai pas encore exploré', q1d:'Ce que cette ville pourrait devenir',
  q2:'À son meilleur, la sécurité devrait ressembler à...',
  q2a:'Quelqu\'un qui me soutient vraiment', q2b:'Quelque chose à quoi on ne pense jamais',
  q2c:'Quelque chose qui ne nous ralentit jamais', q2d:'Une infrastructure qui fonctionne simplement',
  q3:'Une ville qui prend vraiment soin nous donne...',
  q3a:'Un endroit où nous appartenons', q3b:'Une nuit sans le moindre souci',
  q3c:'Toutes les raisons de continuer à explorer', q3d:'Une infrastructure qui dépasse ses fondateurs',
  v1n:'Votre Vault', v1t:'L\'Ami. Chaleureux, humain, présent.',
  v1d:'VibeVault est là avant que vous le demandiez — sac en main, téléphone chargé, retour organisé. Pour tous ceux qui veulent une soirée sans rien dans le chemin.',
  v2n:'L\'Inévitable', v2t:'Élégant, fluide, invisible.',
  v2d:'La sécurité comme quelque chose à quoi on ne pense plus jamais. Une ville qui s\'en est déjà occupée.',
  v3n:'L\'Explorateur', v3t:'Ouvert, libre, pour tous.',
  v3d:'Pour tous ceux qui traversent cette ville, pour n\'importe quelle raison, à tout moment.',
  v4n:'Dossier Infrastructurel', v4t:'Institutionnel, de qualité investissement.',
  v4d:'Le dossier civique pour l\'économie de R24,5 milliards du Cap. Pour les investisseurs et les partenaires.',
  r1n:'Votre Vault', r1t:'L\'ami le plus préparé de la ville.',
  r1d:'VibeVault pour vous est l\'ami qui a pensé à tout avant que vous le demandiez — sac en main, téléphone chargé, retour organisé. Celui qui ne vous laisse jamais penser que vous auriez dû mieux planifier. Vous êtes juste là.',
  r2n:'L\'Inévitable', r2t:'La sécurité, sans le mot.',
  r2d:'VibeVault pour vous est ce que Le Cap ressent quand il fonctionne exactement comme il faut — la sécurité pas comme quelque chose que vous tenez, mais comme l\'air. Déjà là.',
  r3n:'L\'Édition Explorateur', r3t:'La ville, entièrement à vous.',
  r3d:'VibeVault pour vous se déplace quand vous vous déplacez — stockage, trajets, sécurité et soin.',
  r4n:'Le Dossier Infrastructurel', r4t:'Le moment civique décisif du Cap.',
  r4d:'VibeVault pour vous est la thèse d\'investissement vers laquelle une économie de R24,5 milliards a travaillé.'
},

// ESPAÑOL
es: {
  lp:'Selecciona tu idioma', ct:'Continuar →', ln:'Tu experiencia completa continúa en el idioma seleccionado',
  eb:'Antes de entrar', tg:'Tres preguntas.\nTu VibeVault.', sg:'Responde instintivamente — pensar lo complica.',
  bg:'Comenzar →', sk:'salta el cuestionario — ve todas las versiones', sn:'respetamos tu libertad de elección aquí',
  ec:'Tu decisión, completamente', ar2:'Todos los caminos llevan aquí.',
  bs:'Cuatro versiones de VibeVault. Una de ellas es inconfundiblemente tú.',
  ev:'Acceder a esta versión →', bk:'← en realidad, me interesa el juego',
  qo:'Pregunta {n} de 3', yv:'Tu VibeVault', ta:'← Intentar de nuevo', et:'Acceder a esta versión ↗',
  q1:'Ciudad del Cabo, medianoche. ¿Qué importa más ahora mismo?',
  q1a:'Con quién estoy', q1b:'Que este momento sea intocable',
  q1c:'Donde aún no he explorado', q1d:'Lo que esta ciudad podría llegar a ser',
  q2:'En su máxima expresión, la seguridad debería sentirse como...',
  q2a:'Alguien que realmente te tiene', q2b:'Algo en lo que nunca piensas',
  q2c:'Algo que nunca nos frena', q2d:'Infraestructura que simplemente funciona',
  q3:'Una ciudad que realmente se preocupa nos da...',
  q3a:'Un lugar donde pertenecemos', q3b:'Una noche sin ninguna preocupación',
  q3c:'Todas las razones para seguir explorando', q3d:'Infraestructura que supera a sus fundadores',
  v1n:'Tu Vault', v1t:'El Amigo. Cálido, humano, presente.',
  v1d:'VibeVault está ahí antes de que pidas — mochila sujeta, teléfono cargado, viaje a casa resuelto. Para todos los que quieren una noche sin nada en el camino.',
  v2n:'Lo Inevitable', v2t:'Elegante, fluido, invisible.',
  v2d:'La seguridad como algo en lo que nunca volverás a pensar. Una ciudad que ya se ha encargado.',
  v3n:'El Explorador', v3t:'Abierto, libre, para todos.',
  v3d:'Para todos los que se mueven por esta ciudad, por cualquier razón, en cualquier momento.',
  v4n:'Caso de Infraestructura', v4t:'Institucional, grado de inversión.',
  v4d:'El caso cívico para la economía de R24,5 mil millones de Ciudad del Cabo. Para inversores y socios.',
  r1n:'Tu Vault', r1t:'El amigo más preparado de la ciudad.',
  r1d:'VibeVault para ti es el amigo que pensó en todo antes de que pidieras — mochila sujeta, teléfono cargado, viaje a casa resuelto. El que nunca te hace sentir que deberías haber planeado mejor. Solo estás presente.',
  r2n:'Lo Inevitable', r2t:'Seguridad, sin la palabra.',
  r2d:'VibeVault para ti es lo que Ciudad del Cabo se siente como cuando funciona exactamente como debe — seguridad no como algo que sostienes, sino como el aire. Ya está ahí.',
  r3n:'La Edición Explorador', r3t:'La ciudad, completamente tuya.',
  r3d:'VibeVault para ti se mueve cuando te mueves — almacenamiento, viajes, seguridad y cuidado.',
  r4n:'El Caso de Infraestructura', r4t:'El momento cívico decisivo de Ciudad del Cabo.',
  r4d:'VibeVault para ti es la tesis de inversión hacia la que ha trabajado una economía de R24,5 mil millones.'
},

// PORTUGUÊS
pt: {
  lp:'Selecione seu idioma', ct:'Continuar →', ln:'Sua experiência completa continua no idioma selecionado',
  eb:'Antes de entrar', tg:'Três perguntas.\nO seu VibeVault.', sg:'Responda instintivamente — pensar atrapalha.',
  bg:'Começar →', sk:'pule o questionário — veja todas as versões', sn:'respeitamos tua liberdade de escolha aqui',
  ec:'Sua escolha, totalmente', ar2:'Todos os caminhos levam aqui.',
  bs:'Quatro versões do VibeVault. Uma delas é você.',
  ev:'Acessar esta versão →', bk:'← na verdade, estou curioso sobre o jogo',
  qo:'Pergunta {n} de 3', yv:'O seu VibeVault', ta:'← Tentar novamente', et:'Acessar esta versão ↗',
  q1:'Cidade do Cabo, meia-noite. O que importa mais agora?',
  q1a:'Com quem estou', q1b:'Que este momento seja intocável',
  q1c:'Onde ainda não explorei', q1d:'O que esta cidade pode se tornar',
  q2:'Em seu melhor, a segurança deveria parecer...',
  q2a:'Alguém que realmente está do seu lado', q2b:'Algo em que você nunca pensa',
  q2c:'Algo que nunca nos atrasa', q2d:'Infraestrutura que simplesmente funciona',
  q3:'Uma cidade que realmente se importa nos dá...',
  q3a:'Um lugar onde pertencemos', q3b:'Uma noite sem nenhuma preocupação',
  q3c:'Todas as razões para continuar explorando', q3d:'Infraestrutura que supera seus fundadores',
  v1n:'O seu Vault', v1t:'O Amigo. Acolhedor, humano, presente.',
  v1d:'O VibeVault está lá antes de você pedir — bolsa segurada, telefone carregado, volta para casa resolvida. Para quem quer uma noite sem nada no caminho.',
  v2n:'O Inevitável', v2t:'Elegante, fluido, invisível.',
  v2d:'Segurança como algo em que você nunca mais pensa. Uma cidade que já cuidou disso.',
  v3n:'O Explorador', v3t:'Aberto, livre, para todos.',
  v3d:'Para todos que se movem por esta cidade, por qualquer razão, a qualquer momento.',
  v4n:'Caso de Infraestrutura', v4t:'Institucional, grau de investimento.',
  v4d:'O caso cívico para a economia de R24,5 bilhões da Cidade do Cabo. Para investidores e parceiros.',
  r1n:'O seu Vault', r1t:'O amigo mais preparado da cidade.',
  r1d:'O VibeVault para você é o amigo que pensou em tudo antes de você pedir — bolsa segurada, telefone carregado, volta para casa resolvida. Aquele que nunca te faz sentir que deveria ter planejado melhor. Você só precisa estar presente.',
  r2n:'O Inevitável', r2t:'Segurança, sem a palavra.',
  r2d:'O VibeVault para você é o que Cidade do Cabo sente quando funciona exatamente como deveria — segurança não como algo que você segura, mas como o ar. Já está lá.',
  r3n:'A Edição Explorador', r3t:'A cidade, completamente sua.',
  r3d:'O VibeVault para você se move quando você se move — armazenamento, viagens, segurança e cuidado.',
  r4n:'O Caso de Infraestrutura', r4t:'O momento cívico decisivo da Cidade do Cabo.',
  r4d:'O VibeVault para você é a tese de investimento para a qual uma economia de R24,5 bilhões trabalhou.'
},

// ITALIANO
it: {
  lp:'Seleziona la tua lingua', ct:'Continua →', ln:'La tua esperienza completa continua nella lingua selezionata',
  eb:'Prima di entrare', tg:'Tre domande.\nIl tuo VibeVault.', sg:'Rispondi istintivamente — pensare è d\'ostacolo.',
  bg:'Inizia →', sk:'salta il quiz — mostrami tutte le versioni', sn:'rispettiamo la tua libertà di scelta qui',
  ec:'La tua scelta, completamente', ar2:'Tutte le strade portano qui.',
  bs:'Quattro versioni di VibeVault. Una di loro è inconfondibilmente te.',
  ev:'Accedi a questa versione →', bk:'← in realtà sono curioso del gioco',
  qo:'Domanda {n} di 3', yv:'Il tuo VibeVault', ta:'← Riprova', et:'Accedi a questa versione ↗',
  q1:'Città del Capo, mezzanotte. Cosa conta di più adesso?',
  q1a:'Con chi sono', q1b:'Che questo momento sia intoccabile',
  q1c:'Dove non ho ancora esplorato', q1d:'Cosa potrebbe diventare questa città',
  q2:'Alla sua meglio, la sicurezza dovrebbe sembrare...',
  q2a:'Qualcuno che ti sostiene davvero', q2b:'Qualcosa a cui non pensi mai',
  q2c:'Qualcosa che non ci ferma mai', q2d:'Infrastrutture che semplicemente funzionano',
  q3:'Una città che si prende davvero cura ci dà...',
  q3a:'Un posto dove apparteniamo', q3b:'Una notte senza nessuna preoccupazione',
  q3c:'Ogni ragione per continuare ad esplorare', q3d:'Infrastrutture che sopravvivono ai fondatori',
  v1n:'Il tuo Vault', v1t:'L\'Amico. Caldo, umano, presente.',
  v1d:'VibeVault è lì prima che tu chieda — borsa in mano, telefono carico, viaggio a casa risolto. Per chi vuole una sera senza nulla nel cammino.',
  v2n:'L\'Inevitabile', v2t:'Elegante, fluido, invisibile.',
  v2d:'La sicurezza come qualcosa a cui non si pensa mai più. Una città che se ne è già occupata.',
  v3n:'L\'Esploratore', v3t:'Aperto, libero, per tutti.',
  v3d:'Per tutti coloro che si muovono in questa città, per qualsiasi motivo, in qualsiasi momento.',
  v4n:'Caso Infrastrutturale', v4t:'Istituzionale, grado di investimento.',
  v4d:'Il caso civico per l\'economia da R24,5 miliardi di Città del Capo. Per investitori e partner.',
  r1n:'Il tuo Vault', r1t:'L\'amico più preparato della città.',
  r1d:'VibeVault per te è l\'amico che ha pensato a tutto prima che tu chiedessi — borsa in mano, telefono carico, viaggio a casa risolto. Quello che non ti fa mai sentire che avresti dovuto pianificare meglio. Sei semplicemente lì.',
  r2n:'L\'Inevitabile', r2t:'Sicurezza, senza la parola.',
  r2d:'VibeVault per te è quello che Città del Capo sente quando funziona esattamente come dovrebbe — la sicurezza non come qualcosa che tieni, ma come l\'aria. È già lì.',
  r3n:'L\'Edizione Esploratore', r3t:'La città, completamente tua.',
  r3d:'VibeVault per te si muove quando ti muovi — deposito, viaggi, sicurezza e cura.',
  r4n:'Il Caso Infrastrutturale', r4t:'Il momento civico decisivo di Città del Capo.',
  r4d:'VibeVault per te è la tesi di investimento verso cui ha lavorato un\'economia da R24,5 miliardi.'
},

// NEDERLANDS
nl: {
  lp:'Selecteer uw taal', ct:'Doorgaan →', ln:'Uw volledige ervaring gaat verder in de gekozen taal',
  eb:'Voordat u binnengaat', tg:'Drie vragen.\nUw VibeVault.', sg:'Antwoord instinctief — nadenken staat in de weg.',
  bg:'Beginnen →', sk:'sla de quiz over — toon alle versies', sn:'we respecteren je vrijheid van keuze hier',
  ec:'Uw keuze, volledig', ar2:'Alle wegen leiden hier naartoe.',
  bs:'Vier versies van VibeVault. Een ervan bent u onmiskenbaar.',
  ev:'Toegang tot deze versie →', bk:'← eigenlijk ben ik nieuwsgierig naar het spel',
  qo:'Vraag {n} van 3', yv:'Uw VibeVault', ta:'← Opnieuw proberen', et:'Toegang tot deze versie ↗',
  q1:'Kaapstad, middernacht. Wat is nu het belangrijkst?',
  q1a:'Met wie ik ben', q1b:'Dat dit moment onaantastbaar is',
  q1c:'Waar ik nog niet ben geweest', q1d:'Wat deze stad kan worden',
  q2:'Op zijn best zou veiligheid moeten voelen als...',
  q2a:'Iemand die er echt voor je is', q2b:'Iets waar je nooit aan denkt',
  q2c:'Iets dat ons nooit ophoudt', q2d:'Infrastructuur die gewoon werkt',
  q3:'Een stad die echt geeft geeft ons...',
  q3a:'Een plek waar we thuishoren', q3b:'Een nacht zonder enige zorg',
  q3c:'Elke reden om te blijven ontdekken', q3d:'Infrastructuur die haar oprichters overleeft',
  v1n:'Uw Vault', v1t:'De Vriend. Warm, menselijk, aanwezig.',
  v1d:'VibeVault is er voordat u eraan vraagt — tas vastgehouden, telefoon opgeladen, thuisreis geregeld. Voor iedereen die een avond zonder hindernissen wil.',
  v2n:'Het Onvermijdelijke', v2t:'Elegant, naadloos, onzichtbaar.',
  v2d:'Veiligheid als iets waar u nooit meer aan denkt. Een stad die er al voor gezorgd heeft.',
  v3n:'De Ontdekker', v3t:'Open, vrij, voor iedereen.',
  v3d:'Voor iedereen die door deze stad beweegt, om welke reden dan ook, op elk moment.',
  v4n:'Infrastructuurzaak', v4t:'Institutioneel, investeringswaardig.',
  v4d:'De maatschappelijke zaak voor Kaapstads R24,5 miljard economie. Voor investeerders en stadspartners.',
  r1n:'Uw Vault', r1t:'De meest voorbereide vriend van de stad.',
  r1d:'VibeVault voor u is de vriend die aan alles heeft gedacht voordat u eraan vraagt — tas vastgehouden, telefoon opgeladen, thuisreis geregeld. Degene die u nooit laat voelen dat u beter had kunnen plannen. U bent gewoon aanwezig.',
  r2n:'Het Onvermijdelijke', r2t:'Veiligheid, zonder het woord.',
  r2d:'VibeVault voor u is wat Kaapstad voelt wanneer het precies goed werkt — veiligheid niet als iets wat u vasthoudt, maar als de lucht. Al aanwezig.',
  r3n:'De Ontdekker Editie', r3t:'De stad, volledig van u.',
  r3d:'VibeVault voor u beweegt wanneer u beweegt — opslag, ritten, veiligheid en zorg.',
  r4n:'De Infrastructuurzaak', r4t:'Kaapstads bepalend maatschappelijk moment.',
  r4d:'VibeVault voor u is de investeringsthese waar een economie van R24,5 miljard naar heeft gebouwd.'
},

// SVENSKA
sv: {
  lp:'Välj ditt språk', ct:'Fortsätt →', ln:'Din fullständiga upplevelse fortsätter på det valda språket',
  eb:'Innan du går in', tg:'Tre frågor.\nDin VibeVault.', sg:'Svara instinktivt — att tänka är i vägen.',
  bg:'Börja →', sk:'hoppa över testet — visa alla versioner', sn:'vi respekterar din frihet att välja här',
  ec:'Ditt val, helt och hållet', ar2:'Alla vägar leder hit.',
  bs:'Fyra versioner av VibeVault. En av dem är helt enkelt du.',
  ev:'Gå till denna version →', bk:'← faktiskt är jag nyfiken på spelet',
  qo:'Fråga {n} av 3', yv:'Din VibeVault', ta:'← Försök igen', et:'Gå till denna version ↗',
  q1:'Kapstaden, midnatt. Vad spelar störst roll just nu?',
  q1a:'Vem jag är med', q1b:'Att detta ögonblick är orörbart',
  q1c:'Var jag inte utforskat ännu', q1d:'Vad den här staden kan bli',
  q2:'Som bäst borde säkerhet kännas som...',
  q2a:'Någon som verkligen finns där för en', q2b:'Något man aldrig tänker på',
  q2c:'Något som aldrig bromsar oss', q2d:'Infrastruktur som helt enkelt fungerar',
  q3:'En stad som verkligen bryr sig ger oss...',
  q3a:'En plats där vi hör hemma', q3b:'En natt utan ett enda bekymmer',
  q3c:'Alla anledningar att fortsätta utforska', q3d:'Infrastruktur som överlever sina grundare',
  v1n:'Din Vault', v1t:'Vännen. Varm, mänsklig, närvarande.',
  v1d:'VibeVault är där innan du frågar — väska i hand, telefon laddad, hemresan löst. För alla som vill ha en kväll utan något i vägen.',
  v2n:'Det Oundvikliga', v2t:'Elegant, sömlös, osynlig.',
  v2d:'Säkerhet som något du aldrig tänker på igen. En stad som redan tagit hand om det.',
  v3n:'Utforskaren', v3t:'Öppen, fri, för alla.',
  v3d:'För alla som rör sig i den här staden, av vilken anledning som helst, när som helst.',
  v4n:'Infrastrukturfall', v4t:'Institutionellt, investeringsgrad.',
  v4d:'Det medborgerliga fallet för Kapstadens R24,5 miljarder ekonomi. För investerare och stadspartners.',
  r1n:'Din Vault', r1t:'Stadens mest förbereddaste vän.',
  r1d:'VibeVault för dig är vännen som har tänkt på allt innan du frågar — väska i hand, telefon laddad, hemresan löst. Den som aldrig gör att du känner att du borde ha planerat bättre. Du är bara där.',
  r2n:'Det Oundvikliga', r2t:'Säkerhet, utan ordet.',
  r2d:'VibeVault för dig är vad Kapstaden känns som när det fungerar exakt som det ska — säkerhet inte som något du håller i, utan som luften. Redan där.',
  r3n:'Utforskarens Upplaga', r3t:'Staden, helt din.',
  r3d:'VibeVault för dig rör sig när du rör dig — förvaring, resor, säkerhet och omsorg.',
  r4n:'Infrastrukturfallet', r4t:'Kapstadens avgörande medborgerliga stund.',
  r4d:'VibeVault för dig är investeringstesen som en R24,5 miljarder ekonomi arbetat mot.'
},

// ΕΛΛΗΝΙΚΆ
el: {
  lp:'Επιλέξτε τη γλώσσα σας', ct:'Συνέχεια →', ln:'Η πλήρης εμπειρία σας συνεχίζεται στη γλώσσα που επιλέξατε',
  eb:'Πριν μπείτε', tg:'Τρεις ερωτήσεις.\nΤο VibeVault σας.', sg:'Απαντήστε ενστικτωδώς — η σκέψη εμποδίζει.',
  bg:'Ξεκίνα →', sk:'παρακάμψτε το κουίζ — δείξτε όλες τις εκδοχές', sn:'σέβομαι την ελευθερία σας εδώ',
  ec:'Η επιλογή σας, εντελώς', ar2:'Όλοι οι δρόμοι οδηγούν εδώ.',
  bs:'Τέσσερις εκδοχές του VibeVault. Η μία είναι αναμφίβολα εσείς.',
  ev:'Είσοδος σε αυτή την εκδοχή →', bk:'← στην πραγματικότητα, έχω περιέργεια για το παιχνίδι',
  qo:'Ερώτηση {n} από 3', yv:'Το VibeVault σας', ta:'← Δοκιμή ξανά', et:'Είσοδος σε αυτή την εκδοχή ↗',
  q1:'Ακρωτήριο, μεσάνυχτα. Τι είναι πιο σημαντικό τώρα;',
  q1a:'Με ποιον είμαι', q1b:'Ότι αυτή η στιγμή είναι αδιαφόρητη',
  q1c:'Πού δεν έχω εξερευνήσει ακόμα', q1d:'Τι μπορεί να γίνει αυτή η πόλη',
  q2:'Στο καλύτερό της, η ασφάλεια θα έπρεπε να αισθάνεται σαν...',
  q2a:'Κάποιος που είναι αληθινά εκεί για σένα', q2b:'Κάτι που ποτέ δεν σκέφτεσαι',
  q2c:'Κάτι που δεν μας επιβραδύνει ποτέ', q2d:'Υποδομή που απλώς λειτουργεί',
  q3:'Μια πόλη που πραγματικά νοιάζεται μας δίνει...',
  q3a:'Ένα μέρος που ανήκουμε', q3b:'Μια νύχτα χωρίς καμία ανησυχία',
  q3c:'Κάθε λόγο να συνεχίσουμε να εξερευνούμε', q3d:'Υποδομή που επιβιώνει από τους ιδρυτές της',
  v1n:'Το Vault σας', v1t:'Ο Φίλος. Ζεστό, ανθρώπινο, παρών.',
  v1d:'Το VibeVault είναι εκεί πριν ζητήσετε — τσάντα κρατημένη, τηλέφωνο φορτισμένο, επιστροφή σπιτιού λυμένη. Για όλους που θέλουν ένα βράδυ χωρίς τίποτα στο δρόμο.',
  v2n:'Το Αναπόφευκτο', v2t:'Κομψό, απρόσκοπτο, αόρατο.',
  v2d:'Ασφάλεια ως κάτι για το οποίο ποτέ δεν σκέφτεστε ξανά. Μια πόλη που το έχει ήδη φροντίσει.',
  v3n:'Ο Εξερευνητής', v3t:'Ανοιχτό, ελεύθερο, για όλους.',
  v3d:'Για όλους που κινούνται σε αυτή την πόλη, για οποιονδήποτε λόγο, οποιαδήποτε στιγμή.',
  v4n:'Υποδομική Υπόθεση', v4t:'Θεσμικό, επενδυτικής ποιότητας.',
  v4d:'Η πολιτική υπόθεση για την οικονομία R24,5 δισ. του Ακρωτηρίου. Για επενδυτές και εταίρους.',
  r1n:'Το Vault σας', r1t:'Ο πιο προετοιμασμένος φίλος της πόλης.',
  r1d:'Το VibeVault για εσάς είναι ο φίλος που σκέφθηκε τα πάντα πριν ζητήσετε — τσάντα κρατημένη, τηλέφωνο φορτισμένο, επιστροφή σπιτιού λυμένη. Αυτός που δεν σας κάνει να νιώθετε ότι θα έπρεπε να σχεδιάσετε καλύτερα. Απλώς υπάρχετε.',
  r2n:'Το Αναπόφευκτο', r2t:'Ασφάλεια, χωρίς τη λέξη.',
  r2d:'Το VibeVault για εσάς είναι αυτό που νιώθει το Ακρωτήριο όταν λειτουργεί ακριβώς όπως πρέπει — ασφάλεια όχι ως κάτι που κρατάτε, αλλά ως ο αέρας. Ήδη εδώ.',
  r3n:'Η Έκδοση Εξερευνητής', r3t:'Η πόλη, εντελώς δική σας.',
  r3d:'Το VibeVault για εσάς κινείται όταν κινείστε — αποθήκευση, μεταφορές, ασφάλεια και φροντίδα.',
  r4n:'Η Υποδομική Υπόθεση', r4t:'Η καθοριστική πολιτική στιγμή του Ακρωτηρίου.',
  r4d:'Το VibeVault για εσάς είναι η επενδυτική θέση που χτίστηκε μια οικονομία R24,5 δισ.'
},

// РУССКИЙ
ru: {
  lp:'Выберите ваш язык', ct:'Продолжить →', ln:'Весь ваш опыт продолжится на выбранном языке',
  eb:'Прежде чем войти', tg:'Три вопроса.\nВаш VibeVault.', sg:'Отвечайте инстинктивно — обдумывание мешает.',
  bg:'Начать →', sk:'пропустить опрос — показать все версии', sn:'мы уважаем вашу свободу выбора здесь',
  ec:'Ваш выбор, полностью', ar2:'Все дороги ведут сюда.',
  bs:'Четыре версии VibeVault. Одна из них — это вы.',
  ev:'Войти в эту версию →', bk:'← на самом деле, мне интересна игра',
  qo:'Вопрос {n} из 3', yv:'Ваш VibeVault', ta:'← Попробовать снова', et:'Войти в эту версию ↗',
  q1:'Кейптаун, полночь. Что сейчас важнее всего?',
  q1a:'С кем я нахожусь', q1b:'Чтобы этот момент был неприкасаемым',
  q1c:'Куда я ещё не заглядывал', q1d:'Чем может стать этот город',
  q2:'В лучшем своём проявлении безопасность должна ощущаться как...',
  q2a:'Кто-то, кто искренне на вашей стороне', q2b:'То, о чём никогда не думаешь',
  q2c:'То, что никогда не тормозит нас', q2d:'Инфраструктура, которая просто работает',
  q3:'Город, который по-настоящему заботится, даёт нам...',
  q3a:'Место, где мы чувствуем себя своими', q3b:'Ночь без единой тревоги',
  q3c:'Все причины продолжать исследовать', q3d:'Инфраструктуру, которая переживёт своих создателей',
  v1n:'Ваш Vault', v1t:'Друг. Тёплый, человечный, присутствующий.',
  v1d:'VibeVault здесь до того, как вы спросите — сумка в руках, телефон заряжен, дорога домой решена. Для всех, кто хочет вечер без помех.',
  v2n:'Неизбежное', v2t:'Изящное, безупречное, невидимое.',
  v2d:'Безопасность как то, о чём больше никогда не думаешь. Город, который уже позаботился об этом.',
  v3n:'Исследователь', v3t:'Открытое, свободное, для всех.',
  v3d:'Для всех, кто движется по этому городу, по любой причине, в любое время.',
  v4n:'Инфраструктурное дело', v4t:'Институциональное, инвестиционного качества.',
  v4d:'Гражданское дело для экономики Кейптауна в R24,5 млрд. Для инвесторов и городских партнёров.',
  r1n:'Ваш Vault', r1t:'Самый подготовленный друг города.',
  r1d:'VibeVault для вас — друг, который подумал обо всём до того, как вы спросите — сумка в руках, телефон заряжен, дорога домой решена. Тот, кто никогда не даст вам почувствовать, что вы должны были лучше спланировать. Вы просто там.',
  r2n:'Неизбежное', r2t:'Безопасность без слова.',
  r2d:'VibeVault для вас — то, что ощущается Кейптаун, когда всё работает идеально — безопасность не как то, что вы держите, а как воздух. Уже есть.',
  r3n:'Издание «Исследователь»', r3t:'Город — полностью ваш.',
  r3d:'VibeVault для вас движется вместе с вами — хранение, поездки, безопасность и забота.',
  r4n:'Инфраструктурное дело', r4t:'Определяющий гражданский момент Кейптауна.',
  r4d:'VibeVault для вас — инвестиционная теза, к которой двигалась экономика в R24,5 млрд.'
},

// العربية — RTL
ar: {
  lp:'اختر لغتك', ct:'متابعة →', ln:'تستمر تجربتك الكاملة باللغة التي اخترتها',
  eb:'قبل الدخول', tg:'ثلاثة أسئلة.\nVibeVault الخاص بك.', sg:'أجب بشكل غريزي — التفكير يعيق.',
  bg:'ابدأ →', sk:'تخطى الاختبار — أرني جميع الإصدارات', sn:'نحترم حريتك في الاختيار هنا',
  ec:'اختيارك تماماً', ar2:'جميع الطرق تقود إلى هنا.',
  bs:'أربعة إصدارات من VibeVault. واحد منهم أنت بلا شك.',
  ev:'ادخل إلى هذا الإصدار →', bk:'← في الواقع، أنا فضولي بشأن اللعبة',
  qo:'السؤال {n} من 3', yv:'VibeVault الخاص بك', ta:'← حاول مرة أخرى', et:'ادخل إلى هذا الإصدار ↗',
  q1:'كيب تاون، منتصف الليل. ما الأهم الآن؟',
  q1a:'مع من أكون', q1b:'أن هذه اللحظة محرمة',
  q1c:'المكان الذي لم أستكشفه بعد', q1d:'ما يمكن أن تصبحه هذه المدينة',
  q2:'في أفضل حالاتها، ينبغي أن يشعر الأمان مثل...',
  q2a:'شخص يدعمك بصدق', q2b:'شيء لا تفكر فيه أبداً',
  q2c:'شيء لا يبطئنا أبداً', q2d:'بنية تحتية تعمل ببساطة',
  q3:'مدينة تهتم حقاً تمنحنا...',
  q3a:'مكاناً ننتمي إليه', q3b:'ليلة بلا أي قلق',
  q3c:'كل سبب لمواصلة الاستكشاف', q3d:'بنية تحتية تتجاوز مؤسسيها',
  v1n:'Vault الخاص بك', v1t:'الصديق. دافئ، إنساني، موجود.',
  v1d:'VibeVault موجود قبل أن تطلب — حقيبة محمولة، هاتف مشحون، الرحلة للمنزل محددة. لكل من يريد ليلة بدون حواجز.',
  v2n:'الحتمي', v2t:'أنيق، سلس، غير مرئي.',
  v2d:'الأمان كشيء لا تفكر فيه مرة أخرى. مدينة اعتنت بالفعل.',
  v3n:'المستكشف', v3t:'مفتوح، حر، للجميع.',
  v3d:'للجميع الذين يتنقلون في هذه المدينة، لأي سبب، في أي وقت.',
  v4n:'قضية البنية التحتية', v4t:'مؤسسي، درجة استثمار.',
  v4d:'القضية المدنية لاقتصاد كيب تاون بـ R24.5 مليار. للمستثمرين والشركاء.',
  r1n:'Vault الخاص بك', r1t:'الصديق الأكثر استعداداً في المدينة.',
  r1d:'VibeVault لك هو الصديق الذي فكر في كل شيء قبل أن تطلب — حقيبة محمولة، هاتف مشحون، الرحلة للمنزل محددة. من لا يجعلك تشعر أنك كان يجب أن تخطط بشكل أفضل. أنت فقط موجود.',
  r2n:'الحتمي', r2t:'الأمان، بدون الكلمة.',
  r2d:'VibeVault لك هو ما يشعر به كيب تاون عندما يعمل بشكل صحيح تماماً — الأمان ليس كشيء تمسكه، بل كالهواء. موجود بالفعل.',
  r3n:'إصدار المستكشف', r3t:'المدينة، ملكك بالكامل.',
  r3d:'VibeVault لك يتحرك عندما تتحرك — تخزين، رحلات، أمان واهتمام.',
  r4n:'قضية البنية التحتية', r4t:'اللحظة المدنية المحورية لكيب تاون.',
  r4d:'VibeVault لك هو أطروحة الاستثمار التي بنت من أجلها اقتصاد بـ R24.5 مليار.'
},

// اردو — RTL
ur: {
  lp:'اپنی زبان منتخب کریں', ct:'جاری رکھیں →', ln:'آپ کا مکمل تجربہ آپ کی منتخب کردہ زبان میں جاری رہے گا',
  eb:'داخل ہونے سے پہلے', tg:'تین سوال۔\nآپ کا VibeVault۔', sg:'فطری طور پر جواب دیں — سوچنا راستے میں آتا ہے۔',
  bg:'شروع کریں →', sk:'کوز چھوڑیں — تمام ورژن دیکھیں', sn:'ہم یہاں تمہاری خود مختاری کو احترام کرتے ہیں',
  ec:'آپ کا فیصلہ، مکمل طور پر', ar2:'سب راستے یہاں آتے ہیں۔',
  bs:'VibeVault کے چار ورژن۔ ایک واضح طور پر آپ ہے۔',
  ev:'اس ورژن میں داخل ہوں →', bk:'← دراصل، مجھے کھیل کے بارے میں جاننا ہے',
  qo:'سوال {n} از 3', yv:'آپ کا VibeVault', ta:'← دوبارہ کوشش کریں', et:'اس ورژن میں داخل ہوں ↗',
  q1:'کیپ ٹاؤن، آدھی رات۔ ابھی سب سے اہم کیا ہے؟',
  q1a:'میں کس کے ساتھ ہوں', q1b:'کہ یہ لمحہ ناقابلِ رسائی ہے',
  q1c:'جہاں میں ابھی تک نہیں گیا', q1d:'یہ شہر کیا بن سکتا ہے',
  q2:'بہترین صورت میں، حفاظت کو ایسا محسوس ہونا چاہیے جیسے...',
  q2a:'کوئی جو واقعی آپ کے ساتھ ہو', q2b:'کچھ ایسا جس کے بارے میں آپ کبھی نہیں سوچتے',
  q2c:'کچھ جو ہمیں کبھی نہیں روکتا', q2d:'انفراسٹرکچر جو بس کام کرتا ہے',
  q3:'جو شہر واقعی پرواہ کرتا ہے وہ ہمیں دیتا ہے...',
  q3a:'ایک جگہ جہاں ہم تعلق رکھتے ہیں', q3b:'ایک رات بغیر کسی پریشانی کے',
  q3c:'تلاش جاری رکھنے کی ہر وجہ', q3d:'انفراسٹرکچر جو اس کے بانیوں سے آگے جاتا ہے',
  v1n:'آپ کا Vault', v1t:'دوست۔ گرم، انسانی، موجود۔',
  v1d:'VibeVault آپ سے پہلے ہے - بیگ تھامے، فون چارج، گھر کی سواری طے۔ ہر اس شخص کے لیے جو رات بغیر کسی رکاوٹ کے چاہتا ہے۔',
  v2n:'ناگزیر', v2t:'خوبصورت، بے سلائی، غیر مرئی۔',
  v2d:'حفاظت ایک ایسی چیز کے طور پر جس کے بارے میں آپ دوبارہ کبھی نہیں سوچتے۔ وہ شہر جو پہلے ہی اس کا خیال رکھ چکا ہے۔',
  v3n:'کھوجی', v3t:'کھلا، آزاد، سب کے لیے۔',
  v3d:'ہر اس شخص کے لیے جو اس شہر میں چلتا ہے، کسی بھی وجہ سے، کسی بھی وقت۔',
  v4n:'انفراسٹرکچر کیس', v4t:'ادارہ جاتی، سرمایہ کاری کا درجہ۔',
  v4d:'کیپ ٹاؤن کی R24.5 ارب معیشت کا شہری معاملہ۔ سرمایہ کاروں اور شہری شراکت داروں کے لیے۔',
  r1n:'آپ کا Vault', r1t:'شہر کا سب سے تیار دوست۔',
  r1d:'آپ کے لیے VibeVault وہ دوست ہے جس نے آپ سے پہلے سب کچھ سوچا - بیگ تھامے، فون چارج، گھر کی سواری طے۔ وہ جو آپ کو کبھی محسوس نہیں کرتا کہ آپ کو بہتر منصوبہ بندی کرنی چاہیے تھی۔ آپ صرف موجود ہیں۔',
  r2n:'ناگزیر', r2t:'حفاظت، لفظ کے بغیر۔',
  r2d:'آپ کے لیے VibeVault وہ ہے جو کیپ ٹاون محسوس کرتا ہے جب یہ بالکل صحیح کام کرتا ہے — حفاظت اس چیز کے طور پر نہیں جو آپ پکڑتے ہیں، بلکہ ہوا کی طرح۔ پہلے ہی موجود۔',
  r3n:'کھوجی ایڈیشن', r3t:'شہر، مکمل طور پر آپ کا۔',
  r3d:'آپ کے لیے VibeVault تب چلتا ہے جب آپ چلتے ہیں — اسٹوریج، سفر، حفاظت اور دیکھ بھال۔',
  r4n:'انفراسٹرکچر کیس', r4t:'کیپ ٹاؤن کا تعین کن شہری لمحہ۔',
  r4d:'آپ کے لیے VibeVault وہ سرمایہ کاری تھیسس ہے جس کی طرف R24.5 ارب کی معیشت بڑھتی رہی ہے۔'
},

// 中文 — Simplified Mandarin
zh: {
  lp:'请选择您的语言', ct:'继续 →', ln:'您的完整体验将以所选语言继续',
  eb:'进入之前', tg:'三个问题。\n您的VibeVault。', sg:'凭直觉回答 — 思考反而会碍事。',
  bg:'开始 →', sk:'跳过测验 — 查看所有版本', sn:'我们在这里尊重你的自主权',
  ec:'完全由您决定', ar2:'条条大路通罗马。',
  bs:'VibeVault的四个版本。其中一个明确是你。',
  ev:'进入此版本 →', bk:'← 其实，我对这个游戏很感兴趣',
  qo:'第{n}题，共3题', yv:'您的VibeVault', ta:'← 重新开始', et:'进入此版本 ↗',
  q1:'开普敦，午夜。此刻什么最重要？',
  q1a:'与我同在的人', q1b:'这一刻是不可侵犯的',
  q1c:'我还未探索的地方', q1d:'这座城市能变成什么',
  q2:'在最理想的状态下，安全感应该像...',
  q2a:'一个真正支持你的人', q2b:'一件你从不需要思考的事',
  q2c:'一件永远不会拖慢我们的事', q2d:'运转顺畅的基础设施',
  q3:'真正关心我们的城市会给我们...',
  q3a:'一个我们真正归属的地方', q3b:'一个毫无烦恼的夜晚',
  q3c:'继续探索的所有理由', q3d:'比创始人更持久的基础设施',
  v1n:'您的Vault', v1t:'朋友。温暖、人性化、时刻在场。',
  v1d:'VibeVault在你开口前就在这里 — 包包拿好，手机充电，回家的路已安排。为所有想要一个没有障碍的夜晚的人。',
  v2n:'必然之选', v2t:'优雅、无缝、隐形。',
  v2d:'将安全变成您不再需要思考的事。一座已经照顾好一切的城市。',
  v3n:'探索者', v3t:'开放、自由、面向所有人。',
  v3d:'为所有行走在这座城市中的人，无论何种原因，无论何时。',
  v4n:'基础设施案例', v4t:'机构级，投资级别。',
  v4d:'为开普敦R245亿经济的社会投资案例。面向投资者和城市合作伙伴。',
  r1n:'您的Vault', r1t:'城市最周到的朋友。',
  r1d:'VibeVault对您来说是那位在您开口前就想到一切的朋友 — 包包拿好，手机充电，回家的路已安排。那位让你永远不会觉得应该计划得更好的人。你只是在当下。',
  r2n:'必然之选', r2t:'安全，无需言说。',
  r2d:'VibeVault对您来说就是开普敦运作得完美无缺时的感觉 — 安全不是你握紧的东西，而是空气。已经在那里。',
  r3n:'探索者版本', r3t:'这座城市，完全属于您。',
  r3d:'VibeVault随您移动 — 储物、出行、安全与关怀融入每一个角落。',
  r4n:'基础设施案例', r4t:'开普敦决定性的城市时刻。',
  r4d:'VibeVault对您来说是R245亿经济一直在建立的投资论点。'
},

// 繁體中文 — Traditional Chinese (Taiwan)
'zh-TW': {
  lp:'請選擇您的語言', ct:'繼續 →', ln:'您的完整體驗將以所選語言繼續',
  eb:'進入之前', tg:'三個問題。\n您的VibeVault。', sg:'憑直覺回答 — 思考反而會礙事。',
  bg:'開始 →', sk:'跳過測驗 — 查看所有版本', sn:'我們在這裡尊重你的自主權',
  ec:'完全由您決定', ar2:'條條大路通羅馬。',
  bs:'VibeVault的四個版本。其中一個明確是你。',
  ev:'進入此版本 →', bk:'← 其實，我對這個遊戲很感興趣',
  qo:'第{n}題，共3題', yv:'您的VibeVault', ta:'← 重新開始', et:'進入此版本 ↗',
  q1:'開普敦，午夜。此刻什麼最重要？',
  q1a:'與我同在的人', q1b:'這一刻是不可侵犯的',
  q1c:'我還未探索的地方', q1d:'這座城市能變成什麼',
  q2:'在最理想的狀態下，安全感應該像...',
  q2a:'一個真正支持你的人', q2b:'一件你從不需要思考的事',
  q2c:'一件永遠不會拖慢我們的事', q2d:'運轉順暢的基礎設施',
  q3:'真正關心我們的城市會給我們...',
  q3a:'一個我們真正歸屬的地方', q3b:'一個毫無煩惱的夜晚',
  q3c:'繼續探索的所有理由', q3d:'比創始人更持久的基礎設施',
  v1n:'您的Vault', v1t:'朋友。溫暖、人性化、時刻在場。',
  v1d:'VibeVault在你開口前就在這裡 — 包包拿好，手機充電，回家的路已安排。為所有想要一個沒有障礙的夜晚的人。',
  v2n:'必然之選', v2t:'優雅、無縫、隱形。',
  v2d:'將安全變成您不再需要思考的事。一座已經照顧好一切的城市。',
  v3n:'探索者', v3t:'開放、自由、面向所有人。',
  v3d:'為所有行走在這座城市中的人，無論何種原因，無論何時。',
  v4n:'基礎設施案例', v4t:'機構級，投資級別。',
  v4d:'為開普敦R245億經濟的社會投資案例。面向投資者和城市合作夥伴。',
  r1n:'您的Vault', r1t:'城市最周到的朋友。',
  r1d:'VibeVault對您來說是那位在您開口前就想到一切的朋友 — 包包拿好，手機充電，回家的路已安排。那位讓你永遠不會覺得應該計劃得更好的人。你只是在當下。',
  r2n:'必然之選', r2t:'安全，無需言說。',
  r2d:'VibeVault對您來說就是開普敦運作得完美無缺時的感覺 — 安全不是你握緊的東西，而是空氣。已經在那裡。',
  r3n:'探索者版本', r3t:'這座城市，完全屬於您。',
  r3d:'VibeVault隨您移動 — 儲物、出行、安全與關懷融入每一個角落。',
  r4n:'基礎設施案例', r4t:'開普敦決定性的城市時刻。',
  r4d:'VibeVault對您來說是R245億經濟一直在建立的投資論點。'
},

// 廣東話 — Cantonese (Traditional characters, Cantonese vocabulary)
yue: {
  lp:'揀你嘅語言', ct:'繼續 →', ln:'你嘅完整體驗將以所揀語言繼續',
  eb:'入去之前', tg:'三個問題。\n你嘅VibeVault。', sg:'憑直覺答 — 諗嘢反而礙事。',
  bg:'開始 →', sk:'跳過測驗 — 睇所有版本', sn:'我哋響呢度尊重你嘅自主權',
  ec:'完全係你嘅選擇', ar2:'條條大路通到呢度。',
  bs:'VibeVault嘅四個版本。其中一個無疑就係你。',
  ev:'入呢個版本 →', bk:'← 其實，我對呢個遊戲好感興趣',
  qo:'第{n}條問題，共3條', yv:'你嘅VibeVault', ta:'← 再試一次', et:'入呢個版本 ↗',
  q1:'開普敦，夜半。依家最緊要乜嘢？',
  q1a:'同我喺一齊嘅人', q1b:'呢一刻係摸唔到嘅',
  q1c:'我未去過嘅地方', q1d:'呢個城市可以變成點',
  q2:'最理想嘅安全感應該係...',
  q2a:'一個真心支持你嘅人', q2b:'一件你從唔使諗嘅事',
  q2c:'一件永遠唔會拖慢我哋嘅事', q2d:'運作順暢嘅基礎設施',
  q3:'真正關心我哋嘅城市會俾我哋...',
  q3a:'一個我哋真正歸屬嘅地方', q3b:'一個冇煩惱嘅夜晚',
  q3c:'繼續探索嘅所有理由', q3d:'比創辦人更持久嘅基礎設施',
  v1n:'你嘅Vault', v1t:'朋友。溫暖、人性化、就喺到。',
  v1d:'VibeVault喺你開口前就喺嗰度 — 袋袋拎住，手機充滿電，返屋企嘅路已經安排好。為所有想要一個冇嘢擋住嘅夜晚嘅人。',
  v2n:'必然之選', v2t:'優雅、無縫、隱形。',
  v2d:'令安全變成你唔再需要諗嘅嘢。一個已經打點好一切嘅城市。',
  v3n:'探索者', v3t:'開放、自由、面向所有人。',
  v3d:'為所有喺呢個城市行走嘅人，無論乜原因，無論幾時。',
  v4n:'基礎設施案例', v4t:'機構級，投資級別。',
  v4d:'為開普敦R245億經濟嘅社會投資案例。面向投資者同城市合作夥伴。',
  r1n:'你嘅Vault', r1t:'城市最周到嘅朋友。',
  r1d:'VibeVault對你嚟講係嗰位喺你開口前就諗到所有嘢嘅朋友 — 袋袋拎住，手機充滿電，返屋企嘅路已經安排好。嗰位永遠唔會令你覺得應該計劃得更好嘅人。你就喺嗰度。',
  r2n:'必然之選', r2t:'安全，唔使講。',
  r2d:'VibeVault對你嚟講就係開普敦運作得完美無缺時嘅感覺 — 安全唔係你緊握著嘅嘢，而係空氣。已經就喺到。',
  r3n:'探索者版本', r3t:'呢個城市，完全係你嘅。',
  r3d:'VibeVault隨你移動 — 儲物、出行、安全同關懷融入每個角落。',
  r4n:'基礎設施案例', r4t:'開普敦決定性嘅城市時刻。',
  r4d:'VibeVault對你嚟講係R245億經濟一直喺建立嘅投資論點。'
},

// 日本語
ja: {
  lp:'言語を選択してください', ct:'続ける →', ln:'全体の体験は選択した言語で続きます',
  eb:'入る前に', tg:'3つの質問。\nあなたのVibeVault。', sg:'直感で答えてください — 考えると邪魔になります。',
  bg:'始める →', sk:'クイズをスキップ — すべてのバージョンを見る', sn:'ここではあなたの自主性を尊重しています',
  ec:'あなたの選択、完全に', ar2:'すべての道はここに通じる。',
  bs:'VibeVaultの4つのバージョン。その1つは紛れもなくあなた。',
  ev:'このバージョンへ →', bk:'← 実は、ゲームに興味があります',
  qo:'3問中 第{n}問', yv:'あなたのVibeVault', ta:'← もう一度', et:'このバージョンへ ↗',
  q1:'ケープタウン、真夜中。今、何が一番大切ですか？',
  q1a:'一緒にいる人', q1b:'この瞬間が侵襲されない',
  q1c:'まだ探索していない場所', q1d:'この街が何になれるか',
  q2:'最高の状態で、安心感とはこのように感じるべきです...',
  q2a:'本当に味方でいてくれる人', q2b:'一度も考えないこと',
  q2c:'私たちを決して遅らせないもの', q2d:'ただ機能するインフラ',
  q3:'本当に気にかけてくれる街は私たちに与えてくれます...',
  q3a:'私たちが属せる場所', q3b:'何も心配ない夜',
  q3c:'探索し続けるすべての理由', q3d:'創設者よりも長く続くインフラ',
  v1n:'あなたのVault', v1t:'友人。温かく、人間的で、そこにいて。',
  v1d:'VibeVaultはあなたが求める前にそこにいます — バッグ持ち、携帯充電済み、帰宅ルート手配済み。何の邪魔もない夜を望むすべての人のために。',
  v2n:'必然のもの', v2t:'エレガント、シームレス、見えない。',
  v2d:'安全をもう二度と考えなくていいものに。街がすでに対処しています。',
  v3n:'エクスプローラー', v3t:'オープン、自由、すべての人のために。',
  v3d:'どんな理由でも、いつでも、この街を移動するすべての人のために。',
  v4n:'インフラ事例', v4t:'制度的、投資グレード。',
  v4d:'ケープタウンのR245億経済への市民投資事例。投資家と都市パートナー向け。',
  r1n:'あなたのVault', r1t:'街で最も思慮深い友人。',
  r1d:'VibeVaultはあなたにとって、あなたが求める前にすべてを考えてくれた友人です — バッグ持ち、携帯充電済み、帰宅ルート手配済み。より良く計画すべきだったと感じさせない人。あなたはただそこにいるだけ。',
  r2n:'必然のもの', r2t:'安全、言葉なし。',
  r2d:'VibeVaultはケープタウンが完璧に機能するときの感覚です — 安全はあなたが握るものではなく、空気です。もう存在しています。',
  r3n:'エクスプローラーエディション', r3t:'街、完全にあなたのもの。',
  r3d:'VibeVaultはあなたと一緒に動きます — 収納、移動、安全とケア。',
  r4n:'インフラ事例', r4t:'ケープタウンの決定的な市民の瞬間。',
  r4d:'VibeVaultはR245億経済が向かって来た投資論文です。'
},

// 한국어
ko: {
  lp:'언어를 선택하세요', ct:'계속하기 →', ln:'전체 경험이 선택한 언어로 계속됩니다',
  eb:'들어가기 전에', tg:'세 가지 질문。\n당신의 VibeVault。', sg:'본능적으로 답하세요 — 생각하면 방해가 됩니다.',
  bg:'시작하기 →', sk:'퀴즈 건너뛰기 — 모든 버전 보기', sn:'우리는 여기서 당신의 자유를 존중합니다',
  ec:'완전히 당신의 선택', ar2:'모든 길은 여기로 통합니다.',
  bs:'VibeVault의 네 가지 버전. 그 중 하나는 틀림없이 당신입니다.',
  ev:'이 버전으로 →', bk:'← 사실, 게임이 궁금합니다',
  qo:'3개 중 {n}번 질문', yv:'당신의 VibeVault', ta:'← 다시 시도', et:'이 버전으로 ↗',
  q1:'케이프타운, 자정. 지금 가장 중요한 것은?',
  q1a:'함께 있는 사람', q1b:'이 순간이 건드릴 수 없다는 것',
  q1c:'아직 탐험하지 않은 곳', q1d:'이 도시가 무엇이 될 수 있는지',
  q2:'최선의 상태에서, 안전함은 이렇게 느껴져야 합니다...',
  q2a:'진심으로 당신 편인 누군가', q2b:'한 번도 생각하지 않는 무언가',
  q2c:'절대 우리를 느리게 하지 않는 무언가', q2d:'그냥 작동하는 인프라',
  q3:'진정으로 배려하는 도시는 우리에게...',
  q3a:'우리가 속할 수 있는 곳', q3b:'걱정 없는 하룻밤',
  q3c:'계속 탐험할 모든 이유', q3d:'창립자들보다 오래 지속되는 인프라',
  v1n:'당신의 Vault', v1t:'친구. 따뜻하고 인간적이며, 함께 있어。',
  v1d:'VibeVault는 당신이 요청하기 전에 이미 있습니다 — 가방 들고, 휴대폰 충전, 집으로 가는 길 정렬됨. 아무것도 방해하지 않는 밤을 원하는 모든 사람을 위해.',
  v2n:'불가피한 것', v2t:'우아하고, 매끄럽고, 보이지 않는。',
  v2d:'안전을 다시는 생각할 필요 없는 것으로. 이미 처리한 도시.',
  v3n:'탐험가', v3t:'열려 있고, 자유롭고, 모두를 위한。',
  v3d:'어떤 이유로든, 언제든, 이 도시를 움직이는 모든 사람을 위해.',
  v4n:'인프라 사례', v4t:'기관급, 투자 등급。',
  v4d:'케이프타운 R245억 경제를 위한 시민 투자 사례. 투자자와 도시 파트너를 위해.',
  r1n:'당신의 Vault', r1t:'도시에서 가장 따뜻한 코너。',
  r1d:'VibeVault는 당신에게 짊어지지 않아야 할 것을 짊어지는 동반자 — 부탁 전에 존재하고, 걱정 전에 집에.',
  r2n:'불가피한 것', r2t:'안전, 대화 없이。',
  r2d:'VibeVault는 안전이 생각에서 완전히 사라질 만큼 매끄러운 인프라입니다.',
  r3n:'탐험가 에디션', r3t:'도시, 완전히 당신의 것。',
  r3d:'VibeVault는 당신과 함께 움직입니다 — 보관, 이동, 건강과 돌봄.',
  r4n:'인프라 사례', r4t:'케이프타운의 결정적인 시민의 순간。',
  r4d:'VibeVault는 R245억 경제가 향해 온 투자 논문입니다.'
},

// Kiswahili
sw: {
  lp:'Chagua lugha yako', ct:'Endelea →', ln:'Uzoefu wako wote utaendelea kwa lugha uliyochagua',
  eb:'Kabla ya kuingia', tg:'Maswali matatu.\nVibeVault yako.', sg:'Jibu kwa silika — kufikiri kunazuia.',
  bg:'Anza →', sk:'huoni hamu? nionyeshe matoleo yote', sn:'tunaheshimu uhuru wako hapa',
  ec:'Uamuzi wako, kabisa', ar2:'Njia zote zinaelekea hapa.',
  bs:'Matoleo manne ya VibeVault. Watu wanne tofauti. Pata ile inayofanana nawe.',
  ev:'Ingia toleo hili →', bk:'← kwa kweli, ninapendezwa na mchezo',
  qo:'Swali {n} kati ya 3', yv:'VibeVault yako', ta:'← Jaribu tena', et:'Ingia toleo hili ↗',
  q1:'Cape Town, usiku wa manane. Nini kina umuhimu zaidi sasa hivi?',
  q1a:'Niko na nani', q1b:'Kwamba hakuna kinachoweza kukatiza hili',
  q1c:'Mahali ambapo sijagundua bado', q1d:'Mji huu unaweza kuwa nini',
  q2:'Katika hali yake bora, usalama unapaswa kuhisi kama...',
  q2a:'Mtu anayekusaidia kweli kweli', q2b:'Kitu ambacho hufikirii kamwe',
  q2c:'Kitu ambacho hakituzuii kamwe', q2d:'Miundombinu inayofanya kazi tu',
  q3:'Mji unaojali kweli kweli unatupa...',
  q3a:'Mahali ambapo tunamiliki', q3b:'Usiku bila wasiwasi wowote',
  q3c:'Kila sababu ya kuendelea kuchunguza', q3d:'Miundombinu inayodumu zaidi ya waanzilishi wake',
  v1n:'Vault yako', v1t:'Joto, kibinadamu, rafiki.',
  v1d:'VibeVault hubeba unachostahili kubeba — na kukurejesha nyumbani salama. Kwa wote wetu.',
  v2n:'Lisilo na Budi', v2t:'Nzuri, laini, lisiloonekana.',
  v2d:'Usalama kama kitu ambacho hutafikiria tena. Mji ambao tayari umejali.',
  v3n:'Mgunduzi', v3t:'Wazi, huru, kwa wote.',
  v3d:'Kwa wote wanaosafiri katika mji huu, kwa sababu yoyote, wakati wowote.',
  v4n:'Kesi ya Miundombinu', v4t:'Kitaasisi, kiwango cha uwekezaji.',
  v4d:'Kesi ya kiraia kwa uchumi wa R24.5 bilioni wa Cape Town. Kwa wawekezaji na washirika wa jiji.',
  r1n:'Vault yako', r1t:'Kona yenye joto zaidi ya mji.',
  r1d:'VibeVault kwako ni mwenzi anayebeba usichostahili — yuko kabla hujaomba, nyumbani kabla hujasumbuka.',
  r2n:'Lisilo na Budi', r2t:'Usalama, bila mazungumzo.',
  r2d:'VibeVault kwako ni miundombinu laini kiasi kwamba usalama unatoweka kabisa kutoka kwa mawazo yako.',
  r3n:'Toleo la Mgunduzi', r3t:'Mji, wako kabisa.',
  r3d:'VibeVault kwako husogea unaposogea — uhifadhi, safari, afya na huduma.',
  r4n:'Kesi ya Miundombinu', r4t:'Wakati muhimu wa kiraia wa Cape Town.',
  r4d:'VibeVault kwako ni nadharia ya uwekezaji ambayo uchumi wa R24.5 bilioni umekuwa ukijenga.'
},

// Yorùbá
yo: {
  lp:'Yan ede rẹ', ct:'Tẹsiwaju →', ln:'Iriri rẹ ni kikun yoo tẹsiwaju ni ede ti o yan',
  eb:'Ṣaaju ki o to wọle', tg:'Awọn ibeere mẹta.\nVibeVault rẹ.', sg:'Dahun lainidena — ìrònú ń dènà.',
  bg:'Bẹrẹ →', sk:'ko si ifẹ? fi gbogbo ẹya hàn mi', sn:'a bọwọ fun ominira rẹ nibi',
  ec:'Yiyan rẹ, patapata', ar2:'Gbogbo ọna nyorisi ibi.',
  bs:'Awọn ẹya mẹrin ti VibeVault. Eniyan mẹrin ti o yatọ. Wa eyi ti o dabi rẹ.',
  ev:'Wọle si ẹya yii →', bk:'← nitootọ, mo fẹ mọ nipa ere naa',
  qo:'Ibeere {n} ninu 3', yv:'VibeVault rẹ', ta:'← Gbiyanju lẹẹkansii', et:'Wọle si ẹya yii ↗',
  q1:'Cape Town, ọganjọ oru. Kini o ṣe pataki jùlọ nisisiyi?',
  q1a:'Tí mo wà pẹ̀lú rẹ̀', q1b:'Pe ohunkohun ko le da eyi duro',
  q1c:'Ibi ti mi ko ti ṣàbẹwò sibẹ', q1d:'Ohun ti ilu yii le di',
  q2:'Ninu ipo rẹ ti o dara jùlọ, aabo yẹ ki o rilara bii...',
  q2a:'Ẹnikan ti o wa fun ọ nitootọ', q2b:'Nkan ti o kọ́ ní ìrọ̀lẹ̀',
  q2c:'Nkan ti kò dẹ́kùn wa rárá', q2d:'Amayedarí tí ń ṣiṣẹ́ nìkan',
  q3:'Ilu ti o tọ́jú wa nitootọ fún wa...',
  q3a:'Ibi ti a jẹ́ ti', q3b:'Alẹ kan láìsí ìbínú kankan',
  q3c:'Idi gbogbo lati tẹsiwaju ṣàwárí', q3d:'Amayedarí tí ó ju àwọn olùdásílẹ̀ rẹ̀ lọ',
  v1n:'Vault rẹ', v1t:'Gbigbona, eda eniyan, ọrẹ.',
  v1d:'VibeVault gbe ohun ti o kò yẹ ki o gbe — o mu ọ padà sí ilé lailewu. Fun wa gbogbo.',
  v2n:'Ohun Ti Kò Ṣee Yẹra Fún', v2t:'Ẹlẹgbẹ, alaisejemu, alaifarahan.',
  v2d:'Aabo bi ohun ti o kò tún ṣe ìrònú nípa rẹ̀. Ilu kan ti o ti tọ́jú tẹlẹ.',
  v3n:'Aṣàwárí', v3t:'Ṣíṣí, ọ̀fẹ́, fún gbogbo ènìyàn.',
  v3d:'Fun gbogbo eniyan ti o n rin ilu yii, fun idi eyikeyi, nigbakugba.',
  v4n:'Ọrọ Amayedarí', v4t:'Àjọ, ipele ìdókòwò.',
  v4d:'Ọrọ ilu fun ọrọ-aje R24.5 bílíọ̀nù Cape Town. Fun awọn onijọba ati awọn alabaṣiṣẹpọ ilu.',
  r1n:'Vault rẹ', r1t:'Igun ti o gbona jùlọ ti ilu.',
  r1d:'VibeVault fun ọ ni ẹlẹgbẹ ti o gbe ohun ti o kò yẹ ki o gbe — o wa ṣaaju ki o beere, sí ilé ṣaaju ki o yọ.',
  r2n:'Ohun Ti Kò Ṣee Yẹra Fún', r2t:'Aabo, láìsí ìjíròrò.',
  r2d:'VibeVault fun ọ ni amayedarí ti o jẹ alaisejemu ti aabo parẹ patapata lọ ọkan rẹ.',
  r3n:'Ẹya Aṣàwárí', r3t:'Ilu, ti tirẹ patapata.',
  r3d:'VibeVault fun ọ gbe nigba ti o n lọ — ipamọ, irin-ajo, ilera ati itọjú.',
  r4n:'Ọrọ Amayedarí', r4t:'Akoko ilu Cape Town ti o ṣe ipinnu.',
  r4d:'VibeVault fun ọ ni ero ìdókòwò ti ọrọ-aje R24.5 bílíọ̀nù ti n kọ́ sí.'
}
```

---

## FILE 2: translations.js — WEBSITE CONTENT (All 26 languages)

This file is loaded by v1.html, v2.html, v3.html, v4.html.
It provides translated text for all website sections.

Structure: `VV_WEB[lang][version][key]`

For each website version, translate these content blocks:

**SHARED across all versions (translate once):**
- `nav_links[version]` — 4 navigation link labels per version
- `stats` — 3 stat cards (label, description, source note)
- `tier_names` — 5 tier names (Pay as you go, Student, Lite, Vibe, Premium)
- `tier_perks` — 4-5 bullet points per tier
- `free_note` — the "always free" note
- `contact_form` — all form field labels, placeholders, button, note
- `footer` — footer legal text
- `features` — 6 feature blocks (h3 + p)

**PER VERSION:**
- `hero_eyebrow`, `hero_h1`, `hero_sub`, `hero_cta1`, `hero_cta2`
- `section_headings` — all h2/eyebrow/p for each section
- `founder_quote` — the blockquote text

**V4 SPECIFIC:**
- credentials strip (4 labels + values)
- investment case section
- founder cards (3 panels)
- brief CTA

Claude Code: implement all translations accurately. Use your training knowledge.
For the website, the most critical strings to translate precisely are:
1. Hero headline (h1) — this is the first impression
2. Founder quote — must preserve meaning and emotion  
3. Section intro paragraphs — must read naturally, not literally translated

---

## FILE 3: index.html — IMPLEMENTATION REQUIREMENTS

```javascript
// Language detection + storage
var lang = new URLSearchParams(window.location.search).get('lang')
        || localStorage.getItem('vv-lang')
        || (navigator.language || 'en').split('-')[0];
if (!T[lang]) lang = 'en';
localStorage.setItem('vv-lang', lang);

// t() function with Swiss German fallback
function t(key) {
  var l = lang === 'de-CH' ? 'de' : lang;
  return (T[l] || T.en)[key] || T.en[key] || key;
}

// Apply language to all data-t elements
function applyLang() {
  document.querySelectorAll('[data-t]').forEach(function(el) {
    el.textContent = t(el.getAttribute('data-t'));
  });
  // Handle RTL
  var rtl = ['ar', 'ur'];
  document.documentElement.setAttribute('dir', rtl.includes(lang) ? 'rtl' : 'ltr');
  // Rebuild dynamic content
  rebuildLangGrid();
  rebuildVersionCards();
}

// On language select
function selectLang(code) {
  lang = code;
  localStorage.setItem('vv-lang', code);
  stopCycle();
  // Update welcome word
  var ww = document.getElementById('ww');
  ww.style.opacity = '0';
  setTimeout(function() {
    ww.textContent = LANGS.find(function(l){return l.code === code;}).w;
    ww.style.opacity = '1';
  }, 700);
  // Apply to all elements
  applyLang();
}

// Welcome word cycling — Apple-style, gentle pace
// Visible 3.4 seconds, 720ms fade
var CYCLE_VISIBLE = 3400;
var CYCLE_FADE = 720;
```

### index.html CSS Requirements
- Background: #060B12 (slightly darker than ink for the entry feel)
- Welcome word: #40E0D0, font-size clamp(2.2rem, 6.5vw, 3.6rem), font-weight 700
- All interactive divs: explicit `color` set so host CSS cannot override
- Language pill selected state: `border-color: #40E0D0; color: #40E0D0; background: rgba(64,224,208,0.09)`
- Language pill default: `border: 1px solid rgba(255,255,255,0.30); color: rgba(255,255,255,0.88)`
- Answer choice cards: `background: #0C1A28; border: 1px solid rgba(255,255,255,0.24); color: rgba(255,255,255,0.90)`
- Continue/Begin buttons: `background: #40E0D0; color: #060B12; font-weight: 700`
- Skip link: `color: rgba(255,255,255,0.62); text-decoration: underline`
- NEVER use HTML `<button>` tags — always `<div>` with `cursor: pointer`

### Topographic contour lines
- Include the SVG topo map on the language selection and intro screens
- 8-9 nested irregular closed loops (not perfect circles, not straight lines)
- Colour: rgba(64,224,208,0.03) to rgba(64,224,208,0.13) getting stronger inward
- Positioned as background overlay, pointer-events: none

---

## FILES 4-7: v1.html, v2.html, v3.html, v4.html — IMPLEMENTATION

### Language application in each website version
Add to `<head>` of each file: `<script src="translations.js"></script>`

At bottom of each file, before `</body>`:
```javascript
(function() {
  var lang = new URLSearchParams(window.location.search).get('lang')
           || localStorage.getItem('vv-lang')
           || (navigator.language || 'en').split('-')[0];
  if (!VV_WEB[lang]) lang = 'en';
  localStorage.setItem('vv-lang', lang);
  
  var rtl = ['ar', 'ur'];
  document.documentElement.setAttribute('dir', rtl.includes(lang) ? 'rtl' : 'ltr');
  
  // Apply translations
  document.querySelectorAll('[data-i18n]').forEach(function(el) {
    var key = el.getAttribute('data-i18n');
    // Look in version-specific first, then shared
    var ver = VV_WEB[lang] && VV_WEB[lang]['v1']; // replace v1 with actual version
    var shared = VV_WEB[lang] && VV_WEB[lang].shared;
    var val = (ver && ver[key]) || (shared && shared[key]);
    if (val) {
      el.innerHTML = val; // innerHTML to support <br>, <em>, <strong>
    }
  });
})();
```

Add `data-i18n="key"` attributes to ALL text elements.

### V4 special: the "Request a Brief" button
```html
<a href="brief.html" class="ba" download>Request a Brief</a>
```
The `download` attribute triggers download. brief.html should be a well-formatted
single-page HTML investor brief that users can save as PDF via browser print.

---

## FILE 8: brief.html — INVESTOR BRIEF (V4 Download)

A complete, printable investor brief. When printed to PDF, it should look professional.

Include:
- Cover: VibeVault Africa, Investor Brief 2026
- Executive summary (2 paragraphs)
- The problem (with the 3 verified stats)
- The solution (pod system, all features)
- Revenue model (3 streams with projected figures)
- The market (Cape Town tourism + nightlife)
- The founder (Dasha Mohlala, background, why she's the right person)
- Investment opportunity + contact

Print styles:
```css
@media print {
  nav, .no-print { display: none; }
  body { background: white; color: black; }
  * { font-family: 'Times New Roman', serif; }
}
```

---

## V1, V2, V3, V4 CONTENT (What each version says)

### V1 — YOUR VAULT (warm, human, friend)
**Hero**: "Drop your bag. Go live." / "We carry the load. You get the night."
**Founder**: "The best nights are simple: you show up, stay present, go home safe. A great city makes that easy for everyone — not just people who planned better or have more options. I watched too many people leave early, not because they wanted to, but because they had no other option. VibeVault exists so the night stays yours, all the way to the end. For all of us."
**Problem framing**: "Going out shouldn't feel like project management."
**Pillars**: Hold your load / Top you up / Get you home

### V2 — THE INEVITABLE (elegant, poetic, invisible)
**Hero**: "A city where safety never becomes a thought."
**Founder**: "The best infrastructure is invisible — you don't notice roads when they work, only when they don't. I've always been more interested in what cities could be than what they are. VibeVault is my answer to that: care so well-designed into Cape Town's streets that you simply feel it as ease."
**Problem framing**: "The best cities don't remind you they're safe."
**Pillars**: Present / Always on / Invisible

### V3 — THE EXPLORER (open, free, for everyone)
**Hero**: "Cape Town belongs to everyone in it."
**Hero sub**: "You. Me. The tourist, the student, the neighbour. VibeVault moves when you move."
**Founder**: "The most alive I've ever felt in this city is when I've been fully part of it — no hesitation, no half-measures. The city I've grown to love deserves to feel that way for everyone: as welcoming at 2am as it is at 2pm. For tourists, for students, for families. VibeVault exists so more people can have that experience, on their own terms."
**Problem framing**: "Not a warning system. A companion."
**Pillars**: Carry / Connect / Explore
**UNIQUE SECTION**: "Who we're for" — 4 persona cards (Tourist, Student, Family, Local)
  Note: persona card changed from "Explorer" to "Local" — avoids confusion with the version name.

### V4 — INFRASTRUCTURE CASE (investor/institutional)
**Hero**: "The infrastructure Cape Town has been building toward."
**Founder quote 1**: "Cape Town's infrastructure has carried this city far. VibeVault is what the next chapter looks like — systems built for how people actually move through this city, not how we imagined they would."
**Founder — The origin**: "VibeVault emerged from moving through this city with open eyes — watching the gap between Cape Town's promise and its infrastructure, and deciding that closing it was worth building a company around. The founder knows this city not from research, but from living it at every hour."
**Founder — Why it matters**: "Founder-market fit is the single most reliable predictor of startup success. VibeVault is built by the person who knows this city at every hour, in every condition — and has the systems thinking to turn that knowledge into infrastructure. The kind of insight that cannot be acquired from a desk."
**V4 nav amber accent**: use #C9A84C (warm amber) for nav border, eyebrow text, credential labels
**Credentials strip**: Entity type / B-BBEE status / Procurement recognition / Financial year end

---

## VERIFIED STATISTICS (use exactly as written — DO NOT change)
1. "43% of all stranded assistance cases in Cape Town involve a flat phone battery" — Source: Cape Town CCID · 2023
2. "24 million annual visits to the V&A Waterfront — more than the Colosseum, Sagrada Família and Louvre individually" — Source: V&A Waterfront Official · 2024
3. "R24.5 billion generated by Cape Town's tourism economy in 2024" — Source: Wesgro · 2024

---

## IMAGES — HOW TO HANDLE

The images/ folder will contain real Grok-AI-generated images of VibeVault pods.
In the HTML, reference them as:

```html
<!-- V1 hero -->
<div class="hi" style="background-image: url('images/hero-pod.jpg')"></div>

<!-- Always have a dark fallback for when images aren't uploaded yet -->
```

Each image slot has a dark background fallback so the site looks complete without images.
The CSS background property should always have `var(--ink)` before the `url()`.

Image assignments:
- `hero-pod.jpg` = mushroom-shaped teal pod at Camps Bay sunset (rename IMG_5175.jpeg)
- `hero-promenade.jpg` = Camps Bay promenade with pod at dusk (rename IMG_5160.jpeg)
- `hero-solar.jpg` = solar panels at sunrise, sea visible (rename IMG_5179.jpeg)
- `hero-row.jpg` = row of solar-canopied lockers at fiery sunset (rename IMG_5176.jpeg)
- `seating.jpg` = teal glowing seating area at dusk with trees (rename IMG_5162.jpeg)
- `stranded-screen.jpg` = "I'm Stranded" touchscreen close-up (rename IMG_5163.jpeg)

---

## SCROLL REVEAL ANIMATION

Apply to every major content block:
```css
.rv { opacity: 0; transform: translateY(24px); transition: opacity 0.65s ease, transform 0.65s ease; }
.rv.in { opacity: 1; transform: none; }
.d1 { transition-delay: 0.08s; } /* stagger */
.d2 { transition-delay: 0.16s; }
.d3 { transition-delay: 0.24s; }
```

```javascript
var io = new IntersectionObserver(function(entries) {
  entries.forEach(function(e) {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, { threshold: 0.08, rootMargin: '0px 0px -28px 0px' });
document.querySelectorAll('.rv').forEach(function(el) { io.observe(el); });
```

Hero elements animate on page load (not scroll):
```javascript
window.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.hero .rv').forEach(function(el, i) {
    setTimeout(function() { el.classList.add('in'); }, 100 + i * 120);
  });
});
```

---

## FORMSPREE FORM

All contact forms use: `action="https://formspree.io/f/YOUR_FORM_ID" method="POST"`
Hidden spam field: `<input type="text" name="_gotcha" style="display:none" />`
Hidden subject: `<input type="hidden" name="_subject" value="New VibeVault enquiry" />`

---

## QUALITY REQUIREMENTS

1. All files must pass basic HTML validation (no unclosed tags)
2. No broken JavaScript (no undefined references)  
3. All internal links must work (v1.html → v1.html, etc.)
4. All 26 languages must render correctly in the game without any visible English text leaking through
5. RTL languages (ar, ur) must have proper text direction applied
6. The site must look complete even without the images (dark fallback)
7. No Google Fonts. No external font CDNs. System fonts only.
8. Formspree placeholder must be clearly visible in code with a comment saying REPLACE
9. Brief.html must be a complete, printable document

---

## GITHUB PUSH INSTRUCTIONS (for Claude Code to add as README.md)

After building all files, create README.md with:
```
# VibeVault Africa — Website

Live at vibevaultafrica.co.za via GitHub Pages.

## Image Setup (one-time)
1. Rename your Grok images as follows and upload to images/:
   - IMG_5175.jpeg → hero-pod.jpg
   - IMG_5160.jpeg → hero-promenade.jpg
   - IMG_5179.jpeg → hero-solar.jpg
   - IMG_5176.jpeg → hero-row.jpg
   - IMG_5162.jpeg → seating.jpg
   - IMG_5163.jpeg → stranded-screen.jpg

## Formspree Setup (one-time)
1. Go to formspree.io, create a form for dasha@vibevaultafrica.co.za
2. Copy your Form ID (looks like: xyzabcde)
3. Find and replace YOUR_FORM_ID in v1.html, v2.html, v3.html, v4.html

## Deployment
git add .
git commit -m "Update"
git push origin main
```

---

## CLAUDE CODE: EXECUTION ORDER

Do these in order. Do not skip steps. Do not stop until all are done.

1. READ this entire CLAUDE.md file first.
2. CREATE translations.js with all 26 languages, all website content.
3. CREATE index.html (the game) with all 26 languages embedded.
4. CREATE v1.html using translations.js, with data-i18n attributes.
5. CREATE v2.html using translations.js, with data-i18n attributes.
6. CREATE v3.html using translations.js, with data-i18n attributes.
7. CREATE v4.html using translations.js, with data-i18n attributes.
8. CREATE brief.html (printable investor brief).
9. CREATE images/ directory and a placeholder README inside it.
10. CREATE README.md at root level.
11. DELETE the old index.html content (it is being replaced).
12. VERIFY: open each HTML file and check for JS errors, broken links.
13. Report: list all files created and their sizes.

---

END OF SPEC
