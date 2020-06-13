#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
sys.path.append('../frontend')
sys.path.append('../backend')

import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore

from LoanUI import Ui_Loan
from Loan_UI import Ui_Loan_
from Loan import *

class Loan(QMainWindow, Ui_Loan):
    def __init__(self, parent=None):
        super(Loan, self).__init__(parent)
        self.setupUi(self)
        self.StartdateEdit.setMinimumDate(QtCore.QDate.currentDate())
        self.EnddateEdit.setMinimumDate(QtCore.QDate.currentDate())

        

        self.StartdateEdit.dateChanged.connect(self.calc)
        self.EnddateEdit.dateChanged.connect(self.calc)
        self.ConfirmButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.close)

    def setAmount(self):
        self.MaxAmount.setText(str(self.GetMaxAmount()))

    def GetMaxAmount(self):
        return GetMaxLoanAmountByID(self.cardid)

    def accept(self):
        self.next = Loan_()
        self.next.StartdateEdit.setDate(QtCore.QDate.fromString(self.StartdateEdit.text(),'yyyy-M-d'))
        self.next.EnddateEdit.setDate(QtCore.QDate.fromString(self.EnddateEdit.text(),'yyyy-M-d'))
        self.next.MaxAmount = self.MaxAmount.text()
        self.next.cardid = self.cardid
        self.next.show()
        self.close()

    def calc(self):
        startdate = self.StartdateEdit.text()
        enddate = self.EnddateEdit.text()
        lendrate = self.calc_rate(startdate, enddate)
        self.LendRate.setText(str(lendrate*100)+'%')
        
    def calc_rate(self, startdate, enddate):
        startdate = [int(i) for i in startdate.split('-')]
        enddate = [int(i) for i in enddate.split('-')]
        start = datetime.date(startdate[0], startdate[1],startdate[2])
        end = datetime.date(enddate[0], enddate[1],enddate[2])
        loanday = end.__sub__(start).days
        lendrate = 0
        if loanday <0:
            self.EnddateEdit.setDate(QtCore.QDate.fromString(self.StartdateEdit.text(),'yyyy-M-d'))
        elif loanday < 30:
            lendrate = 0.1
        elif loanday < 60:
            lendrate = 0.2
        else:
            lendrate = 0.3 
        return lendrate

    def retinfo(self,text):
        self.retEdit.setStyleSheet("color:red")
        self.retEdit.setText(text)


class Loan_(QMainWindow, Ui_Loan_):
    def __init__(self, parent=None):
        super(Loan_, self).__init__(parent)
        self.setupUi(self)
        
        self.amountEdit.textChanged.connect(self.compare)
        self.StartdateEdit.dateChanged.connect(self.calc)
        self.EnddateEdit.dateChanged.connect(self.calc)
        self.ConfirmButton.clicked.connect(self.accept)
        self.CancelButton.clicked.connect(self.close)


    def compare(self):
        if len(self.amountEdit.text())>=10 or (self.amountEdit.text()!="" and float(self.amountEdit.text())>float(self.MaxAmount)):
            self.amountEdit.setText(self.MaxAmount)

    
    def accept(self):
        amount = self.amountEdit.text()
        startdate = self.StartdateEdit.text()
        enddate = self.EnddateEdit.text()
        rate = Loan().calc_rate(startdate, enddate)
        try:
            if LoanMoney(self.cardid,amount,startdate,enddate,rate)==True:
                self.box = QMessageBox(QMessageBox.Information, "成功", "贷款成功，点击OK或\n等待三秒后返回")
                self.box.setStandardButtons(QMessageBox.Ok)
                self.box.button(QMessageBox.Ok).animateClick(3*1000)
                self.box.exec_()
                self.close()
            else:
                self.retinfo("贷款失败")
        except:
            pass
        pass

    def calc(self):
        startdate = self.StartdateEdit.text()
        enddate = self.EnddateEdit.text()
        lendrate = self.calc_rate(startdate, enddate)
        
    def calc_rate(self, startdate, enddate):
        startdate = [int(i) for i in startdate.split('-')]
        enddate = [int(i) for i in enddate.split('-')]
        start = datetime.date(startdate[0], startdate[1],startdate[2])
        end = datetime.date(enddate[0], enddate[1],enddate[2])
        Loan_day = end.__sub__(start).days
        lendrate = 0
        if Loan_day <0:
            self.EnddateEdit.setDate(QtCore.QDate.fromString(self.StartdateEdit.text(),'yyyy-M-d'))
        elif Loan_day < 30:
            lendrate = 0.1
        elif Loan_day < 60:
            lendrate = 0.2
        else:
            lendrate = 0.3 
        return lendrate

    def retinfo(self,text):
        self.retEdit.setStyleSheet("color:red")
        self.retEdit.setText(text)

