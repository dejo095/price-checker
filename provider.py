import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

class Provider:

  def __init__(self, device, targetPrice, shop, url, classname) -> None:
    
    self.device = device
    self.targetPrice = targetPrice
    self.shop = shop
    self.url = url
    self.classname = classname

  def checkPrice(self) -> float:
    
    page = requests.get(self.url, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    price = soup.select_one(self.classname).get_text().strip()
    price = float(price[0:5])
    
    if(price <= self.targetPrice):
      return price
    
    return 0.0
