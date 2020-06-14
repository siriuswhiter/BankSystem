#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Encrypt import Cryptor
from Config import Configuration

# from database import *
import pymysql
import traceback

def LoginCard(type,card,pwd):
    db = Configuration()
    db.connect()

    re = db.select('cards','salt, password',{'cardtype':type,'cardid':card})
    if re != None:
        crypt = Cryptor()
        _, password = crypt.hash(re[0]['salt'], re[0]['password'])
        if(password == pwd):
            db.close()
            return True
    db.close()
    return False

    # return True

def LoginUser(userid, pwd):
    # return True
    db = Configuration()
    db.connect()

    re = db.select('users','salt, password',{'userid':userid})
    if re != None:
        crypt = Cryptor()
        _, password = crypt.hash(pwd,re[0]['salt'])
        if(password == re[0]['password']):
            db.close()
            return True
    db.close()
    return False
