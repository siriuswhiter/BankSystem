# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(628, 394)
        Main.setMinimumSize(QtCore.QSize(628, 394))
        Main.setMaximumSize(QtCore.QSize(628, 394))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        Main.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        self.frame_2 = QtWidgets.QFrame(Main)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 681, 401))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(-30, 0, 681, 401))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../image/mainslide.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(100, 20, 411, 61))
        self.label_5.setObjectName("label_5")
        self.retEdit = QtWidgets.QLabel(self.frame_2)
        self.retEdit.setGeometry(QtCore.QRect(320, 90, 151, 21))
        self.retEdit.setText("")
        self.retEdit.setObjectName("retEdit")
        self.Save = QtWidgets.QPushButton(self.frame_2)
        self.Save.setGeometry(QtCore.QRect(160, 110, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Save.setFont(font)
        self.Save.setObjectName("Save")
        self.WithDraw = QtWidgets.QPushButton(self.frame_2)
        self.WithDraw.setGeometry(QtCore.QRect(160, 190, 111, 51))
        self.WithDraw.setObjectName("WithDraw")
        self.Repay = QtWidgets.QPushButton(self.frame_2)
        self.Repay.setGeometry(QtCore.QRect(330, 190, 111, 51))
        self.Repay.setObjectName("Repay")
        self.Search = QtWidgets.QPushButton(self.frame_2)
        self.Search.setGeometry(QtCore.QRect(330, 270, 111, 51))
        self.Search.setObjectName("Search")
        self.Trans = QtWidgets.QPushButton(self.frame_2)
        self.Trans.setGeometry(QtCore.QRect(330, 110, 111, 51))
        self.Trans.setObjectName("Trans")
        self.Loan = QtWidgets.QPushButton(self.frame_2)
        self.Loan.setGeometry(QtCore.QRect(160, 270, 111, 51))
        self.Loan.setObjectName("Loan")
        self.Login = QtWidgets.QPushButton(self.frame_2)
        self.Login.setGeometry(QtCore.QRect(550, 10, 75, 31))
        self.Login.setStyleSheet("border:none;color:rgb(24, 78, 255)")
        self.Login.setObjectName("Login")
        self.label_3.raise_()
        self.retEdit.raise_()
        self.Save.raise_()
        self.WithDraw.raise_()
        self.Repay.raise_()
        self.Search.raise_()
        self.Trans.raise_()
        self.Loan.raise_()
        self.label_5.raise_()
        self.Login.raise_()

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)
        Main.setTabOrder(self.Save, self.WithDraw)
        Main.setTabOrder(self.WithDraw, self.Loan)
        Main.setTabOrder(self.Loan, self.Trans)
        Main.setTabOrder(self.Trans, self.Repay)
        Main.setTabOrder(self.Repay, self.Search)
        Main.setTabOrder(self.Search, self.Login)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "古灵阁"))
        self.label_5.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#184eff;\">-- 古 灵 阁 线 上 自 助 系 统--</span></p></body></html>"))
        self.Save.setText(_translate("Main", "存 款"))
        self.WithDraw.setText(_translate("Main", "取款"))
        self.Repay.setText(_translate("Main", "还贷"))
        self.Search.setText(_translate("Main", "查询"))
        self.Trans.setText(_translate("Main", "转账"))
        self.Loan.setText(_translate("Main", "贷款"))
        self.Login.setText(_translate("Main", "登录"))
