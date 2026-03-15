import scrapeHtml from './scrapers/scraper.js';
import parseAliexpressProducts from './parsers/parseAliExpressProducts.js';
import fs from 'fs';
import { execSync } from 'child_process';

const main = async () => {
  try {
    const aliexpressUrl = 'https://www.aliexpress.us/w/wholesale-mama-elephant-cute-clear-stamps.html?page=1&g=y&SearchText=mama+elephant+cute+clear+stamps';
    const aliexpressHtml = await scrapeHtml(aliexpressUrl);
    const aliexpressProducts = await parseAliexpressProducts(aliexpressHtml);
    fs.writeFileSync('data/products_raw_aliexpress.json', JSON.stringify(aliexpressProducts, null, 2));

    execSync("python3 ml/preprocessing/clean_reference_data.py", { stdio: "inherit" });
    execSync("python3 ml/preprocessing/clean_candidate_data.py", { stdio: "inherit" });
    execSync("python3 ml/preprocessing/download_images.py", { stdio: "inherit" });
    
  } catch (error) {
    console.error('Error:', (error as Error).message);
    process.exit(1);
  }
}

main();