from Config import Configuration
from Trade import *
import datetime

def WithdrawMoney(cardid,amount):
    db = Configuration()
    db.connect()

    re = db.select('cards join users using(userid)','balance, cardtype, overlimit, over',{'cardid':cardid})

    if re==None:
        return False
    re = re[0]
    balance = float(re['balance'])
    cardtype = re['cardtype']
    # 判断额度之类的操作
    amount = float(amount)


    if balance>=amount:
        newbalance = str(balance - amount)
        if db.update('cards',{'balance':newbalance},{'cardid':cardid}):
            return newwithdraw(cardid,amount)
        return False 

    elif cardtype==0 or cardtype==1:
        leftover = float(re['overlimit']) - float(re['over'])
        print(leftover,balance,amount)
        if leftover+balance<amount:
            return False
        else:
            newover = float(re['over']) + (amount - balance) 
            newbalance = '0'
            newamount = amount - balance
            startdate = datetime.date.today()
            enddate = startdate + datetime.timedelta(days=7)

            startdate = startdate.isoformat()
            enddate = enddate.isoformat()


            # 透支等同于无利率贷款，限时7天，还贷时通过利率区分。
            re = db.update('cards',{'balance':newbalance,'over':newover},{'cardid':cardid})
            if re and db.insert('loans',{'cardid':cardid,'startdate':startdate,'enddate':enddate,'amount':newamount,'rate':'0','hasrepay':'0'}):
                return newwithdraw(cardid,amount)
            return False
    else:
        return False