import scrapeHtml from './scrapers/aliexpressScraper.js';
import parseProducts from './parsers/parseProducts.js';

const main = async () => {
  try {
    const url = 'https://www.aliexpress.us/w/wholesale-mama-elephant-cute-clear-stamps.html?page=1&g=y&SearchText=mama+elephant+cute+clear+stamps';
    const html = await scrapeHtml(url);
    const products = await parseProducts(html);
    
    console.log('\n=== Parsed Products ===');
    console.log(`Total products found: ${products.length}\n`);
    
    products.forEach((product, index) => {
      console.log(`Product ${index + 1}:`);
      console.log(`  ID: ${product.productId}`);
      console.log(`  Title: ${product.title}`);
      console.log(`  Image: ${product.imageUrl}`);
      console.log(`  URL: ${product.url || 'N/A'}`);
      console.log('');
    });
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

main();