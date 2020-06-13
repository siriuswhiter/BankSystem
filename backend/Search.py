from Config import Configuration
from Trade import *

def Searchinfo(re,info={}):
    db = Configuration()
    db.connect()

    table = 'cards join users using(userid)'
    info = db.select(table,re,info)

    cardtypedict = {}
    re = db.select('cardtypes','cardtype, cardname')
    for cardtype in re:
        cardtypedict[cardtype['cardtype']] = cardtype['cardname']


    willdel = []
    for r in range(len(info)):
        cardid = info[r]['cardid']
        if cardid=='0' or cardid=='1':
            willdel.append(r)
            continue
        info[r]['cardid'] = cardid[0:4]+'***'+cardid[-4:]

        info[r]['cardtype'] =  cardtypedict[info[r]['cardtype']]

    for i in range(len(willdel)-1,-1,-1):
        del info[willdel[i]]
        

    return info

    

def Searchtrade(re,info={}):
    db = Configuration()
    db.connect()

    table = 'trades'
    info = db.select(table,re,info)

    # 对显示的信息进行一些处理
    tradedict = {1:'存款',2:'取款',3:'贷款',4:'转账',5:'还贷'}
    for r in range(len(info)):
        if info[r]['srccard'] == '0' or info[r]['srccard'] == '1':
            info[r]['srccard'] = ''
        else:
            info[r]['srccard'] = info[r]['srccard'][0:4]+'***'+info[r]['srccard'][-4:]
        
        if info[r]['descard'] == '0' or info[r]['descard'] == '1':
            info[r]['descard'] = ''
        else:
            info[r]['descard'] = info[r]['descard'][0:4]+'***'+info[r]['descard'][-4:]
    
        info[r]['tradetype'] = tradedict[info[r]['tradetype']]
    return info

def Queryinfo(userid):
    db = Configuration()
    db.connect()   

    return db.select('cards natural join cardtypes','belong, cardname, cardid, balance, loan,over',{'userid':userid}) 