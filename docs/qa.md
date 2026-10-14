# QA record (DFW Expert Roofers, final run Oct 14 2026)

## Automated checks on the final build (dist/, 97 pages)
| Check | Command | Result |
|---|---|---|
| Build | `python3 build.py` | 97 pages built, 0 failures |
| Rules, SEO, links, images, forms | `python3 scripts/check.py` | 0 errors, 0 warnings |
| Old URLs | `python3 scripts/check_old_urls.py` | 92 old URLs and rules checked, 0 problems (details: docs/qa-urls.md) |
| Duplicate content | `python3 scripts/similarity.py` | 0 FAIL (details: docs/qa-similarity.md) |
| CLAUDE.md final grep | `python3 scripts/grep_check.py` | 0 hits (dashes, banned phrases, old name, Houston, Austin, San Antonio, (832), (903)) |
| Keyword plan | `python3 scripts/keyword_plan.py` | 783 keywords with 10+ searches: 353 assigned, 430 unused with reasons, 0 unclassified |
| Photos | `python3 scripts/apply_image_reuse.py` | 44 photo files (38 distinct photos), 14 planned slots registered, 13 in use |
| Browser | `node scripts/responsive_check.js` (Playwright, Chromium) | 396 page loads at 1440, 1024, 768, 390 (all pages) and 1920, 2560 (sample): 0 problems |

The browser check looks for horizontal overflow (no overflow is hidden to pass), broken images, JS
errors, a hero that is not edge to edge, a hero taller than 720px or a call button below the fold at
1024px and up, a hero headline off the left rail at 1440px and up, and card, panel, step, fact and split
rows whose short last row leaves a hole on the right (390, 768, 1024, 1440, 1920).

## Jaccard similarity, 5-word shingles (CLAUDE.md rule 11)
```
Page pairs (Jaccard, 5-word shingles):
  area     pairs=2211 max=2.3% mean=0.3% min=0.0%
  guide    pairs=  10 max=0.4% mean=0.2% min=0.0%
  legal    pairs=   1 max=0.9% mean=0.9% min=0.9%
  mixed    pairs=2073 max=0.9% mean=0.1% min=0.0%
  page     pairs=  10 max=0.7% mean=0.2% min=0.0%
  service  pairs=  66 max=1.2% mean=0.2% min=0.0%
Against /home/user/houston-roofing-pro/dist (55 pages): max Jaccard 3.1% (/privacy-policy.html vs /privacy-policy.html); pages sharing an 8-word run: 0
```
Every pair of pages of the same type is at or under 2.3%, far below the 15% limit. Against every
Houston Expert Roofers page the highest score is 3.1% (the privacy policies), and no DFW page shares any
run of 8 words with a Houston page. Shared template parts (header, footer, call band, the how-it-works
strip, the disclosure and license notes, link pills, sources) are excluded on both sides, as are the
contact form's mandated option list and two keyword Question rows used verbatim as FAQ questions.

## Visual review (screenshots, scrolled so every photo loaded)
Home page at 390, 1440 and 2560; /roofing-company-frisco-tx/ at 1440 and 1920; /roofing-rockwall-tx/ at
1440 and 2560. Checked section by section: navy header with phone and the gold/white EN-ES toggle; hero
edge to edge with the dark left-to-right fade, logo, headline and buttons on the left rail
(rail = clamp(22px, 5.5vw, 140px)); white sections broken by a navy band, a deep red band and the gold FAQ
band; centered card rows; no white text or white boxes on white; full-width footer town grid in rows; no
broken images. Two fixes came out of the review: a photo-first split now keeps the photo in the narrow
column, and a white section followed by a band gets bottom spacing so a photo never touches the band.

## Forms
Both Netlify forms are in the static HTML with their exact names and fields (checked by check.py):
dallas-roofing-contact on /contact/ (name, phone, city, need, message, bot-field; the seven live "need"
options; action /contact/thanks/) and dallas-hail-checklist on /hail-claim-checklist/ (name, email,
zip, phone, bot-field; action /hail-claim-checklist/thanks/, which links the rebuilt PDF). No test
submissions were sent (no production leads without authorization), so delivery is NOT verified.
