import time
from SendMail import SendMail
from provider import Provider

# Put email creds here
emailFrom = ''
emailTo = ''
emailPass = ''

product1 = Provider("Product Name", 2.920, "Webshop Name", "https://www.", "put element selector here", None)
product2 = Provider("Product Name", 2.500, "Webshop Name", "https://www.", "put element selector here", "span")
product3 = Provider("Product Name", 2.500, "Webshop Name", "https://www.", "put element selector here", "span")

products = [product1, product2, product3]    

def go():
  for product in products:
    actionPrice = product.checkPrice()
    if actionPrice != None:
      SendMail(emailFrom, emailTo, emailPass).send(product.device, product.shop, actionPrice, product.url)
    

while(True):
  go()
  time.sleep(600) # every 10minutes
