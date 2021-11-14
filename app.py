import time
from SendMail import SendMail
from provider import Provider

# Put email creds here
emailFrom = '' # email address from which email will be sent
emailTo = '' # eamil address where you want emails to arrive
emailPass = '' # Gmail app password

product1 = Provider("Product Name here", 1.00, "Webshop Name", "Url to product", "Classname where price is put", "Child element that contains price")
product2 = Provider("Product Name here", 1.00, "Webshop Name", "Url to product", "Classname where price is put", "Child element that contains price")
product3 = Provider("Product Name here", 1.00, "Webshop Name", "Url to product", "Classname where price is put", None)

products = [product1, product2, product3]    

def go():
  for product in products:
    actionPrice = product.checkPrice()
    if actionPrice > 0:
      SendMail(emailFrom, emailTo, emailPass).send(product.device, product.shop, actionPrice, product.url)
    

while(True):
  go()
  time.sleep(7200) # Checks price every 2 hours
