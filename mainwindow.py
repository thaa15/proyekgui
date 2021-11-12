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
        self.token = "null"
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
        self.modul_3_button.clicked.connect(self.modul_3Page)
        self.modul_6_button.clicked.connect(self.modul_6Page)
        self.logout_button.clicked.connect(self.logoutPage)
        self.nama_label.setText(f'Nama: {self.nama}')
        self.npm_label.setText(f'NPM: {self.npm}')
        app.aboutToQuit.connect(self.closeEvent)
        self.force_close = True

    def modul_1Page(self):
        payload = {'activity' : 'Modul 1'}
        requests.put(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}', data=payload)
        self.CurrentWindow = Modul_1(self.nama, self.npm, self.token)
        self.CurrentWindow.show()
        self.force_close = False
        self.close()

    def modul_2Page(self):
        payload = {'activity' : 'Modul 2'}
        requests.put(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}', data=payload)
        self.CurrentWindow = Modul_2(self.nama, self.npm, self.token)
        self.force_close = False
        self.CurrentWindow.show()
        self.close()
    
    def modul_3Page(self):
        payload = {'activity' : 'Modul 3'}
        requests.put(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}', data=payload)
        self.CurrentWindow = Modul_3(self.nama, self.npm, self.token)
        self.force_close = False
        self.CurrentWindow.show()
        self.close()

    def modul_6Page(self):
        payload = {'activity' : 'Modul 6'}
        requests.put(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}', data=payload)
        self.CurrentWindow = Modul_6(self.nama, self.npm, self.token)
        self.force_close = False
        self.CurrentWindow.show()
        self.close()

    def logoutPage(self):
        requests.delete(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}')
        self.CurrentWindow = LoginPage()
        self.CurrentWindow.show()
        self.force_close = False
        self.close()
    def closeEvent(self, event):
        if self.force_close is True:
            requests.delete(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}')
            sys.exit(0)


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
        app.aboutToQuit.connect(self.closeEvent)
        self.force_close = True
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
        self.force_close = False
        self.CurrentWindow.show()
        self.close()

    def closeEvent(self, event):
        if self.force_close is True:
            requests.delete(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}')
            sys.exit(0)


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
        app.aboutToQuit.connect(self.closeEvent)
        self.force_close = True

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
            zeta = str("{:.2f}".format(zeta))
            self.damping_ratio.setText(zeta)
            zeta = float(self.damping_ratio.text())

            wn = 4/((zeta)*(ts))
            wn = str("{:.2f}".format(wn))
            self.nat_freq.setText(wn)
            wn = float(self.nat_freq.text())

            num_hs = wn**2
            num_hs = str("{:.2f}".format(num_hs))
            self.num_hs.setText(num_hs)
            num_hs = float(self.num_hs.text())

            denum2_hs = 2*zeta*wn
            denum2_hs = str("{:.2f}".format(denum2_hs))
            denum3_hs = wn**2
            denum3_hs = str("{:.2f}".format(denum3_hs))
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
        self.force_close = False
        self.CurrentWindow.show()
        self.close()

    def closeEvent(self, event):
        if self.force_close is True:
            requests.delete(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}')
            sys.exit(0)

class Modul_3(QMainWindow):
    def __init__(self, nama, npm, token):
        self.nama = nama
        self.npm = npm
        self.token = token
        QMainWindow.__init__(self)
        loadUi("Modul_3.ui", self)
        self.setWindowTitle("Modul 3 - Saluran Transmisi")
        self.namanpm.setText(f'{self.nama}-{self.npm}')
        self.calculate.clicked.connect(self.hitung)
        self.menu.clicked.connect(self.back_main_menu)
        app.aboutToQuit.connect(self.closeEvent)
        self.force_close = True
    
    def hitung(self):
        try: 
        #ngambil data hubung singkat
            global lokasiHS_1, lokasiHS_2, lokasiHS_3, lokasiHS_4, lokasiHS_5
            global arusHS_1, arusHS_2, arusHS_3, arusHS_4, arusHS_5
            lokasiHS_1 = float(self.lokasi_hs_1.text())
            lokasiHS_2 = float(self.lokasi_hs_2.text())
            lokasiHS_3 = float(self.lokasi_hs_3.text())
            lokasiHS_4 = float(self.lokasi_hs_4.text())
            lokasiHS_5 = float(self.lokasi_hs_5.text())
            arusHS_1 = float(self.arus_hs_1.text())
            arusHS_2 = float(self.arus_hs_2.text())
            arusHS_3 = float(self.arus_hs_3.text())
            arusHS_4 = float(self.arus_hs_4.text())
            arusHS_5 = float(self.arus_hs_5.text())

            #ngambil data resistif
            global lokasiR_1, lokasiR_2, lokasiR_3, lokasiR_4, lokasiR_5
            global arusR_1, arusR_2, arusR_3, arusR_4, arusR_5
            lokasiR_1 = float(self.lokasi_r_1.text())
            lokasiR_2 = float(self.lokasi_r_2.text())
            lokasiR_3 = float(self.lokasi_r_3.text())
            lokasiR_4 = float(self.lokasi_r_4.text())
            lokasiR_5 = float(self.lokasi_r_5.text())
            arusR_1 = float(self.arus_r_1.text())
            arusR_2 = float(self.arus_r_2.text())
            arusR_3 = float(self.arus_r_3.text())
            arusR_4 = float(self.arus_r_4.text())
            arusR_5 = float(self.arus_r_5.text())

            #ngambil data antena
            global lokasiA_1, lokasiA_2, lokasiA_3, lokasiA_4, lokasiA_5
            global arusA_1, arusA_2, arusA_3, arusA_4, arusA_5
            lokasiA_1 = float(self.lokasi_a_1.text())
            lokasiA_2 = float(self.lokasi_a_2.text())
            lokasiA_3 = float(self.lokasi_a_3.text())
            lokasiA_4 = float(self.lokasi_a_4.text())
            lokasiA_5 = float(self.lokasi_a_5.text())
            arusA_1 = float(self.arus_a_1.text())
            arusA_2 = float(self.arus_a_2.text())
            arusA_3 = float(self.arus_a_3.text())
            arusA_4 = float(self.arus_a_4.text())
            arusA_5 = float(self.arus_a_5.text())

            #ngambil data antena
            global lokasiG_1, lokasiG_2, lokasiG_3, lokasiG_4, lokasiG_5
            global arusG_1, arusG_2, arusG_3, arusG_4, arusG_5
            lokasiG_1 = float(self.lokasi_g_1.text())
            lokasiG_2 = float(self.lokasi_g_2.text())
            lokasiG_3 = float(self.lokasi_g_3.text())
            lokasiG_4 = float(self.lokasi_g_4.text())
            lokasiG_5 = float(self.lokasi_g_5.text())
            arusG_1 = float(self.arus_g_1.text())
            arusG_2 = float(self.arus_g_2.text())
            arusG_3 = float(self.arus_g_3.text())
            arusG_4 = float(self.arus_g_4.text())
            arusG_5 = float(self.arus_g_5.text())

            #panjang gelombang pertama
            lamda_13 = 2*(lokasiHS_3 - lokasiHS_1)
            lamda_13 = str(round(lamda_13,2))
            lamda_35 = 2*(lokasiHS_5 - lokasiHS_3)
            lamda_35 = str(round(lamda_35,2))
            lamda_rata = (float(lamda_13) + float(lamda_35))/2
            lamda_rata = str(round(lamda_rata,2))
            self.lamda13.setText(lamda_13)
            self.lamda35.setText(lamda_35)
            self.lamda_rata.setText(lamda_rata)

            #nilai d beban
            d_r = (lokasiR_1 - lokasiHS_1 + lokasiR_3 - lokasiHS_3 + lokasiR_5 - lokasiHS_5)/3
            d_r = str(round(d_r, 2))
            d_a = (lokasiA_1 - lokasiHS_1 + lokasiA_3 - lokasiHS_3 + lokasiA_5 - lokasiHS_5)/3
            d_a = str(round(d_a, 2))
            d_g = (lokasiG_1 - lokasiHS_1 + lokasiG_3 - lokasiHS_3 + lokasiG_5 - lokasiHS_5)/3
            d_g = str(round(d_g, 2))
            self.beban_r.setText(d_r)
            self.beban_a.setText(d_a)
            self.beban_g.setText(d_g)

            #panjang gelombang
            lamdaR = (float(d_r)/float(lamda_rata))
            lamdaR = str(round(lamdaR, 2))
            lamdaA = (float(d_a)/float(lamda_rata))
            lamdaA = str(round(lamdaA, 2))
            lamdaG = (float(d_g)/float(lamda_rata))
            lamdaG = str(round(lamdaG, 2))
            self.lamda_r.setText(lamdaR)
            self.lamda_a.setText(lamdaA)
            self.lamda_g.setText(lamdaG)

            #vswr
            vswr_r = math.sqrt(arusR_2/arusR_1)
            vswr_r = str(round(vswr_r, 2))
            vswr_a = math.sqrt(arusA_2/arusA_1)
            vswr_a = str(round(vswr_a, 2))
            vswr_g = math.sqrt(arusG_2/arusG_1)
            vswr_g = str(round(vswr_g, 2))
            self.vswr_r.setText(vswr_r)
            self.vswr_a.setText(vswr_a)
            self.vswr_g.setText(vswr_g)

            #koefisien pantul
            kp_R = (float(vswr_r) - 1)/(float(vswr_r) + 1)
            kp_R = str(round(kp_R, 2))
            kp_A = (float(vswr_a) - 1)/(float(vswr_a) + 1)
            kp_A = str(round(kp_A, 2))
            kp_G = (float(vswr_g) - 1)/(float(vswr_g) + 1)
            kp_G = str(round(kp_G, 2))
            self.koefpantul_r.setText(kp_R)
            self.koefpantul_a.setText(kp_A)
            self.koefpantul_g.setText(kp_G)

            #return loss
            rl_r = 20*math.log10((float(vswr_r) + 1)/(float(vswr_r) - 1))
            rl_r = str(round(rl_r, 2))
            rl_a = 20*math.log10((float(vswr_a) + 1)/(float(vswr_a) - 1))
            rl_a = str(round(rl_a, 2))
            rl_g = 20*math.log10((float(vswr_g) + 1)/(float(vswr_g) - 1))
            rl_g = str(round(rl_g, 2))
            self.rl_r.setText(rl_r)
            self.rl_a.setText(rl_a)
            self.rl_g.setText(rl_g)

            #presentase daya yang dipantulkan
            pr_r = (float(kp_R)**2)*100
            pr_r = str(round(pr_r, 2))
            persen_r = pr_r + "%"
            pr_a = (float(kp_A)**2)*100
            pr_a = str(round(pr_a, 2))
            persen_a = pr_a + "%"
            pr_g = (float(kp_G)**2)*100
            pr_g = str(round(pr_g, 2))
            persen_g = pr_g + "%"
            self.pr_r.setText(persen_r)
            self.pr_a.setText(persen_a)
            self.pr_g.setText(persen_g)

        except Exception:
            QMessageBox.about(self, "Error", "Isi semua input!")

    def back_main_menu(self):
        payload = {'activity' : 'Main Menu'}
        requests.put(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}', data=payload)
        self.CurrentWindow = Modul_modulpage(self.nama, self.npm, self.token)
        self.force_close = False
        self.CurrentWindow.show()
        self.close()

    def closeEvent(self, event):
        if self.force_close is True:
            requests.delete(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}')
            sys.exit(0)


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
        self.predict_button.clicked.connect(self.predicted_value)
        self.plotGraph.clicked.connect(self.plotgrap)
        app.aboutToQuit.connect(self.closeEvent)
        self.force_close = True
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

            if len(nilai_w_list) != len(nilai_y_list): 
                raise Exception('Panjang Data Fitur dan Label harus sama!')
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
            x = np.linspace(min(nilai_w_list)-1, max(nilai_w_list)+1, 1000)
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
            if len(nilai_w_list) != len(nilai_y_list):
                QMessageBox.about(self, "Error", 'Panjang Data Fitur dan Label harus sama!')
            else:
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
            QMessageBox.about(self, "Error", "Isi semua input!")
        except ValueError:
            QMessageBox.about(self, "Error", "Bukan Nilai!")

    def back_main_menu(self):
        payload = {'activity' : 'Main Menu'}
        requests.put(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}', data=payload)
        self.CurrentWindow = Modul_modulpage(self.nama, self.npm, self.token)
        self.force_close = False
        self.CurrentWindow.show()
        self.close()

    def closeEvent(self, event):
        if self.force_close is True:
            requests.delete(f'https://gui-kel-1.herokuapp.com/profiles/{self.token}')
            sys.exit(0)


app = QApplication([])
mainwindow = LoginPage()
app.setQuitOnLastWindowClosed(True)
mainwindow.show()
sys.exit(app.exec_())
