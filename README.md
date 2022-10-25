# AppleAvalailabilityCheker
Check if Apple devices are in stock and send a notification
1. You need to check the config.py file and fill the required information in that file
2. You have 2 ways for receive the notification Telegram and/or Twilio
3. Telegram using telegram_send:
```
Step 1: Speak with “the BotFather”:
Click this link and it will open your telegram client* and start a chat with the BotFather.
Send the message “/newbot” (no quotes) and follow the instructions.
*you’ll need to sign up for an account if you don’t already have one

Step 2: Install telegram-send and link it to your bot:
To install, open a terminal and run pip install telegram-send followed by telegram-send configure
telegram-send will ask for the token you got from the botfather, and then give you a password that you need to message to your new bot on Telegram.
Send the token you got from the botfather and telegram-send will reply with a 5-digit password you need to send to your new bot.
Forwarding the password to my new bot

Step 3: Send a test message from your python code
import telegram_send
telegram_send.send(messages=["Wow that was easy!"])
 ```
3.2 Twilio:
```
Go to twilio website for your account details information
```
# Useful Info
## JSON Endpoint + URL Request for apple-product-finder.py
```
model = Apple Product Model
j = Number of Product Found (Ex. 10 iphone13 model (differs from GB and Color))
URL Request: "https://www.apple.com/it/shop/product-locator-meta?family=" + model
Part Name:   ['body']['productLocatorOverlayData']['productLocatorMeta']['products'][j]['productTitle']
Part Number: ['body']['productLocatorOverlayData']['productLocatorMeta']['products'][j]['partNumber']
```
### Sample Output
```
Enter iPhone Model all without space (Ex. iphone13pro) : iphone13mini
iPhone 13 mini 128GB rosa - MLK23QL/A
iPhone 13 mini 128GB (PRODUCT)RED - MLK33QL/A
iPhone 13 mini 128GB galassia - MLK13QL/A
iPhone 13 mini 512GB rosa - MLKD3QL/A
iPhone 13 mini 256GB galassia - MLK63QL/A
iPhone 13 mini 256GB rosa - MLK73QL/A
iPhone 13 mini 512GB (PRODUCT)RED - MLKE3QL/A
iPhone 13 mini 256GB blu - MLK93QL/A
iPhone 13 mini 256GB (PRODUCT)RED - MLK83QL/A
iPhone 13 mini 256GB mezzanotte - MLK53QL/A
iPhone 13 mini 512GB blu - MLKF3QL/A
iPhone 13 mini 512GB galassia - MLKC3QL/A
iPhone 13 mini 512GB mezzanotte - MLKA3QL/A
iPhone 13 mini 128GB mezzanotte - MLK03QL/A
iPhone 13 mini 128GB blu - MLK43QL/A
........
```

## JSON Endpoint + URL Request for apple-checker.py
```
PART[c] = Number of model/s found with apple-product-finder.py
j = Number of Apple Store Found (Ex. 5 Apple Store Near)
c = Number of Product to check (If there are more than one in the config)
URL Request: "https://www.apple.com/it/shop/fulfillment-messages?pl=true&parts.0=" + PART[c] + "&location=" + ZIP
Apple Stores: ['body']['content']['pickupMessage']['stores']
Store Name: ['body']['content']['pickupMessage']['stores'][j]['storeName']
Available:  ['body']['content']['pickupMessage']['stores'][j]['partsAvailability'][PART[c]]['pickupDisplay']
Model Name: ['body']['content']['pickupMessage']['stores'][j]['partsAvailability'][PART[c]]['storePickupProductTitle']
```
### Sample Output 2 Stores One Product
```
######################################
Controllo In:
------------    Via del Corso    ------------
NOT AVAILABLE - iPhone 14 Pro 128GB nero siderale == Via del Corso
 
------------    Porta di Roma    ------------
NOT AVAILABLE - iPhone 14 Pro 128GB nero siderale == Porta di Roma
 
######################################
######################################
--------------------------------------------------------------
Attualmente Nessun:
 - iPhone 14 Pro 128GB nero siderale == Via del Corso
 - iPhone 14 Pro 128GB nero siderale == Porta di Roma 
Disponibile Per L'Acquisto
--------------------------------------------------------------
```

