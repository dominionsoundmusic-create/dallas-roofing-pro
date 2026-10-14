#!/usr/bin/env python3
"""One-time photo import (Oct 13 2026, Maurice's reuse rule). Copies the generic roof photos chosen from
the Houston build (nothing Houston-specific: no skyline, bayou, coast, palms, Spanish moss or landmark) into
src/static/images/ under neutral names, and writes docs/photos.json: the catalog of every photo the site
may use, with alt text that describes what the photo actually shows (never a town it was not taken in)
and a `group` (two files cut from the same photo share a group; a page may show a group only once).

Usage: python3 scripts/import_photos.py [--houston ../houston-roofing-pro]
"""
import argparse
import json
import shutil
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "src" / "static" / "images"

HOUSTON = {  # Houston file -> (new name, alt)
    "checking-a-roofer-houston-hero.jpg": ("homeowner-clipboard-checking-roofer-hero.jpg", "Homeowner holding a clipboard in front of a two-story brick house with a white pickup truck parked at the curb"),
    "emergency-roof-tarp-houston.jpg": ("blue-emergency-tarp-on-brick-home.jpg", "Blue emergency tarp covering part of the roof on a brick home after a storm, with a fallen limb on the wet lawn"),
    "flat-roof-ponding-water-houston.jpg": ("flat-roof-ponding-water.jpg", "Water standing on a low-slope roof section over a brick wall after rain"),
    "greater-houston-suburb-rooftops-aerial-hero.jpg": ("suburb-rooftops-aerial-pond-hero.jpg", "Aerial view over a large suburb of shingle-roofed homes, curving streets and a retention pond under a bright sky"),
    "hail-damage-shingles-closeup-houston.jpg": ("hail-damaged-shingles-closeup.jpg", "Close view of asphalt shingles with dark round hail marks where granules were knocked off"),
    "hail-on-lawn-after-storm-houston-hero.jpg": ("hail-on-lawn-after-storm-hero.jpg", "Hailstones scattered across a driveway and lawn in front of a one-story brick home after a storm"),
    "homeowner-phone-call-front-porch-houston-hero.jpg": ("homeowner-phone-call-front-porch-hero.jpg", "Homeowner on a phone call on the front porch of a brick home on a quiet tree-lined street"),
    "houston-acreage-barn-metal-roof.jpg": ("acreage-barn-metal-roof.jpg", "Red barn with a metal roof standing in an open pasture under a clear sky"),
    "houston-attic-roof-decking-inspection.jpg": ("attic-roof-decking-flashlight-inspection.jpg", "Person in an attic shining a flashlight along the roof rafters and decking"),
    "houston-ceiling-leak-bucket-living-room.jpg": ("ceiling-leak-bucket-living-room.jpg", "Water stain on a living room ceiling with a bucket on the floor below and furniture covered in plastic"),
    "houston-dented-gutter-hail-marks.jpg": ("dented-gutter-hail-marks.jpg", "Close view of a gutter and downspout corner on a brick home below a shingle roof edge"),
    "houston-home-office-phone-and-notes-hero.jpg": ("phone-and-notes-on-desk-hero.jpg", "Phone, notepad and coffee cup on a desk by a window looking out at a neighbor's house"),
    "houston-live-oak-limb-on-roof-after-storm.jpg": ("oak-limb-on-roof-after-storm.jpg", "Large oak limb lying across the roof of a brick ranch home after a storm, with wet pavement in front"),
    "houston-neighborhood-roofs-morning-hero.jpg": ("neighborhood-roofs-morning-hero.jpg", "Row of two-story suburban homes with shingle roofs and shade trees along a street in early morning light"),
    "houston-roof-tear-off-decking.jpg": ("roof-tear-off-new-decking.jpg", "Roofers laying new plywood decking and underlayment during a re-roof, with old shingles still on part of the roof"),
    "houston-roofer-ladder-at-gutter-inspection.jpg": ("roofer-ladder-at-gutter.jpg", "Roofer standing at the foot of an aluminum ladder set against the gutter of a brick home"),
    "houston-strip-center-low-slope-roof.jpg": ("strip-center-low-slope-roof.jpg", "Single-story strip center with a white low-slope roof and rooftop air conditioning units"),
    "how-long-roof-lasts-houston-hero.jpg": ("brick-homes-shingle-roofs-aerial-hero.jpg", "Brick homes with hip shingle roofs and mature shade trees seen from above on a sunny day"),
    "humble-main-street-area-home-roof-hero.jpg": ("older-frame-home-shingle-roof-hero.jpg", "Older one-story frame house with a gray shingle roof and a front porch beside a quiet road"),
    "katy-two-story-brick-home-architectural-shingle-roof-hero.jpg": ("two-story-brick-home-architectural-shingles-hero.jpg", "Two-story brick home with a dark architectural shingle roof on a wide suburban street with young trees"),
    "metal-roof-standing-seam-houston-home.jpg": ("standing-seam-metal-roof-farmhouse.jpg", "White two-story farmhouse with a dark standing seam metal roof on an open lot"),
    "pasadena-brick-ranch-home-roof-hero.jpg": ("brick-ranch-home-oak-roof-hero.jpg", "One-story brick ranch home with a brown shingle roof beside a large oak tree and open lawn"),
    "roof-insurance-claim-houston-hero.jpg": ("homeowner-photographing-roof-for-claim-hero.jpg", "Homeowner standing on the front lawn taking photos of the roof of a two-story brick home"),
    "roof-replacement-cost-houston-hero.jpg": ("new-roof-dumpster-driveway-hero.jpg", "Roll-off dumpster in the driveway of a two-story home with a new dark shingle roof"),
    "roofing-contract-kitchen-table-houston.jpg": ("roofing-contract-kitchen-table.jpg", "Homeowner reading a printed roofing contract at a kitchen table beside a coffee mug"),
    "alvin-country-home-metal-roof-pasture-hero.jpg": ("country-home-red-metal-roof-pasture-hero.jpg", "White country home with a red metal roof under shade trees beside a fenced pasture"),
    "cypress-lakeside-two-story-home-shingle-roof-hero.jpg": ("two-story-home-near-pond-hero.jpg", "Two-story stone and siding home with a shingle roof beside a neighborhood pond and walking path"),
    "chimney-step-flashing-houston.jpg": ("chimney-step-flashing.jpg", "Brick chimney rising through a gray shingle roof with metal flashing at its base"),
    "atascocita-two-story-brick-home-roof-hero.jpg": ("two-story-brick-home-street-hero.jpg", "Two-story brick home with a hip shingle roof on a curving street with young trees"),
}
DFW = {  # the 15 photos already in images/ (roof-0N hero and card are the same photo cut two ways)
    "roof-01": "Four roofers working across a gray shingle roof on a two-story home under a clear blue sky",
    "roof-02": "Roofer kneeling on a shingle roof beside a patch of lifted and broken shingles on a sunny day",
    "roof-03": "Two roofers on a damaged shingle roof of a light-colored house with a torn section near the ridge",
    "roof-04": "Roofer in a blue shirt kneeling near the edge of a shingle roof checking the surface in bright sun",
    "roof-05": "Roofer sealing around a roof vent pipe with a caulk gun on an asphalt shingle roof at sunrise",
    "roof-06": "Workers installing a white membrane on a flat commercial roof with rooftop units nearby",
}
DFW_SINGLE = {
    "dallas-roof-hail-hero.jpg": "Hailstones resting on dark asphalt shingles beside a roof vent under a blue sky",
    "dallas-roof-repair-hero.jpg": "Roofer kneeling on a shingle roof making a repair with green trees behind",
    "dallas-roof-replace-hero.jpg": "Crew of roofers laying new shingles on a steep roof of a two-story home",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--houston", default=str(ROOT.parent / "houston-roofing-pro"))
    hsrc = Path(ap.parse_args().houston) / "src" / "static" / "images"
    cat = {}
    for src, (dst, alt) in HOUSTON.items():
        if hsrc.exists():
            shutil.copy2(hsrc / src, IMG / dst)
        w, h = Image.open(IMG / dst).size
        cat[dst] = {"alt": alt, "size": f"{w}x{h}", "group": dst[:-4].replace("-hero", ""), "origin": "Houston build, generic"}
    for g, alt in DFW.items():
        for kind in ("hero", "card"):
            f = f"{g}-{kind}.jpg"
            w, h = Image.open(IMG / f).size
            cat[f] = {"alt": alt, "size": f"{w}x{h}", "group": g, "origin": "DFW images/"}
    for f, alt in DFW_SINGLE.items():
        w, h = Image.open(IMG / f).size
        cat[f] = {"alt": alt, "size": f"{w}x{h}", "group": f[:-4], "origin": "DFW images/"}
    (ROOT / "docs" / "photos.json").write_text(json.dumps(dict(sorted(cat.items())), indent=1) + "\n")
    print(f"{len(cat)} files, {len({v['group'] for v in cat.values()})} distinct photos")


if __name__ == "__main__":
    main()
