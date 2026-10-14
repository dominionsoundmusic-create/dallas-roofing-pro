#!/usr/bin/env python3
"""Rebuild files/dallas-hail-storm-claim-checklist.pdf for DFW Expert Roofers (Oct 13 2026).

The old PDF carried the retired name and a coastal windstorm line that does not apply to DFW. Same URL,
same purpose: a printable two-page checklist for the hours, days and weeks after hail or wind damage.
The phone number is read from src/data/site.json (the one place it lives).

Usage: python3 scripts/make_checklist_pdf.py
"""
import json
import re
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parent.parent
site = json.loads((ROOT / "src" / "data" / "site.json").read_text())
digits = re.sub(r"\D", "", site["business"]["phone"])[-10:]
PHONE = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
NAVY, GOLD = HexColor("#12111a"), HexColor("#8a6d1c")

title = ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=19, leading=23, textColor=NAVY, spaceAfter=4)
sub = ParagraphStyle("s", fontName="Helvetica", fontSize=10.5, leading=14, textColor=HexColor("#333333"), spaceAfter=10)
h2 = ParagraphStyle("h", fontName="Helvetica-Bold", fontSize=12.5, leading=16, textColor=GOLD, spaceBefore=9, spaceAfter=3)
body = ParagraphStyle("b", fontName="Helvetica", fontSize=10, leading=13.4, alignment=TA_LEFT)
small = ParagraphStyle("sm", fontName="Helvetica-Oblique", fontSize=8.6, leading=11.5, textColor=HexColor("#444444"), spaceBefore=8)

SECTIONS = [
    ("1. The first hour", [
        "Stay away from downed power lines. Report them to Oncor or your own electric provider, or call 911.",
        "Keep everyone out of rooms where the ceiling is wet or sagging.",
        "Do not go up on the roof. A wet, storm-hit roof is slick, and damaged decking can give way.",
        "Note the date and time of the storm and how big the hail was if you saw it (pea, quarter, golf ball, baseball).",
    ]),
    ("2. Photograph before anything is moved or fixed", [
        "Shoot every side of the house from the ground: wide shots first, then zoomed in.",
        "Photograph dents in gutters, downspouts, roof vents and the fins of the outdoor air conditioning unit, plus torn window screens, fences and cars. They show how big the hail was at your address.",
        "Photograph granules piled at the downspouts and any shingle pieces in the yard.",
        "Photograph each ceiling stain or drip inside, with the date.",
        "Keep a short log: what you saw, when, and who you talked to.",
    ]),
    ("3. Limit further damage", [
        "Move furniture and electronics away from leaks; set out buckets and towels.",
        "If the roof is open, ask a roofing company to put on an emergency tarp. Policies usually expect reasonable steps to prevent more damage.",
        "Keep every receipt for tarps, supplies and emergency work.",
    ]),
    ("4. Read your policy before you file", [
        "Find your wind and hail deductible. In Texas it is often a percentage of the home's insured value rather than a flat dollar amount.",
        "See whether the roof is covered at replacement cost or actual cash value.",
        "Look for the time limit to report storm damage, and report promptly.",
    ]),
    ("5. Open the claim", [
        "Call your insurance company or file online, and write down the claim number.",
        "Have a roofer inspect the roof and document what it finds before the adjuster visits.",
        "You may ask the roofer to be there when the adjuster comes, to point out damage.",
        "Get the adjuster's estimate in writing and compare it with the roofer's.",
    ]),
    ("6. Hire with care", [
        "Texas does not license roofers. Ask for a certificate of liability insurance sent by the roofer's insurance agent, a local address and recent nearby jobs.",
        "Ask whether your city requires a permit or contractor registration, and who will pull the permit.",
        "Get the scope, shingle brand and line, price, schedule and workmanship warranty in writing before work starts. Never sign a contract with blanks.",
        "Do not pay most of the price up front.",
        "Texas law forbids a contractor to waive, rebate or absorb your deductible. Treat any such offer as a reason to hire someone else.",
        "The claim is between you and your insurer. A contractor may not act as your public adjuster; only a licensed public adjuster may negotiate a claim for you.",
        "Never sign on the spot under pressure from a door-to-door crew after a storm.",
    ]),
    ("7. When the work is finished", [
        "Get the final invoice, any permit and inspection papers your city issues, and the shingle maker's and roofer's warranties.",
        "Photograph the finished roof.",
        "If your insurer held back part of the payment (recoverable depreciation), send it the documents it asks for to release that money.",
        "If you replaced the roof, ask your insurer whether impact-resistant (Class 4) shingles qualify for a premium discount.",
    ]),
]


def bullets(items):
    return ListFlowable([ListItem(Paragraph(t, body), leftIndent=12) for t in items], bulletType="bullet", start="•",
                        leftIndent=12, bulletFontSize=9)


def main():
    out = ROOT / "src" / "static" / "files" / "dallas-hail-storm-claim-checklist.pdf"
    doc = SimpleDocTemplate(str(out), pagesize=letter, leftMargin=0.8 * inch, rightMargin=0.8 * inch,
                            topMargin=0.7 * inch, bottomMargin=0.7 * inch,
                            title="Hail and Storm Damage Roof Claim Checklist", author="DFW Expert Roofers",
                            subject="For Dallas-Fort Worth homeowners after hail or wind damage")
    story = [Paragraph("Hail and Storm Damage Roof Claim Checklist", title),
             Paragraph("For Dallas-Fort Worth homeowners. What to do in the first hours, days and weeks after hail or wind "
                       "damages your roof. From DFW Expert Roofers, dfwexpertroofers.com.", sub)]
    for head, items in SECTIONS:
        story += [Paragraph(head, h2), bullets(items)]
    story += [Spacer(1, 8),
              Paragraph(f"Need a roofer to look at it? Call {PHONE} at any hour. DFW Expert Roofers is a free phone line, not a "
                        "roofing contractor: it connects you with an independent local roofing company, which inspects, quotes and "
                        "does the work, and which you pay directly. Companies may pay the line a referral fee.", body),
              Paragraph("This checklist is general information, not legal or insurance advice. Policies differ, and your policy "
                        "and your insurer have the final word.", small)]
    doc.build(story)
    print("wrote", out)


if __name__ == "__main__":
    main()
