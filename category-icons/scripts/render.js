// Renderiza SVG -> PNG com o Chromium do Playwright
const { chromium } = require(process.env.PW || 'playwright');
const fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const jobs = fs.readdirSync(path.join(root, 'svg')).map(f => [path.join(root, 'svg', f), path.join(root, 'png', f.replace('.svg', '.png'))]);
  jobs.push([path.join(root, 'grid.svg'), path.join(root, 'grid.png')]);
  for (const [src, dst] of jobs) {
    const svg = fs.readFileSync(src, 'utf8');
    const [, w, h] = svg.match(/width="(\d+)" height="(\d+)"/);
    await page.setViewportSize({ width: +w, height: +h });
    await page.setContent(`<html><body style="margin:0">${svg}</body></html>`);
    await page.locator('svg').screenshot({ path: dst });
  }
  await browser.close();
  console.log('rendered', jobs.length);
})();
