# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\admin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(628, 394)
        Admin.setMinimumSize(QtCore.QSize(628, 394))
        Admin.setMaximumSize(QtCore.QSize(628, 394))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(14)
        Admin.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Admin.setWindowIcon(icon)
        self.frame_2 = QtWidgets.QFrame(Admin)
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
        self.Close = QtWidgets.QPushButton(self.frame_2)
        self.Close.setGeometry(QtCore.QRect(250, 190, 111, 51))
        self.Close.setObjectName("Close")
        self.Search = QtWidgets.QPushButton(self.frame_2)
        self.Search.setGeometry(QtCore.QRect(250, 280, 111, 51))
        self.Search.setObjectName("Search")
        self.Open = QtWidgets.QPushButton(self.frame_2)
        self.Open.setGeometry(QtCore.QRect(250, 100, 111, 51))
        self.Open.setObjectName("Open")
        self.label_3.raise_()
        self.Close.raise_()
        self.Search.raise_()
        self.Open.raise_()
        self.label_5.raise_()

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)
        Admin.setTabOrder(self.Open, self.Close)
        Admin.setTabOrder(self.Close, self.Search)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "古灵阁"))
        self.label_5.setText(_translate("Admin", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#184eff;\">-- 古 灵 阁 解 咒 员--</span></p></body></html>"))
        self.Close.setText(_translate("Admin", "销户"))
        self.Search.setText(_translate("Admin", "查询"))
        self.Open.setText(_translate("Admin", "开户"))
