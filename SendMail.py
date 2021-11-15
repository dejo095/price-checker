import smtplib

class SendMail:

  def __init__(self, emailFrom, emailTo, password) -> None:
      self.emailFrom = emailFrom
      self.emailTo = emailTo
      self.password = password

  def send(self, device, shop, price, URL):
    
    # If not using Gmail then update line below
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(self.emailFrom, self.password)

    subject = shop + ' price drop => ' + device
    body = 'On ' + shop + ' price dropped to ' + str(price) + '\n\n'
    body += 'Product link => ' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(self.emailFrom, self.emailTo, msg)
    print('Email sent for ' + shop)
    server.quit()