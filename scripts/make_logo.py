#!/usr/bin/env python3
"""Draw the DFW Expert Roofers logo and favicons (INTAKE.md: a new SVG that reads "DFW EXPERT / ROOFERS"
in the brand colors). The letters are outlined from the self-hosted Inter font (SIL OFL) so the logo looks
the same everywhere, even inside an <img>. Writes src/static/images/logo.svg, src/static/favicon.svg,
favicon.ico and apple-touch-icon.png.

Usage: python3 scripts/make_logo.py   (needs fonttools and brotli: pip install fonttools brotli)
"""
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "src" / "static"
GOLD, GOLD_LIGHT, WHITE, NAVY = "#c9a84c", "#e0c878", "#ffffff", "#12111a"

font = TTFont(STATIC / "fonts" / "inter-latin-var.woff2")
if "fvar" in font:
    font = instantiateVariableFont(font, {"wght": 800, **({"opsz": 32} if any(a.axisTag == "opsz" for a in font["fvar"].axes) else {})})
glyphs = font.getGlyphSet()
cmap = font.getBestCmap()
UPM = font["head"].unitsPerEm


def text_path(text, x, baseline, size, tracking=0.0):
    """SVG path data for `text` set at (x, baseline) with font size `size` px; returns (d, width)."""
    scale = size / UPM
    d, pen_x = [], x
    for ch in text:
        name = cmap[ord(ch)]
        g = glyphs[name]
        sp = SVGPathPen(glyphs)
        tp = TransformPen(sp, (scale, 0, 0, -scale, pen_x, baseline))
        g.draw(tp)
        d.append(sp.getCommands())
        pen_x += g.width * scale + tracking * size
    return " ".join(d), pen_x - x - tracking * size


def mark(ox, oy, s=1.0):
    """Roofline mark: two nested gold gables over a small Texas star."""
    def p(pts):
        return " ".join(f"{'M' if i == 0 else 'L'}{ox + px * s:.1f} {oy + py * s:.1f}" for i, (px, py) in enumerate(pts))
    star = []
    import math
    for i in range(10):
        r = 7.2 if i % 2 == 0 else 2.9
        a = -math.pi / 2 + i * math.pi / 5
        star.append((28 + r * math.cos(a), 30 + r * math.sin(a)))
    return (f'<path d="{p([(3, 34), (28, 9), (53, 34)])}" fill="none" stroke="{GOLD}" stroke-width="{5.5 * s:.1f}" stroke-linejoin="miter"/>'
            f'<path d="{p(star)} Z" fill="{GOLD_LIGHT}"/>'
            f'<path d="{p([(14, 50), (42, 50)])}" stroke="{GOLD}" stroke-width="{3 * s:.1f}"/>')


def main():
    top, w1 = text_path("DFW EXPERT", 66, 30, 25, tracking=0.04)
    bot, w2 = text_path("ROOFERS", 66, 57, 25, tracking=0.235)
    width = round(66 + max(w1, w2) + 4)
    logo = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 64" width="{width}" height="64" role="img" '
            f'aria-label="DFW Expert Roofers"><title>DFW Expert Roofers</title>{mark(0, 4)}'
            f'<path d="{top}" fill="{WHITE}"/><path d="{bot}" fill="{GOLD}"/></svg>\n')
    (STATIC / "images" / "logo.svg").write_text(logo)
    fav = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">'
           f'<rect width="64" height="64" rx="12" fill="{NAVY}"/>{mark(4, 4, 1.0)}</svg>\n')
    (STATIC / "favicon.svg").write_text(fav)
    try:
        import cairosvg  # optional
        cairosvg.svg2png(bytestring=fav.encode(), write_to=str(STATIC / "apple-touch-icon.png"), output_width=180, output_height=180)
    except ImportError:
        from PIL import Image, ImageDraw
        im = Image.new("RGB", (180, 180), NAVY)
        d = ImageDraw.Draw(im)
        k = 180 / 64
        d.line([(7 * k, 38 * k), (32 * k, 13 * k), (57 * k, 38 * k)], fill=GOLD, width=int(5.5 * k), joint="curve")
        d.line([(18 * k, 54 * k), (46 * k, 54 * k)], fill=GOLD, width=int(3 * k))
        import math
        pts = [(32 * k + (7.2 if i % 2 == 0 else 2.9) * k * math.cos(-math.pi / 2 + i * math.pi / 5),
                34 * k + (7.2 if i % 2 == 0 else 2.9) * k * math.sin(-math.pi / 2 + i * math.pi / 5)) for i in range(10)]
        d.polygon(pts, fill=GOLD_LIGHT)
        im.save(STATIC / "apple-touch-icon.png")
        im.resize((48, 48), Image.LANCZOS).save(STATIC / "favicon.ico", sizes=[(48, 48), (32, 32), (16, 16)])
    print(f"logo.svg {width}x64, favicons written")


if __name__ == "__main__":
    main()
