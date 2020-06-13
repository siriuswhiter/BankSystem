#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
sys.path.append('../frontend')
sys.path.append('../backend')

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QTableWidgetItem,QHeaderView,QFrame
from PyQt5 import QtGui,QtCore,Qt
from CloseUI import Ui_Close
from Close_UI import Ui_Close_
from Config import Configuration
from Encrypt import Cryptor
from Close import *
from Login import *

class Close(QMainWindow, Ui_Close):
    def __init__(self, parent=None):
        super(Close, self).__init__(parent)
        self.setupUi(self)
        self.ConfirmButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.close)

    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Return:
    #         self.accept()


    def check(self,info):
        userid = info['userid']
        pwd = info['password']
        if userid != "" and pwd != "" and LoginUser(userid,pwd)==True:
            self.retEdit.setText("")
            return True
            # self.accept()
        else:
            self.retinfo("身份证号或密码出错")
            return False
            
    def accept(self):
        info = {}
        info['userid'] = self.ID_num.text()
        info['password'] = self.passEdit.text()

        db = Configuration()
        db.connect()
        if self.check(info)==True:
            self.next = Close_()
            self.next.userid = info['userid']
            self.next.show_table()
            self.next.show()
            self.close()
        else:
            self.retinfo("身份证号或密码错误")
        


    def retinfo(self,text):
        self.retEdit.setStyleSheet("color:red")
        self.retEdit.setText(text)


class Close_(QMainWindow, Ui_Close_):
    def __init__(self, parent=None):
        super(Close_, self).__init__(parent)
        self.setupUi(self)
        self.ConfirmButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.close)


    def show_table(self):
        db = Configuration()
        db.connect()
        self.re =  db.select('cards','cardtype, cardid',{'userid':self.userid})
        if self.re != ():
            re = self.re
            row = len(re)
            col = 3
            self.retTable.setColumnCount(col)
            self.retTable.setHorizontalHeaderLabels(['','类型','卡号'])
            self.retTable.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
            self.retTable.horizontalHeader().resizeSection(0,20)
            self.retTable.horizontalHeader().resizeSection(1,95)
            self.retTable.horizontalHeader().resizeSection(2,200)
            self.retTable.setRowCount(row)
            
            self.checkBoxs = []
            for r in range(row):
                checkBox = QTableWidgetItem()
                checkBox.setCheckState(QtCore.Qt.Unchecked)
                self.checkBoxs.append(checkBox)

                card_dict = [{'cardtype':'招商银行一卡通','loan':'0','over':'0'},{'cardtype':'工商银行牡丹卡','loan':'0','over':'1'},{'cardtype':'邮政银行生肖卡','loan':'1','over':'0'}]
                cardid = re[r]['cardid']
                cardtype = card_dict[re[r]['cardtype']]['cardtype']
                

                self.retTable.setItem(r,0,checkBox)
                self.retTable.setItem(r,1,QTableWidgetItem(cardtype))
                self.retTable.setItem(r,2,QTableWidgetItem(cardid))
        else:
            self.retinfo("抱歉，您的账户下没有银行卡，快去申请一张吧")




    def accept(self):
        for i in range(len(self.checkBoxs)):
            if self.checkBoxs[i].checkState()==QtCore.Qt.Checked:
                cardid = self.re[i]['cardid']
                if not CloseCard(cardid):
                    self.retinfo("注销失败")
        
        self.box = QMessageBox(QMessageBox.Information, "成功", "注销成功，点击OK或\n等待三秒后返回")
        self.box.setStandardButtons(QMessageBox.Ok)
        self.box.button(QMessageBox.Ok).animateClick(3*1000)
        self.box.exec_()
        self.close()

    def retinfo(self,text):
        self.retEdit.setStyleSheet("color:red")
        self.retEdit.setText(text)
