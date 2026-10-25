const { chromium } = require('playwright');
(async () => {
  const [html, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 2000 } });
  await p.goto('file://' + html); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
  const list = await p.evaluate(() => {
    const res = [];
    document.querySelectorAll('section.page').forEach((pg, i) => {
      const k = (pg.querySelector('.kick') || {}).textContent || '';
      pg.querySelectorAll('.slot > .sl').forEach((s, j) => res.push({ i, j, k }));
    });
    return res;
  });
  const host = await p.evaluateHandle(() => { const h = document.createElement('div'); h.style.cssText = 'position:absolute;left:0;top:0;z-index:99999;background:#fff'; document.body.prepend(h); return h; });
  let n = 0;
  for (const it of list) {
    await p.evaluate(({ i, j }) => {
      const pg = document.querySelectorAll('section.page')[i];
      const s = pg.querySelectorAll('.slot > .sl')[j];
      const h = document.body.firstElementChild; h.innerHTML = '';
      const c = s.cloneNode(true); c.style.setProperty('--w', '1080px'); c.style.boxShadow = 'none'; c.style.borderRadius = '0'; h.appendChild(c);
    }, it);
    await p.waitForTimeout(60);
    const el = await p.$('body > div:first-child > .sl');
    const name = `${String(it.i).padStart(2, '0')}-${String(it.j + 1).padStart(2, '0')}`;
    await el.screenshot({ path: `${out}/${name}.png` }); n++;
  }
  console.log(n);
  await b.close();
})();
