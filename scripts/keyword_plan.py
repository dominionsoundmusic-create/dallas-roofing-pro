#!/usr/bin/env python3
"""Assign every keyword in keywords/DFW-Roofing-Keywords.xlsx (ALL tab, 1,548 rows) to a page as its
target or a supporting keyword, or to the deliberately-unused list with a one-line reason.
Writes docs/keyword-plan.md and docs/towns.json (the town decisions SERVICES.md and site.json use).

CLAUDE.md rule: every DFW keyword with a volume of 10 or more must be assigned or listed as unused with
a reason. Rows under 10 are classified by the same rules for reference ("below 10"). "Near me" rows carry
national volume: they are supporting keywords only, never targets, never proof of DFW demand.

Town rule (Maurice): a DFW town with 10 or more monthly searches on a ROOFING keyword gets a page. Only
Texas rows count: the row must say "tx" or "texas", or name a place that exists only in Texas (Flower
Mound, Trophy Club, Farmers Branch...). Rows naming a roofing company or another state never count.

Usage: python3 scripts/keyword_plan.py   (exit code 1 if any row with volume 10+ is unclassified)
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent

# ---- towns ---------------------------------------------------------------------------------------
# (key, display name, URL). The 15 towns with live pages keep their URLs; every new town page uses
# /roofing-<town>-tx/ (docs/decisions.md D3).
EXISTING = {
    "fort-worth": "/roofing-companies-fort-worth-tx/", "arlington": "/roofing-arlington-tx/",
    "garland": "/roofing-garland-tx/", "plano": "/roofing-contractors-plano-tx/",
    "mckinney": "/roofing-companies-mckinney-tx/", "frisco": "/roofing-company-frisco-tx/",
    "richardson": "/roofing-company-richardson-tx/", "allen": "/roofing-company-allen-tx/",
    "irving": "/roofing-company-irving-tx/", "denton": "/roofing-denton-tx/",
    "flower-mound": "/roofing-company-flower-mound-tx/", "grand-prairie": "/roofing-grand-prairie-tx/",
    "carrollton": "/carrollton-roofing/", "mesquite": "/roofing-company-mesquite-tx/",
    "lewisville": "/roofing-company-lewisville-tx/",
}
TOWN_NAMES = {  # seed tab town -> display name
    "addison": "Addison", "allen": "Allen", "anna": "Anna", "argyle": "Argyle", "arlington": "Arlington",
    "aubrey": "Aubrey", "azle": "Azle", "balch springs": "Balch Springs", "bedford": "Bedford",
    "benbrook": "Benbrook", "burleson": "Burleson", "carrollton": "Carrollton", "cedar hill": "Cedar Hill",
    "celina": "Celina", "cleburne": "Cleburne", "colleyville": "Colleyville", "coppell": "Coppell",
    "corinth": "Corinth", "crowley": "Crowley", "denton": "Denton", "desoto": "DeSoto",
    "duncanville": "Duncanville", "ennis": "Ennis", "euless": "Euless", "farmers branch": "Farmers Branch",
    "fate": "Fate", "flower mound": "Flower Mound", "forney": "Forney", "fort worth": "Fort Worth",
    "frisco": "Frisco", "garland": "Garland", "granbury": "Granbury", "grand prairie": "Grand Prairie",
    "grapevine": "Grapevine", "haltom city": "Haltom City", "haslet": "Haslet", "heath": "Heath",
    "highland park": "Highland Park", "highland village": "Highland Village", "hurst": "Hurst",
    "irving": "Irving", "kaufman": "Kaufman", "keller": "Keller", "lancaster": "Lancaster",
    "lewisville": "Lewisville", "little elm": "Little Elm", "mansfield": "Mansfield", "mckinney": "McKinney",
    "melissa": "Melissa", "mesquite": "Mesquite", "midlothian": "Midlothian", "murphy": "Murphy",
    "north richland hills": "North Richland Hills", "plano": "Plano", "princeton": "Princeton",
    "prosper": "Prosper", "red oak": "Red Oak", "richardson": "Richardson", "roanoke": "Roanoke",
    "rockwall": "Rockwall", "rowlett": "Rowlett", "royse city": "Royse City", "sachse": "Sachse",
    "saginaw": "Saginaw", "seagoville": "Seagoville", "southlake": "Southlake", "sunnyvale": "Sunnyvale",
    "terrell": "Terrell", "the colony": "The Colony", "trophy club": "Trophy Club",
    "university park": "University Park", "watauga": "Watauga", "waxahachie": "Waxahachie",
    "weatherford": "Weatherford", "wylie": "Wylie",
}
# Place names that exist only in Texas (or whose other namesakes are tiny), so a row without "tx" still
# means the DFW town. Addison (IL), Heath (OH, MA), Highland Park (IL, MI, NJ), Lancaster (PA, OH),
# Princeton (NJ), Roanoke (VA), Bedford (several), Murphy (NC) and the like are NOT on this list.
TEXAS_ONLY = {"flower mound", "trophy club", "farmers branch", "grand prairie", "north richland hills",
              "little elm", "haltom city", "highland village", "waxahachie", "burleson", "mckinney",
              "frisco", "plano", "carrollton", "mesquite", "lewisville", "grapevine", "keller", "rockwall",
              "rowlett", "weatherford", "garland", "denton", "irving", "southlake", "colleyville",
              "coppell", "duncanville", "desoto", "euless", "forney", "granbury", "midlothian", "prosper",
              "sachse", "wylie", "celina", "richardson", "mansfield", "watauga", "benbrook", "cleburne", "azle", "argyle",
              "fort worth"}

# Explicit targets for the 15 towns that already have pages (the URL's own keyword where it has volume).
TOWN_TARGET = {
    "fort-worth": "roofing fort worth tx", "arlington": "roofing arlington tx", "garland": "roofing garland tx",
    "plano": "plano tx roofing companies", "mckinney": "roofing companies mckinney tx",
    "frisco": "roofing in frisco tx", "richardson": "roofing company richardson",
    "allen": "roofing company allen tx", "irving": "roofing irving tx", "denton": "roofer denton tx",
    "flower-mound": "flower mound roofing company", "grand-prairie": "roofing grand prairie tx",
    "carrollton": "carrollton roofing", "mesquite": "roofing mesquite tx", "lewisville": "roofing lewisville tx",
}

# ---- companies, other places, off-topic -------------------------------------------------------------
COMPANY = (r"\b(arrington|kpost|needham|priority roofing|supreme roofing|dallastown|quick roofing|alpine roofing|dlv|"
           r"kidd|firefighter|tejas|elite roofing|storm roofing heroes|results roofing|horn brothers|empire roofing|"
           r"firehouse|^tx roofing|victory roofing|new view|abc roofing|roofing giant|crist|chavez|adams brothers|"
           r"dallas roof repair now|roof repair dallas masters|neko|bert roofing|lon smith|anchor roofing|"
           r"restoration roofing|city roofing|garcia brothers|williams brothers|roof source|kingdom roofing|"
           r"storm guard|joe hall|atlas roofing|crc roofing|linear roofing|tarrant roofing|addison's best|"
           r"addison roofing and construction|pickle|greystone|old pro|lone star roofing|clc roofing|"
           r"national roofing partners|trinity roofing|over the top|r&b|big d roofing|beacon|gaf roofing|"
           r"dt roofing|larry miller|jenkins|king of texas|cardinal roofing|skyline|owens corning roofing|"
           r"irving roofing plant|legacy roofing|performance roofing|tallent|rainbow roofing|dfw roofing pro|"
           r"murphy roofing|apple roofing|southern roofing|jackson roofing|concord|3 kings|designer roofing|"
           r"martin roofing|richardson roofing llc|home team|tucker roofing|mason roofing|griffith|"
           r"select roofing|centennial|sons roofing|triple c|bronco|first out|pirate|elevated roofing|"
           r"peak roofing|heath roofing|desoto roofing|kaufman roof|crowne roofing|ben roofing|longhorn|"
           r"my roofing|roof experts texas|williamson|roofing 911|commercial flat roofing of dallas|"
           r"dallas commercial roofing|dallas elite|precision roofing|fate roofing|spring roofing supply|"
           r"roanoke roofing company|duro last|red oak roofing|has roofing|roofing annex|"
           r"[a-z]+ roofing (?:llc|inc|group|co)\b)")
OTHER_PLACE = (r"\b(houston|austin|cypress|katy|conroe|spring tx|pearland|kingwood|el paso|tyler|longview|lubbock|"
               r"georgetown|mcallen|laredo|midland|odessa|hutto|harlingen|brownsville|beaumont|victoria|boerne|"
               r"leander|kyle|bryan|kerrville|waco|bastrop|killeen|lufkin|palestine|edinburg|huntsville|paris|"
               r"belton|baytown|buda|brenham|mineola|orange tx|plainview|stephenville|sherman|greenville|abilene|"
               r"temple|cedar park|amarillo|san antonio|humble|woodlands|texas city|crockett|crosby|gilmer|"
               r"wharton|henderson|jacksonville|jasper|kingsville|marshall|wimberley|seguin|taylor tx|"
               r"central texas|dallas ga|oregon|scottsdale|annapolis|anne arundel|grand rapids|lancaster (?:pa|ohio|ky|ny|ma|county)|"
               r"pa roofing|midlothian va|roanoke va|arlington wa|detroit|highlands ranch|wichita|dc\b|scotland|"
               r"medway|addison il|university\b|roofing temple)")
OFFTOPIC = (r"(weather|\b7\d{4}\b|\busa$|tax rate|tax office|firewood|mesquite wood|wood\b|red oak (?:tree|plywood)|"
            r"is red oak|why is red oak|where to plant|when do red oaks|tin roof (?:detroit|hours)|what time does tin roof|"
            r"where is|how far|good place to live|\bsafe\b|dangerous|directions|car dealerships|what's on tap|"
            r"sachse road|haslet yard|heat tape|what color is mesquite|is mesquite|plano texas companies|"
            r"loan companies|insurance companies in denton|oak roof$|^benbrook tx$|texas university park|"
            r"^roofing university$|^will roof$|^with roofing$|^how roofing$|^how roofing works$|^how roofing is done$|"
            r"^roofing when it rains$|^which roofing company is the best$|how many roof slates|cedar shingles fixing|"
            r"who is responsible for roof repairs in a flat|emergency roof repair dc|^roofing texas city)")
JOBS = (r"\b(jobs?|salary|make in texas|make a year|contractors make|internships?|job description|why roofing companies fail|"
        r"how many roofing companies|how many roofers|worker|engineer\b)")
CONSTRUCTION = r"\bconstruction\b|general contractor in dallas|commercial general contractor"
SUPPLY = r"\b(supply|supplies|cut to size|material|sheets cost|how much roofing do i need|how much metal roofing do i need)\b"
AMBIG = (r"^(roofing addison|addison roofing (?:contractor|company)|bedford roofing|lancaster roofing(?: company| contractors)?|"
         r"roofing companies in lancaster|princeton roofing|princeton roofers|roofing company princeton|roofing roanoke|"
         r"highland park roofing.*|heath roofing company|saginaw roofing|roofing arlington tx usa)$")

# ---- pages -------------------------------------------------------------------------------------------
PAGES = {
    "home": "/", "services": "/services/", "areas": "/service-areas/", "how": "/how-it-works/", "about": "/about/",
    "faq": "/faq/", "contact": "/contact/", "checklist": "/hail-claim-checklist/",
    "repair": "/roof-repair/", "replacement": "/roof-replacement/", "leak": "/roof-leak-repair/",
    "storm": "/storm-damage-roof-repair/", "hail": "/hail-damage-roof-repair/", "wind": "/wind-damage-roof-repair/",
    "inspection": "/roof-inspection/", "emergency": "/emergency-roof-repair/", "commercial": "/commercial-roofing/",
    "flat": "/flat-roof-repair/", "metal": "/metal-roofing/", "flashing": "/roof-flashing-repair/",
    "g-cost": "/roof-replacement-cost-dallas/", "g-insurance": "/roof-insurance-claim-texas/",
    "g-license": "/do-roofers-need-a-license-in-texas/", "g-lifespan": "/how-long-does-a-roof-last-in-texas/",
    "g-storm": "/what-to-do-after-storm-damage-to-roof/",
}
TARGETS = {
    "roofing company in dallas": "home", "roofing service in dallas": "services", "roofing in dfw": "areas",
    "roof repair in dallas": "repair", "roof replacement in dallas": "replacement", "roof leak repair dallas": "leak",
    "storm damage roof repair dallas": "storm", "hail damage roof repair dallas": "hail",
    "roof inspection dallas": "inspection", "emergency roof repair dallas": "emergency",
    "commercial roofing dallas": "commercial", "flat roof repair dallas": "flat", "metal roofing dallas": "metal",
    "where does flashing go on a roof": "flashing", "roof replacement cost dallas": "g-cost",
    "how does roof insurance claim work": "g-insurance", "do roofers need a license in texas": "g-license",
    "how long does a roof last in texas": "g-lifespan", "what is considered storm damage to roof": "g-storm",
}
NO_ROW_TARGETS = {
    "wind": "wind damage roof repair dallas (no row in the Oct 13 2026 pull; CLAUDE.md lists wind damage as a service)",
    "how": "none (support page explaining the free line)", "about": "none (support page)",
    "faq": "none (support page; collects the Question rows)", "contact": "none (contact form page)",
    "checklist": "none (checklist download page)",
}
SUPPORT = {
    "home": ["roofing company dallas", "roofing companies in dallas", "roofing dallas", "roofing dallas texas",
             "roofing contractors dallas texas", "roofing contractor in dallas", "roofing contractors in dallas tx",
             "roofing contractor in dallas texas", "roofing contractor dallas", "roofing in dallas texas",
             "roofing near dallas", "roofing companies near dallas tx", "best roofing contractors in dallas",
             "best roofing company dallas tx", "top roofing companies dallas tx", "top roofing companies in dallas",
             "residential roofing dallas tx", "roofing texas", "roofing companies in texas"],
    "services": ["roofing repair dallas", "dallas roofing repair", "roof repair dallas", "roof repair description"],
    "areas": ["roofing companies dallas fort worth", "roofing companies in dallas fort worth", "roofing companies in dfw",
              "roofing dfw", "roofing dallas fort worth", "denton county roofing"],
    "repair": ["roof repair in dallas tx", "dallas roof repair", "how often roof maintenance"],
    "replacement": ["roof replacement dallas", "dallas roof replacement", "roof replacement estimate example",
                    "when is roofing season", "do roofers work in the winter", "how late do roofers work",
                    "dallas construction permits", "how often is roof replaced"],
    "leak": ["roofing leak repair near me", "dallas roof leak", "roof leak dallas", "who fixes roof leaks near me",
             "how much does it cost to repair leaking roof", "roofing when it rains"],
    "storm": ["roof storm damage", "storm damage roof repairs", "storm damage roof repair near me",
              "storm damage roof repair cost"],
    "hail": ["how much hail damage to replace roof", "how long does hail damage repair take", "why is hail damage bad for a roof",
             "is it worth getting hail damage repair", "is hail damage worth fixing", "will hail damage a new roof",
             "hail damage repair rockwall tx"],
    "inspection": ["roof inspection report example", "when to get a roof inspection", "how often roof inspection"],
    "emergency": ["roof emergency repair", "emergency roof repair near me", "emergency roof leak repair near me",
                  "who to call for a leaky roof", "emergency roof repair dallas tx", "24 hour emergency roof repair near me",
                  "emergency roof repair cost", "emergency roof damage", "what is an emergency repair",
                  "how can i get help to fix my roof", "can you get a grant for roof repairs"],
    "commercial": ["commercial roofing contractors dallas tx", "commercial roofing companies dallas tx", "commercial roofing dallas tx",
                   "commercial roofing contractor dallas", "commercial roofing dfw"],
    "flat": ["flat roof repair near me", "flat roof repair do it yourself", "flat roof repair companies near me",
             "are flat roofs cheaper to replace", "hot tar roofing companies near me"],
    "metal": ["metal roofing in dallas", "metal roofing dallas tx", "metal roof color ideas", "benefits of a tin roof",
              "what is the best color for a metal roof", "whats the best color for a metal roof", "how much does a metal roof cost in texas",
              "how much metal roofing cost", "green metal roofing near me"],
    "flashing": ["roofing metal valleys"],
    "g-cost": ["how much does a roof replacement cost", "how much should a roof replacement cost", "how much is a roof replacement in texas",
               "how much does a roof replacement cost in texas", "why is replacing a roof so expensive", "how much is a new roof going to cost",
               "dallas roof replacement cost", "how much roofing cost", "how much does a new roof cost in texas",
               "how much does a roof cost in texas", "how much is roofing cost per square", "will roofing companies finance",
               "will roofing prices go down", "will roofing costs go down in 2023", "do roofers charge sales tax",
               "cost to install cedar shingles"],
    "g-insurance": ["how much does insurance pay for roof replacement", "can i get my roof replaced for free",
                    "does insurance cover storm damage to roof", "does home insurance cover storm damage to roof",
                    "will insurance pay for storm damage", "how much hail damage for insurance to replace roof",
                    "will a hail damage claim affect my rates", "will roofing companies pay your deductible"],
    "g-license": ["general contractor license dallas", "general contractor license dallas texas", "when should you pay a roofer",
                  "when to pay roofing contractor", "roofing contractor dallas ga"],
    "g-lifespan": [],
    "g-storm": [],
}
SUPPORT["g-license"].remove("roofing contractor dallas ga")  # another state: listed as unused instead


def town_of(kw):
    """The longest town name inside a keyword, or None."""
    best = None
    for t in TOWN_NAMES:
        if re.search(r"\b" + re.escape(t) + r"\b", kw) and (best is None or len(t) > len(best)):
            best = t
    return best


def is_roofing(kw):
    return re.search(r"\broof", kw) is not None


def texas_row(kw, town):
    return bool(re.search(r"\b(tx|texas)\b", kw)) or town in TEXAS_ONLY


def classify(kw, vol):
    """Return ("page", key, role) or ("unused", reason)."""
    if kw in TARGETS:
        return ("page", TARGETS[kw], "target")
    for k, kws in SUPPORT.items():
        if kw in kws:
            return ("page", k, "supporting")
    if re.search(COMPANY, kw):
        return ("unused", "names a specific roofing, supply or construction company (CLAUDE.md rule 3)")
    if re.search(AMBIG, kw):
        return ("unused", "town name without Texas that is larger or as common in another state (Addison IL, Heath OH, "
                          "Highland Park IL, Lancaster PA, Princeton NJ, Roanoke VA, Bedford, Saginaw MI): not counted as DFW demand")
    if re.search(OTHER_PLACE, kw):
        return ("unused", "a Texas metro outside DFW or another state (CLAUDE.md rule 4)")
    if re.search(JOBS, kw):
        return ("unused", "jobs, wages or roofing-industry trivia (not a homeowner looking for roofing help)")
    if re.search(OFFTOPIC, kw):
        return ("unused", "weather, ZIP code, tax rate, firewood, directions, town trivia or a meaningless fragment (no roofing intent)")
    if re.search(SUPPLY, kw):
        return ("unused", "roofing supply or materials-quantity intent (the line sells no materials)")
    if re.search(CONSTRUCTION, kw):
        return ("unused", "general construction, law, news or general-contractor intent (not roofing help)")
    t = town_of(kw)
    if t and t not in ("dallas",):
        if not is_roofing(kw):
            return ("unused", "town row without a roofing term")
        return ("page", "town:" + t, "supporting")
    rules = [("flat roof", "flat"), ("metal roof", "metal"), ("commercial", "commercial"), ("hail", "hail"),
             ("emergency", "emergency"), ("inspect", "inspection"), ("leak", "leak"), ("storm", "storm"),
             ("flashing", "flashing"), ("insurance", "g-insurance"), ("claim", "g-insurance"), ("license", "g-license"),
             ("cost", "g-cost"), ("how much", "g-cost"), ("how long", "g-lifespan"), ("how often", "g-lifespan"),
             ("replace", "replacement"), ("permit", "replacement"), ("repair", "repair"), ("roofing", "home"),
             ("roofer", "home"), ("roof", "home")]
    for needle, p in rules:
        if needle in kw:
            return ("page", p, "rule")
    return None


def main():
    wb = openpyxl.load_workbook(ROOT / "keywords" / "DFW-Roofing-Keywords.xlsx", read_only=True)
    raw = list(wb["ALL"].iter_rows(values_only=True))[1:]
    rows, seen = [], set()
    for seed, kw, typ, vol, sd, cpc, pd in raw:
        kw = str(kw).strip().lower()
        if kw in seen:
            continue
        seen.add(kw)
        rows.append((seed, kw, typ, vol or 0, sd or 0))

    # Town qualification: Texas, roofing, non-company rows with 10+ searches.
    towns = {}
    for t, name in TOWN_NAMES.items():
        key = t.replace(" ", "-")
        quals = []
        for seed, kw, typ, vol, sd in rows:
            if vol < 10 or town_of(kw) != t or not is_roofing(kw):
                continue
            if re.search(COMPANY, kw) or re.search(OTHER_PLACE, kw) or re.search(AMBIG, kw):
                continue
            if not texas_row(kw, t):
                continue
            quals.append((kw, vol, sd, typ))
        quals.sort(key=lambda q: (-q[1], 0 if re.search(r"\b(tx|texas)$", q[0]) else 1, 0 if q[0].startswith("roofing ") else 1, q[0]))
        if key in TOWN_TARGET and not any(q[0] == TOWN_TARGET[key] for q in quals):
            raise SystemExit(f"{key}: target {TOWN_TARGET[key]} does not qualify")
        if key in TOWN_TARGET:
            tgt = next(q for q in quals if q[0] == TOWN_TARGET[key])
        else:
            tgt = quals[0] if quals else None
        url = EXISTING.get(key, f"/roofing-{key}-tx/")
        towns[key] = {"name": name, "url": url, "qualifies": bool(quals), "existing": key in EXISTING,
                      "target": tgt[0] if tgt else None, "volume": tgt[1] if tgt else 0, "sd": tgt[2] if tgt else None,
                      "qualifying_rows": [f"{q[0]} ({q[1]})" for q in quals]}

    by_page = defaultdict(list)
    unused = defaultdict(list)
    unclassified = []
    for seed, kw, typ, vol, sd in rows:
        rec = (kw, typ, vol, sd)
        t = town_of(kw)
        if t and t in TOWN_NAMES and towns[t.replace(" ", "-")]["target"] == kw:
            by_page["town:" + t].append(("target", rec))
            continue
        c = classify(kw, vol)
        if c is None:
            (unclassified if vol >= 10 else unused["below the 10-search threshold and no page fits"]).append(rec)
            continue
        if c[0] == "unused":
            unused[c[1]].append(rec)
            continue
        _, page, role = c
        if page.startswith("town:"):
            tk = page[5:].replace(" ", "-")
            if not towns[tk]["qualifies"]:
                unused[f"{towns[tk]['name']}: no qualifying Texas roofing row with 10+ searches, so no town page"].append(rec)
                continue
            page = "town:" + page[5:]
        if role == "rule":
            role = "supporting" if vol >= 10 else "below 10"
        if role == "supporting" and vol < 10:
            role = "below 10"
        if "near me" in kw and role == "target":
            raise SystemExit(f"near-me row cannot be a target: {kw}")
        by_page[page].append((role, rec))

    qual = {k: v for k, v in towns.items() if v["qualifies"]}
    for k, v in towns.items():
        PAGES["town:" + k.replace("-", " ")] = v["url"]
    total10 = sum(1 for r in rows if r[3] >= 10)
    assigned10 = sum(1 for p in by_page.values() for role, rec in p if rec[2] >= 10)
    unused10 = sum(1 for g in unused.values() for rec in g if rec[2] >= 10)
    out = [
        "# Keyword plan (dfwexpertroofers.com, Playbook 2.0, Oct 13 2026)",
        "",
        "Generated by `python3 scripts/keyword_plan.py` from keywords/DFW-Roofing-Keywords.xlsx (Ubersuggest,",
        "United States, pulled Oct 13 2026, ALL tab, de-duplicated). Volume is monthly searches; SD is Ubersuggest",
        "SEO difficulty; Q marks a Question row.",
        "",
        "Rules applied (CLAUDE.md): every keyword with a volume of 10 or more is a page's target, a supporting",
        "keyword, or listed below as deliberately unused with a reason. \"Near me\" rows are national volume and",
        "are only ever supporting keywords. Rows naming a roofing company, rows about other states or other Texas",
        "metros, and off-topic rows are unused. Rows under 10 are classified by the same rules for reference.",
        "",
        f"Totals: {len(rows)} unique keywords. {total10} have a volume of 10 or more: {assigned10} assigned to a page,",
        f"{unused10} deliberately unused, {len(unclassified)} unclassified.",
        "",
        "## Town page decisions",
        "",
        "Maurice's rule: a DFW town with 10 or more searches a month on a roofing keyword gets a page. Counted",
        "only Texas rows (the row says tx or texas, or the place name exists only in Texas), only roofing keywords,",
        "and never a row naming a roofing company or another state.",
        "",
        f"- {len(qual)} towns qualify (listed under Pages below with their target keyword and volume).",
    ]
    for k, v in sorted(towns.items()):
        if not v["qualifies"]:
            out.append(f"- **{v['name']}: no page.** No Texas roofing row with 10+ searches that is not a company name.")
    out += ["", "## Pages", ""]
    for key, url in PAGES.items():
        items = by_page.get(key, [])
        if key.startswith("town:") and not towns[key[5:].replace(" ", "-")]["qualifies"]:
            continue
        tgt = [rec for role, rec in items if role == "target"]
        sup = sorted([rec for role, rec in items if role == "supporting"], key=lambda r: -r[2])
        low = sorted([rec for role, rec in items if role == "below 10"], key=lambda r: -r[2])
        out.append(f"### {url}" + (f" ({towns[key[5:].replace(' ', '-')]['name']})" if key.startswith("town:") else ""))
        out.append("")
        if tgt:
            t = tgt[0]
            out.append(f"- Target: **{t[0]}** ({t[2]}/mo, SD {t[3]}, {t[1]})")
        elif key in NO_ROW_TARGETS:
            out.append(f"- Target: **{NO_ROW_TARGETS[key]}**")
        else:
            out.append("- Target: none in the data (support page)")
        if sup:
            out.append("- Supporting: " + "; ".join(f"{r[0]} ({r[2]}{', Q' if r[1] == 'Question' else ''}"
                                                       f"{', national near-me' if 'near me' in r[0] else ''})" for r in sup))
        if low:
            out.append("- Under 10 (reference): " + "; ".join(f"{r[0]} ({r[2]}{', Q' if r[1] == 'Question' else ''})" for r in low))
        out.append("")
    out += ["## Deliberately unused", ""]
    for reason, recs in sorted(unused.items(), key=lambda kv: -sum(r[2] for r in kv[1])):
        recs.sort(key=lambda r: -r[2])
        big = [r for r in recs if r[2] >= 10]
        out.append(f"### {reason}")
        out.append("")
        out.append(f"{len(recs)} rows ({len(big)} with 10+ searches).")
        if big:
            out += ["", "10+: " + "; ".join(f"{r[0]} ({r[2]})" for r in big)]
        small = [r[0] for r in recs if r[2] < 10]
        if small:
            out += ["", f"Under 10 ({len(small)}): " + "; ".join(small)]
        out.append("")
    if unclassified:
        out += ["## UNCLASSIFIED (fix scripts/keyword_plan.py)", ""] + [f"- {r[0]} ({r[2]})" for r in unclassified]
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs" / "keyword-plan.md").write_text("\n".join(out) + "\n")
    (ROOT / "docs" / "towns.json").write_text(json.dumps(towns, indent=1) + "\n")
    print(f"{len(rows)} rows; {total10} with 10+: {assigned10} assigned, {unused10} unused, {len(unclassified)} unclassified")
    print(f"{len(qual)} towns qualify; no page: {sorted(v['name'] for v in towns.values() if not v['qualifies'])}")
    for r in unclassified:
        print("UNCLASSIFIED", r)
    found = {rec[0] for v in by_page.values() for role, rec in v if role == "target"}
    missing = [k for k in TARGETS if k not in found]
    for k in missing:
        print("TARGET NOT FOUND IN DATA", k)
    return 1 if unclassified or missing else 0


if __name__ == "__main__":
    sys.exit(main())
