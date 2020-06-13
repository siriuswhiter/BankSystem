#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
sys.path.append('../frontend')
sys.path.append('../backend')
import string
import random
import time

from PyQt5.QtWidgets import *
from PyQt5 import Qt
from PyQt5.QtGui import QIntValidator,QRegExpValidator
from OpenUI import Ui_Open
from Open_UI import Ui_Open_
from Config import Configuration
from Encrypt import Cryptor
from Register import *

class Open(QMainWindow, Ui_Open):
    def __init__(self, parent=None):
        super(Open, self).__init__(parent)
        self.setupUi(self)

        self.isExisting = 0
        self.ID_num.editingFinished.connect(self.find)
        self.passEdit.editingFinished.connect(self.find)
        self.ConfirmButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.close)

    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Return:
    #         self.accept()

    def find(self):
        db = Configuration()
        cursor = db.connect()
        ID_num = self.ID_num.text()
        password = self.passEdit.text()

        if ID_num != '' and password != '':
            re = db.select('users','user,phone,addr,salt,password',{'userid':ID_num})
            if  re != ():
                re = re[0]
                crypt = Cryptor()
                _, password = crypt.hash(password,re['salt'])
                if password==re['password']:
                    user = re['user']
                    phone = re['phone']
                    addr = re['addr']
                    self.nameEdit.setText(user)
                    self.phoneEdit.setText(phone)
                    self.addrEdit.setText(addr)
                    self.nameEdit.setReadOnly(True)
                    self.phoneEdit.setReadOnly(True)
                    self.addrEdit.setReadOnly(True)
                    self.isExisting = 1


    def check(self,info):
        if info['userid'] == '' or info['user'] == '' or info['phone'] == '' or info['addr'] == '' or info['password']=='':
            return False
        return True

    def accept(self):
        if not self.isExisting:
            info = {}
            info['userid'] = self.ID_num.text()
            info['user'] = self.nameEdit.text()
            info['phone'] = self.phoneEdit.text()
            info['addr'] = self.addrEdit.text()
            info['password'] = self.passEdit.text()

            
            if self.check(info) == True and not has_over(info['userid']) and new_user(info)==True:
                self.next = Open_()
                self.next.userid = info['userid']
                self.next.show()
                self.close()
            else:
                self.retinfo("出错啦")
        else:
            self.next = Open_()
            self.next.userid = self.ID_num.text()
            self.next.show()
            self.close()

    def retinfo(self,text):
        self.retEdit.setStyleSheet("color:red")
        self.retEdit.setText(text)


class Open_(QMainWindow, Ui_Open_):
    def __init__(self, parent=None):
        super(Open_, self).__init__(parent)
        self.setupUi(self)
        self.newcard()
        self.cardType.currentIndexChanged.connect(self.newcard)
        self.amountEdit.editingFinished.connect(self.compare)

        #self.amountEdit.setValidator(QIntValidator(10,100000000))
        self.ConfirmButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.close)



    def newcard(self):
        cardid = '620'+str(self.cardType.currentIndex())+''.join([random.choice(string.digits) for _ in range(14)])
        #self.cardId.setFontSize(14)
        self.cardId.setText(cardid)

    def compare(self):
        if self.amountEdit.text()!='' and float(self.amountEdit.text()) < 10:
            self.amountEdit.setText('10')

    def check(self,card):
        if card['cardid'] == '' or card['balance'] == '' or card['password'] =='':
            return False
        return True

    def accept(self):
        password = self.passEdit.text()
        confirm_password = self.confirmpassEdit.text()
    
        if password!= confirm_password:
            self.retinfo('密码不一致')
        card = {}
        card['cardtype'] = self.cardType.currentIndex()
        card['cardid'] = self.cardId.text()
        card['balance'] = self.amountEdit.text()
        card['password'] = password
        card['userid'] = self.userid

        if self.check(card)==True and new_card(card)==True:
            self.box = QMessageBox(QMessageBox.Information, "成功", "申请成功，点击OK或\n等待三秒后返回")
            self.box.setStandardButtons(QMessageBox.Ok)
            self.box.button(QMessageBox.Ok).animateClick(3*1000)
            self.box.exec_()
            self.close()
        else:
            self.retinfo("申请失败")
            

    def retinfo(self,text):
        self.retEdit.setStyleSheet("color:red")
        self.retEdit.setText(text)
