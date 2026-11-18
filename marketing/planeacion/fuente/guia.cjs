// node guia.cjs -> ../VESTA-guia-de-grabacion.pdf (a partir de guia.html)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'guia.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: path.join(__dirname, '..', 'VESTA-guia-de-grabacion.pdf'),
    width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
