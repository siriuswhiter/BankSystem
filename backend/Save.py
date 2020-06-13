from Config import Configuration
from Trade import *

def SaveMoney(cardid,amount):
    db = Configuration()
    db.connect()

    if float(amount)<0:
        return False
        
    balance = str(float(db.select('cards','balance',{'cardid':cardid})[0]['balance']) + float(amount))
    
    if db.update('cards',{'balance': balance},{'cardid':cardid}):
        return newsave(cardid,amount)
    return False 
