from PySide6.QtWidgets import *
from PySide6.QtCore import *

import sys
from __feature__ import true_property

class Window_main(QMainWindow):
    def setupUi(self):
        self.setFixedSize(1280, 720)
        self.styleSheet="background: gray;"
        self.setWindowTitle("JR Group SAC - Predictive Software")

        #Contenedor del titulo
        self.fr_titulo = QFrame(self)
        self.fr_titulo.geometry=QRect(10,10,295, 700)
        self.fr_titulo.styleSheet="background: white;"
        #texto del titulo
        #self.titulo = QLabel(self.fr_titulo)
        #self.titulo.text = "" 
        #self.titulo.geometry = QRect(0,20, 295,30)
        #self.titulo.alignment = Qt.AlignCenter
        #self.titulo.styleSheet = "color: gray; font-size: 25px; font-weight: bold;"
        #botones de las pestañas
        self.boton1 = QPushButton(self.fr_titulo)
        self.boton1.text = "Dashboard"
        self.boton1.geometry = QRect(80, 70, 200,45)
        self.boton1.styleSheet = "background: white; font-size: 25px;"

        self.boton2 = QPushButton(self.fr_titulo)
        self.boton2.text = "Proveedores"
        self.boton2.geometry = QRect(80, 140, 200,45)
        self.boton2.styleSheet = "background: white; font-size: 25px;"

        self.boton3 = QPushButton(self.fr_titulo)
        self.boton3.text = "Recursos"
        self.boton3.geometry = QRect(80, 210, 200,45)
        self.boton3.styleSheet = "background: white; font-size: 25px;"

        self.boton4 = QPushButton(self.fr_titulo)
        self.boton4.text = "Ventas"
        self.boton4.geometry = QRect(80, 280, 200,45)
        self.boton4.styleSheet = "background: white; font-size: 25px;"

        self.boton5 = QPushButton(self.fr_titulo)
        self.boton5.text = "Consultas SQ"
        self.boton5.geometry = QRect(80, 350, 200,45)
        self.boton5.styleSheet = "background: white; font-size: 25px;"

        #cuadro de dialogo
        self.dialogo = QDialog(self)
        self.dialogo.setFixedSize(300, 300)

        #frames del dialogo
        self.fr_titulo_dialogo = QFrame(self.dialogo)
        self.fr_titulo_dialogo.geometry = QRect(10,10, 280, 100)
        self.fr_titulo_dialogo.styleSheet = "background: black;"

        #contenedor arriba
        self.fr_contenedor_arriba = QFrame(self)
        self.fr_contenedor_arriba.geometry=QRect(320, 10, 950, 340)
        self.fr_contenedor_arriba.styleSheet="background: white;"
        #texto del contenedor arriba
        self.texto_cont_arriba = QLabel(self.fr_contenedor_arriba)
        self.texto_cont_arriba.text = "Bienvenido"  
        self.texto_cont_arriba.geometry = QRect(10,0, 850,30)
        self.texto_cont_arriba.alignment = Qt.AlignJustify
        self.texto_cont_arriba.styleSheet = "color: gray; font-size: 25px; font-weight: bold;"
        
        #contenedor abajo
        self.fr_contenedor_abajo = QFrame(self)
        self.fr_contenedor_abajo.geometry=QRect(320, 360, 950, 350)
        self.fr_contenedor_abajo.styleSheet="background: white;"
        #texto del contenedor abajo
        self.texto_cont_abajo = QLabel(self.fr_contenedor_abajo)
        self.texto_cont_abajo.text = "Recursos"  
        self.texto_cont_abajo.geometry = QRect(10,0, 850,30)
        self.texto_cont_abajo.alignment = Qt.AlignJustify
        self.texto_cont_abajo.styleSheet = "color: gray; font-size: 25px;"
        #tabla
        self.tabla = QTableWidget(self.fr_contenedor_abajo)
        self.tabla.dragDropOverwriteMode=False
        self.tabla.selectionBehavior=QAbstractItemView.SelectRows
        self.tabla.selectionMode=QAbstractItemView.SingleSelection
        self.tabla.wordWrap=False
        self.tabla.isSortingEnabled=False
        self.tabla.alternatingRowColors=True
        self.tabla.columnCount= 6
        self.tabla.rowCount = 0
        nombreColumnas = ("Id","Material", "Cantidad", "Precio por unidad", "Precio", "Fecha entrante")
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)
        for indice, ancho in enumerate((80, 120, 120, 110, 150), start=0):
            self.tabla.setColumnWidth(indice, ancho)

        self.tabla.resize(700, 240)
        self.tabla.move(50, 50)
        #boton mostrar datos
        self.boton_mostrar_datos = QPushButton(self.fr_contenedor_abajo)
        self.boton_mostrar_datos.text = "Mostrar datos"
        self.boton_mostrar_datos.clicked.connect(self.datosTabla)
        self.boton_mostrar_datos.geometry = QRect(190, 0, 200,45)
        self.boton_mostrar_datos.styleSheet = "background: white; font-size: 15px;"
    
    def datosTabla(self):
        datos = [("1", "Andres", "Niño", "Masculino", "06/12/2019", "Colombia"),
                 ("2", "Donald", "Trump", "Masculino", "06/12/1950", "Estados Unidos"),
                 ("3", "María Fernanda", "Espinosa", "Femenino", "06/10/1980", "Ecuador"),
                 ("4", "Alberto", "Canosa", "Masculino", "04/05/1876", "España"),
                 ("5", "Virtud", "Pontes", "Femenino", "23/18/1965", "España"),
                 ("6", "Elon", "Musk", "Masculino", "06/12/1960", "Estados Unidos"),
                 ("7", "Richard", "Branson", "Masculino", "14/12/1956", "Reino Unido"),
                 ("8", "Gabriel", "Garcia Marquez", "Masculino", "19/11/1948", "Colombia"),
                 ("9", "Valentina", "Tereshkova", "Femenino", "06/03/1937", "Rusia"),
                 ("10", "Artur", "Fischer", "Masculino", "31/12/1919", "Alemania"),
                 ("11", "Grace", "Murray Hopper", "Femenino", "09/12/1906", "Estados Unidos"),
                 ("12", "Guido van", "Rossum", "Masculino", "31/01/1956", "Países Bajos")]

        self.tabla.clearContents()

        row = 0
        for endian in datos:
            self.tabla.rowCount=row + 1
            
            idDato = QTableWidgetItem(endian[0])
            idDato.setTextAlignment(4)
            
            self.tabla.setItem(row, 0, idDato)
            self.tabla.setItem(row, 1, QTableWidgetItem(endian[1]))
            self.tabla.setItem(row, 2, QTableWidgetItem(endian[2]))
            self.tabla.setItem(row, 3, QTableWidgetItem(endian[3]))
            self.tabla.setItem(row, 4, QTableWidgetItem(endian[4]))
            self.tabla.setItem(row, 5, QTableWidgetItem(endian[5]))

            row += 1

    def setup_name_user(self, username):
        self.titulo = QLabel(self)
        self.titulo.text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" 
        self.titulo.geometry = QRect(0,20, 295,30)
        self.titulo.alignment = Qt.AlignCenter
        self.titulo.styleSheet = "color: gray; font-size: 25px; font-weight: bold;"
        self.titulo.setText(f"¡Hola {username}!!!!!!!!!")