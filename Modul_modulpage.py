# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Modul_modulpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Modul_modulpage(object):
    def setupUi(self, Modul_modulpage):
        Modul_modulpage.setObjectName("Modul_modulpage")
        Modul_modulpage.resize(776, 547)
        self.centralwidget = QtWidgets.QWidget(Modul_modulpage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 20, 471, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setGeometry(QtCore.QRect(640, 10, 91, 31))
        self.logout_button.setObjectName("logout_button")
        self.modul_1_button = QtWidgets.QPushButton(self.centralwidget)
        self.modul_1_button.setGeometry(QtCore.QRect(130, 140, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modul_1_button.setFont(font)
        self.modul_1_button.setObjectName("modul_1_button")
        self.modul_2_button = QtWidgets.QPushButton(self.centralwidget)
        self.modul_2_button.setGeometry(QtCore.QRect(410, 140, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modul_2_button.setFont(font)
        self.modul_2_button.setObjectName("modul_2_button")
        self.modul_3_button = QtWidgets.QPushButton(self.centralwidget)
        self.modul_3_button.setGeometry(QtCore.QRect(130, 210, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modul_3_button.setFont(font)
        self.modul_3_button.setObjectName("modul_3_button")
        self.modul_4_button = QtWidgets.QPushButton(self.centralwidget)
        self.modul_4_button.setGeometry(QtCore.QRect(410, 210, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modul_4_button.setFont(font)
        self.modul_4_button.setObjectName("modul_4_button")
        self.modul_5_button = QtWidgets.QPushButton(self.centralwidget)
        self.modul_5_button.setGeometry(QtCore.QRect(130, 280, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modul_5_button.setFont(font)
        self.modul_5_button.setObjectName("modul_5_button")
        self.modul_6_button = QtWidgets.QPushButton(self.centralwidget)
        self.modul_6_button.setGeometry(QtCore.QRect(410, 280, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modul_6_button.setFont(font)
        self.modul_6_button.setObjectName("modul_6_button")
        Modul_modulpage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Modul_modulpage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 18))
        self.menubar.setObjectName("menubar")
        Modul_modulpage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Modul_modulpage)
        self.statusbar.setObjectName("statusbar")
        Modul_modulpage.setStatusBar(self.statusbar)

        self.retranslateUi(Modul_modulpage)
        QtCore.QMetaObject.connectSlotsByName(Modul_modulpage)

    def retranslateUi(self, Modul_modulpage):
        _translate = QtCore.QCoreApplication.translate
        Modul_modulpage.setWindowTitle(_translate("Modul_modulpage", "MainWindow"))
        self.label.setText(_translate("Modul_modulpage", "PILIH MODUL!"))
        self.logout_button.setText(_translate("Modul_modulpage", "LOG OUT"))
        self.modul_1_button.setText(_translate("Modul_modulpage", "MODUL 1"))
        self.modul_2_button.setText(_translate("Modul_modulpage", "MODUL 2"))
        self.modul_3_button.setText(_translate("Modul_modulpage", "MODUL 3"))
        self.modul_4_button.setText(_translate("Modul_modulpage", "MODUL 4"))
        self.modul_5_button.setText(_translate("Modul_modulpage", "MODUL 5"))
        self.modul_6_button.setText(_translate("Modul_modulpage", "MODUL 6"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Modul_modulpage = QtWidgets.QMainWindow()
    ui = Ui_Modul_modulpage()
    ui.setupUi(Modul_modulpage)
    Modul_modulpage.show()
    sys.exit(app.exec_())