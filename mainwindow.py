from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
import numpy as np
import math
#import gambar_rc

class LoginPage(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("Login_Page.ui",self)
        self.setWindowTitle("Login Page")
        #self.tmbl_gambar.clicked.connect(self.tombol_gambar)
    

app = QApplication([])
mainwindow = LoginPage()
app.setQuitOnLastWindowClosed(True)
mainwindow.show()
sys.exit(app.exec_())