// Headless verification of the static console (Playwright + system Chrome):
// boots the site, opens the Index (branch directory), and checks for broken
// images, duplicate figures per card, console errors, and the stats line.
//
//   cd ~/intel-console/static && python3 -m http.server 8801 &
//   node ~/intel-console/tools/verify_site.mjs http://localhost:8801/ /tmp/out
import { chromium } from '/home/joseph/oz-archive/tools/node_modules/playwright/index.mjs';

const URL = process.argv[2] || 'http://localhost:8801/';
const OUT = process.argv[3] || '/tmp';
const browser = await chromium.launch({ executablePath: '/usr/bin/google-chrome', headless: true,
  args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage', '--disable-gpu'] });
const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });
const errors = [], failed = [];
page.on('pageerror', e => errors.push('pageerror: ' + e.message));
page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
page.on('requestfailed', r => failed.push('FAILED ' + r.url()));
page.on('response', r => { if (r.status() >= 400) failed.push(`${r.status()} ${r.url()}`); });

await page.goto(URL, { waitUntil: 'networkidle', timeout: 120000 });
await page.waitForFunction(() => {
  const ls = document.getElementById('loading-screen');
  return !ls || ls.style.display === 'none' || ls.classList.contains('done');
}, null, { timeout: 120000 });
await page.waitForTimeout(1500);
await page.keyboard.press('Escape');            // dismiss the guide
await page.waitForTimeout(900);
const navOpen = await page.evaluate(() => document.getElementById('navigator-overlay')?.classList.contains('open'));
if (!navOpen) { await page.keyboard.press('i'); await page.waitForTimeout(700); }
await page.waitForTimeout(2000);

const report = await page.evaluate(() => {
  const stats = document.getElementById('stats-bar')?.innerText.replace(/\s+/g, ' ').trim();
  const cards = [...document.querySelectorAll('.nav-card')].map(c => {
    const figs = [...c.querySelectorAll('.nav-fig')].map(f => {
      const im = f.querySelector('img');
      return { name: f.getAttribute('title'), src: im ? im.getAttribute('src') : '',
               broken: !!(im && !im.src.startsWith('data:') && im.complete && im.naturalWidth === 0) };
    });
    const srcs = figs.map(f => f.src).filter(s => s && !s.startsWith('data:'));
    const dupes = srcs.filter((s, i) => srcs.indexOf(s) !== i);
    return { label: c.querySelector('.nav-card-label')?.innerText, count: c.querySelector('.nav-card-count')?.innerText,
             figs: figs.map(f => f.name), broken: figs.filter(f => f.broken).map(f => f.name), dupes };
  });
  return { stats, subtitle: document.querySelector('.nav-subtitle')?.innerText, cards };
});
await page.screenshot({ path: `${OUT}/verify_navigator.png` });

await page.evaluate(() => document.querySelector('.nav-card[data-branch="exploitation"]')?.click());
await page.waitForTimeout(3000);
await page.screenshot({ path: `${OUT}/verify_branch_exploitation.png` });
await page.evaluate(() => toggleBranchFocus('intelligence'));
await page.waitForTimeout(3000);
await page.screenshot({ path: `${OUT}/verify_branch_intelligence.png` });

const nodeImgCheck = await page.evaluate(async () => {
  const data = await API.getGraphFull('speculative');
  const urls = data.nodes.map(n => n.photo_url).filter(u => u && !u.startsWith('data:'));
  const bad = [];
  await Promise.all(urls.map(u => new Promise(res => { const im = new Image(); im.onload = res; im.onerror = () => { bad.push(u); res(); }; im.src = u; })));
  return { total: urls.length, bad };
});
// open Topol's dossier via hash deep link
const topol = await page.evaluate(async () => { const d = await API.getGraphFull('speculative'); return d.nodes.find(n => n.name === 'Chaim Topol')?.id; });
if (topol) {
  await page.goto(`${URL}#entity/${topol}`, { waitUntil: 'networkidle', timeout: 120000 });
  await page.waitForFunction(() => document.getElementById('dossier-panel')?.classList.contains('open'), null, { timeout: 60000 }).catch(() => {});
  await page.waitForTimeout(2500);
  await page.screenshot({ path: `${OUT}/verify_topol_dossier.png` });
}
console.log(JSON.stringify({ report, nodeImgCheck, errors: errors.slice(0, 20), failed: failed.slice(0, 20) }, null, 1));
await browser.close();
