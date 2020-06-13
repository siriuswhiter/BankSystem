from Config import Configuration
from Encrypt import Cryptor
import datetime

def new_user(info):
    db = Configuration()
    cursor = db.connect()
    
    crypt = Cryptor()
    password = info['password']
    salt , password = crypt.hash(password)

    info['credit'] = 100
    info['overlimit'] = 100
    info['salt'] = salt
    info['password'] = password
    if db.insert('users',info)==True:
        return True
    return False

def has_over(userid):
    db = Configuration()
    cursor = db.connect()

    re = db.select('cards','sum(over) as overall',{'userid':userid})
    if re:
        amount = re[0]['overall']
        if float(amount)>0:
            print(float(amount))
            db.close()
            return True
    db.close()
    return False

def new_card(card):
    db = Configuration()
    cursor = db.connect()
    
    crypt = Cryptor()
    password = card['password']
    salt , password = crypt.hash(password)

    card['loan'] = 0
    card['over'] = 0
    card['loanlimit'] = 1000
    card['opendate'] = str(datetime.datetime.now())
    card['salt'] = salt
    card['password'] = password
    if db.insert('cards',card)==True:
        return True
    return False