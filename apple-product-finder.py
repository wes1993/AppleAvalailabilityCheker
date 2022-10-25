import requests
import sys
try:

    model = input("Enter iPhone Model all without space (Ex. iphone13pro) : ")
    
    sys.stdout.flush()
    url = "https://www.apple.com/it/shop/product-locator-meta?family=" + model
    #Do The Request to Apple Servers
    r = requests.get(url)
    # Get Number of near store
    sn = len(r.json()['body']['productLocatorOverlayData']['productLocatorMeta']['products'])
    for j in range (sn):
      print (r.json()['body']['productLocatorOverlayData']['productLocatorMeta']['products'][j]['productTitle'] + " - " + r.json()['body']['productLocatorOverlayData']['productLocatorMeta']['products'][j]['partNumber'])

except KeyError as ke:
    print('########Errore!!! Prodotto Inserito non corretto!!! Verifica il modello == ', model)
    print(ke)
    print(r.json())

except KeyboardInterrupt:
    print('\n Programma Terminato Correttamente')
