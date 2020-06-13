#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
sys.path.append('../frontend')

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from AdminUI import Ui_Admin
from BankOpen import Open
from BankClose import Close
from BankSearch import Search

class Admin(QMainWindow, Ui_Admin):
    def __init__(self, parent=None):
        super(Admin, self).__init__(parent)
        self.setupUi(self)
        self.Open.clicked.connect(lambda: self.response(1))
        self.Close.clicked.connect(lambda: self.response(2))
        self.Search.clicked.connect(lambda: self.response(3))

    def response(self,event):
        self.win = None
        if event==1:
            self.win = Open()             
        elif event==2:
            self.win = Close()
        elif event==3:
            self.win = Search()
        self.win.show()
