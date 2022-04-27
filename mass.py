import requests
import json
import pywaves as pw


transBase = {}

privKey = "your private key here"
assetToSend = "asset ID"
yourDescription = "Your description to attach"
totalReceiver = 0

l = requests.get("https://api.wavesplatform.com/v0/transactions/exchange?sort=desc&limit=100").content


k = json.loads(l)
wTime = int(pw.lastblock()["timestamp"])


num = 0
adres = pw.Address(privateKey=privKey)


def transfer(massArray):
    adres.massTransferAssets(massArray, pw.Asset(assetToSend), yourDescription)

def getExchangeBuyers():
    massTrans = []
    buyArray = []

    eksilt = 0

    while len(buyArray) < totalReceiver:

        try:

            tme = wTime - eksilt
        
            l = requests.get("https://api.wavesplatform.com/v0/transactions/exchange?timeStart=" + str(tme) + "&sort=asc&limit=100").content

            

            k = json.loads(l)
            for transaction in k["data"]:
                buyer = transaction["data"]["order1"]["sender"]

                if buyer in buyArray:
                    pass
                    
                else:
                    #limit to 1000
                    if len(buyArray)<1000:
                        buyArray.append(buyer)
                        transBase["recipient"] = buyer
                        transBase["amount"] = 1
                        massTrans.append(transBase.copy())
                        #send to every 100 new receivers
                        if "00" in str(len(buyArray)):
                            print(massTrans)
                            transfer(massTrans)
                            print("\n\n")
                            massTrans = []

            eksilt = eksilt + 100000

        except Exception as e:
            print(e)
    print("thats all folks")
    #if you want to send a little donation to me:
    #adres.sendWaves("niyo", 1000000)

getExchangeBuyers()

