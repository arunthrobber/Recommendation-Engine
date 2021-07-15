import sys
import RecommendationSystem as rs
import data
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QHeaderView
from PyQt5.uic import loadUi
#from PyQt5.QtGui import QHeaderView

class MainWin(QDialog):
    def __init__(self):
        super(MainWin, self).__init__()
        loadUi('main.ui', self)
        self.setWindowTitle('Recommendation Engine')
        x = self.init_table()
        y = self.fill_genres()
        self.search_button.clicked.connect(self.search)
        self.genre_filter.clicked.connect(self.go)
    
    def search(self):
        title = self.search_box.toPlainText()
        data.movie_list = rs.recommendations(title)
        if data.movie_list == -1:
            from err_msg import ErrorPage
            obj = ErrorPage('Item not found in DataBase')
        else:
            data.get_info()
            from pop_up import NextPage
            obj = NextPage(data.movie_list)
        obj.exec_()
        

    def fill_genres(self):
        for genre in data.genre_set:
            self.genre_dropbox.addItem(genre)
            
    def fill_table(self, data):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['Title','Genre','Actors','Director','Plot'])
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        for row_num, row in data.iterrows():
            self.tableWidget.insertRow(row_num)
            for col_num, col in enumerate(row):
                if type(col) == list:
                    item = ','.join(col)
                else:
                    item = col
                self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(item))
    
    def init_table(self):
        self.fill_table(data.df)

    def go(self):
        genre = self.genre_dropbox.currentText()
        data.filter_by_genre(genre)
        from table_view import Table
        obj = Table(data.df[data.filter_list])
        obj.exec_()


app = QApplication(sys.argv)
widget = MainWin()
widget.show()
sys.exit(app.exec_())