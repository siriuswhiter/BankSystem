#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
sys.path.append('../frontend')
sys.path.append('../backend')
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from SaveUI import Ui_Save
from Save import *


class Save(QMainWindow, Ui_Save):
    def __init__(self, parent=None):
        super(Save, self).__init__(parent)
        self.setupUi(self)
        self.ConfirmButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.close)

    def accept(self):
        id_num = self.ID_num.text()
        amount = self.amountEdit.text()
        try:
            print(id_num,amount)
            if SaveMoney(id_num,amount)==True:
                self.box = QMessageBox(QMessageBox.Information, "成功", "存款成功，点击OK或\n等待三秒后返回")
                self.box.setStandardButtons(QMessageBox.Ok)
                self.box.button(QMessageBox.Ok).animateClick(3*1000)
                self.box.exec_()
                self.close()
            else:
                self.retinfo("存款失败")
        except:
            pass

    def retinfo(self,text):
        self.retEdit.setStyleSheet("color:red")
        self.retEdit.setText(text)
