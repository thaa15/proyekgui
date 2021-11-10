# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Modul_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Modul_1(object):
    def setupUi(self, Modul_1):
        Modul_1.setObjectName("Modul_1")
        Modul_1.resize(785, 740)
        self.centralwidget = QtWidgets.QWidget(Modul_1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, -10, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    font: bold 15px;\n"
"color: white;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(650, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}")
        self.back_button.setObjectName("back_button")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 60, 531, 131))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox{\n"
"    background: #EDEEE9;\n"
"    border: 1px solid #012A3B;\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.frekuensi_input = QtWidgets.QTextEdit(self.groupBox)
        self.frekuensi_input.setGeometry(QtCore.QRect(10, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.frekuensi_input.setFont(font)
        self.frekuensi_input.setStyleSheet("QTextEdit{\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"    border: 1px solid #012A3B;\n"
"}\n"
"\n"
"QTextEdit:hover{\n"
"    border: 1px solid #012A3B;\n"
"}")
        self.frekuensi_input.setTabChangesFocus(True)
        self.frekuensi_input.setObjectName("frekuensi_input")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(150, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.koefisien_input = QtWidgets.QTextEdit(self.groupBox)
        self.koefisien_input.setGeometry(QtCore.QRect(10, 80, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.koefisien_input.setFont(font)
        self.koefisien_input.setStyleSheet("QTextEdit{\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"    border: 1px solid #012A3B;\n"
"}\n"
"\n"
"QTextEdit:hover{\n"
"    border: 1px solid #012A3B;\n"
"}")
        self.koefisien_input.setTabChangesFocus(True)
        self.koefisien_input.setObjectName("koefisien_input")
        self.plotfir = QtWidgets.QPushButton(self.groupBox)
        self.plotfir.setGeometry(QtCore.QRect(450, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.plotfir.setFont(font)
        self.plotfir.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}")
        self.plotfir.setObjectName("plotfir")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(190, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.sample_rate = QtWidgets.QTextEdit(self.groupBox)
        self.sample_rate.setGeometry(QtCore.QRect(190, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.sample_rate.setFont(font)
        self.sample_rate.setStyleSheet("QTextEdit{\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"    border: 1px solid #012A3B;\n"
"}\n"
"\n"
"QTextEdit:hover{\n"
"    border: 1px solid #012A3B;\n"
"}")
        self.sample_rate.setTabChangesFocus(True)
        self.sample_rate.setObjectName("sample_rate")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(320, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lowpass = QtWidgets.QRadioButton(self.groupBox)
        self.lowpass.setGeometry(QtCore.QRect(190, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.lowpass.setFont(font)
        self.lowpass.setObjectName("lowpass")
        self.highpass = QtWidgets.QRadioButton(self.groupBox)
        self.highpass.setGeometry(QtCore.QRect(190, 80, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.highpass.setFont(font)
        self.highpass.setObjectName("highpass")
        self.bandpass = QtWidgets.QRadioButton(self.groupBox)
        self.bandpass.setGeometry(QtCore.QRect(190, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.bandpass.setFont(font)
        self.bandpass.setObjectName("bandpass")
        self.blackmann = QtWidgets.QRadioButton(self.groupBox)
        self.blackmann.setGeometry(QtCore.QRect(320, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.blackmann.setFont(font)
        self.blackmann.setObjectName("blackmann")
        self.hamming = QtWidgets.QRadioButton(self.groupBox)
        self.hamming.setGeometry(QtCore.QRect(320, 80, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.hamming.setFont(font)
        self.hamming.setObjectName("hamming")
        self.hanning = QtWidgets.QRadioButton(self.groupBox)
        self.hanning.setGeometry(QtCore.QRect(320, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.hanning.setFont(font)
        self.hanning.setObjectName("hanning")
        self.frekuensi_input_2 = QtWidgets.QTextEdit(self.groupBox)
        self.frekuensi_input_2.setGeometry(QtCore.QRect(360, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.frekuensi_input_2.setFont(font)
        self.frekuensi_input_2.setStyleSheet("QTextEdit{\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"    border: 1px solid #012A3B;\n"
"}\n"
"\n"
"QTextEdit:hover{\n"
"    border: 1px solid #012A3B;\n"
"}")
        self.frekuensi_input_2.setTabChangesFocus(True)
        self.frekuensi_input_2.setObjectName("frekuensi_input_2")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(490, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(360, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.firplotet = firplotet(self.centralwidget)
        self.firplotet.setGeometry(QtCore.QRect(50, 200, 681, 241))
        self.firplotet.setStyleSheet("QWidget{\n"
"    background: #EDEEE9;\n"
"}")
        self.firplotet.setObjectName("firplotet")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 781, 731))
        self.label_2.setStyleSheet("QLabel{\n"
"    background:#012A3B;\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.stepresponse = stepresponse(self.centralwidget)
        self.stepresponse.setGeometry(QtCore.QRect(50, 460, 681, 231))
        self.stepresponse.setStyleSheet("QWidget{\n"
"    background: #EDEEE9;\n"
"}")
        self.stepresponse.setObjectName("stepresponse")
        self.nama_label = QtWidgets.QLabel(self.centralwidget)
        self.nama_label.setGeometry(QtCore.QRect(10, 0, 161, 21))
        self.nama_label.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.nama_label.setObjectName("nama_label")
        self.npm_label = QtWidgets.QLabel(self.centralwidget)
        self.npm_label.setGeometry(QtCore.QRect(10, 20, 171, 21))
        self.npm_label.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.npm_label.setObjectName("npm_label")
        self.label_2.raise_()
        self.label.raise_()
        self.back_button.raise_()
        self.groupBox.raise_()
        self.firplotet.raise_()
        self.stepresponse.raise_()
        self.nama_label.raise_()
        self.npm_label.raise_()
        Modul_1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Modul_1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 785, 18))
        self.menubar.setObjectName("menubar")
        Modul_1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Modul_1)
        self.statusbar.setObjectName("statusbar")
        Modul_1.setStatusBar(self.statusbar)

        self.retranslateUi(Modul_1)
        QtCore.QMetaObject.connectSlotsByName(Modul_1)

    def retranslateUi(self, Modul_1):
        _translate = QtCore.QCoreApplication.translate
        Modul_1.setWindowTitle(_translate("Modul_1", "MainWindow"))
        self.label.setText(_translate("Modul_1", "MODUL FILTER FIR"))
        self.back_button.setText(_translate("Modul_1", "MENU AWAL"))
        self.groupBox.setTitle(_translate("Modul_1", "Masukkan parameter - parameter di bawah ini:"))
        self.frekuensi_input.setHtml(_translate("Modul_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Modul_1", "   Hz"))
        self.label_4.setText(_translate("Modul_1", "PANJANG KOEFISIEN"))
        self.koefisien_input.setHtml(_translate("Modul_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.plotfir.setText(_translate("Modul_1", "Plot!"))
        self.label_6.setText(_translate("Modul_1", "FREKUENSI CUT-OFF"))
        self.label_8.setText(_translate("Modul_1", "SAMPLE RATE"))
        self.sample_rate.setHtml(_translate("Modul_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.label_10.setText(_translate("Modul_1", "   Hz"))
        self.lowpass.setText(_translate("Modul_1", "Low Pass"))
        self.highpass.setText(_translate("Modul_1", "High Pass"))
        self.bandpass.setText(_translate("Modul_1", "Band Pass"))
        self.blackmann.setText(_translate("Modul_1", "Blackmann"))
        self.hamming.setText(_translate("Modul_1", "Hamming"))
        self.hanning.setText(_translate("Modul_1", "Hanning"))
        self.frekuensi_input_2.setHtml(_translate("Modul_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.label_13.setText(_translate("Modul_1", "   Hz"))
        self.label_14.setText(_translate("Modul_1", "FREKUENSI CUT-OFF2"))
        self.nama_label.setText(_translate("Modul_1", "Nama:"))
        self.npm_label.setText(_translate("Modul_1", "NPM: "))
from firplotet import firplotet
from stepresponse import stepresponse


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Modul_1 = QtWidgets.QMainWindow()
    ui = Ui_Modul_1()
    ui.setupUi(Modul_1)
    Modul_1.show()
    sys.exit(app.exec_())
