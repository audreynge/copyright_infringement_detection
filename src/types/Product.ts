/**
 * Represents a product found on a search results page.
 */
export interface Product {
  /**
   * The ID of the product.
   */
  product_id: string;

  /**
   * The title of the product.
   */
  title: string;

  /**
   * The URL of the first image of the product.
   */
  image_url: string;

  /**
   * The URL of the product.
   */
  url?: string;
}