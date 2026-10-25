const { chromium } = require('playwright');
(async () => {
  const [html, out] = process.argv.slice(2);
  const b = await chromium.launch();
  for (const w of [238, 190, 158]) {
    const ctx = await b.newContext({ viewport: { width: 1123, height: 794 }, deviceScaleFactor: Math.ceil(1080 / w) + 0.5 });
    const p = await ctx.newPage();
    await p.goto('file://' + html); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
    const pages = await p.$$('section.page');
    for (let i = 0; i < pages.length; i++) {
      const pw = await pages[i].evaluate(e => getComputedStyle(e).getPropertyValue('--w').trim());
      if (pw !== w + 'px') continue;
      const kick = await pages[i].$eval('.kick', e => e.textContent);
      const sls = await pages[i].$$('.slot .sl');
      for (let j = 0; j < sls.length; j++) {
        await sls[j].evaluate(e => { e.style.boxShadow = 'none'; e.style.borderRadius = '0'; });
        await sls[j].screenshot({ path: `${out}/${String(i).padStart(2,'0')}-${j + 1}.png` });
      }
    }
    await ctx.close();
  }
  await b.close();
})();
