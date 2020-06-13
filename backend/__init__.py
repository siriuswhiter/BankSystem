'''
@Author: Sirius Whiter
@Date: 2020-05-13 17:46:29
@LastEditors: Sirius Whiter
@LastEditTime: 2020-06-09 10:25:59
@Description: 
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Config import Configuration
import random
import string
import os,stat
from typing import Tuple

def create_func_Func():
    query = '''
        CREATE FUNCTION Func(test VARCHAR(32))
        RETURNS VARCHAR(256)
        BEGIN
        declare newkey VARCHAR(256);
        select HEX(AES_ENCRYPT(test,MD5('bank'))) into newkey;
        RETURN newkey;
        END '''
    cursor.execute(query)


# userid 身份证号
def create_tb_user():
    query = '''
        CREATE TABLE  users(
        userid VARCHAR(18) NOT NULL,
        user VARCHAR(20) NOT NULL, 
        phone VARCHAR(20) NOT NULL, 
        addr VARCHAR(256) NOT NULL,

        credit INT NOT NULL,
        overlimit VARCHAR(20) NOT NULL,

        salt VARCHAR(256) NOT NULL,
        password VARCHAR(256) NOT NULL,

        PRIMARY KEY (userid));'''
    cursor.execute(query)


'''
tradetype: 
    1 - save
    2 - withdraw
    3 - loan
    4 - trans
    5 - repay

'''
def create_tb_trade():
    query = '''
        CREATE TABLE  trades(
        tradeid INT  NOT NULL AUTO_INCREMENT,
        tradetype INT NOT NULL, 
        srccard VARCHAR(18) NOT NULL, 
        descard VARCHAR(18) NOT NULL,
        amount VARCHAR(20) NOT NULL,
        tradedate VARCHAR(256) NOT NULL,
        
        PRIMARY KEY (tradeid),
        FOREIGN KEY (srccard) REFERENCES cards(cardid), 
        FOREIGN KEY (descard) REFERENCES cards(cardid));'''
    cursor.execute(query)

def create_tb_loans():
    query = '''
        CREATE TABLE  loans(
        loanid INT  NOT NULL AUTO_INCREMENT,
        cardid VARCHAR(18) NOT NULL,
        startdate VARCHAR(256) NOT NULL,
        enddate VARCHAR(256) NOT NULL,
        amount VARCHAR(20) NOT NULL,
        rate VARCHAR(10) NOT NULL,
        hasrepay BOOL NOT NULL,

        PRIMARY KEY (loanid),
        FOREIGN KEY (cardid) REFERENCES cards(cardid));'''
    cursor.execute(query)


def create_tb_card():
    query = '''
        CREATE TABLE cards(
        cardtype int NOT NULL,
        cardid VARCHAR(18) NOT NULL,
        userid VARCHAR(18) NOT NULL, 
        opendate VARCHAR(256) NOT NULL,
        balance VARCHAR(20) NOT NULL, 
        loan VARCHAR(20) NOT NULL,
        over VARCHAR(20) NOT NULL,
        loanlimit VARCHAR(20) NOT NULL,

        salt VARCHAR(256) NOT NULL,
        password VARCHAR(256) NOT NULL,

        PRIMARY KEY (cardid),
        FOREIGN KEY (userid) REFERENCES users,
        FOREIGN KEY (cardtype) REFERENCES cardtypes
        );'''
    cursor.execute(query)


def create_tb_cardtype():
    query = '''
        CREATE TABLE cardtypes(
            cardtype int  NOT NULL,
            cardname VARCHAR(32) NOT NULL,
            canover BOOL NOT NULL,
            belong VARCHAR(32) NOT NULL,
            PRIMARY KEY (cardtype)
        );
    '''
    cursor.execute(query)

def insert_cardtype_init():
    query = '''
        INSERT cardtypes VALUES ('0','招商银行一卡通','1','招商银行');
    '''
    cursor.execute(query)
    query = '''
        INSERT cardtypes VALUES ('1','工商银行牡丹卡','1','工商银行');
    '''
    cursor.execute(query)
    query = '''
        INSERT cardtypes VALUES ('2','邮政银行生肖卡','0','邮政银行');
    '''
    cursor.execute(query)


def insert_user_init():
    query = '''
        INSERT users VALUES ('0','0','0','0','0','0','0','0');
        '''
    cursor.execute(query)    
    query = '''
        INSERT users VALUES ('1','1','1','1','1','1','1','1');
        '''
    cursor.execute(query)    

def insert_card_init():
    query = '''
        INSERT cards VALUES ('0','0','0','0','0','0','0','0','0','0');
        '''
    cursor.execute(query)    
    query = '''
        INSERT cards VALUES ('1','1','1','1','1','1','1','1','1','1');
        '''
    cursor.execute(query)    


def create_tb():
    create_tb_user()
    create_tb_cardtype()
    create_tb_card()
    create_tb_trade()
    create_tb_loans()
    insert_cardtype_init()
    insert_user_init()
    insert_card_init()

def create_func():
    create_func_Func()

def gen_keys(table,attrs:Tuple):
    keys = {}
    if os.path.exists('../keys/'+table+'_key.txt'):
        os.remove('../keys/'+table+'_key.txt')
    
    f = open('../keys/'+table+'_key.txt','a')

    for attr in attrs:
        key_list = [random.choice(string.ascii_letters + string.digits) for _ in range(32)]
        key = ''.join(key_list)
        keys[attr] = attrs
        f.writelines(attr + ' '+ key + '\n')
    f.close()
    #os.chmod('../keys/'+table+'_key.txt',stat.S_IRUSR)
    return keys

def main():
    drop_all()
    create_tb()
    #create_func()
    #gen_keys('users',['user','phone','addr','credit','salt','password'])
    #gen_keys('cards',['balance','loan','salt','loanlimit','overlimit','opendate','password'])


def drop_all():
    query = 'drop table if exists users'
    cursor.execute(query)
    query = 'drop table if exists cards'
    cursor.execute(query)    
    query = 'drop table if exists loans'
    cursor.execute(query)
    query = 'drop table if exists cardtypes'
    cursor.execute(query)
    query = 'drop table if exists trades'
    cursor.execute(query)
    query = 'drop function if exists Func'
    cursor.execute(query)

cursor = Configuration().connect()
if __name__ == '__main__':
    main()
