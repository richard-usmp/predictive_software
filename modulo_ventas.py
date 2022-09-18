from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
import os
from conexionDB import *
from datetime import date
from __feature__ import true_property

today = date.today()

class Window_ventas(QMainWindow):
    def setupUi(self):
        self.datosTotal = Registro_datos()

        self.setFixedSize(1280, 720)
        self.styleSheet="background: gray;"
        self.setWindowTitle("JR Group SAC - Predictive Software")

        #Contenedor del titulo
        self.fr_titulo = QFrame(self)
        self.fr_titulo.geometry=QRect(10,10,295, 700)
        self.fr_titulo.styleSheet="background: white;"
        #contenedor de bienvenida
        self.fr_bienvenida = QFrame(self)
        self.fr_bienvenida.geometry=QRect(10,10,295, 45)
        self.fr_bienvenida.styleSheet="background: white;"
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

        #contenedor arriba
        self.fr_contenedor_arriba = QFrame(self)
        self.fr_contenedor_arriba.geometry=QRect(320, 10, 950, 340)
        self.fr_contenedor_arriba.styleSheet="background: white;"
        #texto del contenedor arriba
        self.texto_cont_arriba = QLabel(self.fr_contenedor_arriba)
        self.texto_cont_arriba.text = "Ventas"  
        self.texto_cont_arriba.geometry = QRect(10,0, 850,30)
        self.texto_cont_arriba.alignment = Qt.AlignJustify
        self.texto_cont_arriba.styleSheet = "color: gray; font-size: 25px; font-weight: bold;"
        #inputs
        self.input_cod_venta = QLineEdit(self.fr_contenedor_arriba)
        self.input_cod_venta.placeholderText= "Codigo de venta"
        self.input_cod_venta.geometry = QRect(10,50, 395,20)
        self.input_cod_venta.alignment = Qt.AlignCenter
        self.input_cod_venta.styleSheet = "color: gray; font-size: 15px;"

        self.input_producto = QLineEdit(self.fr_contenedor_arriba)
        self.input_producto.placeholderText= "Producto"
        self.input_producto.geometry = QRect(10,90, 395,20)
        self.input_producto.alignment = Qt.AlignCenter
        self.input_producto.styleSheet = "color: gray; font-size: 15px;"

        self.input_cantidad = QLineEdit(self.fr_contenedor_arriba)
        self.input_cantidad.placeholderText= "Cantidad"
        self.input_cantidad.geometry = QRect(10,130, 395,20)
        self.input_cantidad.alignment = Qt.AlignCenter
        self.input_cantidad.styleSheet = "color: gray; font-size: 15px;"

        self.boton_ingresar_venta = QPushButton(self.fr_contenedor_arriba)
        self.boton_ingresar_venta.text = "Registrar Venta"
        self.boton_ingresar_venta.clicked.connect(self.insertarDatosBD)
        self.boton_ingresar_venta.geometry = QRect(350, 250, 170, 45)
        self.boton_ingresar_venta.styleSheet = "background: white; font-size: 15px;"

        self.boton_ingresar_venta = QPushButton(self.fr_contenedor_arriba)
        self.boton_ingresar_venta.text = "Importar CSV de ventas"
        self.boton_ingresar_venta.geometry = QRect(530, 250, 170, 45)
        self.boton_ingresar_venta.styleSheet = "background: white; font-size: 15px;"
        
        #contenedor abajo
        self.fr_contenedor_abajo = QFrame(self)
        self.fr_contenedor_abajo.geometry=QRect(320, 360, 950, 350)
        self.fr_contenedor_abajo.styleSheet="background: white;"
        #texto del contenedor abajo
        self.texto_cont_abajo = QLabel(self.fr_contenedor_abajo)
        self.texto_cont_abajo.text = "Registro de ventas"  
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
        nombreColumnas = ("Id", "Cod. venta", "Cantidad Productos Vendidos", "Día", "Mes", "Año")
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)
        for indice, ancho in enumerate((80, 120, 120, 110, 150), start=0):
            self.tabla.setColumnWidth(indice, ancho)

        self.tabla.resize(800, 260)
        self.tabla.move(50, 50)
        #boton mostrar datos
        self.boton_mostrar_datos = QPushButton(self.fr_contenedor_abajo)
        self.boton_mostrar_datos.text = "Mostrar datos"
        self.boton_mostrar_datos.clicked.connect(self.datosTabla)
        self.boton_mostrar_datos.geometry = QRect(300, 0, 200,45)
        self.boton_mostrar_datos.styleSheet = "background: white; font-size: 15px;"

    
    def datosTabla(self):
        datos = self.datosTotal.buscar_ventas()

        self.tabla.clearContents()

        row = 0
        for endian in datos:
            self.tabla.rowCount=row + 1
            
            idDato = QTableWidgetItem(str(endian[0]))
            idDato.setTextAlignment(4)
            
            self.tabla.setItem(row, 0, idDato)
            self.tabla.setItem(row, 1, QTableWidgetItem(str(endian[1])))
            self.tabla.setItem(row, 2, QTableWidgetItem(str(endian[2])))
            self.tabla.setItem(row, 3, QTableWidgetItem(str(endian[3])))
            self.tabla.setItem(row, 4, QTableWidgetItem(str(endian[4])))
            self.tabla.setItem(row, 5, QTableWidgetItem(str(endian[5])))

            row += 1
    
    def insertarDatosBD(self):
        if(self.input_cod_venta.text!="" or self.input_producto.text!="" or self.input_cantidad.text!=""):
            dni = self.input_cod_venta.text
            producto = self.input_producto.text
            cantidad = self.input_cantidad.text
            Dia = today.strftime("%d")
            Mes = today.strftime("%m")
            Anio = today.strftime("%Y")
            Año_y_mes = str(Anio + "-" + Mes)
            tot_prod_ven = self.datosTotal.get_total_productos_vendidos(Año_y_mes)


            if(tot_prod_ven==""):
                tot_prod_ven = 0
                total_prod_vendidos = int(tot_prod_ven) + int(cantidad)
            else:
                total_prod_vendidos = int(tot_prod_ven) + int(cantidad)

            self.datosTotal.inserta_ventas(dni, cantidad, Dia, Mes, Anio, total_prod_vendidos, Año_y_mes)
            print("Venta insertada!")
            self.input_cod_venta.clear()
            self.input_producto.clear()
            self.input_cantidad.clear()
        else:
            print("Escribir item a insertar.")

    def setup_name_user(self, username):
        self.titulo = QLabel(f"Bienvenido {username}", alignment = Qt.AlignCenter)
        self.titulo.styleSheet = "color: gray; font-size: 21px; font-weight: bold;"

        self.titulo_layout = QVBoxLayout()
        self.titulo_layout.addWidget(self.titulo)

        self.fr_bienvenida.setLayout(self.titulo_layout)


    def abrir_archivo_csv(self):
        archivo = QFileDialog