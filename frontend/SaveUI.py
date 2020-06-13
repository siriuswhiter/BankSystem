# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\save.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Save(object):
    def setupUi(self, Save):
        Save.setObjectName("Save")
        Save.resize(628, 394)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Save.setWindowIcon(icon)
        self.frame_2 = QtWidgets.QFrame(Save)
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
        self.graphicsView.setGeometry(QtCore.QRect(180, 0, 628, 394))
        self.graphicsView.setMinimumSize(QtCore.QSize(628, 394))
        self.graphicsView.setMaximumSize(QtCore.QSize(628, 394))
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(250, 150, 91, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(250, 220, 81, 31))
        self.label_2.setObjectName("label_2")
        self.amountEdit = QtWidgets.QLineEdit(self.frame_2)
        self.amountEdit.setGeometry(QtCore.QRect(360, 220, 191, 31))
        self.amountEdit.setObjectName("amountEdit")
        self.ConfirmButton = QtWidgets.QPushButton(self.frame_2)
        self.ConfirmButton.setGeometry(QtCore.QRect(310, 300, 61, 31))
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.CancelButton = QtWidgets.QPushButton(self.frame_2)
        self.CancelButton.setGeometry(QtCore.QRect(440, 300, 61, 31))
        self.CancelButton.setObjectName("CancelButton")
        self.retEdit = QtWidgets.QLabel(self.frame_2)
        self.retEdit.setGeometry(QtCore.QRect(360, 110, 151, 21))
        self.retEdit.setText("")
        self.retEdit.setObjectName("retEdit")
        self.ID_num = QtWidgets.QLabel(self.frame_2)
        self.ID_num.setGeometry(QtCore.QRect(360, 160, 181, 21))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.ID_num.setFont(font)
        self.ID_num.setTextFormat(QtCore.Qt.RichText)
        self.ID_num.setObjectName("ID_num")
        self.label_3.raise_()
        self.graphicsView.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.amountEdit.raise_()
        self.ConfirmButton.raise_()
        self.CancelButton.raise_()
        self.retEdit.raise_()
        self.ID_num.raise_()

        self.retranslateUi(Save)
        QtCore.QMetaObject.connectSlotsByName(Save)
        Save.setTabOrder(self.amountEdit, self.ConfirmButton)
        Save.setTabOrder(self.ConfirmButton, self.CancelButton)
        Save.setTabOrder(self.CancelButton, self.graphicsView)

    def retranslateUi(self, Save):
        _translate = QtCore.QCoreApplication.translate
        Save.setWindowTitle(_translate("Save", "存款"))
        self.label_5.setText(_translate("Save", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#184eff;\">-- 古 灵 阁 --</span></p></body></html>"))
        self.label.setText(_translate("Save", "<html><head/><body><p><span style=\" font-size:14pt;\">存入卡号 ：</span></p></body></html>"))
        self.label_2.setText(_translate("Save", "<html><head/><body><p><span style=\" font-size:14pt;\">存款金额</span></p></body></html>"))
        self.ConfirmButton.setText(_translate("Save", "确定"))
        self.CancelButton.setText(_translate("Save", "取消"))
        self.ID_num.setText(_translate("Save", "<html><head/><body><p><br/></p></body></html>"))
