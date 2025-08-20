import { chromium } from 'playwright-extra';
import StealthPlugin from 'puppeteer-extra-plugin-stealth';

chromium.use(StealthPlugin());

(async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  // pretend to be real user
  await page.setExtraHTTPHeaders({ 'accept-language': 'en-US,en;q=0.9' });

  await page.goto('https://www.aliexpress.us/w/wholesale-mama-elephant-cute-clear-stamps.html?page=1&g=y&SearchText=mama+elephant+cute+clear+stamps', {
    waitUntil: 'domcontentloaded',
  });

  // trigger lazy loading with scrolling
  await page.mouse.wheel(0, 500);
  await page.waitForTimeout(2000);

  const html = await page.content();

  console.log(html);

  // await browser.close();
})();