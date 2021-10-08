from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QIntValidator
import sys
import numpy as np
import math
from pylab import *
from scipy.signal import kaiserord, lfilter, firwin, freqz
#import gambar_rc


class LoginPage(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("Login_Page.ui", self)
        self.setWindowTitle("Login Page")

        self.signin_button.clicked.connect(self.tombol_login)
        self.npm_input.setPlaceholderText("Masukkan NPM Anda!")
        self.nama_input.setPlaceholderText("Masukkan Nama Anda!")
        self.setFocus()
        self.show()
        self.setTabOrder(self.nama_input, self.npm_input)

    def keyPressEvent(self, evt):
        self.npm_input.setFocus()
        self.npm_input.keyPressEvent(evt)
        self.nama_input.setFocus()
        self.nama_input.keyPressEvent(evt)

    def tombol_login(self):
        try:
            nama = str(self.nama_input.toPlainText())
            npm = int(self.npm_input.toPlainText())
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Tekan Tombol 'OK' Untuk Masuk.")
            self.msg.setWindowTitle("Berhasil Masuk!")
            self.msg.buttonClicked.connect(self.nextpage_pressed)
            self.msg.show()
        except Exception:
            if len(nama) == 0:
                QMessageBox.about(self, "Eror Kosong Text",
                                  "Jangan kosongkan input!")
            else:
                QMessageBox.about(self, "Eror Input Bukan NPM",
                                  "Masukkan NPM dengan Benar!")

    def nextpage_pressed(self):
        self.CurrentWindow = Modul_modulpage()
        self.CurrentWindow.show()
        self.close()


class Modul_modulpage(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("Modul_modulpage.ui", self)
        self.setWindowTitle("Pilih Modul")
        self.modul_1_button.clicked.connect(self.modul_1Page)

    def modul_1Page(self):
        self.CurrentWindow = Modul_1()
        self.CurrentWindow.show()
        self.close()


class Modul_1(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("Modul_1.ui", self)
        self.setWindowTitle("Modul 1 - Finite Response Impulse")
        self.plotfir.clicked.connect(self.plot_gambar_fir)
        self.back_button.clicked.connect(self.back_main_menu)

    def plot_gambar_fir(self):
        nsamples = int(self.koefisien_input.toPlainText())
        cutoff_hz = int(self.frekuensi_input.toPlainText())
        sample_rate = 100.0
        t = arange(nsamples) / sample_rate
        x = np.cos(2*np.pi*0.5*t) + 0.2*np.sin(2*np.pi*2.5*t+0.1) + \
                0.2*np.sin(2*np.pi*15.3*t) + 0.1*np.sin(2*np.pi*16.7*t + 0.1) + \
                    0.1*np.sin(2*np.pi*23.45*t+.8)
        # The Nyquist rate of the signal.
        nyq_rate = sample_rate / 2.0

        # The desired width of the transition from pass to stop,
        # relative to the Nyquist rate.  We'll design the filter
        # with a 5 Hz transition width.
        width = 5.0/nyq_rate

        # The desired attenuation in the stop band, in dB.
        ripple_db = 60.0

        # Compute the order and Kaiser parameter for the FIR filter.
        N, beta = kaiserord(ripple_db, width)

        # Use firwin with a Kaiser window to create a lowpass FIR filter.
        taps = firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))

        # Use lfilter to filter x with the FIR filter.
        filtered_x = lfilter(taps, 1.0, x)
        w, h = freqz(taps, worN=8000)
        # samRate = 12000
        # vector = np.vectorize(np.float)
        # n = np.arange(0, koefisien, 1)
        # hd = np.sinc(n-koefisien/2)-(freq/samRate) * \
        #     np.sinc((n-koefisien/2)*(freq/samRate))
        # wn = 0.42-0.5*math.cos(2*math.pi*vector(n)/koefisien) + \
        #     0.08*math.cos(4*math.pi*vector(n)/koefisien)
        # hn = hd*wn
        # hn_fft = fft(hn, 1024)
        # f = np.arange(0, samRate, samRate/(1024/2-1))

        self.firplotet.canvas.axes.clear()
        self.firplotet.canvas.axes.plot((w/np.pi)*nyq_rate, np.absolute(h))
        self.firplotet.canvas.axes.set_xlabel("Frequncy")
        self.firplotet.canvas.axes.set_ylabel("Magnitude")
        self.firplotet.canvas.axes.set_title("Signal FIR")
        self.firplotet.canvas.axes.grid()
        self.firplotet.canvas.figure.tight_layout()
        self.firplotet.canvas.draw()

    def back_main_menu(self):
        self.CurrentWindow = Modul_modulpage()
        self.CurrentWindow.show()
        self.close()


app = QApplication([])
mainwindow = LoginPage()
app.setQuitOnLastWindowClosed(True)
mainwindow.show()
sys.exit(app.exec_())
