# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(590, 831)
        self.movie_thumbnail_1 = QtWidgets.QLabel(Dialog)
        self.movie_thumbnail_1.setGeometry(QtCore.QRect(30, 20, 181, 131))
        self.movie_thumbnail_1.setObjectName("movie_thumbnail_1")
        self.movie_title_1 = QtWidgets.QLabel(Dialog)
        self.movie_title_1.setGeometry(QtCore.QRect(260, 20, 311, 21))
        self.movie_title_1.setStyleSheet("font: 16pt \"Impact\";")
        self.movie_title_1.setObjectName("movie_title_1")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 20, 21, 21))
        self.label.setStyleSheet("font: 16pt \"Impact\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 50, 51, 21))
        self.label_2.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.m1_genre = QtWidgets.QTextEdit(Dialog)
        self.m1_genre.setGeometry(QtCore.QRect(280, 50, 291, 21))
        self.m1_genre.setObjectName("m1_genre")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(230, 80, 47, 13))
        self.label_3.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.m1_plot = QtWidgets.QTextEdit(Dialog)
        self.m1_plot.setGeometry(QtCore.QRect(280, 80, 291, 71))
        self.m1_plot.setObjectName("m1_plot")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(20, 160, 551, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(20, 330, 551, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.movie_thumbnail_2 = QtWidgets.QLabel(Dialog)
        self.movie_thumbnail_2.setGeometry(QtCore.QRect(30, 190, 181, 131))
        self.movie_thumbnail_2.setObjectName("movie_thumbnail_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(230, 190, 21, 21))
        self.label_4.setStyleSheet("font: 16pt \"Impact\";")
        self.label_4.setObjectName("label_4")
        self.movie_title_2 = QtWidgets.QLabel(Dialog)
        self.movie_title_2.setGeometry(QtCore.QRect(260, 190, 311, 21))
        self.movie_title_2.setStyleSheet("font: 16pt \"Impact\";")
        self.movie_title_2.setObjectName("movie_title_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(230, 250, 47, 13))
        self.label_5.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(230, 220, 51, 21))
        self.label_6.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_6.setObjectName("label_6")
        self.m2_genre = QtWidgets.QTextEdit(Dialog)
        self.m2_genre.setGeometry(QtCore.QRect(280, 220, 291, 21))
        self.m2_genre.setObjectName("m2_genre")
        self.m2_plot = QtWidgets.QTextEdit(Dialog)
        self.m2_plot.setGeometry(QtCore.QRect(280, 250, 291, 71))
        self.m2_plot.setObjectName("m2_plot")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(20, 490, 551, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.movie_thumbnail_3 = QtWidgets.QLabel(Dialog)
        self.movie_thumbnail_3.setGeometry(QtCore.QRect(30, 350, 181, 131))
        self.movie_thumbnail_3.setObjectName("movie_thumbnail_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(230, 350, 21, 21))
        self.label_7.setStyleSheet("font: 16pt \"Impact\";")
        self.label_7.setObjectName("label_7")
        self.movie_title_3 = QtWidgets.QLabel(Dialog)
        self.movie_title_3.setGeometry(QtCore.QRect(260, 350, 311, 21))
        self.movie_title_3.setStyleSheet("font: 16pt \"Impact\";")
        self.movie_title_3.setObjectName("movie_title_3")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(230, 410, 47, 13))
        self.label_8.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(230, 380, 51, 21))
        self.label_9.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_9.setObjectName("label_9")
        self.m3_genre = QtWidgets.QTextEdit(Dialog)
        self.m3_genre.setGeometry(QtCore.QRect(280, 380, 291, 21))
        self.m3_genre.setObjectName("m3_genre")
        self.m3_plot = QtWidgets.QTextEdit(Dialog)
        self.m3_plot.setGeometry(QtCore.QRect(280, 410, 291, 71))
        self.m3_plot.setObjectName("m3_plot")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(20, 650, 551, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.movie_thumbnail_4 = QtWidgets.QLabel(Dialog)
        self.movie_thumbnail_4.setGeometry(QtCore.QRect(30, 510, 181, 131))
        self.movie_thumbnail_4.setObjectName("movie_thumbnail_4")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(230, 510, 21, 21))
        self.label_10.setStyleSheet("font: 16pt \"Impact\";")
        self.label_10.setObjectName("label_10")
        self.movie_title_4 = QtWidgets.QLabel(Dialog)
        self.movie_title_4.setGeometry(QtCore.QRect(260, 510, 311, 21))
        self.movie_title_4.setStyleSheet("font: 16pt \"Impact\";")
        self.movie_title_4.setObjectName("movie_title_4")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(230, 570, 47, 13))
        self.label_11.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(230, 540, 51, 21))
        self.label_12.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_12.setObjectName("label_12")
        self.m4_genre = QtWidgets.QTextEdit(Dialog)
        self.m4_genre.setGeometry(QtCore.QRect(280, 540, 291, 21))
        self.m4_genre.setObjectName("m4_genre")
        self.m4_plot = QtWidgets.QTextEdit(Dialog)
        self.m4_plot.setGeometry(QtCore.QRect(280, 570, 291, 71))
        self.m4_plot.setObjectName("m4_plot")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(20, 810, 551, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.movie_thumbnail_5 = QtWidgets.QLabel(Dialog)
        self.movie_thumbnail_5.setGeometry(QtCore.QRect(30, 670, 181, 131))
        self.movie_thumbnail_5.setObjectName("movie_thumbnail_5")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(230, 670, 21, 21))
        self.label_13.setStyleSheet("font: 16pt \"Impact\";")
        self.label_13.setObjectName("label_13")
        self.movie_title_5 = QtWidgets.QLabel(Dialog)
        self.movie_title_5.setGeometry(QtCore.QRect(260, 670, 311, 21))
        self.movie_title_5.setStyleSheet("font: 16pt \"Impact\";")
        self.movie_title_5.setObjectName("movie_title_5")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(230, 730, 47, 13))
        self.label_14.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
"")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(230, 700, 51, 21))
        self.label_15.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.label_15.setObjectName("label_15")
        self.m5_genre = QtWidgets.QTextEdit(Dialog)
        self.m5_genre.setGeometry(QtCore.QRect(280, 700, 291, 21))
        self.m5_genre.setObjectName("m5_genre")
        self.m5_plot = QtWidgets.QTextEdit(Dialog)
        self.m5_plot.setGeometry(QtCore.QRect(280, 730, 291, 71))
        self.m5_plot.setObjectName("m5_plot")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.movie_thumbnail_1.setText(_translate("Dialog", "IMG"))
        self.movie_title_1.setText(_translate("Dialog", "Title"))
        self.label.setText(_translate("Dialog", "1,"))
        self.label_2.setText(_translate("Dialog", "Genre: "))
        self.label_3.setText(_translate("Dialog", "Plot"))
        self.movie_thumbnail_2.setText(_translate("Dialog", "IMG"))
        self.label_4.setText(_translate("Dialog", "2."))
        self.movie_title_2.setText(_translate("Dialog", "Title"))
        self.label_5.setText(_translate("Dialog", "Plot"))
        self.label_6.setText(_translate("Dialog", "Genre: "))
        self.movie_thumbnail_3.setText(_translate("Dialog", "IMG"))
        self.label_7.setText(_translate("Dialog", "3."))
        self.movie_title_3.setText(_translate("Dialog", "Title"))
        self.label_8.setText(_translate("Dialog", "Plot"))
        self.label_9.setText(_translate("Dialog", "Genre: "))
        self.movie_thumbnail_4.setText(_translate("Dialog", "IMG"))
        self.label_10.setText(_translate("Dialog", "4."))
        self.movie_title_4.setText(_translate("Dialog", "Title"))
        self.label_11.setText(_translate("Dialog", "Plot"))
        self.label_12.setText(_translate("Dialog", "Genre: "))
        self.movie_thumbnail_5.setText(_translate("Dialog", "IMG"))
        self.label_13.setText(_translate("Dialog", "5."))
        self.movie_title_5.setText(_translate("Dialog", "Title"))
        self.label_14.setText(_translate("Dialog", "Plot"))
        self.label_15.setText(_translate("Dialog", "Genre: "))

