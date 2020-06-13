#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import traceback
from typing import Dict
from Database import *


class Configuration:
    def __init__(self):
        self.myconfig ={
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'passwd': '123456',
            'db': 'bank',
            'cursorclass':pymysql.cursors.DictCursor
        }


    def connect(self):
        self.conn = pymysql.connect(**self.myconfig)
        self.conn.autocommit(1)
        self.cursor = self.conn.cursor()
        return self.cursor

    def no_autocommit(self):
        self.conn.autocommit(0)

    def commit(self):
        self.conn.commit()

        
    def autocommit(self):
        self.conn.autocommit(1)

    # insert into table values info
    def insert(self,table, info:Dict):
        #info = Encrypt(table, info)
        schema = ', '.join(str(x) for x in info.keys())
        value = '\', \''.join(str(x) for x in info.values())
        value = '\''+value+'\''
        # insert
        sql = "INSERT INTO %s(%s) VALUES (%s)" % (table,schema,value)
        try:
            print(sql)
            self.cursor.execute(sql)
            return True
        except:
            traceback.print_exc()
            return False

    # delete from table where restrict
    def delete(self, table,restrict:Dict):
        sche = []
        for (schema,value) in restrict.items():
            sche.append(schema + '=\'' + value +'\'')
        sche = ' and '.join(x for x in sche)

        sql = 'DELETE FROM %s WHERE %s' % (table,sche)
        try:
            #print(sql)
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except:
            traceback.print_exc()
            return False

    # update table set info where restrict
    def update(self,table,info:Dict,restrict:Dict):
        #info = Encrypt(table, info)
        #restrict = Encrypt(table,restrict)

        sche = []
        for (schema,value) in restrict.items():  
            value = str(value)
            sche.append(schema + ' = \'' + value +'\'')
        sche = ' and '.join(x for x in sche)

        info_ = []
        for (schema,value) in info.items():  
            value = str(value)
            info_.append(schema + ' = ' + value)
        info_ = ' , '.join(x for x in info_)

        sql = "UPDATE %s SET %s WHERE %s"%(table,info_,sche)
        try:
            print(sql)
            self.cursor.execute(sql)
            return True
        except:
            traceback.print_exc()
            return False
            
    
    # select info from table where restrict
    def select(self,table,info,restrict={}):
        #info = Encrypt(table,)Decrypt_attrs(table,info)
        
        if restrict:
            sche = []
            for (schema,value) in restrict.items():
                value = str(value)
                if '%' in value:
                    sche.append(schema + ' like \'' + value +'\'')
                else:
                    sche.append(schema + ' = \'' + value +'\'')

            sche = ' and '.join(x for x in sche)
            sql = "SELECT %s FROM %s WHERE %s" % (info,table,sche)
        else:
            sql = "SELECT %s FROM %s"%(info,table)
        try:
            print(sql)
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except:
            traceback.print_exc()
            return False

    def close(self):
        self.conn.close()
    
    def rollback(self):
        self.conn.rollback()

    