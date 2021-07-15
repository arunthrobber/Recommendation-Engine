import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap

class NextPage(QDialog):
    def __init__(self, movie_list):
        super(NextPage, self).__init__()
        loadUi('result.ui', self)
        self.setWindowTitle('Top 5 Recommended Movies')
        path = r'.\Sources\{}.jpg'
        title = ''.join(list(movie_list[0]['Title'])).replace(':', '-').replace('?', '')
        pixmap = QPixmap(path.format(title))
        self.movie_thumbnail_1.setPixmap(pixmap)
        self.movie_title_1.setText(title)
        self.m1_genre.setText(''.join(list(movie_list[0]['Genre'])))
        self.m1_plot.setText(''.join(list(movie_list[0]['Plot'])))
        title1 = ''.join(list(movie_list[1]['Title'])).replace(':', '-').replace('?', '')
        pixmap = QPixmap(path.format(title1))
        self.movie_thumbnail_2.setPixmap(pixmap)
        self.movie_title_2.setText(title1)
        self.m2_genre.setText(''.join(list(movie_list[1]['Genre'])))
        self.m2_plot.setText(''.join(list(movie_list[1]['Plot'])))
        title2 = ''.join(list(movie_list[2]['Title'])).replace(':', '-').replace('?', '')
        pixmap = QPixmap(path.format(title2))
        self.movie_thumbnail_3.setPixmap(pixmap)
        self.movie_title_3.setText(title2)
        self.m3_genre.setText(''.join(list(movie_list[2]['Genre'])))
        self.m3_plot.setText(''.join(list(movie_list[2]['Plot'])))