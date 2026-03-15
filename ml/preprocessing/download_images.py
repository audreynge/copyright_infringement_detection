import pandas as pd
import requests

def download_images(df: pd.DataFrame, output_dir: str) -> None:
  for i, row in df.iterrows():
    image_url = row['image_url']
    res = requests.get(image_url)
    res.raise_for_status()

    with open(f'{output_dir}/{row["product_id"]}.jpg', 'wb') as f:
      f.write(res.content)

if __name__ == '__main__':
  df_reference = pd.read_csv('data/products_reference.csv')
  df_candidate = pd.read_csv('data/products_candidates.csv')

  download_images(df_reference, 'data/reference_images')
  download_images(df_candidate, 'data/candidate_images')

