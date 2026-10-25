const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  for (const [h, out, shots] of JSON.parse(process.argv[2])) {
    await p.goto('file://' + h, { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(500);
    await p.pdf({ path: out, format: 'A4', landscape: true, printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
    await p.setViewportSize({ width: 1123, height: 794 });
    const pages = await p.$$('section.page');
    for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: `${shots}-${i + 1}.png` });
  }
  await b.close();
})();
