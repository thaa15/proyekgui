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
        self.btngroup1 = QButtonGroup()
        self.btngroup2 = QButtonGroup()

        self.btngroup1.addButton(self.lowpass)
        self.btngroup1.addButton(self.highpass)
        self.btngroup1.addButton(self.bandpass)
        self.btngroup2.addButton(self.blackmann)
        self.btngroup2.addButton(self.hamming)
        self.btngroup2.addButton(self.hanning)
        self.lowpass.toggled.connect(lambda: self.filterstate(self.lowpass))
        self.highpass.toggled.connect(lambda: self.filterstate(self.highpass))
        self.bandpass.toggled.connect(lambda: self.filterstate(self.bandpass))

        self.blackmann.toggled.connect(
            lambda: self.methodstate(self.blackmann))
        self.hamming.toggled.connect(lambda: self.methodstate(self.hamming))
        self.hanning.toggled.connect(lambda: self.methodstate(self.hanning))

    def filterstate(self, b):
        if b.text() == "Low Pass":
            if b.isChecked() == True:
                self.filter = "lowpass"

        if b.text() == "High Pass":
            if b.isChecked() == True:
                self.filter = "highpass"

        if b.text() == "Band Pass":
            if b.isChecked() == True:
                self.filter = "bandpass"

    def methodstate(self, b):
        if b.text() == "Blackmann":
            if b.isChecked() == True:
                self.method = "blackman"

        if b.text() == "Hamming":
            if b.isChecked() == True:
                self.method = "hamming"

        if b.text() == "Hanning":
            if b.isChecked() == True:
                self.method = "hann"

    def plot_gambar_fir(self):
        try:
            nsamples = int(self.koefisien_input.toPlainText())
            cutoff_hz = int(self.frekuensi_input.toPlainText())
            cutoff_hz2 = 0
            sample_rate = int(self.sample_rate.toPlainText())
            if nsamples % 2 == 0:
                nsamples = nsamples + 1
            passzero = True
            if self.filter == "highpass" or self.filter == "bandpass":
                passzero = False
            if self.filter == "bandpass":
                cutoff_hz2 = int(self.frekuensi_input_2.toPlainText())
                taps = firwin(nsamples, cutoff=[
                              cutoff_hz/sample_rate, cutoff_hz2/sample_rate], window=self.method, pass_zero=passzero)
            else:
                taps = firwin(nsamples, cutoff=cutoff_hz/sample_rate,
                              window=self.method, pass_zero=passzero)
            w, h = freqz(taps, 1)
            impulse = repeat(0., len(taps))
            impulse[0] = 1.
            x = arange(0, len(taps))
            response = lfilter(taps, 1, impulse)

            self.firplotet.canvas.axes.clear()
            self.firplotet.canvas.axes.plot(
                w/max(w), 20*np.log10(np.absolute(h)))
            self.firplotet.canvas.axes.set_xlabel("Normalized Frequncy")
            self.firplotet.canvas.axes.set_ylabel("Magnitude (db)")
            self.firplotet.canvas.axes.set_title("Frequency Response")
            self.firplotet.canvas.axes.grid()
            self.firplotet.canvas.figure.tight_layout()
            self.firplotet.canvas.draw()

            self.stepresponse.canvas.axes.clear()
            self.stepresponse.canvas.axes.plot(x, response)
            self.stepresponse.canvas.axes.set_xlabel("Frequncy")
            self.stepresponse.canvas.axes.set_ylabel(f'{nsamples} (sample)')
            self.stepresponse.canvas.axes.set_title("Impulse Response")
            self.stepresponse.canvas.axes.grid()
            self.stepresponse.canvas.figure.tight_layout()
            self.stepresponse.canvas.draw()
        except Exception:
            QMessageBox.about(self, "Error","Isi semua input!")

    def back_main_menu(self):
        self.CurrentWindow = Modul_modulpage()
        self.CurrentWindow.show()
        self.close()


app = QApplication([])
mainwindow = LoginPage()
app.setQuitOnLastWindowClosed(True)
mainwindow.show()
sys.exit(app.exec_())
