#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
sys.path.append('../frontend')
sys.path.append('../backend')

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QHeaderView,QTableWidgetItem
from QueryUI import Ui_Query
from Search import *

class Query(QMainWindow, Ui_Query):
    def __init__(self, parent=None):
        super(Query, self).__init__(parent)
        self.setupUi(self)


    def showInfo(self):
# [{'belong':'1','cardtype':'1','cardid':'123','balance':'1','loan':'1'}]#
        info = Queryinfo(self.user)

        row = len(info)
        col = 6
        self.infoTable.setRowCount(row)
        self.infoTable.setColumnCount(col)
        self.infoTable.setHorizontalHeaderLabels(['所属银行','类型','卡号','存款','贷款','透支'])
        self.infoTable.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.infoTable.horizontalHeader().resizeSection(0,60)
        self.infoTable.horizontalHeader().resizeSection(1,100)
        self.infoTable.horizontalHeader().resizeSection(2,140)
        self.infoTable.horizontalHeader().resizeSection(3,50)
        self.infoTable.horizontalHeader().resizeSection(4,50)
        self.infoTable.horizontalHeader().resizeSection(5,50)



        

        
        for r in range(row):
            belong = info[r]['belong']
            type = info[r]['cardname']
            cardid = info[r]['cardid']
            balance = info[r]['balance']
            loan = info[r]['loan']
            over = info[r]['over']


            self.infoTable.setItem(r,0,QTableWidgetItem(belong))
            self.infoTable.setItem(r,1,QTableWidgetItem(type))
            self.infoTable.setItem(r,2,QTableWidgetItem(cardid))
            self.infoTable.setItem(r,3,QTableWidgetItem(balance))
            self.infoTable.setItem(r,4,QTableWidgetItem(loan))
            self.infoTable.setItem(r,5,QTableWidgetItem(over))


