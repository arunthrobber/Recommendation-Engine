import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QHeaderView
from PyQt5.uic import loadUi

class Table(QDialog):
    def __init__(self, data):
        super(Table, self).__init__()
        loadUi('table.ui', self)
        self.setWindowTitle('Filtered Results')
        self.fill_table(data)
    
    def fill_table(self, data):
        data = data.reset_index(drop = True)
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setHorizontalHeaderLabels(['Title','Genre','Actors','Director','Plot'])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        for row_num, row in data.iterrows():
            for col_num, col in enumerate(row):
                if type(col) == list:
                    item = ','.join(col)
                else:
                    item = col
                self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(item))