import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class ErrorPage(QDialog):
    def __init__(self, err_msg):
        super(ErrorPage, self).__init__()
        loadUi('error.ui', self)
        self.setWindowTitle('Error')
        self.error_msg.setText('Error: ' + err_msg)