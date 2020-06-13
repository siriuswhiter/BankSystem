from Config import Configuration
from Trade import *


def TransMoney(src_cardid,des_cardid,amount):
    db = Configuration()
    db.connect()

    # 看对方卡号在不在
    
    des = db.select('cards','cardtype',{'cardid':des_cardid})
    if(des==None):
        return False
    des = des[0]

    # 看余额够不够
    src = db.select('cards','cardtype, balance',{'cardid':src_cardid})
    src = src[0]

    # 判断转账费用    
    balance = float(src['balance'])
    amount = float(amount)
    
    if src['cardtype']==des['cardtype']:
        scale = 0.02
    else:
        scale = 0.05

    re_amount = balance*(1+scale)
    if re_amount > amount:
        return False

    # 转账，这一步要做断电处理

    src_newbalance = str(balance-re_amount)
    des_newbalance = str(float(db.select('cards','balance',{'cardid':des_cardid})[0]['balance'])+amount)

    db.no_autocommit()
    try:
        if(db.update('cards', {'balance':src_newbalance}, {'cardid':src_cardid}) and 
        db.update('cards', {'balance':des_newbalance},{'cardid':des_cardid})):
            newtrans(src_cardid,des_cardid,amount)
        db.commit()
        return True
    except:
        db.rollback()

    db.autocommit()
    db.close()
    return False
    
    
