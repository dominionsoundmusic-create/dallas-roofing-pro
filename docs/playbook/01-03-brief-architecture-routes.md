# Playbook 2.0, Prompts 1 to 3 (DFW Expert Roofers, Oct 13 2026)

## Prompt 1: Client fact brief (from INTAKE.md, the live site and CLAUDE.md)

| Item | Value | Status |
|---|---|---|
| Official name | DFW Expert Roofers, a d/b/a of Dominion Digital Group | Confirmed |
| Old name | "Dallas Metro Roofing Pro": removed everywhere, never written again | Confirmed |
| Category | Free roofing referral phone line for the Dallas-Fort Worth metroplex (NOT a roofing company) | Confirmed |
| Services | Chosen from the keyword data: 12 service pages (SERVICES.md) | Confirmed |
| Not offered | Gutters alone, solar, siding, remodeling, insurance advice, public adjusting, claim handling | Confirmed |
| Service area | Dallas, Tarrant, Collin, Denton, Rockwall, Kaufman, Ellis, Johnson, Parker, Hood counties; 67 town pages | Confirmed |
| Address | Not displayed | Confirmed (omit) |
| Phone | (469) 649-7066, tel:+14696497066, shared Dallas line, ONE place only: src/data/site.json | Confirmed |
| Email | UNKNOWN: no email shown | Missing, deferrable |
| Hours | Line answered 24/7 by an automated assistant | Confirmed |
| Primary CTA | Call the number (header and hero of every page) | Confirmed |
| Secondary CTA | How the free line works / page-specific anchors | Confirmed |
| Colors | Navy #12111a, gold #c9a84c (dark text on gold), deep red second band and Call button, white sections | Confirmed |
| Logo | New SVG "DFW EXPERT / ROOFERS" + favicons (old logo carries old name) | Confirmed (to build) |
| Top bar | "John 3:16" left; quote exact; credited Jesse Duplantis (the one allowed dash) | Confirmed |
| Footer | "© 2026 Dominion Digital Group. All rights reserved." + followed credit link to dominionwebdesignpro.com | Confirmed |
| Disclosure | Referral disclosure on every page (INTAKE wording) | Confirmed |
| History, team, reviews, licenses, guarantees | None. Never invented | Confirmed (omit) |
| Social | Facebook https://www.facebook.com/dallasmetroroofingpro (only social URL present on the live pages; the Oct 10 commit message mentions Instagram, TikTok and YouTube, but no URLs for them exist in any page, so those slots stay hidden) | Confirmed / others missing, deferrable |
| Google Business Profile | UNKNOWN | Missing, deferrable |
| Forms | Netlify "dallas-roofing-contact" (/contact/; name, phone, city, need, message, bot-field; thanks /contact/thanks/) and "dallas-hail-checklist" (/hail-claim-checklist/; name, email, phone, zip, bot-field; thanks delivers files/dallas-hail-storm-claim-checklist.pdf) | Confirmed |
| Contact form "need" options | Leak; Hail or storm damage; Roof inspection; Replacement quote; Second opinion on a quote; Commercial roof; Something else (exactly as live) | Confirmed |
| Analytics | GA4 G-DDH28794K5 with the phone_call_click tel-tap event, every page | Confirmed |
| Photos | 15 in images/ (roof-01..06 hero+card, 3 Dallas heroes) + generic Houston roof photos; new images listed in docs/image-list.md | Confirmed |
| Domain | https://dfwexpertroofers.com (Netlify, deploys from main) | Confirmed |
| Words to avoid | INTAKE section 8 + CLAUDE.md banned list (enforced by scripts/check.py) | Confirmed |

Contradictions found: (1) the live footer and title used the old name; resolved by INTAKE (new name).
(2) The live home page said "Expert Installation" and "The roofer fixes the actual problem" style copy and
offered GAF/Owens Corning/CertainTeed as if installed by the line, and a ServiceTitan ad block; all dropped.
(3) The old hail page said "insurers often pay for a full replacement"; insurance outcomes are never promised.
(4) The checklist PDF mentions "On the coast" windstorm policies (not relevant to DFW); the PDF is rebuilt.
Launch blockers: none for the build branch. Going live is Maurice's decision (merge to main).

## Prompt 2: Architecture

Not a TanStack/SSR project: this is a static site generator (Python 3 + Jinja2 + PyYAML + Pillow), copied
from the Houston build. `python3 build.py` renders every page in src/pages (YAML front matter + Jinja body)
through src/templates into complete static HTML in dist/. All content, titles, descriptions, canonicals,
Open Graph tags and JSON-LD are in the raw HTML (no client rendering). Netlify publishes dist/
(netlify.toml). Shared data: src/data/site.json (business, nav, services, guides, areas, social, forms).
Components: templates/partials (header, hero, faq, cta, footer), templates/macros.html. robots.txt and
sitemap.xml are generated. Forms are plain Netlify HTML forms in the static HTML. Checks: scripts/check.py
(rules, SEO, links, images, forms), scripts/similarity.py, scripts/check_old_urls.py, scripts/grep_check.py,
scripts/responsive_check.js (Playwright). No typecheck/lint tooling exists for a static site.

## Prompt 3: Baseline and route matrix

Baseline: the old site is 32 hand-built HTML files with inline styles and the old name; no build step, so no
baseline build to run. Old pages move to docs/old-site/ (git mv) and are read as research.

| Route | Type | Source | Nav | Sitemap | Index | Status |
|---|---|---|---|---|---|---|
| / | home | src/pages/index.html | logo | yes | yes | to build |
| /services/, /service-areas/, /how-it-works/, /about/, /faq/ | core | src/pages/*.html | yes | yes | yes | to build |
| /contact/ | contact + form | src/pages/contact/index.html | yes | yes | yes | to build |
| /contact/thanks/, /hail-claim-checklist/thanks/ | thanks | src/pages/... | no | no | noindex | to build |
| /hail-claim-checklist/ | form | src/pages/hail-claim-checklist/index.html | footer | yes | yes | to build |
| /privacy-policy.html, /terms.html | legal | url: front matter | footer | yes | yes | to build |
| /404.html | 404 | src/pages/404.html | no | no | noindex | to build |
| 12 service URLs (SERVICES.md) | service | src/pages/<slug>.html, site.json services | Services menu | yes | yes | to build |
| 5 guide URLs | guide | site.json guides | Guides menu | yes | yes | to build |
| 67 town URLs | area | site.json areas | Service Areas menu | yes | yes | to build |
| Old URLs and _redirects rules | redirect | src/static/_redirects | no | no | 301 | to build |

Plan: Prompts 4 to 6 (site.json, brand, logo, header/footer/nav, old-site move, redirects) -> 7 to 12 (home,
services, 12 service pages, areas overview, 67 researched town pages, about/FAQ/how-it-works/guides/legal) ->
13 to 15 (forms, PDF, social, photo reuse and image list) -> 16 to 17 (SEO, remnant sweep) -> 18 to 20
(responsive, functional, fact-check, final QA, handoff).
