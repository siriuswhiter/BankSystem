# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\trans.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Trans(object):
    def setupUi(self, Trans):
        Trans.setObjectName("Trans")
        Trans.resize(628, 394)
        Trans.setMinimumSize(QtCore.QSize(628, 394))
        Trans.setMaximumSize(QtCore.QSize(628, 394))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Trans.setWindowIcon(icon)
        self.frame_2 = QtWidgets.QFrame(Trans)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 681, 401))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(-50, 0, 231, 401))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../image/slide1.jpeg"))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(250, 20, 281, 61))
        self.label_5.setObjectName("label_5")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame_2)
        self.graphicsView.setGeometry(QtCore.QRect(180, 0, 451, 421))
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(250, 150, 81, 41))
        self.label.setObjectName("label")
        self.cardEdit = QtWidgets.QLineEdit(self.frame_2)
        self.cardEdit.setGeometry(QtCore.QRect(360, 161, 191, 20))
        self.cardEdit.setObjectName("cardEdit")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(250, 220, 81, 31))
        self.label_2.setObjectName("label_2")
        self.amountEdit = QtWidgets.QLineEdit(self.frame_2)
        self.amountEdit.setGeometry(QtCore.QRect(360, 220, 191, 21))
        self.amountEdit.setObjectName("amountEdit")
        self.ConfirmButton = QtWidgets.QPushButton(self.frame_2)
        self.ConfirmButton.setGeometry(QtCore.QRect(310, 300, 61, 31))
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.CancelButton = QtWidgets.QPushButton(self.frame_2)
        self.CancelButton.setGeometry(QtCore.QRect(440, 300, 61, 31))
        self.CancelButton.setObjectName("CancelButton")
        self.retEdit = QtWidgets.QLabel(self.frame_2)
        self.retEdit.setGeometry(QtCore.QRect(360, 110, 181, 21))
        self.retEdit.setText("")
        self.retEdit.setObjectName("retEdit")
        self.label_3.raise_()
        self.graphicsView.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.cardEdit.raise_()
        self.label_2.raise_()
        self.amountEdit.raise_()
        self.ConfirmButton.raise_()
        self.CancelButton.raise_()
        self.retEdit.raise_()

        self.retranslateUi(Trans)
        QtCore.QMetaObject.connectSlotsByName(Trans)
        Trans.setTabOrder(self.cardEdit, self.amountEdit)
        Trans.setTabOrder(self.amountEdit, self.ConfirmButton)
        Trans.setTabOrder(self.ConfirmButton, self.CancelButton)
        Trans.setTabOrder(self.CancelButton, self.graphicsView)

    def retranslateUi(self, Trans):
        _translate = QtCore.QCoreApplication.translate
        Trans.setWindowTitle(_translate("Trans", "转账"))
        self.label_5.setText(_translate("Trans", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#184eff;\">-- 古 灵 阁 --</span></p></body></html>"))
        self.label.setText(_translate("Trans", "<html><head/><body><p><span style=\" font-size:14pt;\">转账卡号</span></p></body></html>"))
        self.label_2.setText(_translate("Trans", "<html><head/><body><p><span style=\" font-size:14pt;\">转账金额</span></p></body></html>"))
        self.ConfirmButton.setText(_translate("Trans", "确定"))
        self.CancelButton.setText(_translate("Trans", "取消"))
