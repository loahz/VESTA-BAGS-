// node guia.cjs -> ../VESTA-plantilla-capcut-y-ganchos.pdf (a partir de plantilla.html)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'plantilla.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: path.join(__dirname, '..', 'VESTA-plantilla-capcut-y-ganchos.pdf'),
    width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
