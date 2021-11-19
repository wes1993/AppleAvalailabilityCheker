# AppleAvalailabilityCheker
Check if Apple devices are in stock and send a notification
1. You need to check the config.py file and fill the required information in that file
2. You have 2 ways for receive the notification
 2.1 Telegram using telegram_send:
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
 2.2 Twilio:
 ```
 Go to twilio website for your account details information
 ```
