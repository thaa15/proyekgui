from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QIntValidator
import sys
import numpy as np
import math
import cmath
from pylab import *
from scipy.signal import kaiserord, lfilter, firwin, freqz
from matplotlib import pyplot as plt
#import gambar_rc

class Modul_2(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("Modul_2.ui", self)
        self.setWindowTitle("Modul 2 - Root Locus")
        self.calculate.clicked.connect(self.hitung)
        self.plot_akar.clicked.connect(self.plot)
        self.cari_letak.clicked.connect(self.letak)
    
    def hitung(self):

        global denum1, denum2, denum3

        num = float(self.numerator.text())
        denum1 = float(self.denum1.text())
        denum2 = float(self.denum2.text())
        denum3 = float(self.denum3.text())
        os = float(self.persen_os.text())
        ts = float(self.sampling_time.text())

        zeta = -1*np.log((os)/100)/math.sqrt(pi**2+(np.log((os)/100))**2)
        zeta = str(round(zeta, 2))
        self.damping_ratio.setText(zeta)
        zeta = float(self.damping_ratio.text())

        wn = 4/((zeta)*(ts))
        wn = str(round(wn, 2))
        self.nat_freq.setText(wn)
        wn = float(self.nat_freq.text())

        num_hs = wn**2
        num_hs = str(round(num_hs, 2))
        self.num_hs.setText(num_hs)
        num_hs = float(self.num_hs.text())

        denum2_hs = 2*zeta*wn
        denum2_hs = str (round(denum2_hs, 4))
        denum3_hs = wn**2
        denum3_hs = str (round(denum3_hs, 4))
        denum_hs = "s^2 + " + denum2_hs + "s + " + denum3_hs
        self.denum_hs.setText(denum_hs)
        denum_hs = self.denum_hs.text()

        koef_hs = [1,denum2_hs,denum3_hs]
        global s_hs 
        s_hs = np.roots(koef_hs)
        self.s_hs.setText(str(s_hs))

        global s_awal
        koef_awal = [denum1,denum2,denum3]
        s_awal = np.roots(koef_awal)
        self.s_awal.setText(str(s_awal))

        print(s_hs)
        print(s_awal)

    def plot(self):

        fig, ax = plt.subplots()
        ax.axhline(y=0, color='black')
        ax.axvline(x=0, color='black')
        ax.scatter(s_hs.real, s_hs.imag, color='blue')
        ax.scatter(s_awal.real, s_awal.imag, color='red')

        plt.show()
    
    def letak(self):

        float(s_hs.imag[0])
        float(s_hs.real[0])
        teta_3 = float(self.teta_3.text()) 
        x = -(s_hs.imag[1]/np.tan(teta_3)+s_hs.real[0])
        x = str (round(x, 2))
        self.x.setText(x)
        x = float(self.x.text())

        gpd_hasil = "s +" + str(-x)
        self.gpd.setText(gpd_hasil)

        #KD

        gs = 1/(denum1*(s_hs[0]**2)+denum2*s_hs[0]+denum3)
        gpd = (s_hs[0]-(x))
        denum_kd= gs*gpd
        kd_hasil = (1/denum_kd)
        kd = abs(kd_hasil)

        kd = str(round(kd, 2))
        self.kd.setText(kd)
    
 


app = QApplication([])
mainwindow = Modul_2()
app.setQuitOnLastWindowClosed(True)
mainwindow.show()
sys.exit(app.exec_())