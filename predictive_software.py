from login import Window_login
from main import Window_main
from modulo_consultas_SQ import Window_consultas_SQ
from modulo_proveedores import Window_proveedores
from modulo_recursos import Window_recursos
from modulo_ventas import Window_ventas
import sys
from PySide6.QtWidgets import QApplication
from conexionDB import *

class predictive_software:
    def __init__(self):
        #base de datos
        self.datosTotal = Registro_datos()

        #ventanas
        self.login = Window_login()
        self.main = Window_main()
        self.modulo_consultas_SQ = Window_consultas_SQ()
        self.modulo_proveedores = Window_proveedores()
        self.modulo_recursos = Window_recursos()
        self.modulo_ventas = Window_ventas()

        self.login.setupUi()
        self.main.setupUi()
        self.modulo_consultas_SQ.setupUi()
        self.modulo_proveedores.setupUi()
        self.modulo_recursos.setupUi()
        self.modulo_ventas.setupUi()

        #usuario = self.login.usuario.text()

        #cambiar a ventanas
        self.login.boton_login.clicked.connect(self.logearse)

        self.main.boton1.clicked.connect(self.entrar_dashboard)
        self.main.boton2.clicked.connect(self.entrar_Proveedores)
        self.main.boton3.clicked.connect(self.entrar_Recursos)
        self.main.boton4.clicked.connect(self.entrar_Ventas)
        self.main.boton5.clicked.connect(self.entrar_Consultas)

        self.modulo_proveedores.boton1.clicked.connect(self.entrar_dashboard)
        self.modulo_proveedores.boton2.clicked.connect(self.entrar_Proveedores)
        self.modulo_proveedores.boton3.clicked.connect(self.entrar_Recursos)
        self.modulo_proveedores.boton4.clicked.connect(self.entrar_Ventas)
        self.modulo_proveedores.boton5.clicked.connect(self.entrar_Consultas)

        self.modulo_consultas_SQ.boton1.clicked.connect(self.entrar_dashboard)
        self.modulo_consultas_SQ.boton2.clicked.connect(self.entrar_Proveedores)
        self.modulo_consultas_SQ.boton3.clicked.connect(self.entrar_Recursos)
        self.modulo_consultas_SQ.boton4.clicked.connect(self.entrar_Ventas)
        self.modulo_consultas_SQ.boton5.clicked.connect(self.entrar_Consultas)

        self.modulo_recursos.boton1.clicked.connect(self.entrar_dashboard)
        self.modulo_recursos.boton2.clicked.connect(self.entrar_Proveedores)
        self.modulo_recursos.boton3.clicked.connect(self.entrar_Recursos)
        self.modulo_recursos.boton4.clicked.connect(self.entrar_Ventas)
        self.modulo_recursos.boton5.clicked.connect(self.entrar_Consultas)

        self.modulo_ventas.boton1.clicked.connect(self.entrar_dashboard)
        self.modulo_ventas.boton2.clicked.connect(self.entrar_Proveedores)
        self.modulo_ventas.boton3.clicked.connect(self.entrar_Recursos)
        self.modulo_ventas.boton4.clicked.connect(self.entrar_Ventas)
        self.modulo_ventas.boton5.clicked.connect(self.entrar_Consultas)

    def logearse(self):
        if(self.login.signalLogin):
            self.login.hide()
            self.main.show()
        else:
            self.login.show()
            

    def entrar_dashboard(self):
        self.main.hide()
        self.modulo_proveedores.hide()
        self.modulo_recursos.hide()
        self.modulo_ventas.hide()
        self.modulo_consultas_SQ.hide()
        self.main.show()
    
    def entrar_Proveedores(self):
        self.main.hide()
        self.modulo_proveedores.hide()
        self.modulo_recursos.hide()
        self.modulo_ventas.hide()
        self.modulo_consultas_SQ.hide()
        self.modulo_proveedores.show()

    def entrar_Recursos(self):
        self.main.hide()
        self.modulo_proveedores.hide()
        self.modulo_recursos.hide()
        self.modulo_ventas.hide()
        self.modulo_consultas_SQ.hide()
        self.modulo_recursos.show()
    
    def entrar_Ventas(self):
        self.main.hide()
        self.modulo_proveedores.hide()
        self.modulo_recursos.hide()
        self.modulo_ventas.hide()
        self.modulo_consultas_SQ.hide()
        self.modulo_ventas.show()
    
    def entrar_Consultas(self):
        self.main.hide()
        self.modulo_proveedores.hide()
        self.modulo_recursos.hide()
        self.modulo_ventas.hide()
        self.modulo_consultas_SQ.hide()
        self.modulo_consultas_SQ.show()

app = QApplication(sys.argv)

inicio = predictive_software()
inicio.login.show()

sys.exit(app.exec())