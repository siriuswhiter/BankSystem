# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\check_.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Check_(object):
    def setupUi(self, Check_):
        Check_.setObjectName("Check_")
        Check_.resize(628, 394)
        Check_.setMinimumSize(QtCore.QSize(628, 394))
        Check_.setMaximumSize(QtCore.QSize(628, 394))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Check_.setWindowIcon(icon)
        self.frame_2 = QtWidgets.QFrame(Check_)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 681, 401))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(-50, 0, 231, 401))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../image/slide5.jpeg"))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(250, 20, 281, 61))
        self.label_5.setObjectName("label_5")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame_2)
        self.graphicsView.setGeometry(QtCore.QRect(180, -20, 451, 421))
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setObjectName("graphicsView")
        self.retEdit = QtWidgets.QLabel(self.frame_2)
        self.retEdit.setGeometry(QtCore.QRect(330, 90, 151, 21))
        self.retEdit.setText("")
        self.retEdit.setObjectName("retEdit")
        self.CancelButton = QtWidgets.QPushButton(self.frame_2)
        self.CancelButton.setGeometry(QtCore.QRect(440, 280, 61, 31))
        self.CancelButton.setObjectName("CancelButton")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(233, 130, 81, 21))
        self.label.setObjectName("label")
        self.LoginButton = QtWidgets.QPushButton(self.frame_2)
        self.LoginButton.setGeometry(QtCore.QRect(300, 280, 61, 31))
        self.LoginButton.setObjectName("LoginButton")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(253, 200, 61, 21))
        self.label_2.setObjectName("label_2")
        self.passEdit = QtWidgets.QLineEdit(self.frame_2)
        self.passEdit.setGeometry(QtCore.QRect(330, 200, 191, 21))
        self.passEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passEdit.setObjectName("passEdit")
        self.nameEdit = QtWidgets.QLineEdit(self.frame_2)
        self.nameEdit.setGeometry(QtCore.QRect(330, 130, 191, 20))
        self.nameEdit.setObjectName("nameEdit")
        self.label_3.raise_()
        self.graphicsView.raise_()
        self.label_5.raise_()
        self.retEdit.raise_()
        self.CancelButton.raise_()
        self.label.raise_()
        self.LoginButton.raise_()
        self.label_2.raise_()
        self.passEdit.raise_()
        self.nameEdit.raise_()

        self.retranslateUi(Check_)
        QtCore.QMetaObject.connectSlotsByName(Check_)
        Check_.setTabOrder(self.nameEdit, self.passEdit)
        Check_.setTabOrder(self.passEdit, self.LoginButton)
        Check_.setTabOrder(self.LoginButton, self.CancelButton)
        Check_.setTabOrder(self.CancelButton, self.graphicsView)

    def retranslateUi(self, Check_):
        _translate = QtCore.QCoreApplication.translate
        Check_.setWindowTitle(_translate("Check_", "身份验证"))
        self.label_5.setText(_translate("Check_", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#184eff;\">-- 古 灵 阁 --</span></p></body></html>"))
        self.CancelButton.setText(_translate("Check_", "取消"))
        self.label.setText(_translate("Check_", "<html><head/><body><p><span style=\" font-size:14pt;\">身份证号</span></p></body></html>"))
        self.LoginButton.setText(_translate("Check_", "登录"))
        self.label_2.setText(_translate("Check_", "<html><head/><body><p><span style=\" font-size:14pt;\">密  码</span></p></body></html>"))
