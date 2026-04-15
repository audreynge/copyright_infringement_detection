import os
from urllib.parse import urlparse
import pandas as pd
import requests

def download_images(df: pd.DataFrame, output_dir: str) -> None:
  os.makedirs(output_dir, exist_ok=True) # make output folder if doesn't exist
  for i, row in df.iterrows():
    image_url = row['image_url']
    res = requests.get(image_url)
    res.raise_for_status()

    path = urlparse(image_url).path
    ext = os.path.splitext(path)[1]
    with open(f'{output_dir}/{row["product_id"]}{ext}', 'wb') as f:
      f.write(res.content)

if __name__ == '__main__':
  df_candidate = pd.read_csv('data/candidate_products.csv')
  df_reference = pd.read_csv('data/reference_products.csv')

  download_images(df_candidate, 'data/candidate_images')
  download_images(df_reference, 'data/reference_images')

