// Prévia de legibilidade: todos os ícones em 96, 64, 48 e 32 px (densidade 2x)
const { chromium } = require(process.env.PW || 'playwright');
const fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..');
(async () => {
  const files = fs.readdirSync(path.join(root, 'svg')).sort();
  const rows = [96, 64, 48, 32].map(s => `<div style="display:flex;gap:10px;align-items:center;margin:10px 0">
    <span style="width:44px;font:600 12px sans-serif;color:#4A4A4A">${s}px</span>
    ${files.map(f => `<img src="file://${path.join(root, 'svg', f)}" width="${s}" height="${s}">`).join('')}</div>`).join('');
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 2, viewport: { width: 900, height: 400 } });
  const tmp = path.join(root, '.sizes.html');
  fs.writeFileSync(tmp, `<!doctype html><body style="margin:0;padding:12px 16px;background:#F5F2ED">${rows}</body>`);
  await page.goto('file://' + tmp);
  await page.waitForTimeout(300);
  await page.screenshot({ path: path.join(root, 'sizes.png'), fullPage: true });
  await browser.close();
  fs.unlinkSync(tmp);
})();
