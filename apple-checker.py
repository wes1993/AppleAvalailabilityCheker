import requests
import sys
import time
from twilio.rest import Client

#Insert Variables HERE 

account_sid = ""
auth_token = ""
PART = ["MLL73QL/A", "MLQF3QL/A"] # Insert Part Number or List Here (EX <["MLL73QL/A", "MLQF3QL/A"]>) you'll have to do some sleuthing on apple.com "check availability" network requests to figure out what to look for, example MLQF3QL/A
ZIP = "00118" #Insert Zip Code or City here
number = ["Number1", "Number2"] #Insert Number List
p = len(PART)
n = len(number)

def check_iphone():
  sys.stdout.flush()
  sa = "Disponibile in:"
  ava = False
  for c in range (p):
    url = "https://www.apple.com/it/shop/fulfillment-messages?pl=true&parts.0=" + PART[c] + "&location=" + ZIP
    #Do The Request to Apple Servers
    r = requests.get(url)
    # Get Number of near store
    sn = len(r.json()['body']['content']['pickupMessage']['stores'])
    for j in range (sn):
      ##Is the product (Apple Part) listed as "available" in that Apple Store
      available = r.json()['body']['content']['pickupMessage']['stores'][j]['partsAvailability'][PART[c]]['pickupDisplay']
      if available == "available":
        print ("AVAILABLE - " + r.json()['body']['content']['pickupMessage']['stores'][j]['partsAvailability'][PART[c]]['storePickupProductTitle'] + "==" + r.json()['body']['content']['pickupMessage']['stores'][j]['storeName'])
        sa = (sa + " - " + r.json()['body']['content']['pickupMessage']['stores'][j]['partsAvailability'][PART[c]]['storePickupProductTitle'] + "==" + r.json()['body']['content']['pickupMessage']['stores'][j]['storeName'])
        ava = True
      else:
        print ("NOT AVAILABLE - " + r.json()['body']['content']['pickupMessage']['stores'][j]['partsAvailability'][PART[c]]['storePickupProductTitle'] + "==" + r.json()['body']['content']['pickupMessage']['stores'][j]['storeName'])
    
    if ava == True:
      client = Client(account_sid, auth_token)
      print (sa)
      for d in range(n):
        message = client.messages.create(
          body=sa,
          to=number[d],
          from_=""
        )
      time.sleep(1800)
      return False


while not check_iphone():
  time.sleep(30)