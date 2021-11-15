# price-checker

## Small python app that checks webshops for a price drop and sends email in case actual price is less than target price

For this to work you need to have python installed. <br>

You also need PIP instaled <br>
Using PIP you need to install dependencies:
``` 
pip install requests bs4
```
You also need to have Gmail 2FA enabled and setup Gmail app passwords, then use this generated password for
```
emailPass = '' # Gmail app password
```

to run the app, just type:
```
python app.py
```
to stop the app just CTRL+C