import scrapy
from pathlib import Path

class AliExpressSpider(scrapy.Spider):
  name = 'aliexpress'

  def start_requests(self):
    urls = [
      f"https://www.aliexpress.us/w/wholesale-mama-elephant-cute-clear-stamps.html?page={page}&g=y&SearchText=mama+elephant+cute+clear+stamps" 
      for page in range(1, 3)
    ]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    page = response.url.split("page=")[-1].split("&")[0]
    filename = f"aliexpress-{page}.html"
    Path(filename).write_bytes(response.body)
    self.log(f"Saved file {filename}")