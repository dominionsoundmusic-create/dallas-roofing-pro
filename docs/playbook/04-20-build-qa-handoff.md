# Playbook 2.0, Prompts 4 to 20 (DFW Expert Roofers, Oct 13 to 14 2026)

Prompt 4 (business data): src/data/site.json holds the name, d/b/a, the one copy of the phone number
(display and tel forms derived by build.py), hours, origin, GA4 G-DDH28794K5 with the tel-tap event,
form names, Facebook URL, disclosure text, quote and footer credit. No email, address, reviews or GBP.
Prompt 5 (brand): navy #12111a, gold #c9a84c with dark text, deep red #a3201d for the Call button and
the occasional band, white sections; new outlined SVG logo and favicons (scripts/make_logo.py); Inter
self-hosted woff2; WebP 480/800/1200/1600/1920 srcset with a preloaded, fetchpriority-high hero.
Prompt 6 (navigation): Services, Service Areas (67 towns), Guides, How It Works, About, FAQ, Contact;
keyboard-operable submenus; footer with services, guides, company links and the full town grid.
Prompts 7 to 12 (pages): home, services and areas overviews, 12 service pages, 67 town pages, 5 guides,
how it works, about, FAQ, privacy, terms, 404. Every page researched and written for its keyword;
research notes with sources in docs/research/. Roughly 22 writer sub-agents plus the coordinator.
Prompt 13 (forms): both Netlify forms rebuilt in the static HTML with exact names and fields; the
checklist PDF rebuilt (new name, no coastal content). Delivery not tested (no production submissions).
Prompt 14 (social): Facebook icon in the footer; other slots hidden (no URLs on the live site).
Prompt 15 (media): reuse first. 15 DFW photos plus 29 generic Houston photos (new neutral names, new
alt text; nothing Houston-specific); 13 new Artistly images still wanted (docs/image-list.md), each
shown through a reused photo until it arrives; check.py fails any photo shown twice on a page.
Prompt 16 (SEO): unique titles and descriptions, canonicals on dfwexpertroofers.com, Open Graph and
Twitter tags, one H1, one JSON-LD graph per page (Organization, WebPage, BreadcrumbList, Service on
service and town pages, Article on guides, FAQPage everywhere with FAQs), sitemap.xml without noindex
pages, robots.txt, 404 noindex.
Prompt 17 (sweep): old name, old phone formats, other cities' numbers, Houston places, ServiceTitan
ad, CenterPoint, placeholders and dashes: 0 hits (scripts/grep_check.py and check.py).
Prompts 18 to 19 (responsive, functional): Playwright run, 0 problems; screenshots reviewed; all
internal links resolve; all old URLs resolve or 301 (docs/qa-urls.md).
Prompt 20 (final): docs/qa.md, docs/fact-check.md (12 independent checkers, 1,138 claims, 123
corrected, 28 removed or softened).

Route inventory: SERVICES.md (97 pages). Status: every route PASS on build, check.py, old-URL and
browser checks. NOT VERIFIED: live form delivery to Netlify, Google Translate and GA4 loading (no outside
network in the test browser), and anything on the live domain (nothing was deployed).
Launch blockers: none in the build. To go live, Maurice reviews the build branch and merges it to main.
Remaining client inputs: 13 Artistly images (optional; reused photos stand in), Instagram, TikTok,
YouTube and Google Business Profile URLs if they exist.
