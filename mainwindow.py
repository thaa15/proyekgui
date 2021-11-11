from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import sys
import numpy as np
import math
import cmath
from pylab import *
from scipy.signal import lfilter, firwin, freqz
import cv2
import pytesseract
import requests
#import gambar_rc
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\abang\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'


class LoginPage(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("Login_Page.ui", self)
        self.setWindowTitle("Login Page")

        self.signin_button.clicked.connect(self.tombol_login)
        self.camera_button.clicked.connect(self.open_camera)
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
            self.nama = str(self.nama_input.toPlainText())
            self.npm = int(self.npm_input.toPlainText())
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Tekan Tombol 'OK' Untuk Masuk.")
            self.msg.setWindowTitle("Berhasil Masuk!")
            self.msg.buttonClicked.connect(self.nextpage_pressed)
            self.msg.show()
            payload = {'name':self.nama, 'npm': self.npm, 'activity' : 'Main Menu'}
            r = requests.post('https://gui-kel-1.herokuapp.com/profiles', json=payload)
            self.token = r.json()['data']['profilesId']
            print(self.token, type(self.token))
        except Exception:
            if len(self.nama) == 0:
                QMessageBox.about(self, "Eror Kosong Text",
                                  "Jangan kosongkan input!")
            else:
                QMessageBox.about(self, "Eror Input Bukan NPM",
                                  "Masukkan NPM dengan Benar!")

    def open_camera(self):
        self.CurrentWindow = CameraOpen()
        self.CurrentWindow.show()
        self.close()

    def nextpage_pressed(self):
        self.CurrentWindow = Modul_modulpage(self.nama, self.npm, self.token)
        self.CurrentWindow.show()
        self.close()


class CameraOpen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("Camera_login.ui", self)
        self.setWindowTitle("Letakkan KTM depan Kamera!")
        self.back_button.clicked.connect(self.to_main_login)
        self.Camera = Camera()
        self.Camera.start()
        self.Camera.ImageUpdate.connect(self.ImageUpdateSlot)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def to_main_login(self):
        self.Camera.stop()
        self.CurrentWindow = LoginPage()
        self.CurrentWindow.show()
        self.close()


class Camera(QThread):
    ImageUpdate = pyqtSignal(QImage)
    font = cv2.FONT_HERSHEY_PLAIN

    def run(self):
        Capture = cv2.VideoCapture(0)
        self.ThreadActive = True
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                imgH, imgW, _ = frame.shape
                imgchar = pytesseract.image_to_string(frame)
                print(imgchar)
                imgboxes = pytesseract.image_to_boxes(frame)
                for boxes in imgboxes.splitlines():
                    boxes = boxes.split(' ')
                    x, y, w, h = int(boxes[1]), int(
                        boxes[2]), int(boxes[3]), int(boxes[4])
                    cv2.rectangle(frame, (x, imgH-y),
                                  (w, imgH-h), (0, 0, 255), 3)
                strings = imgchar.splitlines()
                FlippedImage = cv2.flip(frame, 1)
                ConvertToQtFormat = QImage(
                    FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)

            else:
                break

    def stop(self):
        self.ThreadActive = False


class Modul_modulpage(QMainWindow):
    def __init__(self, nama, npm, token):
        self.nama = nama
        self.npm = npm
        self.token = token
        QMainWindow.__init__(self)
        loadUi("Modul_modulpage.ui", self)
        self.setWindowTitle("Pilih Modul")
        self.modul_1_button.clicked.connect(self.modul_1Page)
        self.modul_2_button.clicked.connect(self.modul_2Page)
        self.modul_6_button.clicked.connect(self.modul_6Page)
        self.logout_button.clicked.connect(self.logoutPage)
        self.nama_label.setText(f'Nama: {self.nama}')
        self.npm_label.setText(f'NPM: {self.npm}')

    def modul_1Page(self):
        payload = {'activity' : 'Modul 1'}
        requests.put(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}', data=payload)
        self.CurrentWindow = Modul_1(self.nama, self.npm, self.token)
        self.CurrentWindow.show()
        self.close()

    def modul_2Page(self):
        payload = {'activity' : 'Modul 2'}
        requests.put(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}', data=payload)
        self.CurrentWindow = Modul_2(self.nama, self.npm, self.token)
        self.CurrentWindow.show()
        self.close()

    def modul_6Page(self):
        payload = {'activity' : 'Modul 6'}
        requests.put(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}', data=payload)
        self.CurrentWindow = Modul_6(self.nama, self.npm, self.token)
        self.CurrentWindow.show()
        self.close()

    def logoutPage(self):
        requests.delete(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}')
        self.CurrentWindow = LoginPage()
        self.CurrentWindow.show()
        self.close()


class Modul_1(QMainWindow):
    def __init__(self, nama, npm, token):
        self.nama = nama
        self.npm = npm
        self.token = token
        QMainWindow.__init__(self)
        loadUi("Modul_1.ui", self)
        self.setWindowTitle("Modul 1 - Finite Response Impulse")
        self.plotfir.clicked.connect(self.plot_gambar_fir)
        self.back_button.clicked.connect(self.back_main_menu)
        self.nama_label.setText(f'Nama: {self.nama}')
        self.npm_label.setText(f'NPM: {self.npm}')
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
            self.cutoff_hz = int(self.frekuensi_input.toPlainText())
            self.cutoff_hz2 = 0
            sample_rate = int(self.sample_rate.toPlainText())
            if nsamples % 2 == 0:
                nsamples = nsamples + 1
            passzero = True
            if self.filter == "highpass" or self.filter == "bandpass":
                passzero = False
            if self.filter == "bandpass":
                self.cutoff_hz2 = int(self.frekuensi_input_2.toPlainText())
                taps = firwin(nsamples, cutoff=[
                              self.cutoff_hz/sample_rate, self.cutoff_hz2/sample_rate], window=self.method, pass_zero=passzero)
            else:
                taps = firwin(nsamples, cutoff=self.cutoff_hz/sample_rate,
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
            QMessageBox.about(self, "Error", "Isi semua input!")

    def back_main_menu(self):
        payload = {'activity' : 'Main Menu'}
        requests.put(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}', data=payload)
        self.CurrentWindow = Modul_modulpage(self.nama, self.npm, self.token)
        self.CurrentWindow.show()
        self.close()


class Modul_2(QMainWindow):
    def __init__(self, nama, npm, token):
        self.nama = nama
        self.npm = npm
        self.token = token
        QMainWindow.__init__(self)
        loadUi("Modul_2.ui", self)
        self.setWindowTitle("Modul 2 - Root Locus")
        self.calculate.clicked.connect(self.hitung)
        self.plot_akar.clicked.connect(self.plot)
        self.cari_letak.clicked.connect(self.letak)
        self.hitung_ki.clicked.connect(self.hitungKI)
        self.pushButton.clicked.connect(self.back_main_menu)

    def hitung(self):
        try:
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
            denum2_hs = str(round(denum2_hs, 4))
            denum3_hs = wn**2
            denum3_hs = str(round(denum3_hs, 4))
            denum_hs = "s^2 + " + denum2_hs + "s + " + denum3_hs
            self.denum_hs.setText(denum_hs)
            denum_hs = self.denum_hs.text()

            koef_hs = [1, denum2_hs, denum3_hs]
            global s_hs
            s_hs = np.roots(koef_hs)
            self.s_hs.setText(str(s_hs))

            global s_awal
            koef_awal = [denum1, denum2, denum3]
            s_awal = np.roots(koef_awal)
            self.s_awal.setText(str(s_awal))
        except Exception:
            QMessageBox.about(self, "Error", "Isi semua input!")

    def plot(self):
        try:
            fig, ax = plt.subplots()
            ax.axhline(y=0, color='black')
            ax.axvline(x=0, color='black')
            ax.scatter(s_hs.real, s_hs.imag, color='blue')
            ax.scatter(s_awal.real, s_awal.imag, color='red')
            plt.show()
        except Exception:
            QMessageBox.about(self, "Error", "Isi semua input!")

    def letak(self):
        try:
            float(s_hs.imag[0])
            float(s_hs.real[0])
            teta_3 = float(self.teta_3.text())
            x = -(s_hs.imag[1]/np.tan(teta_3)+s_hs.real[0])
            x = str(round(x, 2))
            self.x.setText(x)
            x = float(self.x.text())

            gpd_hasil = "s +" + str(-x)
            self.gpd.setText(gpd_hasil)

            # KD
            global kd_hasil

            gs = 1/(denum1*(s_hs[0]**2)+denum2*s_hs[0]+denum3)
            gpd = (s_hs[0]-(x))
            denum_kd = gs*gpd
            kd_hasil = (1/denum_kd)
            kd = abs(kd_hasil)

            kd = str(round(kd, 2))
            self.kd.setText(kd)
        except Exception:
            QMessageBox.about(self, "Error", "Isi semua input!")
    
    def hitungKI(self):
        
        zero_gpi = float(self.zero_gpi.text())
        gpi = (s_hs[0]+zero_gpi)/(s_hs[0])
        ki_hasil = kd_hasil*(1/gpi)
        ki = abs(ki_hasil)

        ki = str(round(ki,2))
        self.ki.setText(ki)


    def back_main_menu(self):
        payload = {'activity' : 'Main Menu'}
        requests.put(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}', data=payload)
        self.CurrentWindow = Modul_modulpage(self.nama, self.npm, self.token)
        self.CurrentWindow.show()
        self.close()


class Modul_6(QMainWindow):
    def __init__(self, nama, npm, token):
        self.nama = nama
        self.npm = npm
        self.token = token
        QMainWindow.__init__(self)
        loadUi("Modul_6.ui", self)
        self.setWindowTitle("Modul 6 (Kalkulator) - Regresi dan Klasifikasi")
        self.back_button.clicked.connect(self.back_main_menu)
        self.nama_label.setText(f'Nama: {self.nama}')
        self.npm_label.setText(f'NPM: {self.npm}')
        self.tabWidget.setTabText(0, "Regresi")
        self.tabWidget.setTabText(1, "KNN")
        self.predict_button.clicked.connect(self.predicted_value)
        self.plotGraph.clicked.connect(self.plotgrap)
        self.btngroup1 = QButtonGroup()
        self.btngroup2 = QButtonGroup()
        self.btngroup1.addButton(self.W_norm)
        self.btngroup1.addButton(self.lnW_norm)
        self.btngroup1.addButton(self.logW_norm)
        self.btngroup1.addButton(self.seperW_norm)
        self.btngroup2.addButton(self.Y_norm)
        self.btngroup2.addButton(self.lnY_norm)
        self.btngroup2.addButton(self.logY_norm)
        self.btngroup2.addButton(self.seperY_norm)
        self.W_norm.toggled.connect(lambda: self.chooseW(self.W_norm))
        self.lnW_norm.toggled.connect(lambda: self.chooseW(self.lnW_norm))
        self.logW_norm.toggled.connect(lambda: self.chooseW(self.logW_norm))
        self.seperW_norm.toggled.connect(
            lambda: self.chooseW(self.seperW_norm))

        self.Y_norm.toggled.connect(lambda: self.chooseY(self.Y_norm))
        self.lnY_norm.toggled.connect(lambda: self.chooseY(self.lnY_norm))
        self.logY_norm.toggled.connect(lambda: self.chooseY(self.logY_norm))
        self.seperY_norm.toggled.connect(
            lambda: self.chooseY(self.seperY_norm))

    def chooseW(self, a):
        if a.text() == "W":
            if a.isChecked() == True:
                self.chW = "norm"
        if a.text() == "ln W":
            if a.isChecked() == True:
                self.chW = "ln"
        if a.text() == "log W":
            if a.isChecked() == True:
                self.chW = "log"
        if a.text() == "1/W":
            if a.isChecked() == True:
                self.chW = "seper"

    def chooseY(self, b):
        if b.text() == "Y":
            if b.isChecked() == True:
                self.chY = "norm"
        if b.text() == "ln Y":
            if b.isChecked() == True:
                self.chY = "ln"
        if b.text() == "log Y":
            if b.isChecked() == True:
                self.chY = "log"
        if b.text() == "1/Y":
            if b.isChecked() == True:
                self.chY = "seper"

    def plotgrap(self):
        try:
            nilai_w = self.nilai_W.toPlainText()
            nilai_y = self.nilai_Y.toPlainText()
            nilai_w_list = []
            nilai_y_list = []
            for nilai in nilai_w.splitlines():
                nilai_w_list.append(float(nilai))
            for nilai in nilai_y.splitlines():
                nilai_y_list.append(float(nilai))

            if self.chW == "norm":
                nilai_w_list = nilai_w_list
            elif self.chW == "ln":
                nilai_w_list = list(np.log(nilai_w_list))
            elif self.chW == "log":
                nilai_w_list = list(np.log10(nilai_w_list))
            else:
                nilai_w_list = [1/x for x in nilai_w_list]

            if self.chY == "norm":
                nilai_y_list = nilai_y_list
            elif self.chY == "ln":
                nilai_y_list = list(np.log(nilai_y_list))
            elif self.chY == "log":
                nilai_y_list = list(np.log10(nilai_y_list))
            else:
                nilai_y_list = [1/y for y in nilai_y_list]

            sum_of_xy = 0
            sum_of_x = 0
            sum_of_y = 0
            sum_of_xsquare = 0
            sum_of_ysquare = 0
            for i in range(len(nilai_w_list)):
                sum_of_xy = sum_of_xy + nilai_w_list[i]*nilai_y_list[i]
            for i in range(len(nilai_w_list)):
                sum_of_x = sum_of_x + nilai_w_list[i]
            for i in range(len(nilai_w_list)):
                sum_of_y = sum_of_y + nilai_y_list[i]
            for i in range(len(nilai_w_list)):
                sum_of_xsquare = sum_of_xsquare + nilai_w_list[i]**2
            for i in range(len(nilai_y_list)):
                sum_of_ysquare = sum_of_ysquare + nilai_y_list[i]**2
            mean_w = sum_of_x/(len(nilai_w_list))
            mean_y = sum_of_y/(len(nilai_y_list))
            self.w = (len(nilai_w_list)*sum_of_xy - sum_of_x*sum_of_y) / \
                (len(nilai_w_list)*sum_of_xsquare-(sum_of_x)**2)
            self.b = mean_y - self.w*mean_w
            mse_raw = 0
            x = np.linspace(0, max(nilai_w_list), 1000)
            y = self.w*x + self.b
            for i in range(len(nilai_w_list)): 
                mse_raw = mse_raw + (self.b + nilai_w_list[i]*self.w - nilai_y_list[i])**2
            korelation_r = (len(nilai_w_list)*sum_of_xy - sum_of_x*sum_of_y)/(math.sqrt((len(nilai_w_list)*sum_of_xsquare-(sum_of_x)**2))*math.sqrt(len(nilai_y_list)*sum_of_ysquare-(sum_of_y)**2))
            mse = mse_raw/(len(nilai_w_list))
            self.korelasi.setText(f'R = {"{:.2f}".format(korelation_r)}')
            self.mse.setText(f'MSE = {"{:.2f}".format(mse)}')
            self.persamaan.setText(
                f'Y = {"{:.2f}".format(self.w)}x + {"{:.2f}".format(self.b)}')
            fig, ax = plt.subplots()
            ax.scatter(nilai_w_list, nilai_y_list, color='blue')
            ax.plot(x, y, color='red')
            plt.show()
        except Exception:
            QMessageBox.about(self, "Error", "Isi semua input dengan benar!")

    def predicted_value(self):
        try:
            nilai_prediksi = float(self.prediksi.toPlainText())
            y_prediksi = self.w*nilai_prediksi + self.b
            if self.chY == "seper":
                y_prediksi = 1/y_prediksi
            elif self.chY == "ln":
                y_prediksi = np.exp(y_prediksi)
            elif self.chY == "log":
                y_prediksi = 10**(y_prediksi)
            self.hasil_predik.setText(f'{"{:.2f}".format(y_prediksi)}')
        except Exception:
            QMessageBox.about(self, "Error", "Bukan Nilai!")

    def back_main_menu(self):
        payload = {'activity' : 'Main Menu'}
        requests.put(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}', data=payload)
        self.CurrentWindow = Modul_modulpage(self.nama, self.npm, self.token)
        self.CurrentWindow.show()
        self.close()


app = QApplication([])
mainwindow = LoginPage()
app.setQuitOnLastWindowClosed(True)
mainwindow.show()
sys.exit(app.exec_())
