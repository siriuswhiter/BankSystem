#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from Crypto.Cipher import AES
# from binascii import b2a_hex, a2b_hex
import hashlib
import string
import random

class Cryptor:
    # 私有函数
    def __init__(self,encode_method = 0, encode_times = 1000):
        self.encode_method = encode_method
        self.encode_times = encode_times

    def __get_salt(self,length=32):
        salt_list = [random.choice(string.ascii_letters + string.digits) for _ in range(length)]
        salt = ''.join(salt_list)
        return salt

    def __salt_hash(self,text,salt= None):
        
        if salt is None:
            salt= self.__get_salt()

        text += salt
        
        if self.encode_method == 0:
            sha256 = hashlib.sha256()
            for i in range(self.encode_times):
                sha256.update(text.encode('utf-8'))
                text = sha256.hexdigest()
        else:
            sha512 = hashlib.sha512()
            for i in range(self.encode_times):
                sha512.update(text.encode('utf-8'))
                text = sha512.hexdigest()
        
        cipher = text
        return salt,cipher

    # # AES 模块
    # def __aes_enc(self, text):
    #     aes = AES.new(self.key)
    #     cipher = aes.encrypt(text.encode('utf-8'))
    #     # AES 192
    #     length = 24
    #     add = length - (len(text) % length)
    #     text += ('\0' * add)
    #     ciphertext = aes.encrypt(text)
    #     return b2a_hex(ciphertext)

    # def __aes_dec(self, ciphertext):
    #     cryptor = AES.new(self.key)
    #     text = cryptor.decrypt(a2b_hex(ciphertext))
    #     return text.rstrip('\0')


    # 暴露的外部公有函数

    def hash(self, text, salt=None):
        return self.__salt_hash(text,salt)
