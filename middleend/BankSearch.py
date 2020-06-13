#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
sys.path.append('../frontend')
sys.path.append('../backend')

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QHeaderView, QTableWidgetItem
from SearchUI import Ui_Search
from Search import *

class Search(QMainWindow, Ui_Search):
    def __init__(self, parent=None):
        super(Search, self).__init__(parent)
        self.setupUi(self)
        # info{ID_num,name,cardid,cardtype}
        # trade{srccard_card,descard_card,date,amount}
        self.showTable()
        self.cardEdit.editingFinished.connect(self.change)
        self.nameEdit.editingFinished.connect(self.change)
        self.phoneEdit.editingFinished.connect(self.change)
        self.idEdit.editingFinished.connect(self.change)
        self.dateEdit.editingFinished.connect(self.change)
        self.amountEdit.editingFinished.connect(self.change)

        self.SaveBox.stateChanged.connect(self.change)
        self.WithdrawBox.stateChanged.connect(self.change)
        self.TransBox.stateChanged.connect(self.change)
        self.LoanBox.stateChanged.connect(self.change)

    def showTable(self):
        self.showInfoTable()
        self.showTradeTable()

    # trade{srccard_card,descard_card,tradedate,amount}
    def showTradeTable(self,strict = {}):
        trade = Searchtrade('tradetype, srccard, descard, tradedate, amount',strict)
        #trade = [{'srccard':'001','descard':'002','tradedate':'2020-1-1', 'amount':'100'}]
        row = len(trade)
        col = 5
        self.tradeTable.setRowCount(row)
        self.tradeTable.setColumnCount(col)
        self.tradeTable.setHorizontalHeaderLabels(['类型','原账户','目标账户','日期','金额'])
        self.tradeTable.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tradeTable.horizontalHeader().resizeSection(0,50)
        self.tradeTable.horizontalHeader().resizeSection(1,80)
        self.tradeTable.horizontalHeader().resizeSection(2,80)
        self.tradeTable.horizontalHeader().resizeSection(3,90)
        self.tradeTable.horizontalHeader().resizeSection(4,50)
        

        
        for r in range(row):
            type = trade[r]['tradetype']
            id = trade[r]['srccard']
            name = trade[r]['descard']
            cardid = trade[r]['tradedate']
            cardtype = trade[r]['amount']

                
            self.tradeTable.setItem(r,0,QTableWidgetItem(type))
            self.tradeTable.setItem(r,1,QTableWidgetItem(id))
            self.tradeTable.setItem(r,2,QTableWidgetItem(name))
            self.tradeTable.setItem(r,3,QTableWidgetItem(cardid))
            self.tradeTable.setItem(r,4,QTableWidgetItem(cardtype))


    def showInfoTable(self,strict={}):
        info = Searchinfo('userid, user, cardid, cardtype',strict)
        row = min(len(info),50)
        col = 4
        self.infoTable.setRowCount(row)
        self.infoTable.setColumnCount(col)
        self.infoTable.setHorizontalHeaderLabels(['身份证号','姓名','卡号','卡类型'])
        self.infoTable.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.infoTable.horizontalHeader().resizeSection(0,100)
        self.infoTable.horizontalHeader().resizeSection(1,60)
        self.infoTable.horizontalHeader().resizeSection(2,90)
        self.infoTable.horizontalHeader().resizeSection(3,95)

        print(info)
        for r in range(row):
            id = info[r]['userid']
            name = info[r]['user']
            cardid = info[r]['cardid']
            cardtype = info[r]['cardtype']

            self.infoTable.setItem(r,0,QTableWidgetItem(id))
            self.infoTable.setItem(r,1,QTableWidgetItem(name))
            self.infoTable.setItem(r,2,QTableWidgetItem(cardid))
            self.infoTable.setItem(r,3,QTableWidgetItem(cardtype))


    def change(self):
        cardid = self.cardEdit.text()
        user =  self.nameEdit.text()
        phone = self.phoneEdit.text()
        userid = self.idEdit.text()
        date = self.dateEdit.text()
        amount = self.amountEdit.text()

        isSave = self.SaveBox.isChecked()
        isWithdraw = self.WithdrawBox.isChecked()
        isTrans = self.TransBox.isChecked()
        isLoan = self.LoanBox.isChecked()

        info = {}
        if cardid:
            info['cardid'] = '%'+cardid+'%'
        if user:
            info['user'] = '%'+user+'%'
        if phone:
            info['phone'] = '%'+phone+'%'
        if userid:
            info['userid'] = '%'+userid+'%'
        
        self.showInfoTable(info)

        trade = {}
        if date:
            trade['date'] = date
        if amount:
            trade['amount'] = amount
        
        
        self.showTradeTable(trade)
