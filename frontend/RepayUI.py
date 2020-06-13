# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\repay.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Repay(object):
    def setupUi(self, Repay):
        Repay.setObjectName("Repay")
        Repay.resize(628, 394)
        Repay.setMinimumSize(QtCore.QSize(628, 394))
        Repay.setMaximumSize(QtCore.QSize(628, 394))
        Repay.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Repay.setWindowIcon(icon)
        self.frame_2 = QtWidgets.QFrame(Repay)
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
        self.ConfirmButton = QtWidgets.QPushButton(self.frame_2)
        self.ConfirmButton.setGeometry(QtCore.QRect(300, 320, 61, 31))
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.CancelButton = QtWidgets.QPushButton(self.frame_2)
        self.CancelButton.setGeometry(QtCore.QRect(440, 320, 61, 31))
        self.CancelButton.setObjectName("CancelButton")
        self.retTable = QtWidgets.QTableWidget(self.frame_2)
        self.retTable.setGeometry(QtCore.QRect(230, 90, 341, 201))
        self.retTable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.retTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.retTable.setShowGrid(True)
        self.retTable.setGridStyle(QtCore.Qt.SolidLine)
        self.retTable.setObjectName("retTable")
        self.retTable.setColumnCount(0)
        self.retTable.setRowCount(0)
        self.retTable.horizontalHeader().setVisible(True)
        self.retTable.verticalHeader().setVisible(False)
        self.retEdit = QtWidgets.QLabel(self.frame_2)
        self.retEdit.setGeometry(QtCore.QRect(270, 70, 231, 16))
        self.retEdit.setText("")
        self.retEdit.setObjectName("retEdit")

        self.retranslateUi(Repay)
        QtCore.QMetaObject.connectSlotsByName(Repay)
        Repay.setTabOrder(self.ConfirmButton, self.CancelButton)

    def retranslateUi(self, Repay):
        _translate = QtCore.QCoreApplication.translate
        Repay.setWindowTitle(_translate("Repay", "还贷"))
        self.label_5.setText(_translate("Repay", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#184eff;\">-- 古 灵 阁 --</span></p></body></html>"))
        self.ConfirmButton.setText(_translate("Repay", "还贷"))
        self.CancelButton.setText(_translate("Repay", "取消"))
