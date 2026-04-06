"""
patch_topo.py — Injects topographic SVG overlays into VibeVault hero sections.

ONLY does two things:
  1. Injects amber SVG overlay into v4.html hero
  2. Injects white SVG overlay into v1.html, v2.html, v3.html hero

Does NOT touch any CSS, layout, images, dimensions, or anything else.
Safe to run on already-working files.

Run from the vibevaultafrica repo root:
    python3 patch_topo.py
"""

import re, os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Load SVG paths from generated preview files ─────────────────────────────

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
amber_paths = load_paths('amber_light.html')
white_paths = load_paths('white_light.html')

# ── Build overlay div ────────────────────────────────────────────────────────

def build_overlay(paths, stroke, opacity, clip_id):
    path_tags = '\n'.join(f'    <path d="{p}"/>' for p in paths)
    return (
        '<!-- topo-overlay -->'
        '<div style="position:absolute;inset:0;pointer-events:none;z-index:0;overflow:hidden;" aria-hidden="true">'
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" style="position:absolute;inset:0;width:100%;height:100%;">'
        f'<defs><clipPath id="{clip_id}"><rect width="1440" height="900"/></clipPath></defs>'
        f'<g clip-path="url(#{clip_id})" fill="none" stroke="{stroke}" stroke-opacity="{opacity}" stroke-width="0.85" stroke-linecap="round" stroke-linejoin="round">'
        f'\n{path_tags}\n'
        '</g></svg></div>'
        '<!-- /topo-overlay -->'
    )

amber_overlay = build_overlay(amber_paths, '#C9A84C', '0.38', 'topo-v4')
white_overlay = build_overlay(white_paths, '#ffffff', '0.28', 'topo-v123')

# ── Inject helper ────────────────────────────────────────────────────────────

def inject_overlay(html, overlay, filename):
    # Remove any previous topo overlay injection to avoid duplicates
    html = re.sub(
        r'<!-- topo-overlay -->.*?<!-- /topo-overlay -->',
        '',
        html,
        flags=re.DOTALL
    )

    # Find the opening tag of the .hero section/div and insert overlay right after it
    pattern = r'(<(?:section|div)[^>]+class="[^"]*\bhero\b[^"]*"[^>]*>)'
    match = re.search(pattern, html)
    if not match:
        print(f"  WARNING: .hero element not found in {filename} — skipped")
        return html

    insert_pos = match.end()
    html = html[:insert_pos] + '\n' + overlay + '\n' + html[insert_pos:]
    return html

# ── Patch each file ──────────────────────────────────────────────────────────

def patch_file(filename, overlay):
    fpath = os.path.join(os.getcwd(), filename)
    if not os.path.exists(fpath):
        print(f"  ERROR: {fpath} not found — run from repo root?")
        return
    with open(fpath, 'r', encoding='utf-8') as f:
        original = f.read()
    patched = inject_overlay(original, overlay, filename)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(patched)
    added = len(patched) - len(original)
    print(f"  {filename}: +{added:,} chars (overlay injected)")

print("\nPatching HTML files...")
patch_file('v4.html', amber_overlay)
patch_file('v1.html', white_overlay)
patch_file('v2.html', white_overlay)
patch_file('v3.html', white_overlay)

print("\nDone. Commit with:")
print("  git add v1.html v2.html v3.html v4.html")
print('  git commit -m "Add topographic SVG overlays to all hero sections"')
print("  git push origin main")
