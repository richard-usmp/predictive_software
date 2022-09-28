from xml.dom.minidom import Element
from login import Window_login
from main import Window_main
from modulo_consultas_SQ import Window_consultas_SQ
from modulo_proveedores import Window_proveedores
from modulo_recursos import Window_recursos
from modulo_ventas import Window_ventas
from modulo_log_materiales import Window_material_log
from main_admin import Window_main_admin
from crear_usuario import Window_crear_usuario
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
        self.modulo_material_log = Window_material_log()
        self.main_admin = Window_main_admin()
        self.crear_usuario = Window_crear_usuario()

        self.login.setupUi()
        self.main.setupUi()
        self.modulo_consultas_SQ.setupUi()
        self.modulo_proveedores.setupUi()
        self.modulo_recursos.setupUi()
        self.modulo_ventas.setupUi()
        self.modulo_material_log.setupUi()
        self.main_admin.setupUi()
        self.crear_usuario.setupUi()

        #cambiar a ventanas
        self.login.boton_login.clicked.connect(self.logearse)

        self.main.boton1.clicked.connect(self.entrar_dashboard)
        self.main.boton2.clicked.connect(self.entrar_Proveedores)
        self.main.boton3.clicked.connect(self.entrar_Recursos)
        self.main.boton4.clicked.connect(self.entrar_Ventas)
        self.main.boton5.clicked.connect(self.entrar_Consultas)

        self.main_admin.boton1.clicked.connect(self.entrar_dashboard_admin)
        self.main_admin.boton2.clicked.connect(self.entrar_Proveedores)
        self.main_admin.boton3.clicked.connect(self.entrar_Recursos)
        self.main_admin.boton4.clicked.connect(self.entrar_Ventas)
        self.main_admin.boton5.clicked.connect(self.entrar_Consultas)
        self.main_admin.boton6.clicked.connect(self.entrar_crear_usuario)

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
        self.modulo_recursos.boton_mostrar.clicked.connect(self.entrar_Recursos_log)

        self.modulo_ventas.boton1.clicked.connect(self.entrar_dashboard)
        self.modulo_ventas.boton2.clicked.connect(self.entrar_Proveedores)
        self.modulo_ventas.boton3.clicked.connect(self.entrar_Recursos)
        self.modulo_ventas.boton4.clicked.connect(self.entrar_Ventas)
        self.modulo_ventas.boton5.clicked.connect(self.entrar_Consultas)

    def logearse(self):
        if(self.login.signalLogin):
            self.login.hide()
            if(self.login.usuario.text == "user_prueba"):
                self.main_admin.show()
                self.main_admin.setup_name_user(self.login.usuario.text)
            else:
                self.main.show()
                self.main.setup_name_user(self.login.usuario.text)
        else:
            self.login.show()
            

    def entrar_dashboard(self):
        self.main.hide()
        self.modulo_proveedores.hide()
        self.modulo_recursos.hide()
        self.modulo_ventas.hide()
        self.modulo_consultas_SQ.hide()
        if(self.login.usuario.text == "user_prueba"):
            self.main.hide()
            self.main_admin.show()
            self.main_admin.setup_name_user(self.login.usuario.text)
        else:
            self.main_admin.hide()
            self.main.show()
            self.main.setup_name_user(self.login.usuario.text)

    def entrar_dashboard_admin(self):
        self.main.hide()
        self.modulo_proveedores.hide()
        self.modulo_recursos.hide()
        self.modulo_ventas.hide()
        self.modulo_consultas_SQ.hide()
        self.main_admin.show()
        self.main_admin.setup_name_user(self.login.usuario.text)

    def entrar_crear_usuario(self):
        self.main.hide()
        self.modulo_proveedores.hide()
        self.modulo_recursos.hide()
        self.modulo_ventas.hide()
        self.modulo_consultas_SQ.hide()
        self.crear_usuario.show()
    
    def entrar_Proveedores(self):
        self.main.hide()
        self.modulo_proveedores.hide()
        self.modulo_recursos.hide()
        self.modulo_ventas.hide()
        self.modulo_consultas_SQ.hide()
        self.main_admin.hide()
        self.modulo_proveedores.show()
        self.modulo_proveedores.setup_name_user(self.login.usuario.text)

    def entrar_Recursos(self):
        self.main.hide()
        self.modulo_proveedores.hide()
        self.modulo_recursos.hide()
        self.modulo_ventas.hide()
        self.modulo_consultas_SQ.hide()
        self.main_admin.hide()
        self.modulo_recursos.show()
        self.modulo_recursos.setup_name_user(self.login.usuario.text)
    
    def entrar_Ventas(self):
        self.main.hide()
        self.modulo_proveedores.hide()
        self.modulo_recursos.hide()
        self.modulo_ventas.hide()
        self.modulo_consultas_SQ.hide()
        self.main_admin.hide()
        self.modulo_ventas.show()
        self.modulo_ventas.setup_name_user(self.login.usuario.text)
    
    def entrar_Consultas(self):
        self.main.hide()
        self.modulo_proveedores.hide()
        self.modulo_recursos.hide()
        self.modulo_ventas.hide()
        self.modulo_consultas_SQ.hide()
        self.main_admin.hide()
        self.modulo_consultas_SQ.show()
        self.modulo_consultas_SQ.setup_name_user(self.login.usuario.text)

    def entrar_Recursos_log(self):
        self.main.hide()
        self.modulo_proveedores.hide()
        self.modulo_ventas.hide()
        self.modulo_consultas_SQ.hide()
        self.main_admin.hide()
        self.modulo_material_log.show() 

app = QApplication(sys.argv)

inicio = predictive_software()
inicio.login.show()

sys.exit(app.exec())