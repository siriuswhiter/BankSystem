# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\check.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Check(object):
    def setupUi(self, Check):
        Check.setObjectName("Check")
        Check.resize(628, 394)
        Check.setMinimumSize(QtCore.QSize(628, 394))
        Check.setMaximumSize(QtCore.QSize(628, 394))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Check.setWindowIcon(icon)
        self.frame_2 = QtWidgets.QFrame(Check)
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
        self.graphicsView.setGeometry(QtCore.QRect(180, 0, 451, 421))
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setObjectName("graphicsView")
        self.retEdit = QtWidgets.QLabel(self.frame_2)
        self.retEdit.setGeometry(QtCore.QRect(330, 90, 151, 21))
        self.retEdit.setText("")
        self.retEdit.setObjectName("retEdit")
        self.CancelButton = QtWidgets.QPushButton(self.frame_2)
        self.CancelButton.setGeometry(QtCore.QRect(440, 290, 61, 31))
        self.CancelButton.setObjectName("CancelButton")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(260, 180, 54, 21))
        self.label.setObjectName("label")
        self.LoginButton = QtWidgets.QPushButton(self.frame_2)
        self.LoginButton.setGeometry(QtCore.QRect(300, 290, 61, 31))
        self.LoginButton.setObjectName("LoginButton")
        self.cardType = QtWidgets.QComboBox(self.frame_2)
        self.cardType.setGeometry(QtCore.QRect(330, 131, 191, 21))
        self.cardType.setObjectName("cardType")
        self.cardType.addItem("")
        self.cardType.addItem("")
        self.cardType.addItem("")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(260, 230, 54, 21))
        self.label_2.setObjectName("label_2")
        self.passEdit = QtWidgets.QLineEdit(self.frame_2)
        self.passEdit.setGeometry(QtCore.QRect(330, 230, 191, 21))
        self.passEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passEdit.setObjectName("passEdit")
        self.cardEdit = QtWidgets.QLineEdit(self.frame_2)
        self.cardEdit.setGeometry(QtCore.QRect(330, 180, 191, 20))
        self.cardEdit.setObjectName("cardEdit")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(260, 130, 41, 21))
        self.label_4.setObjectName("label_4")
        self.label_3.raise_()
        self.graphicsView.raise_()
        self.label_5.raise_()
        self.retEdit.raise_()
        self.CancelButton.raise_()
        self.label.raise_()
        self.LoginButton.raise_()
        self.cardType.raise_()
        self.label_2.raise_()
        self.passEdit.raise_()
        self.cardEdit.raise_()
        self.label_4.raise_()

        self.retranslateUi(Check)
        QtCore.QMetaObject.connectSlotsByName(Check)
        Check.setTabOrder(self.cardType, self.cardEdit)
        Check.setTabOrder(self.cardEdit, self.passEdit)
        Check.setTabOrder(self.passEdit, self.LoginButton)
        Check.setTabOrder(self.LoginButton, self.CancelButton)
        Check.setTabOrder(self.CancelButton, self.graphicsView)

    def retranslateUi(self, Check):
        _translate = QtCore.QCoreApplication.translate
        Check.setWindowTitle(_translate("Check", "身份验证"))
        self.label_5.setText(_translate("Check", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#184eff;\">-- 古 灵 阁 --</span></p></body></html>"))
        self.CancelButton.setText(_translate("Check", "取消"))
        self.label.setText(_translate("Check", "<html><head/><body><p><span style=\" font-size:14pt;\">卡号</span></p></body></html>"))
        self.LoginButton.setText(_translate("Check", "登录"))
        self.cardType.setItemText(0, _translate("Check", "招商银行一卡通"))
        self.cardType.setItemText(1, _translate("Check", "工商银行牡丹卡"))
        self.cardType.setItemText(2, _translate("Check", "邮政银行生肖卡"))
        self.label_2.setText(_translate("Check", "<html><head/><body><p><span style=\" font-size:14pt;\">密码</span></p></body></html>"))
        self.label_4.setText(_translate("Check", "<html><head/><body><p><span style=\" font-size:14pt;\">类型</span></p></body></html>"))
