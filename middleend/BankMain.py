#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
sys.path.append('../frontend')

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from MainUI import Ui_Main
from BankCheck import Check,Check_
from BankAdmin import Admin 

class MyMainForm(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        
        self.Save.clicked.connect(lambda: self.response(1))
        self.WithDraw.clicked.connect(lambda: self.response(2))
        self.Loan.clicked.connect(lambda: self.response(3))
        self.Trans.clicked.connect(lambda: self.response(4))
        self.Repay.clicked.connect(lambda: self.response(5))

        self.Search.clicked.connect(self.response2)
        self.next2 = Admin()
        self.Login.clicked.connect(self.next2.show)

    def response2(self):
        self.next = Check_()
        self.next.show()

    def response(self,event):
        self.next = Check()
        self.next.option = event 
        self.next.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyMainForm()
    main.show()
    sys.exit(app.exec_())