import * as cheerio from 'cheerio';
import { Product } from '../types/Product.js';

/**
 * Parses the raw HTML and returns a list of products.
 * @param html - The HTML content of the page to parse.
 * @returns products - The list of products
 */
const parseProducts = async (html: string): Promise<Product[]> => {
  const $ = cheerio.load(html);
  const products: Product[] = [];
  const seenIds = new Set<string>();

  $('a.search-card-item').each((_, element) => {
    const $element = $(element);
    const href = $element.attr('href') || '';
    
    const productIdMatch = href.match(/item\/(\d+)\.html/) || href.match(/product\/(\d+)/);
    const productId = productIdMatch ? productIdMatch[1] : '';
    
    if (!productId || seenIds.has(productId)) {
      return;
    }
    seenIds.add(productId);

    const firstImg = $element.find('img').first();
    const imageUrl = firstImg.attr('src') || firstImg.attr('data-src') || '';
    const title = firstImg.attr('alt') || $element.attr('title') || '';
    
    const url = href.startsWith('http') ? href : `https://www.aliexpress.com${href}`;

    if (productId && title && imageUrl) {
      products.push({
        product_id: productId,
        title: title.trim(),
        image_url: imageUrl.startsWith('//') ? `https:${imageUrl}` : imageUrl,
        url
      });
    }
  });

  return products;
}

export default parseProducts;