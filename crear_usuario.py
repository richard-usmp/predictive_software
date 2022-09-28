from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
from conexionDB import *
from datetime import date
from __feature__ import true_property

today = date.today()

class Window_crear_usuario(QMainWindow):
    def setupUi(self):
        self.datosTotal = Registro_datos()

        self.setFixedSize(1130, 380)
        self.styleSheet="background: gray;"
        self.setWindowTitle("JR Group SAC - Predictive Software")

        self.fr_frame_tabla = QFrame(self)
        self.fr_frame_tabla.geometry=QRect(20, 20, 1090, 340)
        self.fr_frame_tabla.styleSheet="background: white;"

        #texto del contenedor
        self.texto_cont = QLabel(self.fr_frame_tabla)
        self.texto_cont.text = "Crear usuario"  
        self.texto_cont.geometry = QRect(10,0, 850,30)
        self.texto_cont.alignment = Qt.AlignJustify
        self.texto_cont.styleSheet = "color: blue; font-size: 25px; font-weight: bold;"

        self.usuario = QLineEdit(self.fr_frame_tabla)
        self.usuario.placeholderText= "Usuario"
        self.usuario.geometry = QRect(10,50, 395,20)
        self.usuario.alignment = Qt.AlignCenter
        self.usuario.styleSheet = "color: gray; font-size: 15px;"
        
        self.contra = QLineEdit(self.fr_frame_tabla, echoMode=QLineEdit.Password)
        self.contra.placeholderText= "Contraseña"
        self.contra.geometry = QRect(10,70, 395,20)
        self.contra.alignment = Qt.AlignCenter
        self.contra.styleSheet = "color: gray; font-size: 15px;"

        self.confirm_contra = QLineEdit(self.fr_frame_tabla, echoMode=QLineEdit.Password)
        self.confirm_contra.placeholderText= "Confirmar Contraseña"
        self.confirm_contra.geometry = QRect(10,90, 395,20)
        self.confirm_contra.alignment = Qt.AlignCenter
        self.confirm_contra.styleSheet = "color: gray; font-size: 15px;"

        self.boton_mostrar_datos = QPushButton(self.fr_frame_tabla)
        self.boton_mostrar_datos.text = "Crear usuario"
        self.boton_mostrar_datos.clicked.connect(self.crearUsuario)
        self.boton_mostrar_datos.geometry = QRect(10, 110, 200,45)
        self.boton_mostrar_datos.styleSheet = "background: white; font-size: 15px;"

    def crearUsuario(self):
        if(self.usuario.text != "" or self.contra.text != "" or self.confirm_contra.text != ""):
            user = self.usuario.text
            passw = self.contra.text
            conf_passw = self.confirm_contra.text
            if(passw == conf_passw):
                self.datosTotal.inserta_usuario(user, passw)
                print("¡Usuario Creado!")
            else:
                print("Contraseñas no son iguales.")
        else:
            print("Escribir datos del usuario.")