# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(508, 343)
        Dialog.setStyleSheet("font: 75 10pt \"Calibri\";")
        self.search_box = QtWidgets.QPlainTextEdit(Dialog)
        self.search_box.setGeometry(QtCore.QRect(10, 30, 361, 21))
        self.search_box.setObjectName("search_box")
        self.search_button = QtWidgets.QPushButton(Dialog)
        self.search_button.setGeometry(QtCore.QRect(390, 30, 101, 23))
        self.search_button.setObjectName("search_button")
        self.genre_dropbox = QtWidgets.QComboBox(Dialog)
        self.genre_dropbox.setGeometry(QtCore.QRect(360, 70, 81, 22))
        self.genre_dropbox.setObjectName("genre_dropbox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.label.setStyleSheet("font: 10pt \"Calibri\";")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 50, 481, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_2.setStyleSheet("font: 10pt \"Calibri\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(270, 70, 91, 20))
        self.label_3.setStyleSheet("font: 10pt \"Calibri\";")
        self.label_3.setObjectName("label_3")
        self.genre_filter = QtWidgets.QPushButton(Dialog)
        self.genre_filter.setGeometry(QtCore.QRect(450, 70, 41, 23))
        self.genre_filter.setObjectName("genre_filter")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(15, 100, 471, 231))
        self.tableWidget.setRowCount(250)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.search_button.setText(_translate("Dialog", "Search"))
        self.label.setText(_translate("Dialog", "Browse Movies"))
        self.label_2.setText(_translate("Dialog", "Recommendation"))
        self.label_3.setText(_translate("Dialog", "Filter by Genre"))
        self.genre_filter.setText(_translate("Dialog", "Go"))

