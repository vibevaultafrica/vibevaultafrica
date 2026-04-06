"""
patch_topo.py — VibeVault topographic overlay injector
Run this from inside the vibevaultafrica repo directory.

Usage:
    python3 patch_topo.py

What it does:
  1. Reads SVG path data from amber.html and white_v5.html (in the same folder as this script)
  2. Injects amber topo overlay into v4.html hero section
  3. Injects white topo overlay into v1.html, v2.html, v3.html hero sections
  4. Fixes V2 + V3 hero full-bleed (removes max-width constraint)
  5. Writes patched files back in place
"""

import re, os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── 1. Load SVG paths from generated preview files ─────────────────────────

def load_paths(filename):
    fpath = os.path.join(SCRIPT_DIR, filename)
    if not os.path.exists(fpath):
        print(f"ERROR: Cannot find {fpath}")
        sys.exit(1)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    paths = re.findall(r'<path d="([^"]+)"', html)
    print(f"  {filename}: {len(paths)} paths loaded")
    return paths

print("Loading SVG data...")
amber_paths = load_paths('amber.html')
white_paths = load_paths('white_v5.html')

# ── 2. Build SVG overlay blocks ─────────────────────────────────────────────

def build_overlay(paths, stroke, opacity, clip_id):
    path_tags = '\n'.join(f'    <path d="{p}"/>' for p in paths)
    return (
        '<div style="position:absolute;top:0;left:0;width:100%;height:100%;'
        'pointer-events:none;z-index:0;overflow:hidden;" aria-hidden="true">\n'
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 900" '
        'preserveAspectRatio="xMidYMid slice" '
        'style="position:absolute;top:0;left:0;width:100%;height:100%">\n'
        f'<defs><clipPath id="{clip_id}"><rect width="1440" height="900"/></clipPath></defs>\n'
        f'<g clip-path="url(#{clip_id})" fill="none" stroke="{stroke}" '
        f'stroke-opacity="{opacity}" stroke-width="0.85" '
        'stroke-linecap="round" stroke-linejoin="round">\n'
        + path_tags + '\n</g>\n</svg>\n</div>'
    )

amber_overlay = build_overlay(amber_paths, '#C9A84C', '0.38', 'topo-v4')
white_overlay = build_overlay(white_paths, '#ffffff', '0.28', 'topo-v123')

# ── 3. Patch helper ─────────────────────────────────────────────────────────

def patch_file(filename, transforms):
    fpath = os.path.join(os.getcwd(), filename)
    if not os.path.exists(fpath):
        print(f"ERROR: {fpath} not found — are you running from the repo root?")
        return False
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    original_len = len(html)
    for fn in transforms:
        html = fn(html, filename)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  {filename}: patched ({original_len} → {len(html)} chars)")
    return True

# ── 4. Transform functions ───────────────────────────────────────────────────

def inject_topo(overlay):
    """Return a function that inserts the overlay div right after the opening <section>
    or <div> tag that has class 'hero', making the hero position:relative if needed."""
    def _inject(html, fname):
        # Already has topo? Remove old one first to avoid duplicates
        html = re.sub(
            r'<div style="position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0;overflow:hidden;" aria-hidden="true">.*?</div>',
            '',
            html,
            flags=re.DOTALL
        )

        # Find the hero section/div opening tag and inject right after it
        # Hero is typically: <section class="hero ..."> or <div class="hero ...">
        pattern = r'(<(?:section|div)[^>]+class="[^"]*\bhero\b[^"]*"[^>]*>)'
        match = re.search(pattern, html)
        if match:
            insert_pos = match.end()
            html = html[:insert_pos] + '\n' + overlay + '\n' + html[insert_pos:]
            # Ensure the hero container has position:relative so the overlay positions correctly
            hero_tag = match.group(0)
            if 'position:relative' not in hero_tag and 'position: relative' not in hero_tag:
                # Add it to the inline style if present, or note it — handled via CSS below
                pass
        else:
            print(f"    WARNING: no .hero section found in {fname}")
        return html
    return _inject


def fix_hero_css(html, fname):
    """Ensure .hero has position:relative, and for V2/V3 fix the max-width constraint."""
    # Add/update .hero CSS rule to ensure position:relative and full bleed
    # Find existing .hero { rule in <style>
    hero_rule_pattern = r'(\.hero\s*\{[^}]*)\}'

    def update_hero_rule(m):
        rule_body = m.group(1)
        # Add position:relative if missing
        if 'position' not in rule_body:
            rule_body += '\n  position: relative;'
        else:
            rule_body = re.sub(r'position\s*:\s*\w+', 'position: relative', rule_body)
        # Add/fix max-width: none for full bleed
        if 'max-width' not in rule_body:
            rule_body += '\n  max-width: none;'
        else:
            rule_body = re.sub(r'max-width\s*:[^;]+;', 'max-width: none;', rule_body)
        # Ensure width:100%
        if 'width' not in rule_body:
            rule_body += '\n  width: 100%;'
        return rule_body + '\n}'

    new_html = re.sub(hero_rule_pattern, update_hero_rule, html, count=1)
    if new_html == html:
        # No .hero rule found — inject one before </style>
        new_html = html.replace(
            '</style>',
            '.hero { position: relative; max-width: none; width: 100%; }\n</style>',
            1
        )
    return new_html


def fix_content_zindex(html, fname):
    """Make sure content inside hero sits above the topo overlay (z-index:1)."""
    # Add .hero > * { position: relative; z-index: 1; } to ensure content is above overlay
    z_rule = '.hero > * { position: relative; z-index: 1; }\n'
    if '.hero > *' not in html:
        html = html.replace('</style>', z_rule + '</style>', 1)
    return html


# ── 5. Apply patches ─────────────────────────────────────────────────────────

print("\nPatching HTML files...")

# V4 — amber overlay
patch_file('v4.html', [
    inject_topo(amber_overlay),
    fix_hero_css,
    fix_content_zindex,
])

# V1, V2, V3 — white overlay + hero full-bleed fix
for vf in ['v1.html', 'v2.html', 'v3.html']:
    patch_file(vf, [
        inject_topo(white_overlay),
        fix_hero_css,
        fix_content_zindex,
    ])

print("\nAll done. Review changes, then:")
print("  git add v1.html v2.html v3.html v4.html")
print("  git commit -m 'Add topographic SVG overlays to all pages'")
print("  git push origin main")
