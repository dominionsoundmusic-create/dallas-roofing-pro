# Decisions log (DFW Expert Roofers, Playbook 2.0 rebuild, started Oct 13 2026)

Maurice is not watching this session, so every judgment call is written here (CLAUDE.md).

D1. Branch. CLAUDE.md says work on `build`; the session also assigned `claude/friendly-shannon-vuiirh`.
Both pointed at the same commit (efd2e9f). Work is committed on `build` and pushed to `build` after each
phase (the user asked for this explicitly), and the same commits are mirrored to the session branch.
Nothing is merged or pushed to `main`, nothing is deployed, no Netlify setting is touched.

D2. Build system. Copied from houston-roofing-pro branch `build` (5080cb4): build.py, scripts/check.py,
similarity.py, check_old_urls.py, apply_image_reuse.py, grep_check.py, keyword_plan.py (rewritten for DFW),
src/templates, site.css, site.js, the self-hosted Inter woff2, netlify.toml, the docs set as a pattern.
Every template sentence, macro sentence and page sentence is newly written for DFW; similarity.py compares
every DFW page with every Houston page and fails any shared 8-word run.

D3. URL pattern for NEW town pages: `/roofing-<town>-tx/` (for example /roofing-rockwall-tx/). It matches
the seed keyword form "roofing <town> tx" used for every town tab. The 15 towns with live pages keep their
current URLs (they are indexed and some rank), even where the slug pattern differs (/carrollton-roofing/,
/roofing-contractors-plano-tx/ and so on).

D4. Town qualification (checked row by row by scripts/keyword_plan.py, not taken from the first pass).
67 towns qualify. The first pass found 69; this check differs on two:
- Addison: its 10+ rows are "roofing addison", "addison roofing company" and "addison roofing contractor"
  (10 each, no Texas qualifier; Addison IL is larger) plus company names (Linear Roofing, Tarrant Roofing,
  Addison's Best, Addison Roofing and Construction). No Texas row with 10+: no page.
- Heath: "heath roofing and construction" (30) is a company name and "heath roofing company" (10) has no
  Texas qualifier (Heath OH, Heath MA); "roofing heath tx" shows 0. No page.
Same reasoning already excluded Highland Park ("highland park roofing", no Texas qualifier; Highland Park
IL, MI, NJ). Balch Springs, Fate, Royse City, Terrell and University Park have no roofing row with 10+.
Rows without "tx"/"texas" count only for place names that exist only in Texas (list in the script).

D5. Old URLs. Kept where the URL matches the page's keyword (all service hubs, the 15 town pages, core
pages, .html legal pages). Changed with a 301:
- /free-roof-inspection/ -> /roof-inspection/ ("free inspection" is a banned phrase; the keyword in the
  data is "roof inspection dallas"). The old wildcard /free-roof-inspection/* now points to /roof-inspection/.
- Old blog redirects that pointed at /free-roof-inspection/ or /roof-replacement/ for cost and lifespan
  topics now point straight at the closer new page (the guide), so no chains.
All old _redirects rules are kept.

D6. Services. The 11 services CLAUDE.md lists plus roof flashing repair ("where does flashing go on a roof",
210/mo, Question row in the Allen and Carrollton tabs; "roofing metal valleys" 1,900 supports it). Wind
damage has no row in the pull but is kept because CLAUDE.md names it and DFW wind events are well documented.

D7. Photos (Maurice's reuse rule): the 15 photos in images/ first, then generic roof photos copied from the
Houston build (no skyline, bayou, coast, palms or landmarks; new DFW alt text), one photo never twice on a
page. Slots that still need a new image are listed in docs/image-list.md and filled with a reused photo
(docs/image-reuse.json + scripts/apply_image_reuse.py) until the Artistly image arrives, so no page ever
shows a placeholder block or a broken image.

D8. Brand. Navy #12111a (header, first band), gold #c9a84c (buttons with dark text, accents), deep red
#a3201d for the Call button and the occasional second band, pure white sections. New SVG logo
"DFW EXPERT / ROOFERS" and matching favicons replace the old-name logo.

D9. Utility. Downed-line advice names Oncor (the wires utility for most of DFW) "or your local electric
utility", because some towns are served by a city utility or a co-op instead
(for example Denton and Garland run their own; CoServ and other co-ops serve parts of the suburbs). Town pages name the right utility only where research confirms it.

D10. Research method. WebFetch and curl cannot reach outside hosts from this container (proxy 403/DNS);
WebSearch works. Facts are verified from search results on the official or primary domain where possible,
and every source is listed on the page. Anything not verifiable is left out.

D11. Similarity limit and the Houston comparison: 15% Jaccard (5-word shingles) within each page type, and
every DFW page against every Houston page (houston-roofing-pro/dist). Shared template parts are excluded from
the comparison the same way on both sides.
