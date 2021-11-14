import time
from datetime import datetime
from SendMail import SendMail
from provider import Provider

# Put email creds here
emailFrom = '' # email address from which email will be sent
emailTo = '' # eamil address where you want emails to arrive
emailPass = '' # Gmail app password

# Create as many products as you need
# example = Provide("Led TV", targetPrice, "Ebay", "http://www.ebay.com/product/....", ".product-price div p.action")
product1 = Provider("Product Name here", 1.00, "Webshop Name", "Url to product", "Classname where price is located")
product2 = Provider("Product Name here", 1.00, "Webshop Name", "Url to product", "Classname where price is located")
product3 = Provider("Product Name here", 1.00, "Webshop Name", "Url to product", "Classname where price is located")

# add products in array here
products = [product1, product2, product3]    

def go():
  for product in products:
    actionPrice = product.checkPrice()
    if actionPrice > 0:
      SendMail(emailFrom, emailTo, emailPass).send(product.device, product.shop, actionPrice, product.url)
    

while(True):
  now = datetime.now()
  print("--- " + now.strftime("%H:%M:%S"))
  go()
  time.sleep(7200) # Checks price every 2 hours
