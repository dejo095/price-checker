# price-checker

## Small python app that checks webshops for a price drop and send email in that case

For this to work you need to have python installed. <br>

You also need PIP pre instaled <br>
Using PIP you need to install:
``` 
pip install requests bs4
```
You also need to have Gmail 2Fa enabled and setup Gmail app password, then use this generated password for
```
emailPass = '' # Gmail app password
```

to run the app, just type:
```
python app.py
```
to stop the app just CTRL+C