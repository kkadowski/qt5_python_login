# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import hashlib
from db_conn import dbConnection
from main import Ui_FormMainWindow

class Ui_FormLogin(object):
    def setupUi(self, FormLogin):
        FormLogin.setObjectName("FormLogin")
        FormLogin.resize(550, 170)
        FormLogin.setMinimumSize(QtCore.QSize(550, 170))
        FormLogin.setMaximumSize(QtCore.QSize(650, 220))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(FormLogin)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelImage = QtWidgets.QLabel(FormLogin)
        self.labelImage.setMinimumSize(QtCore.QSize(200, 0))
        self.labelImage.setText("")
        self.labelImage.setObjectName("labelImage")
        self.horizontalLayout.addWidget(self.labelImage)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelEmail = QtWidgets.QLabel(FormLogin)
        self.labelEmail.setObjectName("labelEmail")
        self.verticalLayout.addWidget(self.labelEmail)
        self.lineEditEmail = QtWidgets.QLineEdit(FormLogin)
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.verticalLayout.addWidget(self.lineEditEmail)
        self.labelPassword = QtWidgets.QLabel(FormLogin)
        self.labelPassword.setObjectName("labelPassword")
        self.verticalLayout.addWidget(self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(FormLogin)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.pushButtonLogin = QtWidgets.QPushButton(FormLogin)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.verticalLayout.addWidget(self.pushButtonLogin)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(FormLogin)
        QtCore.QMetaObject.connectSlotsByName(FormLogin)
        self.pushButtonLogin.clicked.connect(self.zaloguj)
        
    def messagebox(self, title, message, icon, button):
        mess= QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        if icon == "Information":
            mess.setIcon(QtWidgets.QMessageBox.Icon.Information)
        elif icon == "Warning":
            mess.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        if button == "Ok":
            mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        elif button == "Cancel":
            mess.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        mess.exec_()       
        
    def OpenWindow(self):
        FormLogin.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FormMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
        
    
    def zaloguj(self):
        email = self.lineEditEmail.text()
        password = hashlib.md5(self.lineEditPassword.text().encode('utf-8')).hexdigest()
        #print(email, password)  
        db = dbConnection()
        db.connect()
        query = "SELECT COUNT(*) FROM users WHERE email=%s AND pass=%s"
        params = (email, password)
        row = db.fetchone(query, params)
        db.close()
        if row[0] == 1:
            self.messagebox("Logged in",f"You are logged in as {email}","Information", "Ok")
            self.OpenWindow()
        else:
            self.messagebox("Login problem", "Your login or email is not correct.", "Warning","Cancel")
        

    def retranslateUi(self, FormLogin):
        _translate = QtCore.QCoreApplication.translate
        FormLogin.setWindowTitle(_translate("FormLogin", "Logowanie"))
        self.labelEmail.setText(_translate("FormLogin", "E-mail"))
        self.labelPassword.setText(_translate("FormLogin", "Password"))
        self.pushButtonLogin.setText(_translate("FormLogin", "Login"))
        pixmap = QPixmap('ui/login_icon.png')
        self.labelImage.setPixmap(pixmap)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormLogin = QtWidgets.QWidget()
    ui = Ui_FormLogin()
    ui.setupUi(FormLogin)
    FormLogin.show()
    sys.exit(app.exec_())
