from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
import numpy as np
import math
import gambar_rc

class mainwindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #loadUi("sinusoid_gui.ui",self)
        self.setWindowTitle("GUI PRAKTIKUM")
        #self.tmbl_gambar.clicked.connect(self.tombol_gambar)
    

app = QApplication([])
mainwindow = mainwindow()
app.setQuitOnLastWindowClosed(True)
mainwindow.show()
sys.exit(app.exec_())