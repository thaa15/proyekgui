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
        Modul_1.resize(776, 547)
        self.centralwidget = QtWidgets.QWidget(Modul_1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 0, 471, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(640, 10, 91, 31))
        self.back_button.setObjectName("back_button")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 60, 331, 131))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 101, 41))
        self.label_2.setObjectName("label_2")
        self.frekuensi_input = QtWidgets.QTextEdit(self.groupBox)
        self.frekuensi_input.setGeometry(QtCore.QRect(90, 30, 131, 31))
        self.frekuensi_input.setTabChangesFocus(True)
        self.frekuensi_input.setObjectName("frekuensi_input")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(240, 20, 31, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 101, 51))
        self.label_4.setObjectName("label_4")
        self.koefisien_input = QtWidgets.QTextEdit(self.groupBox)
        self.koefisien_input.setGeometry(QtCore.QRect(90, 80, 131, 31))
        self.koefisien_input.setTabChangesFocus(True)
        self.koefisien_input.setObjectName("koefisien_input")
        self.plotfir = QtWidgets.QPushButton(self.groupBox)
        self.plotfir.setGeometry(QtCore.QRect(255, 96, 61, 31))
        self.plotfir.setObjectName("plotfir")
        self.firplotet = firplotet(self.centralwidget)
        self.firplotet.setGeometry(QtCore.QRect(30, 200, 721, 301))
        self.firplotet.setObjectName("firplotet")
        Modul_1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Modul_1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 18))
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
        self.label_2.setText(_translate("Modul_1", "FREKUENSI CUT-OFF"))
        self.frekuensi_input.setHtml(_translate("Modul_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Modul_1", "kHz"))
        self.label_4.setText(_translate("Modul_1", "PANJANG KOEFISIEN"))
        self.koefisien_input.setHtml(_translate("Modul_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.plotfir.setText(_translate("Modul_1", "Plot!"))
from firplotet import firplotet


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Modul_1 = QtWidgets.QMainWindow()
    ui = Ui_Modul_1()
    ui.setupUi(Modul_1)
    Modul_1.show()
    sys.exit(app.exec_())
