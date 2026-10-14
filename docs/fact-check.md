# Independent fact-check (DFW Expert Roofers, Oct 13 to 14 2026)

Method (CLAUDE.md "Before you finish"): twelve separate sub-agents that did NOT write the pages checked every
factual claim and every listed source on all 97 pages, following docs/fact-check/BRIEF.md. Each checker
searched the web (official city sites, weather.gov / SPC / NOAA, TDI, Texas statutes, the Census Bureau,
established news), corrected wrong claims in the page source, removed or softened what could not be
verified, confirmed the pages still passed check.py and similarity.py, and wrote a per-page claim table in
docs/fact-check/fc1.md to fc12.md. The writers' research notes (docs/research/) were updated where a
checker found a note wrong.

| Checker | Pages | Claims | Verified | Corrected | Removed or softened | Not checked |
|---|---|---:|---:|---:|---:|---:|
| fc1 | 11 core pages, roofer-check and insurance guides, shared notes, checklist PDF | 98 | 85 | 8 | 0 | 2 |
| fc2 | repair, replacement, leak, flashing, storm, hail | 78 | 56 | 4 | 0 | 1 |
| fc3 | wind, inspection, emergency, commercial, flat, metal | 66 | 50 | 10 | 2 | 0 |
| fc4 | cost, storm-steps and roof-life guides; Fort Worth, Arlington, Grand Prairie | 96 | 63 | 9 | 4 | 0 |
| fc5 | North Richland Hills, Haltom City, Watauga, Saginaw, Haslet, Hurst, Euless, Bedford | 132 | 86 | 19 | 3 | 24 |
| fc6 | Colleyville, Grapevine, Southlake, Keller, Benbrook, Crowley, Burleson, Cleburne | 96 | 85 | 5 | 2 | 4 |
| fc7 | Granbury, Weatherford, Azle, Mansfield, Midlothian, Waxahachie, Ennis, Irving | 104 | 66 | 14 | 5 | 2 |
| fc8 | Garland, Mesquite, Rowlett, Rockwall, Sunnyvale, Forney, Kaufman, Plano | 78 | 50 | 4 | 1 | 0 |
| fc9 | Richardson, Allen, Murphy, Sachse, Wylie, McKinney, Frisco, Prosper | 101 | 58 | 19 | 4 | 20 |
| fc10 | Celina, Anna, Melissa, Princeton, Carrollton, Lewisville, Flower Mound, Farmers Branch | 89 | 66 | 9 | 0 | 0 |
| fc11 | Coppell, The Colony, Highland Village, DeSoto, Duncanville, Cedar Hill, Lancaster, Seagoville, Red Oak | 96 | 64 | 14 | 1 | 1 |
| fc12 | Denton, Corinth, Argyle, Aubrey, Little Elm, Roanoke, Trophy Club | 104 | 52 | 8 | 6 | 33 |
| **Total** | **97 pages** | **1,138** | **781** | **123** | **28** | **87** |

The remaining claims in each report are generic statements or low-risk facts already backed by a source
listed on the page (marked OK). "Not checked" claims were left as the writer sourced them because the
shared search budget (200 searches per turn) ran short; they are mostly population figures, office
hours, phone extensions and dates already cited from the city or the Census Bureau. Each is listed in
its checker's report so a later pass can confirm them.

## Corrections that touched more than one page (applied sitewide)
- Mayfest 1995: the about $2 billion figure is not on the National Weather Service page; it is now
  given as commonly cited, with the earlier, lower estimates noted (home, hail page, Fort Worth).
- Impact-rated roofs: TDI's label and form PC068 rules are written for the coastal windstorm insurer;
  other insurers set their own proof. Replacement, metal and roof-life pages now say to ask the insurer.
- Plano Building Inspections: all links now point to the city page that search confirms,
  https://www.plano.gov/350/Building-Inspections-Permits.
- The home page's Texas hail statistic was wrong (878 in 2024); TPR reports 902 major hail events in
  Texas in 2025 (Insurance Information Institute). Fixed.
- April 3 2012 tornadoes: Forney EF-3, Royse City (Rockwall County) EF-2, Lancaster EF-2. A research
  note that put the EF-3 near Royse City was corrected; no page carried the error.
- A WFAA hail article cited as "May 2023" is about March 24 2019 (Allen and Frisco pages fixed).

## Examples of page-level corrections
Saginaw's permit phone (817-230-0453, not the main line); Weatherford's City Hall windstorm dated
March 2 2023; Celina permits moved to MGO Connect after Dec 8 2025; Princeton requires a permit for any
roof repair or replacement ($90); Lewisville Dam completed August 1955; Corinth page no longer places
Sutton Fields (a Celina-area community) in Corinth; Denton historic-district timing rule replaced with
the city checklist's actual rule; Grand Prairie's March 16 2023 damage was EF-0 (the 105 mph peak was in
Irving); Burleson population 55,220 (2023 Census estimate); Highland Village hail now cites SPC reports
instead of an aggregator; the Attorney General ice-storm alert is dated February 8 2023.

No checker found a hard-rule problem that remained: nothing implies the line does roof work, no
insurance promises, no prices presented as the line's, no named roofing company, no place outside DFW,
no DIY roof advice.
