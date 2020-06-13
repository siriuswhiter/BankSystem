'''
@Author: Sirius Whiter
@Date: 2020-06-07 17:36:15
@LastEditors: Sirius Whiter
@LastEditTime: 2020-06-08 19:21:24
@Description: 
'''
import datetime
from Config import Configuration

def newsave(cardid,amount):
    db = Configuration()
    db.connect()
    trade = {}
    trade['tradetype'] = '1'
    trade['srccard'] = '1'
    trade['descard'] = cardid
    trade['amount'] = amount
    trade['tradedate'] = str(datetime.datetime.now())

    return db.insert('trades',trade)

def newwithdraw(cardid,amount):
    db = Configuration()
    db.connect()
    trade = {}

    trade['tradetype'] = '2'
    trade['srccard'] = '0'
    trade['descard'] = cardid
    trade['amount'] = amount
    trade['tradedate'] = str(datetime.datetime.now())
    
    return db.insert('trades',trade)

def newloan(cardid,amount):
    db = Configuration()
    db.connect()
    trade = {}
    trade['tradetype'] = '3'
    trade['srccard'] = '0'
    trade['descard'] = cardid
    trade['amount'] = amount
    trade['tradedate'] = str(datetime.datetime.now())
    return db.insert('trades',trade)


def newtrans(srccard,descard,amount):
    db = Configuration()
    db.connect()
    trade = {}
    trade['tradetype'] = '4'
    trade['srccard'] = srccard
    trade['descard'] = descard
    trade['amount'] = amount
    trade['tradedate'] = str(datetime.datetime.now())

    return db.insert('trades',trade)   

def newrepay(cardid,amount):
    db = Configuration()
    db.connect()
    trade = {}
    trade['tradetype'] = '5'
    trade['srccard'] = '1'
    trade['descard'] = cardid
    trade['amount'] = amount
    trade['tradedate'] = str(datetime.datetime.now())
    
    return db.insert('trades',trade)
