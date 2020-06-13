# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\query.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Query(object):
    def setupUi(self, Query):
        Query.setObjectName("Query")
        Query.resize(628, 394)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Query.setWindowIcon(icon)
        self.frame_2 = QtWidgets.QFrame(Query)
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
        self.label_5.setGeometry(QtCore.QRect(210, 10, 181, 41))
        self.label_5.setObjectName("label_5")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.frame_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(80, 60, 471, 311))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.infoTable = QtWidgets.QTableWidget(self.frame_2)
        self.infoTable.setGeometry(QtCore.QRect(80, 60, 471, 311))
        self.infoTable.setObjectName("infoTable")
        self.infoTable.setColumnCount(0)
        self.infoTable.setRowCount(0)
        self.infoTable.horizontalHeader().setHighlightSections(False)
        self.infoTable.verticalHeader().setVisible(False)

        self.retranslateUi(Query)
        QtCore.QMetaObject.connectSlotsByName(Query)
        Query.setTabOrder(self.graphicsView_2, self.infoTable)

    def retranslateUi(self, Query):
        _translate = QtCore.QCoreApplication.translate
        Query.setWindowTitle(_translate("Query", "查询"))
        self.label_5.setText(_translate("Query", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#184eff;\">-- 古 灵 阁 --</span></p></body></html>"))
