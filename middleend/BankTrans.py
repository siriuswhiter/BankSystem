#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
sys.path.append('../frontend')

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from TransUI import Ui_Trans
from Trans import *

class Trans(QMainWindow, Ui_Trans):
    def __init__(self, parent=None):
        super(Trans, self).__init__(parent)
        self.setupUi(self)
        self.ConfirmButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.close)



    def accept(self):
        des_card = self.cardEdit.text()
        amount = self.amountEdit.text()
        try:
            if self.src_card != des_card and float(amount) >0 and TransMoney(self.src_card ,des_card,amount)==True:
                self.box = QMessageBox(QMessageBox.Information, "成功", "转账成功，点击OK或\n等待三秒后返回")
                self.box.setStandardButtons(QMessageBox.Ok)
                self.box.button(QMessageBox.Ok).animateClick(3*1000)
                self.box.exec_()
                self.close()
            else:
                self.retinfo("转账失败，卡号不存在或余额不足")
        except:
            pass

    def retinfo(self,text):
        self.retEdit.setStyleSheet("color:red")
        self.retEdit.setText(text)