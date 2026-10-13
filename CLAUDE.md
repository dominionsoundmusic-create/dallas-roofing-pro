# DFW Expert Roofers (dfwexpertroofers.com): PLAYBOOK 2.0 REBUILD. INSTRUCTIONS FOR CLAUDE CODE

You are rebuilding Maurice Johnson's Dallas-Fort Worth roofing referral-line site from scratch by
running Dominic & Dalton's Website Builder Prompt Playbook 2.0 (PLAYBOOK.md), Prompts 1 to 20, in
full. This is the biggest build so far (about 100 pages, about 69 of them town pages). Every page is
researched and written by hand for its own keyword. NO TEMPLATES, no name-swapped pages.

## RUN STRAIGHT THROUGH. DO NOT STOP.
Maurice is not watching this session and cannot approve anything. Do NOT pause at the end of each
playbook phase, do NOT ask "continue?", do NOT wait for input. Make reasonable decisions yourself,
write them down in docs/decisions.md, and keep going until Prompt 20 is finished and every check
below passes. Commit and push the `build` branch after each phase so work is never lost if the
session ends (pushing `build` does not go live). The only reasons to stop early: something would
cost money, deploy, merge to main, or change a repository other than this one.

## Source files (read all of them first)
- INTAKE.md: the facts. It wins over anything else. UNKNOWN means leave it off the site.
- PLAYBOOK.md: the playbook (Operating Rules, then Prompts 1 to 20). It was written for GHL AI
  Studio; apply its rules and its 20 steps to this static build system.
- keywords/DFW-Roofing-Keywords.xlsx: Ubersuggest, United States, pulled Oct 13 2026. 1,548 unique
  keywords, a tab per seed (15 service seeds, 75 town seeds) plus an ALL tab, each row typed
  Suggestion or Question. The "roofing dallas" Questions export is missing; the other Dallas
  service seeds cover those questions. Every DFW keyword with a volume of 10 or more must be
  assigned to a page as a target or supporting keyword, or listed in docs/keyword-plan.md as
  deliberately unused with a one-line reason. "Near me" terms are national volume: supporting
  keywords only, never proof of DFW demand. Rows about other states or metros (Saginaw MI, Allen
  or Garland outside Texas and so on), rows naming a specific roofing company, and off-topic rows
  (weather, zip codes, "where is ...") go in the unused list (summarize by group).
- The CURRENT site in this repo: every existing page holds research (DFW hail, storm damage, roof
  replacement cost, hail claim steps). Read every page before writing. Keep the facts that check
  out, verify them again, and improve them for each page's keyword. Never copy the old layout.

## Copy the build system from Houston Expert Roofers (NOT its words)
Clone dominionsoundmusic-create/houston-roofing-pro, branch `build` (a finished Playbook 2.0 roofing
site, checked Oct 13 2026, with the full-width layout, centered card rows, photo reuse script and
old-URL check). Copy its BUILD SYSTEM: build.py (Jinja2, writes dist/), scripts/check.py,
scripts/similarity.py, scripts/check_old_urls.py, scripts/apply_image_reuse.py and
docs/image-reuse.json pattern, src/templates/, src/static/css/site.css and JS, the macros, the
site.json structure, netlify.toml (publish = "dist") and the docs/ document set as a pattern.
Adapt every value to DFW Expert Roofers. NEVER copy page text, paragraphs, FAQs or sentence runs
from Houston or any other site; the similarity script must also compare DFW pages against the
Houston pages and stay under 15%.
Keep the speed fix exactly (WebP 480/800/1200/1600/1920 srcset, preloaded hero with fetchpriority
high, self-hosted woff2 font) and the full-width layout (`--rail: clamp(22px, 5.5vw, 140px)`;
header, hero content, bands, text, photos, cards and footer all on the same left and right edge).
Card rows: 3 / 2 / 1 columns, any short last row CENTERED, never a hole on the right. Footer town
list runs across the full width in rows, never one long column.

## PHOTOS: REUSE FIRST (Maurice's standing rule)
1. Use the 15 photos in images/ first.
2. Then reuse GENERIC roof photos from the Houston build (houston-roofing-pro branch `build`,
   src/static/images): roofs, shingles, hail and storm damage, inspections, tarps, gutters,
   flashing, metal and flat roofs. Copy only photos that show nothing Houston-specific (no
   Houston skyline, bayou, palm-lined coast or Houston landmark) and write new alt text for DFW.
3. One photo may fill several spots across the site, but never twice on the same page.
4. Only after that, list what is still needed in docs/image-list.md (heroes first; town heroes may
   share a pool of DFW-suburb street photos). Aim for 20 or fewer new Artistly images. Each needed
   image shows a reused photo (never a broken image or an empty box) until it arrives.

## OLD URLS MUST KEEP WORKING
Every URL the live site has today must still return a page or a 301 to the closest new page:
/, /about/, /contact/, /contact/thanks/, /faq/, /services/, /free-roof-inspection/,
/hail-claim-checklist/, /hail-claim-checklist/thanks/, /hail-damage-roof-repair/,
/roof-leak-repair/, /roof-repair/, /roof-replacement/, /storm-damage-roof-repair/,
/commercial-roofing/, /privacy-policy.html, /terms.html, /carrollton-roofing/,
/roofing-arlington-tx/, /roofing-companies-fort-worth-tx/, /roofing-companies-mckinney-tx/,
/roofing-company-allen-tx/, /roofing-company-flower-mound-tx/, /roofing-company-frisco-tx/,
/roofing-company-irving-tx/, /roofing-company-lewisville-tx/, /roofing-company-mesquite-tx/,
/roofing-company-richardson-tx/, /roofing-contractors-plano-tx/, /roofing-denton-tx/,
/roofing-garland-tx/, /roofing-grand-prairie-tx/, /files/dallas-hail-storm-claim-checklist.pdf,
plus every rule in the current _redirects (keep them all). Keep a URL where it already ranks for
its keyword; otherwise 301 it. Pick ONE consistent URL pattern for NEW town pages and record it in
docs/decisions.md. Write scripts/check_old_urls.py that lists every old URL and proves it resolves
in dist/ or has a redirect. Move the old page files into docs/old-site/ with `git mv` so they are
not published. Keep images/, favicons and files/ in the new static folder.

## Pages to build (decide the exact list from the keywords, then follow it)
- Core (about 13): home (target "roofing company in dallas"), services overview, service areas
  overview, how it works, about, FAQ, contact + thanks, hail claim checklist + thanks, privacy,
  terms, 404.
- Service pages (about 12), one per real service with DFW demand: roof repair, roof replacement,
  roof leak repair, storm damage, hail damage, wind damage, roof inspection, emergency roof repair
  and tarping, commercial roofing, flat roof repair, metal roofing, plus anything else the data
  supports.
- Guide pages (about 5), each researched and sourced: roof replacement cost in Dallas-Fort Worth;
  roof insurance claims in Texas (hail and wind, deductibles, ACV vs replacement cost, what a
  roofer may and may not do under Texas law, including the deductible law); how to check a roofer
  before hiring (Texas has no state roofing license: state it correctly, plus city contractor
  registration where it exists); how long a roof lasts in North Texas; emergency steps after storm
  damage.
- Town pages: Maurice's rule is ANY DFW town with 10 or more searches a month on a ROOFING keyword
  gets its own page. A first pass of the data found 69 towns that pass and 6 that do not (Balch
  Springs, Fate, Highland Park, Royse City, Terrell, University Park: no page). Check every town in
  the data yourself: count only Texas rows, only roofing keywords, and do not count rows that name
  a specific roofing company or another state. A town whose only 10+ rows are company names gets no
  page. Record the exact keyword and volume per town in SERVICES.md. Keep the existing town URLs
  for the 15 towns that already have pages.
- Write SERVICES.md (every page, URL, target keyword with volume/SEO difficulty) and
  docs/keyword-plan.md BEFORE writing pages.

## TOWN PAGES: ORIGINAL RESEARCH, NEVER A TEMPLATE
Each town page is researched on the web for THAT town and written from that research. Before
writing a town, gather and keep notes in docs/research/<town>.md with sources: its county; its own
hail, tornado and storm history (named events and dates, e.g. the hailstorms and tornadoes that
hit that town, verified); housing age and common roof types in its neighborhoods; real
neighborhoods, subdivisions or areas residents would recognize; its building or permit office and
whether that city requires a roofing permit or contractor registration; HOA rules where relevant;
anything local that affects roofs (trees, wind exposure, lake or prairie location). Each page leads
with what is true and particular about that town. Different towns get different section orders and
different angles; do not run the same outline 69 times. Small towns with little documented history
get shorter pages, honestly, rather than padding. If a fact cannot be verified, leave it out.

## Hard rules for every page
1. Never "our roofers", "our crew", "our team", "we repair", "we replace", "we inspect", "we
   install", "we are licensed/insured/certified" or anything implying the line does roofing work.
2. Never invent licenses, certifications, insurance, reviews, ratings, prices, years in business,
   team members, job counts, guarantees, response times, awards or statistics. Tell readers what
   to ask a roofer for.
3. Never name a specific roofing company (partner or not). Shingle brands may be named only as
   general product information, never as a partner certification.
4. Only DFW places. No other Texas metros.
5. No em dashes or en dashes in visible copy (except the Duplantis credit). No eyebrow labels.
   American spelling.
6. Safety first, no DIY roof work: never tell a homeowner to climb on a roof. Safe steps only:
   stay off the roof, move belongings away from a leak, catch drips, photograph damage from the
   ground and inside, stay away from downed lines (call Oncor or the local utility), call the
   insurer.
7. No prices presented as the line's prices. Cost guides cite published, sourced ranges and say
   real quotes vary. Never say insurance will pay; say what to ask the insurer. Never suggest a
   roofer can waive or cover a deductible (research the Texas law and state it correctly).
8. Every page except privacy, terms and 404 has 3 to 6 FAQs written the way people ask (use the
   Question rows), rendered visibly AND as FAQPage JSON-LD.
9. Every page has a full-width hero image plus at least two in-body images, each with filename,
   alt, width, height and loading="lazy" (hero eager), following the PHOTOS section above.
10. Facts must be real and current. Research each page on the web and cite every source in the
    page's sources list. If you cannot verify a fact, leave it out.
11. Each page is written for its own keyword. Measure Jaccard similarity on 5-word shingles between
    every pair of pages of the same type, and every DFW page against every Houston roofing page;
    any pair above 15% gets rewritten. Record the numbers in docs/qa.md.
12. The referral disclosure appears on every page (wording in INTAKE.md).
13. Banned phrases: "your trusted partner", "one-stop solution", "look no further", "unmatched
    excellence", "we've got you covered", plus the WORDS TO AVOID in INTAKE.md.
14. Never write the old name "Dallas Metro Roofing Pro" anywhere.
15. Mark every page with the HTML comment `dwdp:handwritten 2026-10-13` in the first 4KB.

## Design (Maurice's standing rules, check each one)
- Header/menu bar in a real brand color (the navy), never dull gray. Phone visible with
  tap-to-call. EN/ES Google Translate toggle in the header on every page, in brand colors.
- Hero stretches edge to edge on every page: full-strength photo, dark left-to-right fade behind
  the headline, logo/headline/buttons aligned to the left rail at 1440, 1920 and 2560 wide. Hero
  stays above the fold (max-height about 700px) with the call button visible.
- Body text, photos and cards run FULL WIDTH on the rail. Never box text into a narrow center strip.
  A photo standing alone in the text run is capped at about 560px tall (object-fit: cover).
- Mostly WHITE sections broken by occasional bold color bands (hero, white, navy band, white, a
  second band in gold or deep red). Never pale off-white or cream tints. Never every section tinted.
- No white text or white boxes on white. Every card, box, form field and button has clear contrast.

## Before you finish (all must pass)
- `python3 build.py` then `python3 scripts/check.py`: 0 errors.
- `python3 scripts/check_old_urls.py`: every old URL resolves or redirects.
- Grep the built site for: em/en dashes in visible text (except the Duplantis credit), "we
  repair", "we replace", "we inspect", "our roofers", "our crew", "our team", "licensed and
  insured", "free estimate", "free inspection", "same-day", "guarantee", "GAF certified",
  "Dallas Metro Roofing Pro", "Houston", "Austin", "San Antonio", "(832)", "(903)". Fix every hit
  (a "Houston" hit is allowed only inside a sourced weather or insurance fact that truly needs it).
- No horizontal overflow at 1440, 1024, 768 and 390 px wide (do not hide overflow to pass).
  Scan every page for card, step and photo rows that leave a hole on the right at 390, 768, 1024,
  1440 and 1920 wide, and fix them. Screenshot the home page and two town pages at 1440, 1920 and
  2560, scroll so every photo loads, and look at each section yourself: hero content near the left
  edge, nothing invisible, no white on white, rows centered, no broken images.
- Both Netlify forms present in the static HTML with their exact names and fields.
- Independent fact-check: start separate sub-agents that did not write the pages (split the town
  pages among several), have them check every factual claim and source on every page, and fix
  what they find. Record it in docs/fact-check.md. Never say "fact-checked" unless this was run.
- docs/image-list.md lists every image still needed, heroes first: File name, Size (heroes
  1920x1080, in-body 1200x800), then an Artistly prompt (bright, clearly visible, North Texas
  homes and roofs, no text, no logos, no recognizable faces, "wide cinematic landscape shot,
  subject positioned on right third of frame, well lit").

## Git
- Work on the branch `build`. Commit as you go with clear messages and push `build` after each
  phase. The live site deploys from `main`, so pushing `build` does not go live.
- Do NOT merge to main, do NOT push to main, do NOT change Netlify settings, do NOT pay for
  anything. Maurice decides when it goes live.

## Final report (Maurice reads on his phone, 5 lines max)
Pages built (count by type), checks passed, old URLs all resolving (yes/no), duplication range,
fact-check result, how many images need Artistly, and the one thing Maurice must do next.
