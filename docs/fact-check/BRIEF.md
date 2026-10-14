# Independent fact-check brief (DFW Expert Roofers, Oct 2026)

You did NOT write these pages. Your job is to check every factual claim and every source on the pages
assigned to you, and fix what is wrong. Repo: /home/user/dallas-roofing-pro (branch `build`; do not commit).

Read first: CLAUDE.md (hard rules), INTAKE.md, docs/WRITING-GUIDE.md (rules and the verified Texas law
facts), then for each page: the page source in src/pages/ and its research notes in docs/research/
(<slug>.md for towns, service-<slug>.md or guide-<slug>.md otherwise).

For each page:
1. List every factual claim: dates, storm ratings and wind speeds, damage figures, populations, county
   lines, permit and registration rules, fees, phone numbers, addresses, code sections, laws, program
   amounts, utility providers, neighborhood names, history.
2. Check each claim against a source: the page's own Sources list first, then WebSearch (WebFetch and curl
   do not work here; search with `allowed_domains` set to the official domain where you can). Also check
   that each listed source actually supports what the page says and that the URL looks right.
3. Classify: VERIFIED, CORRECTED (you changed the page), REMOVED (could not verify, so you took it out or
   softened it to what is verifiable), or OK-UNCHECKED (a generic statement that needs no source).
4. Fix the page directly: correct wrong numbers, remove or soften unverifiable claims, fix or remove bad
   sources. Keep the page's voice; keep the hard rules (no dashes, no banned phrases, no DIY, no invented
   claims, the phone number never typed, the line never doing roof work).
5. Also flag rule problems you notice: anything implying the line does roof work, insurance promises,
   prices presented as the line's, named roofing companies, places outside DFW.

After editing, build to your own folder and confirm your pages still pass:
`python3 build.py --out /tmp/<you>/dist`, `python3 scripts/check.py --dist /tmp/<you>/dist --only <url>
--skip-links` (0 errors) and `python3 scripts/similarity.py --dist /tmp/<you>/dist --only <url>` (no FAIL).

Search budget: about 200 searches per turn are shared by every agent running. Spend searches on the claims
most likely to be wrong (numbers, dates, ratings, fees, rules) and on claims whose source is weak (an
aggregator, an undated article, a third-party site). If WebSearch says the budget is used up, finish the
checks you can from the listed sources, mark the rest NOT CHECKED, and say so.

Write your report to docs/fact-check/<your id>.md: one section per page with a table
(claim | source | result | action), then a summary line (claims checked, verified, corrected, removed,
not checked). Report back briefly with those totals and the most important corrections.
