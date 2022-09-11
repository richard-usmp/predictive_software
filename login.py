from logging import PlaceHolder
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
from __feature__ import true_property
from conexionDB import Registro_datos

class Window_login(QMainWindow):
        def setupUi(self):
            self.datosTotal = Registro_datos()

            self.setFixedSize(1280, 720)
            self.styleSheet="background: gray;"
            self.setWindowTitle("JR Group SAC - Predictive Software")

            #contenedor logo
            #self.fr_logo = QFrame (self)
            #self.fr_logo.geometry=QRect(50,50,500, 500)
            #self.fr_logo.styleSheet="background: white;"
            #imagen logo
            self.label = QLabel(self)
            self.label.geometry=QRect(200,0,1000, 500)
            self.label.pixmap = QPixmap("images/logo_JR.jpg")

            #contenedor login
            self.fr_login = QFrame(self)
            self.fr_login.geometry=QRect(640,50,500, 500)
            self.fr_login.styleSheet="background: white;"
            #titulo login
            self.titulo = QLabel(self.fr_login)
            self.titulo.text = "LOGIN"  
            self.titulo.geometry = QRect(0,10, 500,30)
            self.titulo.alignment = Qt.AlignCenter
            self.titulo.styleSheet = "color: gray; font-size: 25px; font-weight: bold;"
            #login
            self.usuario = QLineEdit(self.fr_login, placeholderText ="Usuario")
            self.usuario.geometry=QRect(20,60,460,45)
            self.contra = QLineEdit(self.fr_login, placeholderText ="Contraseña", echoMode=QLineEdit.Password)
            self.contra.geometry=QRect(20,120,460,45)
            self.radioButton_recordar = QRadioButton(self.fr_login)
            self.radioButton_recordar.geometry=QRect(90, 210, 82, 17)
            self.radioButton_recordar.text = "Recordar"
            self.boton_login = QPushButton(self.fr_login)
            self.boton_login.geometry=QRect(220, 260, 75, 23)
            self.boton_login.text = "INGRESAR"

            self.boton_login.clicked.connect(self.checklogin)

        signalLogin = False
        def checklogin(self):
            usuario = str("'"+self.usuario.text+"'")
            contra = str("'"+self.contra.text+"'")
            usuario_DB = self.datosTotal.getUser(usuario)
            contra_DB = self.datosTotal.getPass(contra)
            print("usuario: "+usuario)
            print("usuario_DB: "+usuario_DB)
            print("contra: "+contra)
            print("contra_DB: "+contra_DB)
            if(self.usuario.text!="" or self.contra.text!=""):
                if(usuario_DB == self.usuario.text and contra_DB == self.contra.text):
                    print("Login passed!")
                    self.signalLogin = True
                else:
                    print("Login error!")
                    self.signalLogin = False
            else:
                print("Login error2!")
                self.signalLogin = False
                