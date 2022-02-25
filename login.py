"""
Login window
Made by K>K> 
2022    
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os
from db_con import dbConnection
import hashlib


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(500, 200)
        Login.setMinimumSize(QtCore.QSize(500, 200))
        Login.setBaseSize(QtCore.QSize(500, 200))
        self.imagelabel = QtWidgets.QLabel(Login)
        self.imagelabel.setGeometry(QtCore.QRect(50, 30, 161, 121))
        self.imagelabel.setObjectName("imagelabel")
        self.widget = QtWidgets.QWidget(Login)
        self.widget.setGeometry(QtCore.QRect(250, 20, 241, 158))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        
        # my 
        self.pushButton.clicked.connect(self.login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.imagelabel.setText(_translate("Login", ""))
        pixmap = QPixmap('ui/login_graphic.png')    
        self.imagelabel.setPixmap(pixmap)                   # loading image as pixmap to label
        self.label.setText(_translate("Login", "Username / E-mail"))
        self.label_2.setText(_translate("Login", "Password"))
        self.label_3.setText(_translate("Login", "Forgot Password?"))
        self.pushButton.setText(_translate("Login", "Login"))

    #my funcs
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
        
    def warningbox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
        
    def login(self):
        email = self.lineEdit.text()    
        password = hashlib.md5(self.lineEdit_2.text().encode('utf-8')).hexdigest()
        db = dbConnection()
        db.connect()
        query = f"SELECT count(*) FROM users WHERE email=\'{email}\' AND pass = \'{password}\'"
        row = db.fetchone(query)
        db.close()
        if row[0] == 1:
            loggedas=f"You are logged as {email}"
            self.messagebox("Login ", loggedas)
        else:
            self.warningbox("Login problem", "Your email or password is not correct. Enter correct details. ")
        
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
