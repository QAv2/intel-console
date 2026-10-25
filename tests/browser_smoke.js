#!/usr/bin/env node
/**
 * Browser smoke test: serve static/ and load it in headless Chromium.
 * Fails on any console error, page error or failed request, or if the
 * graph does not render.
 *
 * Run: node tests/browser_smoke.js   (needs the `playwright` npm package
 * and its Chromium; `uv run pytest` runs this and skips it if they're missing)
 */
const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const STATIC = path.join(__dirname, '..', 'static');
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css',
                '.json': 'application/json', '.jpg': 'image/jpeg', '.png': 'image/png' };

const server = http.createServer((req, res) => {
    let rel = decodeURIComponent(new URL(req.url, 'http://x').pathname);
    if (rel.endsWith('/')) rel += 'index.html';
    const file = path.join(STATIC, rel);
    if (!file.startsWith(STATIC) || !fs.existsSync(file)) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(file)] || 'application/octet-stream' });
    fs.createReadStream(file).pipe(res);
});

server.listen(0, async () => {
    const url = `http://127.0.0.1:${server.address().port}/`;
    const browser = await chromium.launch();
    const errors = [];
    let failed = false;
    try {
        const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });
        page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
        page.on('pageerror', e => errors.push('pageerror: ' + e.message));
        page.on('requestfailed', r => errors.push('request failed: ' + r.url()));
        page.on('response', r => { if (r.status() >= 400) errors.push(`${r.status()} ${r.url()}`); });

        await page.goto(url, { waitUntil: 'networkidle' });
        const nodes = await page.locator('svg circle').count();
        const crumb = await page.locator('#breadcrumb-bar').innerText();

        // Click a node: should open the dossier and enter ego mode.
        await page.locator('svg circle').nth(5).click({ force: true });
        await page.waitForTimeout(1000);
        const crumbAfter = await page.locator('#breadcrumb-bar').innerText();

        console.log(`nodes rendered: ${nodes}; breadcrumb: "${crumb}" -> "${crumbAfter.replace(/\s+/g, ' ')}"`);
        if (nodes < 100) { errors.push(`only ${nodes} SVG circles rendered`); }
        if (!crumb.includes('Network Overview')) { errors.push('initial breadcrumb not drawn'); }
        if (!crumbAfter.includes('Hub')) { errors.push('clicking a node did not enter ego mode'); }
    } catch (e) {
        errors.push('exception: ' + e.message);
    } finally {
        await browser.close();
        server.close();
    }
    if (errors.length) {
        failed = true;
        console.error('FAIL\n' + errors.join('\n'));
    } else {
        console.log('OK: no console errors');
    }
    process.exit(failed ? 1 : 0);
});
