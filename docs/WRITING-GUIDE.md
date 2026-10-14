# Writing guide: dfwexpertroofers.com pages (Playbook 2.0 rebuild, Oct 13 2026)

Repo: /home/user/dallas-roofing-pro (branch `build`). Read first, in full:
1. `CLAUDE.md` (hard rules) and `INTAKE.md` (facts; it wins; read "WHAT THE BUSINESS ACTUALLY IS" twice).
2. `SERVICES.md` and `docs/keyword-plan.md`: your page's URL, TARGET keyword, supporting keywords and the
   Question rows (turn those into FAQs, written the way people ask).
3. `src/data/site.json` (slugs, names and URLs of services, guides and the 67 towns).
4. `src/templates/macros.html` (service_cards, guide_cards, area_cards, area_pills, related, call_box,
   how_it_works_short, disclosure, license_check, deductible_note, safety_box, sources).
5. `docs/photos.json` (every photo you may use, its size, what it shows) and `docs/image-reuse.json` (new
   images planned but not made yet; each is shown through an existing photo until it arrives).
6. YOUR PAGE'S OLD VERSION, if any, in `docs/old-site/` (plain text copies are listed in the task).
   Keep facts that check out after you verify them again; never copy its wording or layout. Some old
   advice is banned now ("have a roofer install a tarp" is fine, but nothing DIY; no "insurers often pay
   for a full replacement"; no "free inspection").
7. STRUCTURE ONLY: `/home/user/houston-roofing-pro/src/pages/roof-repair.html` (a service page) and
   `/home/user/houston-roofing-pro/src/pages/roofing-webster-tx.html` (a town page) show the front matter
   format, section rhythm and macro use of a finished sister site. NEVER copy a sentence, FAQ or phrase
   from any Houston page. `scripts/similarity.py` compares every DFW page with every Houston page and FAILS
   on any shared run of 8 words or a Jaccard score above 15%.

## The business in one paragraph
DFW Expert Roofers is a FREE PHONE LINE and website, NOT a roofing company. An automated assistant
answers at any hour, asks which service the caller needs (the same number also answers air conditioning
and heating and pressure washing calls) and what is going on with the roof, then transfers the call to
an independent, locally owned DFW roofing company, which hears a short summary before it picks up. If
that company cannot answer, the caller's name, callback number, city, need and urgency are passed on for
a call back. The roofing company inspects, quotes, does the work and is paid directly by the customer
(or the customer's insurer, as the customer arranges). The line never climbs a roof, inspects, sells,
quotes, repairs, replaces, tarps, files claims or schedules anything; it holds no license and never
charges the caller; companies may pay it a referral fee. Write "the roofing company you are connected
with", "the roofer", "a roofing company that takes calls in Keller". NEVER "our roofers", "our crew",
"our team", "we repair/replace/inspect/install/tarp", "we'll send someone", "we are licensed/insured".
Never say connected companies are licensed, insured, certified (GAF, Owens Corning, CertainTeed or any
program), rated, reviewed, fast or experienced. Never name a roofing company, supply house or contractor.
Shingle brands only as general product information. The phone number is NEVER typed in a page: use
`{{ site.business.phone_display }}`, `tel:{{ site.business.phone_tel }}` or `{{ site.cta.primary_label }}`.
Public agency numbers (a city permit office, TDI, Oncor) are fine when sourced.

## Hard rules (scripts/check.py enforces most; your pages must show 0 errors)
- No em dashes or en dashes anywhere (copy, titles, descriptions, FAQs, alt text, source labels). Use
  commas, colons, periods or "to" ("15 to 20 years"). American spelling. No eyebrow labels or badges.
- Only DFW places (Dallas, Tarrant, Collin, Denton, Rockwall, Kaufman, Ellis, Johnson, Parker, Hood
  counties and their towns). Never name Houston, Austin, San Antonio, El Paso, Lubbock, Waco, any other
  Texas metro, another state or a coastal topic (TWIA, windstorm certificates), not even in a comparison
  or a source label. Shorten a source label that names one.
- Never invent licenses, certifications, insurance, reviews, ratings, prices, years in business, team
  members, job counts, guarantees, response times, awards or statistics. Public statistics are fine with
  the source named in the sentence and listed in Sources. Prices: explain what drives them; a published
  range only with its source named on the page and a line that real quotes vary. Never a price as the
  line's price. Never "insurance will pay"; say what to ask the insurer.
- Banned (checker fails): "free estimate(s)", "free inspection", "same-day", "same day", "guarantee" in
  ANY form (also "guaranteed": use "promise" or "warranty"), "best price", "cheapest", "top-rated",
  "years of experience", "#1", "number one", "licensed and insured", "fully insured", "GAF certified",
  "certified roofer/contractor/installer", "we work with all insurance", "we handle your claim", "no out of
  pocket", "we pay your deductible", "deductible waived", any response-time promise ("within 2 hours"),
  "your trusted partner", "one-stop solution", "look no further", "unmatched excellence", "we've got you
  covered", "our team", "our crew", "our roofers", "Dallas Metro Roofing Pro", and "we + any work verb".
  Say "many roofers inspect at no charge; ask on the call" instead of "free inspection".
- SAFETY FIRST, NO DIY ROOF WORK. Never tell anyone to climb on a roof, put a ladder up to the roof,
  tarp it themselves, poke a hole in a ceiling or work in the breaker panel. Safe steps only: stay off
  the roof; move belongings away from a leak; catch drips; keep people out of a room with a sagging
  ceiling; photograph from the ground and inside; stay away from downed lines and report them to Oncor
  (or the town's own electric provider when your research confirms it) or 911; call the insurer.
  `m.safety_box()` says this (pass `utility='...'` on a town page whose provider is not Oncor).
- Texas law (verified Oct 13 2026; `m.deductible_note()` and `m.license_check()` carry it):
  TDI: a contractor may not waive, rebate or absorb a deductible or pad an estimate to cover it; a contract
  of $1,000 or more paid with insurance money must include a notice that the insured owes the deductible;
  the insurer may ask for proof it was paid (Business and Commerce Code 27.02; Insurance Code 707.002).
  Only a licensed public adjuster may negotiate a claim for you; a contractor may not act as a public
  adjuster on a property it works on or may work on (Insurance Code 4102.163, broadened to all contractors
  in 2019). Texas has no state roofing license; HB 3344 (2025) to create one cleared committee but died
  without a House floor vote. Report deductible offers to the Attorney General consumer line 800-621-0508.
  Sources: https://www.tdi.texas.gov/tips/can-a-contractor-waive-my-deductible.html ,
  https://www.tdi.texas.gov/Consumer/storms/roofing-and-insurance-know-the-law.html ,
  https://capitol.texas.gov/tlodocs/89R/analysis/html/HB03344H.htm
- Cities differ. Some require a permit for a re-roof and some make roofers register: research YOUR city
  on its own site (search with `allowed_domains` set to the city's domain). Plano (verified): a permit is
  required for all re-roof projects; the city does a final roof inspection (Plano Building Inspections,
  1520 K Avenue, Suite 220; https://www.plano.gov/220/Building-Inspections). Unincorporated county land
  usually has no city permit: say so only if you find it stated.
- Facts must be real and current. WebSearch works (WebFetch and curl do not reach outside sites here),
  so verify against search results from the official or primary source. Cite every source you use in
  the page's `m.sources([...])` list with a plain label and the URL. If you cannot verify it, leave it
  out. Never cite a page you did not see in results. Search frugally (the search budget is shared by all
  writers): combine questions in one query, and if a search returns a limit error, stop researching,
  write only what you verified, and report what is left.
- Each page is written for its own keyword and its own facts. Do not reuse paragraphs, outlines or stock
  sentences between pages. Within each type (towns, services, guides) every pair must stay under 15%
  Jaccard on 5-word shingles; vary sentence openings, section order and angles.

## Page format
YAML front matter then `{% block content %} ... {% endblock %}`. Front matter:
- `type`: service | guide | area (towns) | page
- `title`: 50 to 65 characters, has the target keyword or a close form, unique, no dashes.
- `description`: 120 to 160 characters, unique, has the keyword.
- `h1`: one clear H1 (the hero shows it). Town H1s name the town; service H1s name the service.
- `crumb`, `keyword` (the exact target keyword), `card_summary` (one or two sentences, 120 to 200
  characters, used on cards and lists elsewhere: what is specific to this page).
- Towns also: `city_name`, `county` (as verified, for example "Collin" or "Collin and Denton"),
  `schema_service: {name: "Free connection to a local roofing company in <Town>, Texas", type: "Roofing referral"}`.
- `hero`: `image`, `alt` (what the photo shows; no town claim for a reused photo), `lead` (one or two
  sentences, under 260 characters), `secondary_label` + `secondary_href` (a useful in-page anchor or
  page), optional `position` (CSS object-position). Optional `desc` is not needed.
- `cta_title` (optional): a page-specific heading for the closing call band. `faq_title` (optional):
  a page-specific heading for the FAQ block (default "Questions North Texas homeowners ask").
- `faqs`: 3 to 6 items; `q` the way people ask (use Question rows), `a` HTML (`<p>...</p>`), 50 to 110
  words, at least one internal link across the set. They render visibly and as FAQPage JSON-LD.
- URL: comes from the file name: `src/pages/roofing-keller-tx.html` -> /roofing-keller-tx/. Never set
  `url:` unless told to.

## Photos (Maurice's rule: reuse first)
- Hero plus at least TWO in-body images (`{{ img('file.jpg', 'alt text', W, H) }}`, W and H from
  docs/photos.json, or 1200, 800 for a planned in-body image; heroes 1920x1080).
- Use only files in docs/photos.json or keys in docs/image-reuse.json. Do not invent new image names.
- One photo never twice on the same page. Files in the same `group` are the same photo (roof-02-hero.jpg
  and roof-02-card.jpg), and a planned image counts as its stand-in (`from`). SERVICE CARDS SHOW PHOTOS
  TOO: each service in site.json has a `card_image`; if your page shows `m.service_cards([...])`, do not
  use those services' card photos (or their groups) for your hero or body images. check.py fails a
  repeat.
- Alt text describes what the photo really shows. Never claim a reused photo was taken in your town.
- Town heroes: use one of the planned DFW pool images where it fits the town (dfw-suburb-brick-two-story-
  street-hero.jpg, dfw-older-ranch-homes-pecan-trees-hero.jpg, dfw-new-subdivision-rooftops-hero.jpg,
  dfw-lakeside-homes-shingle-roofs-hero.jpg, north-texas-small-town-historic-homes-hero.jpg,
  north-texas-ranch-land-home-metal-roof-hero.jpg, north-texas-supercell-over-suburb-hero.jpg,
  dfw-storm-damaged-roofs-tarps-street-hero.jpg) or an existing 1920-wide photo. Spread the choice so
  neighboring towns do not all share one hero.

## Sections and design
Mostly white sections (`<section class="prose">`) with at most two color bands per page
(`<section class="band band--tint"><div class="wide">...</div></section>`; the first becomes navy, the
second deep red, automatically; the FAQ band is always gold). Never two bands back to back. Parts:
`.split` (text + image side by side), `.grid-2` / `.grid-3` with `.panel`, `<ol class="steps">`,
`<ul class="checks">`, `<ul class="facts">`, `<div class="table-wrap"><table>` with `<thead>`, `.note`,
`m.call_box()`. H2 for sections, H3 inside. Give each page at least one treatment that suits it (a storm
timeline, a comparison table, a checklist, a permit step list) and do not run the same outline on every
page. Card rows center a short last row automatically; use 3, 6 or 2/4 cards where you can.

### Town page (Prompt 11): research first, then write
Before writing, save notes in `docs/research/<town-slug>.md` with a source URL for each fact:
county or counties; incorporated city or not; the city's building/permit office and whether a re-roof
needs a permit or the roofer must register (from the city's own site); storm history that actually hit
THAT town (named tornadoes and hailstorms with dates, from NWS, NOAA, the city or reliable news);
housing age and common roof types; real neighborhoods, subdivisions or areas residents know (verified);
HOA notes where relevant (Texas Property Code 202.011 lets owners use impact-resistant or energy-efficient
shingles an HOA cannot ban outright, if they look like allowed ones: verify before citing); local factors
(lake, trees, prairie wind, growth, rural acreage); the electric provider. Also list what you could NOT
verify and left out.
Then write the page from that research. Lead with what is true and particular about the town. Include:
a localized opening section with an image beside it (`.split`); services that fit the town
(`m.service_cards([...])`, 3 or 6 slugs); four local reasons people there call (four `.panel`s or another
treatment, each reason tied to a local fact); the permit or registration facts; storm history if any;
questions to ask a roofer there; FAQs; `m.how_it_works_short()` or a short plain explanation;
`m.disclosure()`; `m.related([...])` with 2 to 4 nearby towns (`'area:slug'`) and a guide (`'guide:slug'`);
`m.area_pills(exclude='slug')` under a heading such as "Other towns the line covers"; `m.sources([...])`.
Length: 1,200 to 2,000 words of page copy for a well documented town; a small town with little
documented history gets a shorter, honest page (800 words or more) rather than padding. Vary the order of
sections and the angle from town to town. Never invent an office, address, customer count, project
history or travel time.

### Service page (Prompt 9), about 1,500 to 2,200 words
What the service is; who needs it; common problems on North Texas roofs; how a careful roofer handles it
(the line's own part is only: answer, connect, pass details); options and what to expect; questions to
ask; a design treatment; `m.related([...])`; `m.how_it_works_short()`, `m.license_check()`,
`m.disclosure()`; `m.area_pills()`; Sources.

### Guide page, about 1,800 to 2,500 words
Answer the target question in the first paragraph, then go deep: sourced facts, a table or checklist,
what to ask, mistakes to avoid, `m.disclosure()`, a fitting call box. `type: guide`.

## Before you report back
Build to YOUR OWN output folder so writers do not collide:
`python3 build.py --out /tmp/<your-name>/dist` then
`python3 scripts/check.py --dist /tmp/<your-name>/dist --only <your url> --skip-links` (0 errors) and
`python3 scripts/similarity.py --dist /tmp/<your-name>/dist --only <your url>` (no FAIL for your page).
Do not edit shared files (site.json, templates, CSS, scripts) and do not commit; report needed changes.
