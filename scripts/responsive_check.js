// Browser QA over the built site: horizontal overflow at 1440/1024/768/390, JS errors, broken images,
// hero height and call button above the fold, hero text on the left rail at 1440/1920/2560, and card,
// panel, step and photo rows whose short last row leaves a hole on the right (390/768/1024/1440/1920).
// Usage: (serve dist on :8765 first) NODE_PATH=$(npm root -g) node scripts/responsive_check.js [baseUrl] [--shots dir]
const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");
const base = process.argv[2] && !process.argv[2].startsWith("--") ? process.argv[2] : "http://127.0.0.1:8765";
const shotsIdx = process.argv.indexOf("--shots");
const shots = shotsIdx > -1 ? process.argv[shotsIdx + 1] : "";
const dist = process.env.DIST || path.join(__dirname, "..", "dist");

function pages(dir, out = []) {
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    if (fs.statSync(p).isDirectory()) pages(p, out);
    else if (f.endsWith(".html")) {
      let u = "/" + path.relative(dist, p).split(path.sep).join("/");
      if (u.endsWith("/index.html")) u = u.slice(0, -"index.html".length);
      out.push(u);
    }
  }
  return out;
}

(async () => {
  const urls = pages(dist).sort();
  const browser = await chromium.launch();
  const problems = [];
  let checks = 0;
  for (const width of [1440, 1024, 768, 390, 1920, 2560]) {
    const ctx = await browser.newContext({ viewport: { width, height: width >= 1440 ? 900 : 844 } });
    const page = await ctx.newPage();
    let errs = [];
    page.on("pageerror", (e) => errs.push(String(e)));
    // Third-party scripts (Google Analytics, Google Translate) are blocked here: the sandbox has no
    // outside network. Only same-origin failures and real script errors count.
    await page.route("**/*", (r) => (r.request().url().startsWith(base) ? r.continue() : r.abort()));
    page.on("console", (m) => { if (m.type() === "error" && !m.text().startsWith("Failed to load resource")) errs.push(m.text()); });
    page.on("response", (rs) => { if (rs.url().startsWith(base) && rs.status() >= 400) errs.push(rs.status() + " " + rs.url()); });
    const list = width > 1440 ? urls.filter((u) => u === "/" || u.includes("fort-worth-tx") || u.includes("plano-tx") || u === "/roof-repair/") : urls;
    for (const u of list) {
      errs = [];
      await page.goto(base + u, { waitUntil: "load" });
      checks++;
      const r = await page.evaluate(() => {
        const de = document.documentElement;
        const over = de.scrollWidth - de.clientWidth;
        const wide = [];
        if (over > 0) {
          for (const el of document.querySelectorAll("body *")) {
            const b = el.getBoundingClientRect();
            if (b.right > de.clientWidth + 1 && b.width > 0) wide.push(el.tagName + "." + el.className);
            if (wide.length > 4) break;
          }
        }
        const broken = [...document.images].filter((i) => i.complete && i.naturalWidth === 0).map((i) => i.src);
        const hero = document.querySelector(".hero");
        const h1 = document.querySelector(".hero h1");
        const call = document.querySelector(".hero .btn--orange");
        const hb = hero ? hero.getBoundingClientRect() : null;
        return {
          over, wide, broken,
          heroH: hb ? Math.round(hb.height) : null,
          heroW: hb ? Math.round(hb.width) : null,
          h1Left: h1 ? Math.round(h1.getBoundingClientRect().left) : null,
          callBottom: call ? Math.round(call.getBoundingClientRect().bottom) : null,
          vh: window.innerHeight, vw: de.clientWidth,
          holes: (() => {
            const out = [];
            for (const c of document.querySelectorAll(".cards, .grid-2, .grid-3, .facts, .how-strip, .cta__facts, .split")) {
              const kids = [...c.children].filter((k) => k.getBoundingClientRect().width > 0);
              if (kids.length < 2) continue;
              const cb = c.getBoundingClientRect();
              // rows = items whose vertical ranges overlap (a centered, shorter column is still the same row)
              const boxes = kids.map((k) => k.getBoundingClientRect()).sort((a, b) => a.top - b.top);
              const rows = [];
              for (const b of boxes) {
                const r = rows[rows.length - 1];
                if (r && b.top < r.bottom - 1) { r.items.push(b); r.bottom = Math.max(r.bottom, b.bottom); }
                else rows.push({ items: [b], bottom: b.bottom });
              }
              if (rows.length < 2) continue; // one row only: nothing wraps
              const last = rows[rows.length - 1].items;
              const left = Math.min(...last.map((b) => b.left)) - cb.left;
              const right = cb.right - Math.max(...last.map((b) => b.right));
              if (right > 60 && left < 10) out.push((c.className || c.tagName) + ` (${last.length} item(s) in last row, ${Math.round(right)}px empty on the right)`);
            }
            return out;
          })(),
        };
      });
      if (r.over > 0) problems.push(`${width}px ${u}: horizontal overflow ${r.over}px (${r.wide.join(", ")})`);
      if ([390, 768, 1024, 1440, 1920].includes(width) && r.holes.length) problems.push(`${width}px ${u}: row with a hole on the right: ${r.holes.join("; ")}`);
      if (r.broken.length) problems.push(`${width}px ${u}: broken images ${r.broken.join(", ")}`);
      if (errs.length) problems.push(`${width}px ${u}: JS errors ${errs.join(" | ")}`);
      if (r.heroW !== null && r.heroW < r.vw - 1) problems.push(`${width}px ${u}: hero not edge to edge (${r.heroW} of ${r.vw})`);
      if (width >= 1024 && r.heroH !== null && r.heroH > 720) problems.push(`${width}px ${u}: hero ${r.heroH}px tall`);
      if (width >= 1024 && r.callBottom !== null && r.callBottom > r.vh) problems.push(`${width}px ${u}: call button below the fold (${r.callBottom} > ${r.vh})`);
      if (width >= 1440 && r.h1Left !== null && r.h1Left > Math.min(140, width * 0.055) + 2) problems.push(`${width}px ${u}: hero headline not on the left rail (left ${r.h1Left})`);
      if (shots && (u === "/" || u === "/roofing-companies-fort-worth-tx/" || u === "/roofing-contractors-plano-tx/" || u === "/roof-repair/")) {
        fs.mkdirSync(shots, { recursive: true });
        await page.screenshot({ path: path.join(shots, `${width}${u.replace(/[\/.]/g, "_")}.png`), fullPage: width <= 1440 });
      }
    }
    await ctx.close();
  }
  await browser.close();
  for (const p of problems) console.log("PROBLEM", p);
  console.log(`\n${checks} page loads checked at 1440/1024/768/390 (all pages) and 1920/2560 (sample), ${problems.length} problems`);
  process.exit(problems.length ? 1 : 0);
})();
