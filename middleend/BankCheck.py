#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
sys.path.append('../frontend')
sys.path.append('../backend')

import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import *
from CheckUI import Ui_Check
from Check_UI import Ui_Check_
from BankSave import Save
from BankWithdraw import Withdraw
from BankLoan import Loan
from BankTrans import Trans
from BankRepay import Repay
from BankQuery import Query
from Login import *


class Check(QMainWindow, Ui_Check):
    def __init__(self, parent=None):
        super(Check, self).__init__(parent)
        self.setupUi(self)
        self.LoginButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.close)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.accept()

    def accept(self):
        type = self.cardType.currentIndex()
        card = self.cardEdit.text()
        pwd = self.passEdit.text()
        self.passEdit.setText("")
        try:
            if self.check_card(card) and LoginCard(type,card,pwd)==True:
                self.retEdit.setText("")
                self.change()
            else:
                self.retinfo("卡号或密码出错")
        except:
            pass

    def check_card(self,card):
        reg = "620\d{1}"
        if re.match(reg,card)!=None:
            return True
        return False
        
    
    def change(self):
        if self.option == 1:
            self.next = Save()
            self.next.ID_num.setText(self.cardEdit.text())
            
        elif self.option == 2:
            self.next = Withdraw()
            self.next.ID_num.setText(self.cardEdit.text())

        elif self.option == 3:
            self.next = Loan()
            self.next.cardid = self.cardEdit.text()
            self.next.setAmount()

        elif self.option == 4:
            self.next = Trans()
            self.next.src_card = self.cardEdit.text()
            
        elif self.option == 5:
            self.next = Repay()
            self.next.cardid = self.cardEdit.text()
            self.next.showLoan()
            

        self.next.show()
        self.close()

    def retinfo(self,text):
        self.retEdit.setStyleSheet("color:red")
        self.retEdit.setText(text)

    # def closeEvent(self,event):
    #     self.box = QMessageBox(QMessageBox.Warning, "警告", "确认退出？")
    #     yes = self.box.addButton(self.tr("确定"), QMessageBox.YesRole)
    #     no = self.box.addButton(self.tr("取消"), QMessageBox.NoRole)
    #     self.box.exec_()
    #     if self.box.clickedButton() ==yes:
    #         event.accept()
    #     else:
    #         event.ignore()  


class Check_(QMainWindow, Ui_Check_):
    def __init__(self, parent=None):
        super(Check_, self).__init__(parent)
        self.setupUi(self)
        self.LoginButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.close)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.accept()

    def accept(self):
        userid = self.nameEdit.text()
        pwd = self.passEdit.text()
        self.passEdit.setText("")
        try:
            if userid != "" and pwd != "" and LoginUser(userid,pwd)==True:
                self.retEdit.setText("")
                self.change()
            else:
                self.retinfo("身份证号或密码出错")
        except:
            pass

    
    def change(self):
        self.next = Query()
        self.next.user = self.nameEdit.text()
        self.next.showInfo()
        self.next.show()
        self.close()

    def retinfo(self,text):
        self.retEdit.setStyleSheet("color:red")
        self.retEdit.setText(text)


