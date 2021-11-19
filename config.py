#Settings for tracking Devices ad ZIP code for zone
# Insert Part Number or List Here (EX <["MLL73QL/A", "MLQF3QL/A"]>) you'll have to do some sleuthing on apple.com "check availability" network requests to figure out what to look for, example MLQF3QL/A
# Alternatively try the apple-product-finder.py but is a WIP
PART = ["MLL73QL/A", "MLQF3QL/A"]
#Insert Zip Code or City here
ZIP = "00118"
#Chose how many store want to check, See the first run to know the order based by ZIP and chose the value
store = 10
#Delay before new check (Seconds)
refresh = 30

#Twilio Settings
use_twilio = False
#Twilio Account Details
account_sid = ""
auth_token = ""
twilio_number = ""
twilio_wa_number = 'whatsapp:<insert number twilio with prefix ex +1number>'
#Insert Number List
number = ["<insert number 1 with prefix ex +1number>", "<insert number 2 with prefix ex +1number>"] 
#Insert Delay between SMS (Not applied to Telegram)
smsdelay = 15

#Telegram Settings
use_telegram = True
