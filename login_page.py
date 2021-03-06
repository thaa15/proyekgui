# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(554, 417)
        LoginPage.setStyleSheet("background: rgb(1, 42, 59);\n"
"color: white;")
        self.centralwidget = QtWidgets.QWidget(LoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway Bold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 14pt \"Raleway Bold\";\n"
"color: rgb(161, 209, 210);\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.nama_input = QtWidgets.QTextEdit(self.centralwidget)
        self.nama_input.setGeometry(QtCore.QRect(170, 110, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nama_input.setFont(font)
        self.nama_input.setStyleSheet("background-color: rgb(237, 238, 233);\n"
"font: 8pt \"Raleway\";\n"
"color:rgb(1, 42, 59);\n"
"")
        self.nama_input.setTabChangesFocus(True)
        self.nama_input.setObjectName("nama_input")
        self.signin_button = QtWidgets.QPushButton(self.centralwidget)
        self.signin_button.setGeometry(QtCore.QRect(210, 260, 131, 31))
        self.signin_button.setStyleSheet("font: 8pt \"Raleway\";\n"
"color: rgb(237, 238, 233);\n"
"border: 1px solid rgb(238, 65, 76) radius")
        self.signin_button.setObjectName("signin_button")
        self.npm_input = QtWidgets.QTextEdit(self.centralwidget)
        self.npm_input.setGeometry(QtCore.QRect(170, 160, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.npm_input.setFont(font)
        self.npm_input.setStyleSheet("background-color: rgb(237, 238, 233);\n"
"font: 8pt \"Raleway\";\n"
"color:rgb(1, 42, 59);")
        self.npm_input.setTabChangesFocus(True)
        self.npm_input.setObjectName("npm_input")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 60, 281, 251))
        self.label_2.setStyleSheet("border: 2px solid rgb(161, 209, 210)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.nama_input.raise_()
        self.signin_button.raise_()
        self.npm_input.raise_()
        LoginPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 18))
        self.menubar.setObjectName("menubar")
        LoginPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginPage)
        self.statusbar.setObjectName("statusbar")
        LoginPage.setStatusBar(self.statusbar)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "MainWindow"))
        self.label.setText(_translate("LoginPage", "LOG IN"))
        self.nama_input.setHtml(_translate("LoginPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Raleway\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p></body></html>"))
        self.signin_button.setText(_translate("LoginPage", "SIGN IN"))
import assets_gambar_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QMainWindow()
    ui = Ui_LoginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())
