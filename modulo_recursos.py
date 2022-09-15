from unicodedata import decimal
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
from conexionDB import *
from datetime import date
from __feature__ import true_property

today = date.today()

class Window_recursos(QMainWindow):
    def setupUi(self):
        self.datosTotal = Registro_datos()

        self.setFixedSize(1280, 720)
        self.styleSheet="background: gray;"
        self.setWindowTitle("JR Group SAC - Predictive Software")

        #Contenedor del titulo
        self.fr_titulo = QFrame(self)
        self.fr_titulo.geometry=QRect(10,10,295, 700)
        self.fr_titulo.styleSheet="background: white;"
        #texto del titulo
        self.titulo = QLabel(self.fr_titulo)
        self.titulo.text = "¡Hola Admin01!"  
        self.titulo.geometry = QRect(0,20, 295,30)
        self.titulo.alignment = Qt.AlignCenter
        self.titulo.styleSheet = "color: gray; font-size: 25px; font-weight: bold;"
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
        self.texto_cont_arriba.text = "Materia prima"  
        self.texto_cont_arriba.geometry = QRect(10,0, 850,30)
        self.texto_cont_arriba.alignment = Qt.AlignJustify
        self.texto_cont_arriba.styleSheet = "color: gray; font-size: 25px; font-weight: bold;"
        #inputs
        self.nombre_producto = QLineEdit(self.fr_contenedor_arriba)
        self.nombre_producto.placeholderText= "Nombre producto"
        self.nombre_producto.geometry = QRect(10,50, 395,20)
        self.nombre_producto.alignment = Qt.AlignCenter
        self.nombre_producto.styleSheet = "color: gray; font-size: 15px;"

        self.unid_medida = QLineEdit(self.fr_contenedor_arriba)
        self.unid_medida.placeholderText= "Unidad de medida"
        self.unid_medida.geometry = QRect(10,90, 395,20)
        self.unid_medida.alignment = Qt.AlignCenter
        self.unid_medida.styleSheet = "color: gray; font-size: 15px;"

        self.cantidad_entrante = QLineEdit(self.fr_contenedor_arriba)
        self.cantidad_entrante.placeholderText= "Cantidad entrante"
        self.cantidad_entrante.geometry = QRect(10,130, 395,20)
        self.cantidad_entrante.alignment = Qt.AlignCenter
        self.cantidad_entrante.styleSheet = "color: gray; font-size: 15px;"

        self.cmb_sumar_restar = QComboBox(self.fr_contenedor_arriba)
        self.cmb_sumar_restar.placeholderText= "+"
        self.cmb_sumar_restar.geometry = QRect(400,130, 50,20)
        self.cmb_sumar_restar.styleSheet = "color: gray; font-size: 15px;"
        self.cmb_sumar_restar.addItem("+")
        self.cmb_sumar_restar.addItem("-")

        self.costo = QLineEdit(self.fr_contenedor_arriba)
        self.costo.placeholderText= "Costo"
        self.costo.geometry = QRect(10,170, 395,20)
        self.costo.alignment = Qt.AlignCenter
        self.costo.styleSheet = "color: gray; font-size: 15px;"

        self.boton_ingresar_recurso = QPushButton(self.fr_contenedor_arriba)
        self.boton_ingresar_recurso.text = "Registrar"
        self.boton_ingresar_recurso.clicked.connect(self.insertarDatosBD)
        self.boton_ingresar_recurso.geometry = QRect(350, 250, 170, 45)
        self.boton_ingresar_recurso.styleSheet = "background: white; font-size: 15px;"

        #seccion de modificar
        self.cmb_producto_BD = QComboBox(self.fr_contenedor_arriba)
        self.cmb_producto_BD.placeholderText= "Producto para modificar..."
        self.cmb_producto_BD.geometry = QRect(500,50, 395,20)
        self.cmb_producto_BD.styleSheet = "color: gray; font-size: 15px;"
        self.cmb_producto_BD.addItems(self.datosTotal.buscar_material_cmb())

        self.boton_Modificar = QPushButton(self.fr_contenedor_arriba)
        self.boton_Modificar.text = "Modificar"
        self.boton_Modificar.clicked.connect(self.modificarDatosBD)
        self.boton_Modificar.geometry = QRect(520, 250, 170, 45)
        self.boton_Modificar.styleSheet = "background: white; font-size: 15px;"
        
        #contenedor abajo
        self.fr_contenedor_abajo = QFrame(self)
        self.fr_contenedor_abajo.geometry=QRect(320, 360, 950, 350)
        self.fr_contenedor_abajo.styleSheet="background: white;"
        #texto del contenedor abajo
        self.texto_cont_abajo = QLabel(self.fr_contenedor_abajo)
        self.texto_cont_abajo.text = "Materia prima disponible"  
        self.texto_cont_abajo.geometry = QRect(10,0, 850,30)
        self.texto_cont_abajo.alignment = Qt.AlignJustify
        self.texto_cont_abajo.styleSheet = "color: gray; font-size: 25px;"
        #tabla
        self.tabla_recursos = QTableWidget(self.fr_contenedor_abajo)
        self.tabla_recursos.dragDropOverwriteMode=False
        self.tabla_recursos.selectionBehavior=QAbstractItemView.SelectRows
        self.tabla_recursos.selectionMode=QAbstractItemView.SingleSelection
        self.tabla_recursos.wordWrap=False
        self.tabla_recursos.isSortingEnabled=False
        self.tabla_recursos.alternatingRowColors=True
        self.tabla_recursos.columnCount= 7
        self.tabla_recursos.rowCount = 0
        nombreColumnas = ("Id","Nombre", "Unidad de medida", "Stock", "Precio de compra unitario", "Mes", "Año")
        self.tabla_recursos.setHorizontalHeaderLabels(nombreColumnas)
        for indice, ancho in enumerate((80, 120, 120, 110, 150), start=0):
            self.tabla_recursos.setColumnWidth(indice, ancho)

        self.tabla_recursos.resize(800, 260)
        self.tabla_recursos.move(50, 50)
        #boton mostrar datos
        self.boton_mostrar_datos = QPushButton(self.fr_contenedor_abajo)
        self.boton_mostrar_datos.text = "Mostrar datos"
        self.boton_mostrar_datos.clicked.connect(self.datosTabla)
        self.boton_mostrar_datos.geometry = QRect(300, 0, 200,45)
        self.boton_mostrar_datos.styleSheet = "background: white; font-size: 15px;"

    def datosTabla(self):
        datos = self.datosTotal.buscar_material()

        self.tabla_recursos.clearContents()

        row = 0
        for endian in datos:
            self.tabla_recursos.rowCount=row + 1
            
            idDato = QTableWidgetItem(str(endian[0]))
            idDato.setTextAlignment(4)
            
            self.tabla_recursos.setItem(row, 0, idDato)
            self.tabla_recursos.setItem(row, 1, QTableWidgetItem(endian[1]))
            self.tabla_recursos.setItem(row, 2, QTableWidgetItem(endian[2]))
            self.tabla_recursos.setItem(row, 3, QTableWidgetItem(str(endian[3])))
            self.tabla_recursos.setItem(row, 4, QTableWidgetItem(str(endian[4])))
            self.tabla_recursos.setItem(row, 5, QTableWidgetItem(endian[5]))
            self.tabla_recursos.setItem(row, 6, QTableWidgetItem(endian[6]))

            row += 1

    def insertarDatosBD(self):
        if(self.nombre_producto.text!="" or self.unid_medida.text!="" or self.cantidad_entrante.text!="" or self.costo.text!=""):
            Descripcion = self.nombre_producto.text
            Unid_medida = self.unid_medida.text
            Stock = self.cantidad_entrante.text
            Precio_compra_unit = self.costo.text
            Dia = today.strftime("%d")
            Mes = today.strftime("%B")
            Anio = today.strftime("%Y")
            Estado = "Nuevo"

            self.datosTotal.inserta_material(Descripcion, Unid_medida, Stock, Precio_compra_unit, Mes, Anio)

            descripcion_app = "'"+self.nombre_producto.text+"'"
            ID_material= self.datosTotal.getID_Material(descripcion_app)

            self.datosTotal.insertar_log_material(ID_material, Descripcion, Stock, Precio_compra_unit, Dia, Mes, Anio, Estado)
            print("Dato insertado!")
            self.nombre_producto.clear()
            self.unid_medida.clear()
            self.cantidad_entrante.clear()
            self.costo.clear()
        else:
            print("Escribir item a insertar.")

    def modificarDatosBD(self):
        Stock = self.cantidad_entrante.text
        Precio_compra_unit = self.costo.text
        Descripcion = self.cmb_producto_BD.currentText
        Dia = today.strftime("%d")
        Mes = today.strftime("%B")
        Anio = today.strftime("%Y")
        Estado=""

        descripcion_app = "'"+self.cmb_producto_BD.currentText+"'"
        descripcion_DB = self.datosTotal.getMaterial(descripcion_app)
        ID_material= self.datosTotal.getID_Material(descripcion_app)
        print("ID_material: "+str(ID_material))

        if(self.cmb_producto_BD.currentIndex==-1):
            print("Seleccionar item a modificar.")
        elif(self.cantidad_entrante.text!=""):
            get_stock = self.datosTotal.getStock(descripcion_app)
            if(self.cmb_sumar_restar.currentIndex==-1 or self.cmb_sumar_restar.currentIndex==0):
                Stock_sumado = get_stock + decimal(Stock)
                Estado = "Suma"
            else:
                Stock_sumado = get_stock - decimal(Stock)
                Estado = "Resta"

            if(descripcion_DB == Descripcion):
                self.datosTotal.actualizar_stock_material(Stock_sumado, Descripcion)
                self.datosTotal.insertar_log_material(ID_material, Descripcion, Stock, Precio_compra_unit, Dia, Mes, Anio, Estado)
                print("Stock actualizado!")
            else:
                print("Else de modificarDatosBD:actualizar_stock_material")
        else:
            print("Escribir cantidad entrante del item a modificar.")
        
        if(self.cmb_producto_BD.currentIndex==-1):
            print("Seleccionar item a modificar.")
        elif(self.costo.text!=""):
            if(descripcion_DB == Descripcion):
                Estado="Cambio de precio"
                self.datosTotal.actualizar_precio_material(Descripcion, Precio_compra_unit)
                self.datosTotal.insertar_log_material(ID_material, Descripcion, Stock, Precio_compra_unit, Dia, Mes, Anio, Estado)
                print("Precio actualizado!")
            else:
                print("Else de modificarDatosBD:actualizar_precio_material")
        else:
            print("Escribir costo del item a modificar.")
