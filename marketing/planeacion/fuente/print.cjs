// node print.cjs [carpeta_frames]
// Imprime ../VESTA-plan-ventas-contenido-navidad-2026.pdf y, si se pasa una carpeta,
// guarda ahí un PNG por cuadro de cada video (para armar los GIF con gif.py).
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'plan.html'), { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: path.join(__dirname, '..', 'VESTA-plan-ventas-contenido-navidad-2026.pdf'),
    width: '297mm', height: '210mm', printBackground: true, preferCSSPageSize: true });
  const outDir = process.argv[2];
  if (outDir) {
    const g = await b.newPage();
    await g.goto('file://' + path.join(__dirname, 'frames.html'), { waitUntil: 'networkidle' });
    await g.evaluate(() => document.fonts.ready);
    for (const el of await g.$$('.gf')) {
      const id = await el.getAttribute('id');
      await el.screenshot({ path: path.join(outDir, id + '.png') });
    }
  }
  await b.close();
})();
