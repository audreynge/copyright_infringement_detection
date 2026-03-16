import pandas as pd

def load_data(products_raw_path: str) -> pd.DataFrame:
  """
  Loads the data from a JSON file and returns a pandas DataFrame.
  """
  with open(products_raw_path, 'r') as f:
    data = pd.read_json(f)

  return data.to_csv('data/candidate_products.csv', index=False)

if __name__ == '__main__':
  load_data('data/products_raw_aliexpress.json')