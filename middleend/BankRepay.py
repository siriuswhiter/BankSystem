#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
sys.path.append('../frontend')
sys.path.append('../backend')


from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QTableWidgetItem,QHeaderView,QFrame
from PyQt5 import QtGui,QtCore,Qt
from RepayUI import Ui_Repay
from Config import *
from Repay import *

class Repay(QMainWindow, Ui_Repay):
    def __init__(self, parent=None):
        super(Repay, self).__init__(parent)
        self.setupUi(self)
        self.ConfirmButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.close)

    def showLoan(self):
        db = Configuration()
        db.connect()
        self.re =  db.select('loans','loanid, amount, startdate, enddate',{'cardid':self.cardid, 'hasrepay':'0'})
        if self.re != ():
            re = self.re
            row = len(re)
            col = 5
            self.retTable.setRowCount(row)
            self.retTable.setColumnCount(col)
            self.retTable.setHorizontalHeaderLabels(['','贷款号','贷款','开始日期','结束日期'])
            self.retTable.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
            self.retTable.horizontalHeader().resizeSection(0,20)
            self.retTable.horizontalHeader().resizeSection(1,50)
            self.retTable.horizontalHeader().resizeSection(2,65)
            self.retTable.horizontalHeader().resizeSection(3,100)
            self.retTable.horizontalHeader().resizeSection(4,100)

            
            
            self.checkBoxs = []
            for r in range(row):
                checkBox = QTableWidgetItem()
                checkBox.setCheckState(QtCore.Qt.Unchecked)
                self.checkBoxs.append(checkBox)

                loanid = str(re[r]['loanid'])
                amount = re[r]['amount']
                startdate = re[r]['startdate']
                enddate = re[r]['enddate']

                self.retTable.setItem(r,0,checkBox)
                self.retTable.setItem(r,1,QTableWidgetItem(loanid))
                self.retTable.setItem(r,2,QTableWidgetItem(amount))
                self.retTable.setItem(r,3,QTableWidgetItem(startdate))
                self.retTable.setItem(r,4,QTableWidgetItem(enddate))
        else:
            self.retinfo("您没有贷款哦")        

    def accept(self):
        for i in range(len(self.checkBoxs)):
            if self.checkBoxs[i].checkState()==QtCore.Qt.Checked:
                loanid = self.re[i]['loanid']
                if not RepayMoney(loanid):
                    self.retinfo("还贷失败，余额不足哦")
                    return
        
        self.box = QMessageBox(QMessageBox.Information, "成功", "还贷成功，点击OK或\n等待三秒后返回")
        self.box.setStandardButtons(QMessageBox.Ok)
        self.box.button(QMessageBox.Ok).animateClick(3*1000)
        self.box.exec_()
        self.close()

    def retinfo(self,text):
        self.retEdit.setStyleSheet("color:red")
        self.retEdit.setText(text)
