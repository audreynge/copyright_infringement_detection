import requests
import pandas as pd

def get_reference_products(url: str) -> list[dict]:
  res = requests.get(url)
  products = res.json().get('products', [])

  rows = []

  for product in products:
    images = product.get('images', [])
    first_image_url = images[0].get('src', '')

    rows.append({
      'product_id': product.get('id'),
      'title': product.get('title'),
      'image_url': first_image_url,
      'url': f'https://mamaelephant.com/products/{product.get("handle")}'
    })

  df = pd.DataFrame(rows)
  df.to_csv('data/products_reference.csv', index=False)

if __name__ == '__main__':
  url = 'https://mamaelephant.com/collections/stamps/products.json'
  get_reference_products(url)