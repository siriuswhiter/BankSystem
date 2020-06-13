# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\close.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Close(object):
    def setupUi(self, Close):
        Close.setObjectName("Close")
        Close.resize(630, 399)
        Close.setMinimumSize(QtCore.QSize(628, 394))
        Close.setMaximumSize(QtCore.QSize(630, 399))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Close.setWindowIcon(icon)
        self.frame_2 = QtWidgets.QFrame(Close)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 681, 401))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(-50, 0, 691, 401))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../image/mainslide.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(170, 10, 281, 61))
        self.label_5.setObjectName("label_5")
        self.ConfirmButton = QtWidgets.QPushButton(self.frame_2)
        self.ConfirmButton.setGeometry(QtCore.QRect(200, 300, 61, 31))
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.CancelButton = QtWidgets.QPushButton(self.frame_2)
        self.CancelButton.setGeometry(QtCore.QRect(350, 300, 61, 31))
        self.CancelButton.setObjectName("CancelButton")
        self.retEdit = QtWidgets.QLabel(self.frame_2)
        self.retEdit.setGeometry(QtCore.QRect(250, 90, 151, 21))
        self.retEdit.setText("")
        self.retEdit.setObjectName("retEdit")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame_2)
        self.graphicsView.setGeometry(QtCore.QRect(120, 0, 401, 401))
        self.graphicsView.setObjectName("graphicsView")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(160, 210, 91, 41))
        self.label_7.setObjectName("label_7")
        self.passEdit = QtWidgets.QLineEdit(self.frame_2)
        self.passEdit.setGeometry(QtCore.QRect(250, 220, 201, 20))
        self.passEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passEdit.setObjectName("passEdit")
        self.ID_num = QtWidgets.QLineEdit(self.frame_2)
        self.ID_num.setGeometry(QtCore.QRect(250, 140, 201, 20))
        self.ID_num.setObjectName("ID_num")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(160, 130, 81, 41))
        self.label.setObjectName("label")
        self.label_3.raise_()
        self.graphicsView.raise_()
        self.label_5.raise_()
        self.ConfirmButton.raise_()
        self.CancelButton.raise_()
        self.retEdit.raise_()
        self.label_7.raise_()
        self.passEdit.raise_()
        self.ID_num.raise_()
        self.label.raise_()

        self.retranslateUi(Close)
        QtCore.QMetaObject.connectSlotsByName(Close)

    def retranslateUi(self, Close):
        _translate = QtCore.QCoreApplication.translate
        Close.setWindowTitle(_translate("Close", "验证个人信息"))
        self.label_5.setText(_translate("Close", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#184eff;\">-- 古 灵 阁 销 户 --</span></p></body></html>"))
        self.ConfirmButton.setText(_translate("Close", "确定"))
        self.CancelButton.setText(_translate("Close", "取消"))
        self.label_7.setText(_translate("Close", "<html><head/><body><p><span style=\" font-size:14pt;\">账户密码</span></p></body></html>"))
        self.label.setText(_translate("Close", "<html><head/><body><p><span style=\" font-size:14pt;\">身份证号</span></p></body></html>"))
