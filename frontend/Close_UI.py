# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\close_.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Close_(object):
    def setupUi(self, Close_):
        Close_.setObjectName("Close_")
        Close_.resize(628, 394)
        Close_.setMinimumSize(QtCore.QSize(628, 394))
        Close_.setMaximumSize(QtCore.QSize(628, 394))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Close_.setWindowIcon(icon)
        self.frame_2 = QtWidgets.QFrame(Close_)
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
        self.ConfirmButton.setGeometry(QtCore.QRect(220, 330, 61, 31))
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.CancelButton = QtWidgets.QPushButton(self.frame_2)
        self.CancelButton.setGeometry(QtCore.QRect(350, 330, 61, 31))
        self.CancelButton.setObjectName("CancelButton")
        self.retEdit = QtWidgets.QLabel(self.frame_2)
        self.retEdit.setGeometry(QtCore.QRect(200, 140, 221, 41))
        self.retEdit.setObjectName("retEdit")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame_2)
        self.graphicsView.setGeometry(QtCore.QRect(120, 0, 401, 401))
        self.graphicsView.setObjectName("graphicsView")
        self.retTable = QtWidgets.QTableWidget(self.frame_2)
        self.retTable.setGeometry(QtCore.QRect(150, 80, 341, 221))
        self.retTable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.retTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.retTable.setShowGrid(True)
        self.retTable.setGridStyle(QtCore.Qt.SolidLine)
        self.retTable.setObjectName("retTable")
        self.retTable.setColumnCount(0)
        self.retTable.setRowCount(0)
        self.retTable.horizontalHeader().setVisible(True)
        self.retTable.verticalHeader().setVisible(False)
        self.label_3.raise_()
        self.graphicsView.raise_()
        self.label_5.raise_()
        self.ConfirmButton.raise_()
        self.CancelButton.raise_()
        self.retEdit.raise_()
        self.retTable.raise_()

        self.retranslateUi(Close_)
        QtCore.QMetaObject.connectSlotsByName(Close_)

    def retranslateUi(self, Close_):
        _translate = QtCore.QCoreApplication.translate
        Close_.setWindowTitle(_translate("Close_", "销户"))
        self.label_5.setText(_translate("Close_", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#184eff;\">-- 古 灵 阁 销 户 --</span></p></body></html>"))
        self.ConfirmButton.setText(_translate("Close_", "注销"))
        self.CancelButton.setText(_translate("Close_", "取消"))
        self.retEdit.setText(_translate("Close_", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
