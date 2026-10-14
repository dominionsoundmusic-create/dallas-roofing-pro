# Fact-check fc1: core pages, two guides, shared macros and checklist PDF (Oct 14 2026)

Checker: fc1 (independent; did not write these pages). 33 web searches used. WebFetch/curl unavailable, so
claims were checked against search results from official domains (capitol.texas.gov, tdi.texas.gov,
texasattorneygeneral.gov, city sites, weather.gov) where possible.
Result key: VERIFIED, CORRECTED (page changed), REMOVED, OK-UNCHECKED (generic, needs no source).

## / (index.html)

| Claim | Source | Result | Action |
|---|---|---|---|
| May 5, 1995 Mayfest storm, softball-size hail, Fort Worth | NWS FWD mayfest15; Wikipedia; WFAA | VERIFIED | none |
| "the National Weather Service put its damage ... at about $2 billion" | Wikipedia, WFAA give $2B; NWS page in results did not show the figure | CORRECTED | Attribution to NWS removed; now "left about $2 billion in damage"; NWS Mayfest page added to sources; Wikipedia label shortened |
| June 13, 2012 storm "sent baseball-size hail into North Dallas" (KERA URL) | NWS FWD june132012: baseball, orange, softball hail across Dallas, Collin, Fannin; North Dallas car windows and skylights. KERA URL not found in search | CORRECTED | Sentence rewritten to the NWS facts; KERA source replaced with NWS june132012 |
| Dec 26, 2015 tornado crossed Sunnyvale, Garland, Rowlett | NWS FWD damage survey (EF4, start near Sunnyvale); Wikipedia | VERIFIED | NWS survey PDF added to sources |
| EF3 tornado in North Dallas Oct 20, 2019 | NWS FWD tornadoes-october2019 | VERIFIED | none |
| DFW Airport fell to -2 F on Feb 16, 2021 | NWS FWD Feb-2021-WinterEvent | VERIFIED | none |
| TPR: 878 hail events of 1 inch+ in Texas in 2024, most of any state | TPR (May 2026) actually reports 902 major hail events in Texas in 2025 (Insurance Information Institute figure); 878 not found anywhere | CORRECTED | Now "Citing the Insurance Information Institute, TPR reported 902 major hail events (stones an inch across or larger) in Texas in 2025, more than any other state" |
| Worst hail usually March to June | general NWS climatology | OK-UNCHECKED | none |
| Dallas and Plano require a re-roof permit; some cities register roofers | Dallas storm repair page; Plano re-roof sheet; Richardson, Arlington, Garland pages | VERIFIED | Plano source URL corrected (see below) |
| Deductible law (waive/rebate/absorb barred) | TDI waive-deductible tip; B&C Code 27.02 | VERIFIED | none |
| 67 town pages, ten counties | site.json (67 areas); INTAKE.md | VERIFIED | none |
| Plano source URL plano.gov/220/Building-Inspections | Search shows the Building Inspections page at plano.gov/217/Building-Inspections; /220 never surfaced (the team's own plano.md cites /217; "220" appears to be a suite number) | CORRECTED | Changed to /217/ |

## /services/

| Claim | Source | Result | Action |
|---|---|---|---|
| Twelve kinds of roof work | site.json services (12) | VERIFIED | none |
| HB 3344 / no state license (license_check) | capitol.texas.gov HB03344H analysis; LegiScan: committee report sent to Calendars May 8 2025, died | VERIFIED | none |
| Service descriptions, repair vs replace advice | generic | OK-UNCHECKED | none |

## /service-areas/

| Claim | Source | Result | Action |
|---|---|---|---|
| "Dallas, Fort Worth and 65 more towns" / "65 suburbs" | site.json: 67 town pages = Fort Worth + 66 others (Dallas has no town page) | CORRECTED | description and hero lead now say 66 |
| 67 town pages; county lists by area | site.json | VERIFIED | none |
| Dallas and Plano require a permit for every re-roof | Dallas: permit for large areas or whole roof; Plano: re-roof permit | VERIFIED | none (FAQ wording "every re-roof" is fair for whole-roof jobs) |
| Neighborhood housing descriptions (1950s ranches, 1980s/90s brick, new subdivisions) | generic | OK-UNCHECKED | none |
| Plano source URL | as above | CORRECTED | /217/ |

## /how-it-works/, /about/, /faq/

| Claim | Source | Result | Action |
|---|---|---|---|
| How the call works (assistant, transfer, call back, referral fee) | INTAKE.md | VERIFIED | none |
| d/b/a of Dominion Digital Group | INTAKE.md | VERIFIED | none |
| Only licensed public adjusters may negotiate; contractor may not adjust where it works | Ins. Code 4102.163 (texas.public.law); TDI know-the-law and B-0007-25 | VERIFIED | none |
| A roofer may document damage and discuss its estimate with the adjuster | TDI FAQ and Bulletin B-0007-25 | VERIFIED | none |
| Texas never created a roofing license; 2025 bill died without floor vote | HB 3344 analysis, LegiScan | VERIFIED | none |
| Insurer may ask for proof the deductible was paid | TDI tip; Ins. Code 707 | VERIFIED | none |
| Percentage deductibles common in Texas; hail claim may affect premium | TDI deductibles tip | VERIFIED / OK-UNCHECKED | none |
| Roofing season, winter work, noise hours | generic | OK-UNCHECKED | none |
| Plano source URL (faq) | as above | CORRECTED | /217/ |
| Two DIY warnings from check.py (about, how-it-works) | false positives: the sentences say the site never asks you to climb, and "check its insurance" | OK | none |

## /contact/, /contact/thanks/, /hail-claim-checklist/, /hail-claim-checklist/thanks/

| Claim | Source | Result | Action |
|---|---|---|---|
| Form names and fields (dallas-roofing-contact: name, phone, city, need, message, bot-field; dallas-hail-checklist: name, email, phone, zip, bot-field) | INTAKE.md; site.forms | VERIFIED | none |
| No public email, no office | INTAKE.md | VERIFIED | none |
| Checklist sections match the PDF's seven sections | scripts/make_checklist_pdf.py | VERIFIED | none |
| Deductible notes | TDI | VERIFIED | none |

## /privacy-policy.html, /terms.html

| Claim | Source | Result | Action |
|---|---|---|---|
| GA4, Netlify forms, Google Translate cookie | INTAKE.md and the build | VERIFIED | none |
| Texas Data Privacy and Security Act may give additional rights | statute exists (eff. July 1 2024); "may" wording | OK-UNCHECKED | none |
| Texas does not issue a state roofing license | HB 3344 analysis | VERIFIED | none |

## /do-roofers-need-a-license-in-texas/

| Claim | Source | Result | Action |
|---|---|---|---|
| No state roofing license, exam or board | HB 3344 committee analysis ("does not currently require") | VERIFIED | none |
| HB 3344 (2025) would license re-roofing contractors through TDLR; cleared House committee (Trade, Workforce & Economic Development, heard Apr 15 2025); no floor vote; died | capitol.texas.gov analysis, fiscal note, witness list; LegiScan | VERIFIED | none |
| RCAT voluntary "Licensed Roofing Contractor"; exams (business/safety + roofing), proof of liability insurance, annual renewal | Jobber, Labyrinth, NEXT, Arrivy (third-party, consistent on these points; details like fees conflict and are left off) | VERIFIED (weak sources) | none |
| Dallas: re-roof permit for large areas or entire roof; minor repairs and tarps exempt; registered contractor on application; homeowner exemption form | dallascityhall.com storm damage page; homeowner exemption PDF | VERIFIED | none |
| Fort Worth: shingle-only on 1 or 2-family home no permit; decking/sheathing/rafters need one; Contractor Registration required except homestead owner | fortworthtexas.gov roofing FAQ and residential info | VERIFIED | none |
| Plano: permit on all re-roofs with final roof inspection; roofers register as General Contractor yearly; city posts active list | Plano re-roof sheet (civicplus); registration docs cited in docs/research/plano.md | VERIFIED | Plano URL corrected to /217/ |
| Arlington: permit for roof covering replacement since Nov 1 2011; roofers register; searchable on portal | arlingtontx.gov permits page and roofing tips page | VERIFIED | none |
| Garland: permit at $2,000+; register as GC; insurance naming city as certificate holder; $300,000 GL minimum | garlandtx.gov Re-Roofing page; registration application PDF (note: one other city form says "additional insured") | VERIFIED | none |
| Grand Prairie: permit for any roof replacement, recover or repair; GC registration | gptx.org residential re-roof page; GC registration page | VERIFIED | residential re-roof page added to sources |
| Richardson: permit above about 25% of roof; all contractors register; one year | cor.net roof page and registration page | VERIFIED | roof permit page added to sources |
| Allen: replacement needs permit; contractors register yearly in portal before being added to a permit | cityofallen.org registration page, hail tips | VERIFIED | none |
| Workers' comp optional for most private Texas employers; non-subscriber notice; can be sued | TDI DWC non-subscriber page (also general knowledge) | VERIFIED | none |
| B&C Code 27.02 deductible ban; notice required on $1,000+ insurance-paid contracts | texas.public.law 27.02; HB 2102 (2019) | VERIFIED | none |
| Ins. Code 4102.163 | texas.public.law; HB 2103 (2019) broadened to all contractors | VERIFIED | none |
| B&C Code ch. 58: applies after a natural disaster when contractor lacks a 1-year physical address in the county or an adjacent county; no payment before work; boldface notice; DTPA; no waiver | statutes.capitol.texas.gov ch. 58; 58.002(b), 58.003 per search; proportionate partial payment per writer's notes from the statute (not re-shown in my results) | VERIFIED (partial payment wording NOT re-checked) | none |
| Property Code 53.259 bills-paid affidavit as condition of final payment | texas.public.law 53.259 | VERIFIED | none |
| AG ice storm alert: may cancel door-to-door contract up to three days; seller must tell you; otherwise voidable | texasattorneygeneral.gov release | VERIFIED | none |
| (missing precision) the rescission window is three BUSINESS days, in writing | AG door-to-door sales page | CORRECTED | sentence added with the AG door-to-door page as a new source |
| McKinney requires a solicitor's permit, issued by police | mckinneytexas.org MPD Solicitor's Permit | VERIFIED | none |
| GAF warranty activation and enhanced warranty conditions | GAF blog (cited) | NOT CHECKED (search budget) | none; general product info, no partner claim |
| AG consumer line 800-621-0508 | TDI tip page | VERIFIED | none |

## /roof-insurance-claim-texas/

| Claim | Source | Result | Action |
|---|---|---|---|
| Ch. 542: acknowledge ~15 days (TDI consumer page says business days; statute and Bill of Rights say days) | TDI blog; Consumer Bill of Rights | VERIFIED (page already notes the difference) | none |
| Decide within 15 business days after receiving requested info; rejection reasons in writing | TDI blog; 542.056 | VERIFIED | none |
| Up to 45 more days with notice of why | TDI blog | VERIFIED | none |
| Pay within 5 business days | TDI blog | VERIFIED | none |
| 15 more days after a weather catastrophe | TDI blog; 542.059 | VERIFIED | none |
| Missed deadlines: may collect claim, interest, attorney's fees | TDI blog | VERIFIED | none |
| TDI help line 800-252-3439; AG line 800-621-0508 | TDI | VERIFIED | none |
| RCV two checks, depreciation held back until work billed; ACV not paid back | TDI home insurance guide; RCV/ACV tip | VERIFIED | none |
| Some insurers switch aging roofs to ACV at renewal; worn roof may not be covered | TDI "Insurance and your roof" tip. Note: TDI's Sept 29 2026 proposed clarification of 28 TAC 21.1006 bars declining/non-renewing on roof AGE alone (hearing Nov 3 2026); it does not change the ACV statement | VERIFIED | none (coordinator may want to mention the pending rule) |
| Permanent repairs before inspection can give a reason to deny; some policies set a 1-year filing deadline; mortgage company on the check | TDI getting-claim-paid and replacing-your-roof tips (Houston fc2/fc3 verified) | VERIFIED (prior check) | none |
| Cosmetic hail exclusion endorsement with impact-resistant roof credit | TDI B-0030-98 (metal roofs, HO-145/TDP-022 optional, must be signed); B-0024-98 covers other coverings | VERIFIED | source label clarified; B-0024-98 added |
| Impact-resistant discounts set company by company | TDI roofing discounts page | VERIFIED | none |
| Worked example arithmetic ($300k x 2% = $6,000; 18,000 - 5,000 - 6,000 = 7,000; $11,000 ACV) and $400k x 2% = $8,000 | arithmetic | VERIFIED | none |
| Contractor may estimate and discuss with insurer, may not act as public adjuster or negotiate | Ins. Code 4102.163; TDI FAQ; B-0007-25 | VERIFIED | none |
| B&C 27.02; $1,000 notice; Ins. Code 707 proof | statute; TDI | VERIFIED | none |
| Penalty up to $2,000 fine and up to six months jail (TDI) | TDI "state law cracks down on roof scams" (older article); consistent with the Class B misdemeanor set by HB 2102 (2019): fine up to $2,000, jail up to 180 days | VERIFIED | none |
| Chapter 58 no pre-payment rule | statute | VERIFIED | none |
| Appraisal clause in many policies | TDI home-damaged FAQ (prior check) | VERIFIED | none |

## Shared files (reported, not edited)

| File | Claim | Result | Note |
|---|---|---|---|
| macros.html license_check | HB 3344 cleared committee, no floor vote, died | VERIFIED | Says "certificate of liability insurance sent from the insurer"; other pages say "from the insurance agent". Both acceptable; "agent or insurer" would be more consistent |
| macros.html deductible_note | 27.02 ban, $1,000 notice, proof of payment, 4102.163 | VERIFIED | none |
| macros.html safety_box | safe steps only, Oncor | OK | none |
| scripts/make_checklist_pdf.py | percentage deductibles common; RCV/ACV; deductible law; public adjuster rule; Class 4 discount question; no DIY | VERIFIED | no problems; no forbidden claims, correct name |
| Other pages using plano.gov/220/Building-Inspections | roofing-contractors-plano-tx, commercial-roofing, roof-replacement, roof-replacement-cost-dallas, and docs/WRITING-GUIDE.md | FLAG | Should be https://www.plano.gov/217/Building-Inspections (the page search finds; plano.md already uses it) |

## Summary

Claims checked: 98. Verified: 85. Corrected: 8 (Mayfest damage attribution, June 2012 storm detail and source,
878 to 902 hail events in 2025, 65 to 66 towns in two places, Plano URL on four pages, AG three-business-day rule
added, two source additions/label fixes). Removed: 0. Not checked: 2 (GAF warranty wording; Chapter 58
proportionate partial payment wording re-check). The rest OK-UNCHECKED generic statements.
Builds: `python3 build.py --out /tmp/fc1/dist`; check.py 0 errors on all 14 URLs (2 pre-existing false-positive DIY
warnings on /about/ and /how-it-works/); similarity.py no FAIL (max 1.3% vs Houston).
