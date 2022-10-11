from PySide6.QtWidgets import *
from PySide6.QtCore import *
from conexionDB import *
import sys
from __feature__ import true_property

class Window_perfil(QMainWindow):
    def setupUi(self):
        self.datosTotal = Registro_datos()
        self.user = ""

        self.setFixedSize(520, 320)
        self.styleSheet="background: gray;"
        self.setWindowTitle("JR Group SAC - Predictive Software")

        #Contenedor del titulo
        self.fr_titulo = QFrame(self)
        self.fr_titulo.geometry=QRect(10,10,500, 300)
        self.fr_titulo.styleSheet="background: white;"

        #contenedor de bienvenida
        self.fr_bienvenida = QFrame(self)
        self.fr_bienvenida.geometry=QRect(10,10,300, 45)
        self.fr_bienvenida.styleSheet="background: white;"

        self.texto_cont_arriba = QLabel(self)
        self.texto_cont_arriba.text = "Para cambiar contraseña escriba su nueva contraseña:"  
        self.texto_cont_arriba.geometry = QRect(20,60, 380,25)
        self.texto_cont_arriba.alignment = Qt.AlignJustify
        self.texto_cont_arriba.styleSheet = "background: white; color: black; font-size: 15px; font-weight: bold;"

        self.input_cantidad = QLineEdit(self)
        self.input_cantidad.placeholderText= "Nueva contraseña"
        self.input_cantidad.geometry = QRect(20,100, 320,20)
        self.input_cantidad.alignment = Qt.AlignCenter
        self.input_cantidad.styleSheet = "color: white; font-size: 15px;"

        #boton cambiar contraseña
        self.cambiar_pass = QPushButton(self.fr_titulo)
        self.cambiar_pass.text = "Cambiar contraseña"
        self.cambiar_pass.clicked.connect(self.cambiar_contra)
        self.cambiar_pass.geometry = QRect(25, 130, 200,45)
        self.cambiar_pass.styleSheet = "background: white; font-size: 20px;"

    def setup_name_user(self, username):
        self.titulo = QLabel(f"Usuario: {username}", alignment = Qt.AlignCenter)
        self.titulo.styleSheet = "color: gray; font-size: 21px; font-weight: bold;"

        self.titulo_layout = QVBoxLayout()
        self.titulo_layout.addWidget(self.titulo)

        self.fr_bienvenida.setLayout(self.titulo_layout)

        self.user = username

    def cambiar_contra(self):
        user_ = self.user
        new_pass = self.input_cantidad.text
        self.datosTotal.modificar_pass(new_pass, user_)
        self.input_cantidad.clear()
        print("¡Contraseña modificada!")