import requests
import sys
import time
import telegram_send
from twilio.rest import Client
from config import *
import datetime

p = len(PART)
n = len(number)
delay = datetime.datetime.now()

try:

    def check_iphone():
      sys.stdout.flush()
      sa = "Disponibile in:"
      ava = False
      noava = True
      iphnoava = "Attualmente Nessun:"
      global delay
      global store
      for c in range (p):
        url = "https://www.apple.com/it/shop/fulfillment-messages?pl=true&parts.0=" + PART[c] + "&location=" + ZIP
        #Do The Request to Apple Servers
        r = requests.get(url)
        # Get Number of near store
        try:
            sn = len(r.json()['body']['content']['pickupMessage']['stores'])
            if sn < store:
              store = sn
            print ("######################################")
            print ("Controllo In:")
            for j in range (store):
              print ("------------    " + r.json()['body']['content']['pickupMessage']['stores'][j]['storeName'] + "    ------------")
              ##Is the product (Apple Part) listed as "available" in that Apple Store
              available = r.json()['body']['content']['pickupMessage']['stores'][j]['partsAvailability'][PART[c]]['pickupDisplay']
              if available == "available":
                print ("AVAILABLE - " + r.json()['body']['content']['pickupMessage']['stores'][j]['partsAvailability'][PART[c]]['messageTypes']['regular']['storePickupProductTitle'] + " == " + r.json()['body']['content']['pickupMessage']['stores'][j]['storeName'])
                sa = (sa + "\n - " + r.json()['body']['content']['pickupMessage']['stores'][j]['partsAvailability'][PART[c]]['messageTypes']['regular']['storePickupProductTitle'] + " == " + r.json()['body']['content']['pickupMessage']['stores'][j]['storeName'])
                ava = True
                noava = False
              else:
                print ("NOT AVAILABLE - " + r.json()['body']['content']['pickupMessage']['stores'][j]['partsAvailability'][PART[c]]['messageTypes']['regular']['storePickupProductTitle'] + " == " + r.json()['body']['content']['pickupMessage']['stores'][j]['storeName'])
                noava = True
              print (" ")    
              
              if noava == True:
                iphnoava = (iphnoava + "\n - " + r.json()['body']['content']['pickupMessage']['stores'][j]['partsAvailability'][PART[c]]['messageTypes']['regular']['storePickupProductTitle'] + " == " + r.json()['body']['content']['pickupMessage']['stores'][j]['storeName'])
            print ("######################################")
        except KeyError as ke:
            print('########Errore!!! Codice Prodotto non corretto!!! Verifica Il Seguente Codice == ', PART[c])
            print(ke)
            print(r.json())
    
    
      print ("######################################")
      print ("--------------------------------------------------------------")
    
      if ava == True:
        print (sa)
        print (" ") 
        if use_telegram == True:
          telegram_send.send(messages=[sa])
          print ("Invio Notifica Telegram")
        if use_twilio == True:
          now = datetime.datetime.now()
          if datetime.datetime.now() > delay:
            delay = now + datetime.timedelta(minutes=smsdelay) # days, seconds, then other fields.
            client = Client(account_sid, auth_token)
            for d in range(n):
              print ("Invio SMS Twilio a: " + number[d])
            #Uncomment Here if you want SMS Message
            ###########################################
              message = client.messages.create(
                body=sa,
                to=number[d],
                from_=twilio_number
              )
              print ("Invio WhatsApp Twilio a: " + number[d])
            ###########################################
            #Uncomment Here if you want Whatsapp Message Need More Settings from twilio website
            ###########################################
            #  message = client.messages.create( 
            #    from_=twilio_wa_number,
            #    body=sa,
            #    to='whatsapp:' + number[d]
            #  )  
            ########################################### 
      #else:
      # print ("Attualmente nessun " + r.json()['body']['content']['pickupMessage']['stores'][j]['partsAvailability'][PART[c]]['messageTypes']['regular']['storePickupProductTitle'] + " disponibile nei nogozi scelti")
      
      if iphnoava != "Attualmente Nessun:":
        print (iphnoava + " \nDisponibile Per L'Acquisto" )
       
      print ("--------------------------------------------------------------")
    while not check_iphone():
      time.sleep(refresh)

except KeyboardInterrupt:
    print('\n Programma Terminato Correttamente')
