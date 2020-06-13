'''
@Author: Sirius Whiter
@Date: 2020-06-08 19:44:39
@LastEditors: Sirius Whiter
@LastEditTime: 2020-06-12 14:18:30
@Description: 
'''
from Config import Configuration
from Trade import *
import datetime


def RepayMoney(loanid):
    db = Configuration()
    db.connect()

    info = db.select('loans join cards using(cardid)','balance,loan,over,amount,enddate, rate,cardid,userid',{'loanid':loanid})

    if info:
        info = info[0]
        amount = float(info['amount'])
        balance = float(info['balance'])
        loan = float(info['loan'])
        over = float(info['over'])
        rate = float(info['rate'])
        cardid = info['cardid']
        userid = info['userid']

        if balance<amount*(1+rate):
            return False
        else:
            newbalance = balance-amount*(1+rate)
            # 加个逾期处理

            enddate = info['enddate']
            nowdate  = str(datetime.datetime.now()).split(' ')[0]

            nowdate = [int(i) for i in nowdate.split('-')]
            enddate = [int(i) for i in enddate.split('-')]
            start = datetime.date(nowdate[0], nowdate[1],nowdate[2])
            end = datetime.date(enddate[0], enddate[1],enddate[2])
            day = end.__sub__(start).days
            
            if day>0:
                # 逾期多赔每天0.1的利率按日结
                newbalance = balance-amount*(1+rate)-amount*day*(0.1+rate)
                # 同时信用值变为最低50
                db.update('users',{'credit':'50'},{'userid':userid})


            # 计算还完的新余额为0则还贷失败
            if newbalance<0:
                return False

            # rate为0时还的是透支的钱
            if rate!=0:
                newloan = loan-amount
                if not db.update('cards',{'loan':newloan,'balance':newbalance},{'cardid':cardid}):
                    return False
            else:
                newover = over-amount
                if not db.update('cards',{'over':newover,'balance':newbalance},{'cardid':cardid}):
                    return False
            
            if db.update('loans',{'hasrepay':'1'},{'loanid':loanid}):
                db.close()
                return newrepay(cardid,amount)