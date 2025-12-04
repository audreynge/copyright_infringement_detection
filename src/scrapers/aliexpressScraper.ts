import puppeteer from 'puppeteer-extra';
import StealthPlugin from 'puppeteer-extra-plugin-stealth';
import * as readline from 'readline';
import { writeFileSync } from 'fs';
import { exec } from 'child_process';
import { join } from 'path';

puppeteer.use(StealthPlugin());

const waitForUserInput = (): Promise<void> => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  return new Promise((resolve) => {
    console.log('\nPlease complete the bot check in the browser window.');
    console.log('\nPress Enter in the terminal once you have completed the bot check and the page has loaded.\n');
    rl.question('', () => {
      rl.close();
      resolve();
    });
  });
};

const scrapeHtml = async (url: string) => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  // pretend to be real user
  await page.setExtraHTTPHeaders({ 'accept-language': 'en-US,en;q=0.9' });

  await page.goto(url, {
    waitUntil: 'domcontentloaded',
  });

  await waitForUserInput();
  await new Promise(resolve => setTimeout(resolve, 2000));
  
  // trigger lazy loading with scrolling
  await page.evaluate(() => {
    window.scrollTo(0, document.body.scrollHeight);
  });
  await new Promise(resolve => setTimeout(resolve, 1000));
  
  const html = await page.content();
  const filePath = join(process.cwd(), 'scraped-page.txt');
  writeFileSync(filePath, html, 'utf-8');
  exec(`open "${filePath}"`);
  console.log('Page scraped successfully');
  
  return html;
};

export default scrapeHtml;