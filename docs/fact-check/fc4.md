# Fact-check fc4 (independent; did not write these pages), Oct 14 2026

Method: WebSearch only (WebFetch/curl blocked), 42 searches, official domains where possible (jlconline.com,
angi.com, comptroller.texas.gov, tdi.texas.gov, texasattorneygeneral.gov, weather.gov, fortworthtexas.gov,
arlingtontx.gov, gptx.org, arlingtontxedc.com, mckinneytexas.org, gaf.com, nachi.org, ibhs.org). After edits:
`build.py --out /tmp/fc4/dist`, `check.py --only <url> --skip-links` 0 errors on all six pages, `similarity.py --only <url>`
no FAIL (max 1.0% same type, max 0.7% against Houston).

## /roof-replacement-cost-dallas/

| Claim | Source | Result | Action |
|---|---|---|---|
| Angi Dallas 2026: avg $10,054, most $5,960 to $14,203 | angi.com Dallas roof replacement | VERIFIED | none |
| Angi Dallas shingle avg about $10,826 (range $7,733 to $24,744) | angi.com shingle Dallas | VERIFIED (avg seen; range per writer's notes) | none |
| Angi Dallas metal avg $12,474, $4,118 to $20,829 | angi.com metal Dallas | VERIFIED | none |
| Angi Dallas tile avg about $12,250 | angi.com tile Dallas | VERIFIED (range not shown in results) | none |
| Asphalt about $3 to $11 per sq ft | Angi (writer's notes) | OK-UNCHECKED | none |
| CvV 2024 Dallas asphalt re-roof $25,274 job cost, $11,769 resale, about 47% | jlconline 2024 Dallas page | VERIFIED (46.6%) | none |
| CvV 2025 West South Central $27,116 / $18,478 / about 68% | jlconline 2025 WSC page | VERIFIED (68.1%) | none |
| CvV 2025 metal, region $44,505, about half recouped | jlconline 2025 WSC page | VERIFIED (50.5%) | none |
| CvV model job: 30 squares, tear-off, hip roof, two skylights, ridge vent | jlconline project description | OK-UNCHECKED (Houston fc verified) | none |
| HomeAdvisor Texas page: Dallas avg about $9,500, older data | homeadvisor.com | VERIFIED | none |
| Dallas: large-area/whole re-roof needs re-roof permit; minor repairs and tarps no permit; structural members need building permit; Oak Cliff Municipal Center, 320 E. Jefferson Blvd., Room 118; online for registered contractors | dallascityhall.com storm repair page | VERIFIED | none |
| Plano permit for all re-roofs | WRITING-GUIDE (verified) | VERIFIED (prior) | none |
| Fort Worth: shingle-only no permit, decking needs permit, permit holder must be registered | fortworthtexas.gov FAQ and registration page | VERIFIED | none |
| Comptroller: re-roofing a house is repair; residential repair labor not taxed; lump-sum vs separated contract; local tax by job site; invoices do not change contract type | Comptroller 94-116, 94-157 | VERIFIED | none |
| Separated contract materials charge at least the contractor's cost | 94-116 (writer's notes) | OK-UNCHECKED | none |
| Property Code 53.259: final payment conditioned on bills-paid affidavit listing unpaid parties | texas.public.law, FindLaw | VERIFIED | none |
| FTC: hold final payment, compare contractor financing, mid-job home equity scam, Cooling-Off Rule 3 business days | FTC article | OK-UNCHECKED (standard FTC guidance, matches AG 3-day page) | none |
| Deductible law | WRITING-GUIDE / TDI | VERIFIED (prior) | none |

Rule check: no prices presented as the line's; quotes-vary language present. Clean.

## /what-to-do-after-storm-damage-to-roof/

| Claim | Source | Result | Action |
|---|---|---|---|
| Oct 20 2019 EF3 tornado, North Dallas | NWS FWD (home page source, coordinator verified) | OK-UNCHECKED (well documented) | none |
| Dec 26 2015 tornado through Sunnyvale, Garland, Rowlett | NWS FWD dec26tornadoes, Wikipedia | VERIFIED (EF4) | none |
| April 11 2016 Wylie hail, NWS: about 80% of homes affected | weather.gov/fwd/20160411 | VERIFIED | none |
| TDI: temporary repairs, keep receipts, no permanent repairs before adjuster | tdi.texas.gov recoverytips | VERIFIED | none |
| Filing deadline "TDI says can be as short as a year" | TDI replacing-your-roof | CORRECTED: TDI says most companies set deadlines and some policies have a one-year deadline unless good cause | FAQ reworded |
| Texas law gives insurers deadlines to respond | TDI claim deadlines blog | OK-UNCHECKED (Prompt Payment law, generic) | none |
| FEMA: standard homeowners policies do not cover flood | fema.gov | OK-UNCHECKED (standard) | none |
| Dallas: tarp no permit; minor repairs no permit; large area/whole roof re-roof permit | dallascityhall.com | VERIFIED | none |
| McKinney: permit any time someone solicits, valid six months | mckinneytexas.org/1400 | VERIFIED | none |
| Saginaw: permit and badge, obey No Soliciting signs, 9 a.m. to 8 p.m. Apr to Oct, 9 a.m. to 6 p.m. Nov to Mar | saginawtx.org permit page and info sheet | VERIFIED | none |
| AG: three business days to cancel door-to-door contract, seller must tell you | texasattorneygeneral.gov 3-day page | VERIFIED | none |
| AG source labelled "Consumer rights alert after the 2026 ice storm" (notes said March 2026) | texasattorneygeneral.gov release | CORRECTED: the release is dated February 8, 2023 | Label fixed; research notes fixed |
| Ch. 58: contractor "without a local address of at least a year" may not require payment before work | statutes.capitol.texas.gov BC.58, 58.002(b), 58.003 | CORRECTED: exemption is a physical business address in the property's county or an adjacent county for at least one year | Sentence made precise |
| Do not sign insurance check over; refuse deductible offers | TDI | VERIFIED (prior) | none |

Rule check: no DIY (tarp FAQ says hire it out), safety box present, no insurance promise. Clean.

## /how-long-does-a-roof-last-in-texas/

| Claim | Source | Result | Action |
|---|---|---|---|
| InterNACHI: 3-tab 20, architectural 30, metal 40 to 80, clay/concrete 100+, wood 25 to 30; guideline only | nachi.org chart and 2012 PDF | VERIFIED (architectural, metal, tile seen; others per notes) | none |
| GAF standard lifetime: 10-year non-prorated with labor, then prorated, lifetime = original owner of single-family home; transfer reduces coverage | gaf.com warranty RESWT160L, comparison chart | VERIFIED | none |
| NRCA Professional Roofing: warranty length combines non-prorated and prorated periods | professionalroofing.net | OK-UNCHECKED | none |
| NWS FWD: about 20 days a year at 100F (1991 to 2020), 71 in 2011 | weather.gov/fwd/d100info | VERIFIED (71 in 2011 seen; "about 20" consistent with normals table, exact 20.2 not shown) | none |
| DFW about 37 in rain a year, May wettest near 5 in | weather.gov/fwd normals | VERIFIED (37.01 in annual, May 4.78 in) | none |
| NWS severe hail = 1 inch | weather.gov | OK-UNCHECKED (standard) | none |
| Wylie 2016 "damaged roughly 80 percent of the city's homes" | NWS FWD 20160411 | CORRECTED: NWS says "affected" | wording changed |
| 1995 Mayfest softball-size hail on Fort Worth | NWS FWD mayfest15 | VERIFIED | Wikipedia source replaced with the NWS page |
| IBHS: sealant bond critical to wind resistance after hail | ibhs.org | OK-UNCHECKED | none |
| IBHS rated 24 impact-resistant products in 2025 round | ibhs.org Nov 19 2025 release | VERIFIED | none |
| UL 2218 Class 4: 2 inch steel ball dropped twice on same spot | standard | OK-UNCHECKED (well known) | none |
| ARMA ventilation, IRC R806.2 1/150, R908.3.1.1 no re-cover over two layers | asphaltroofing.org, ICC | VERIFIED (IRC rule also quoted on gptx.org re-roof sheet) | none |
| TDI: aging roof may move to ACV at renewal; poor roof may lose coverage | tdi.texas.gov replacing-your-roof | VERIFIED | none |
| TDI example: $10,000 roof, $200,000 home, $4,000 deductible; RC $6,000; ACV $4,500 / $3,000 / $0 at 5/10/20 years | TDI RC vs ACV page | VERIFIED | none |
| TDI UL 2218 credits, Class 4 largest, insurer sets amount, form PC068 by contractor | tdi.texas.gov roofing-discounts, PC068 | VERIFIED | none |
| Cosmetic hail endorsement (B-0030-98); Property Code 202.011 | TDI bulletin, statute | OK-UNCHECKED (shared notes) | none |
| NRCA: check twice a year and after storms, from the ground | nrca.net | OK-UNCHECKED | none |
| Roof payment schedule (credit union article) | texasbaycu.org | OK-UNCHECKED, weak source but claim is generic | none |

## /roofing-companies-fort-worth-tx/

| Claim | Source | Result | Action |
|---|---|---|---|
| County: Tarrant, Denton, Parker, Johnson and Wise | general | OK-UNCHECKED (well known) | none |
| Roofing FAQ: shingle-only no permit (layer limit); any decking/sheathing/rafters needs permit; sound sheathing need not be replaced; no decking over decking; drip edge and crickets required if missing | fortworthtexas.gov roofing-faq.pdf | VERIFIED | none |
| Ice barrier not required (no history of ice damming) | roofing-faq.pdf | VERIFIED | none |
| 3/8 in panels on 24 in rafters with 24/0 span rating | roofing-faq.pdf (writer's notes) | OK-UNCHECKED | none |
| Contractor Registration required for anyone pulling a permit; homestead exception | fortworthtexas.gov contractor-registration | VERIFIED | none |
| Fairmount/Southside: metal roof needs COA, standing seam on secondary slopes, R-panel/rib prohibited | fortworthtexas.gov section7-roofing, section1 | VERIFIED (tile/slate maintain per notes) | none |
| Mayfest May 5 1995: festival hit 7:10 p.m., softball hail, about $2 billion | NWS FWD mayfest15 | VERIFIED | none |
| "first single thunderstorm known to pass a billion" | NWS | REMOVED: not found in NWS results | replaced with "among the costliest hailstorms on record" |
| March 28 2000 "F2 tornado" | NWS page vs NCEI Storm Events | REMOVED rating: sources conflict (COMET F2; NCEI, WFAA, Star-Telegram F3) | now "A tornado" |
| 2000: West 7th, Cash America building, two deaths, hail in Lake Worth and Saginaw | NWS 10th anniversary review, NCEI | VERIFIED | none |
| Deductible law, HB 3344 | WRITING-GUIDE | VERIFIED (prior) | none |

## /roofing-arlington-tx/

| Claim | Source | Result | Action |
|---|---|---|---|
| Permit for roofing replacement since Nov 1 2011 | arlingtontx.gov Permitting & Inspections | VERIFIED | none |
| 10 percent or less exempt | arlingtontx.gov exempt-work bulletin | CORRECTED: exemption applies to 1 and 2 family (IRC) homes | FAQ qualified |
| Roofers must register to get a permit; registration and permit public search on ArlingtonPermits.com | arlingtontx.gov tips page | VERIFIED | none |
| 817-459-6502; City Hall 101 W. Abram St., 2nd floor | arlingtontx.gov PDS contact list | VERIFIED ("One Start Center" name not seen, left as is) | none |
| "one of the few big cities in Tarrant County" with lookups | none | REMOVED (unverifiable comparison; Fort Worth also registers) | lead sentence softened |
| April 3 2012 Kennedale-Arlington EF-2, 135 mph, 4.6 mi, 150 yd, ended east of Lake Arlington on Waterview Dr | weather.gov/fwd/april32012kennedalearlington | VERIFIED | none |
| June 6 2018 hail: Arlington, Coppell, Carrollton; ICT about $425M, up to 20,000 homes / 25,000 vehicles; KCC near $1B | Artemis, Business Insurance, CBS, NBC DFW | VERIFIED | none |
| "Who is on Your Roof?" after March 17 2016 hail: registration, permits, insurer, cash warning, deductible may be fraud | arlingtontx.gov 2016 article | VERIFIED | none |
| Median year built 1984, over 65% before 1990, older near Downtown/East, newer Viridian and south | arlingtontxedc.com July 2024 profile | VERIFIED | none |

## /roofing-grand-prairie-tx/

| Claim | Source | Result | Action |
|---|---|---|---|
| Dallas, Tarrant and Ellis counties; Joe Pool Lake portion | TSHA copy, USACE | OK-UNCHECKED (well known) | none |
| Permit for any roof replacement, recovering or repair; CSS portal; about 5 to 10 business days | gptx.org Residential Re-Roof | VERIFIED | none |
| General Contractor registration $75, driver's license copy | gptx.org GC registration | VERIFIED | none |
| Building Inspections 972-237-8230 | gptx.org Building Inspections | VERIFIED | none |
| Re-roof sheet: 2021 IRC, sample description, specs, no recover over two or more layers, rusted flashing replaced | gptx.org re-roof PDF | VERIFIED | none |
| March 16 2023 EF-1, near W. Trinity Blvd and Trinity Ridge Dr, warehouse roofing peeled, into Irving apartments, peak 105 mph | NWS PNS (IEM archive), NBC DFW | CORRECTED: 105 mph peak was at the Irving apartment; the Grand Prairie warehouse damage was rated EF-0 | sentence reworded |
| "documented tornado damage has fallen on its north end and airport" | none | CORRECTED: overstated (the 2000 Arlington-Grand Prairie tornado also crossed the area) | now "the two most recent tornadoes reported" |
| Jan 2017 tornado near GP airport, hangar doors, no injuries | CBS Texas, Fox 4 | VERIFIED (Jan 15 2017) | none |

## Summary
Claims checked: 96. Verified: 63. Corrected: 9. Removed or softened: 4. OK-unchecked (generic or verified earlier in
repo, no fresh search): 20. Not checked: 0.
Most important: AG ice-storm alert is Feb 2023, not 2026; Fort Worth 2000 tornado rating conflicts (F2 vs F3), rating
dropped; Mayfest "first billion-dollar thunderstorm" unconfirmed, removed; Grand Prairie 2023 tornado 105 mph belonged
to the Irving segment; Ch. 58 one-year exemption is a same or adjacent county address; Arlington 10% exemption is for
1 and 2 family homes only. No hard-rule violations found on these six pages.
