#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Tuple,Dict

def AES_enc_stream(attr,key):
    key = "Func('"+key+"')"
    return "HEX(AES_ENCRYPT('"+attr+"', "+key+"))"

def AES_dec_stream(attr,key):
    key = "Func('"+key+"')"
    return "AES_DECRYPT(UNHEX('"+attr+"'), "+key+")"

def AES_dec_stream_attr(attr_name, key):
    key = "Func('"+key+"')"
    
    # 需要将解密得到的值转换为字符串
    return "CAST(AES_DECRYPT(UNHEX("+attr_name+"), "+key+") as CHAR) as "+attr_name

# def Encrypt_attrs(table,attrs):
#     key = keys(table)

#     attrs = attrs.strip(' ').split(',')
#     for i in range(len(attrs)):
#         attrs[i] = AES_enc_stream(attrs[i],key[attrs[i]])

#     attr = ','.join(i for i in attrs)
#     return attr

def Decrypt_attrs(table,attrs):
    key = keys(table)

    attrs = attrs.strip(' ').split(',')
    for i in range(len(attrs)):
        attrs[i] = AES_dec_stream_attr(attrs[i],key[attrs[i]])

    attr = ','.join(i for i in attrs)
    return attr


def Encrypt(table,info:Dict):
    # get key
    key = keys(table)

    # get attr
    for attr in key.keys():
        if attr in info.keys():
            info[attr] = AES_enc_stream(str(info[attr]), key[attr])

    return info

def Decrypt(table,info:Dict):
    # get key
    key = keys(table)

    # get attr
    for attr in key.keys():
        if attr in info.keys():
            info[attr] = AES_dec_stream(str(info[attr]), key[attr])

    return info

def keys(table):
    keys = {}
    with open('../keys/'+table+'_key.txt','r') as f:    
        for pair in f.readlines():
            pair = pair.strip('\n')
            attr = pair.split(' ')[0]
            key = pair.split(' ')[1]
            keys[attr] = key
    return keys


# ["id","salt"]
def get_src(cursor,user,attrs:Tuple,key):
    enc = [_ for _ in range(len(attrs))]
    for i in range(len(attrs)):
        enc[i] = AES_dec_stream(attrs[i],key[attrs[i]])

    sql = "SELECT * FROM users where userid = '%s'"%user
    cursor.execute(sql)
    enc_dict = cursor.fetchall()[0]

    # generate sql
    sql = "SELECT "
    for i in range(len(attrs)):
        string = AES_dec_stream(enc_dict[attrs[i]],key[attrs[i]])
        sql += "%s as %s,"%(string,attrs[i])
    sql = sql.rstrip(',')

    # deal dict
    cursor.execute(sql)
    results = cursor.fetchall()[0]
    for i in results:
        results[i] = results[i].decode('utf-8')
    return results
