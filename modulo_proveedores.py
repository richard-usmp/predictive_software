from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
from conexionDB import *
from __feature__ import true_property

class Window_proveedores(QMainWindow):
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
        self.texto_cont_arriba.text = "Proveedores"  
        self.texto_cont_arriba.geometry = QRect(10,0, 850,30)
        self.texto_cont_arriba.alignment = Qt.AlignJustify
        self.texto_cont_arriba.styleSheet = "color: gray; font-size: 25px; font-weight: bold;"
        #inputs
        self.nombre_empresa = QLineEdit(self.fr_contenedor_arriba)
        self.nombre_empresa.placeholderText= "Nombre de empresa"
        self.nombre_empresa.geometry = QRect(10,50, 395,20)
        self.nombre_empresa.alignment = Qt.AlignCenter
        self.nombre_empresa.styleSheet = "color: gray; font-size: 15px;"

        self.representante = QLineEdit(self.fr_contenedor_arriba)
        self.representante.placeholderText= "Representante"
        self.representante.geometry = QRect(10,90, 395,20)
        self.representante.alignment = Qt.AlignCenter
        self.representante.styleSheet = "color: gray; font-size: 15px;"

        self.ruc = QLineEdit(self.fr_contenedor_arriba)
        self.ruc.placeholderText= "RUC"
        self.ruc.geometry = QRect(10,130, 395,20)
        self.ruc.alignment = Qt.AlignCenter
        self.ruc.styleSheet = "color: gray; font-size: 15px;"

        self.celular = QLineEdit(self.fr_contenedor_arriba)
        self.celular.placeholderText= "Celular"
        self.celular.geometry = QRect(10,170, 395,20)
        self.celular.alignment = Qt.AlignCenter
        self.celular.styleSheet = "color: gray; font-size: 15px;"

        self.email = QLineEdit(self.fr_contenedor_arriba)
        self.email.placeholderText= "E-mail"
        self.email.geometry = QRect(10,210, 395,20)
        self.email.alignment = Qt.AlignCenter
        self.email.styleSheet = "color: gray; font-size: 15px;"

        self.tipo = QLineEdit(self.fr_contenedor_arriba)
        self.tipo.placeholderText= "Tipo Proveedor"
        self.tipo.geometry = QRect(10,250, 395,20)
        self.tipo.alignment = Qt.AlignCenter
        self.tipo.styleSheet = "color: gray; font-size: 15px;"

        self.boton_ingresar_proveedor = QPushButton(self.fr_contenedor_arriba)
        self.boton_ingresar_proveedor.text = "Registrar"
        self.boton_ingresar_proveedor.clicked.connect(self.insertarDatosBD)
        self.boton_ingresar_proveedor.geometry = QRect(350, 290, 170, 45)
        self.boton_ingresar_proveedor.styleSheet = "background: white; font-size: 15px;"

        #seccion de eliminar
        self.cmb_proveedor_BD = QComboBox(self.fr_contenedor_arriba)
        self.cmb_proveedor_BD.placeholderText= "Proveedor a eliminar..."
        self.cmb_proveedor_BD.geometry = QRect(500,50, 395,20)
        self.cmb_proveedor_BD.styleSheet = "color: gray; font-size: 15px;"
        self.cmb_proveedor_BD.addItems(self.datosTotal.buscar_proveedor_cmb())
        
        self.boton_eliminar_proveedor = QPushButton(self.fr_contenedor_arriba)
        self.boton_eliminar_proveedor.text = "Eliminar"
        self.boton_eliminar_proveedor.clicked.connect(self.eliminarProveedor)
        self.boton_eliminar_proveedor.geometry = QRect(520, 290, 170, 45)
        self.boton_eliminar_proveedor.styleSheet = "background: white; font-size: 15px;"

        
        #contenedor abajo
        self.fr_contenedor_abajo = QFrame(self)
        self.fr_contenedor_abajo.geometry=QRect(320, 360, 950, 350)
        self.fr_contenedor_abajo.styleSheet="background: white;"
        #texto del contenedor abajo
        self.texto_cont_abajo = QLabel(self.fr_contenedor_abajo)
        self.texto_cont_abajo.text = "Proveedores Registrados"  
        self.texto_cont_abajo.geometry = QRect(10,0, 850,30)
        self.texto_cont_abajo.alignment = Qt.AlignJustify
        self.texto_cont_abajo.styleSheet = "color: gray; font-size: 25px;"
        #tabla
        self.tabla_proveedores = QTableWidget(self.fr_contenedor_abajo)
        self.tabla_proveedores.dragDropOverwriteMode=False
        self.tabla_proveedores.selectionBehavior=QAbstractItemView.SelectRows
        self.tabla_proveedores.selectionMode=QAbstractItemView.SingleSelection
        self.tabla_proveedores.wordWrap=False
        self.tabla_proveedores.isSortingEnabled=False
        self.tabla_proveedores.alternatingRowColors=True
        self.tabla_proveedores.columnCount= 6
        self.tabla_proveedores.rowCount = 0
        nombreColumnas = ("Id", "Empresa", "Representante", "RUC", "Celular", "E-mail")
        self.tabla_proveedores.setHorizontalHeaderLabels(nombreColumnas)
        for indice, ancho in enumerate((80, 120, 120, 110, 150), start=0):
            self.tabla_proveedores.setColumnWidth(indice, ancho)

        self.tabla_proveedores.resize(800, 260)
        self.tabla_proveedores.move(50, 50)

        # campo de filtrado
        self.filtro_edit = QLineEdit(self.fr_contenedor_abajo, placeholderText ="Filtrar por empresa")
        self.filtro_edit.returnPressed.connect(self.aplicarFiltro)
        self.filtro_edit.geometry = QRect(560, 10, 200,33)

        #boton mostrar datos
        self.boton_mostrar_proveedor = QPushButton(self.fr_contenedor_abajo)
        self.boton_mostrar_proveedor.text = "Mostrar datos"
        self.boton_mostrar_proveedor.clicked.connect(self.datosTabla)
        self.boton_mostrar_proveedor.geometry = QRect(300, 0, 200,45)
        self.boton_mostrar_proveedor.styleSheet = "background: white; font-size: 15px;"
    
    def datosTabla(self):
        datos = self.datosTotal.buscar_proveedores()

        self.tabla_proveedores.clearContents()

        row = 0
        for endian in datos:
            self.tabla_proveedores.rowCount=row + 1
            
            idDato = QTableWidgetItem(str(endian[0]))
            idDato.setTextAlignment(4)
            
            self.tabla_proveedores.setItem(row, 0, idDato)
            self.tabla_proveedores.setItem(row, 1, QTableWidgetItem(endian[1]))
            self.tabla_proveedores.setItem(row, 2, QTableWidgetItem(endian[2]))
            self.tabla_proveedores.setItem(row, 3, QTableWidgetItem(endian[3]))
            self.tabla_proveedores.setItem(row, 4, QTableWidgetItem(endian[4]))
            self.tabla_proveedores.setItem(row, 5, QTableWidgetItem(endian[5]))

            row += 1

    def insertarDatosBD(self):
        if(self.nombre_empresa.text!="" or self.representante.text!="" or self.ruc.text!="" or self.celular.text!="" or self.email.text!="" or self.tipo.text!=""):
            empresa = self.nombre_empresa.text
            representante = self.representante.text
            ruc = self.ruc.text
            celular = self.celular.text
            email = self.email.text
            tipo = self.tipo.text

            self.datosTotal.inserta_proveedor(empresa, representante, ruc, celular, email, tipo)	
            print("Dato insertado!")
            QMessageBox.information(self, "Insertar Proveedores", "Dato insertado!")
            self.nombre_empresa.clear()
            self.representante.clear()
            self.ruc.clear()
            self.celular.clear()
            self.email.clear()
            self.tipo.clear()
        else:
            print("Escribir datos del proveedor a insertar.")
            QMessageBox.warning(self, "Insertar Proveedores", "Escribir datos del proveedor a insertar.")

    def eliminarProveedor(self):
        if(self.cmb_proveedor_BD.currentIndex!=-1):
            proveedor_app = "'"+self.cmb_proveedor_BD.currentText+"'"
            self.datosTotal.elimina_proveedor(proveedor_app)
            print("¡Proveedor eliminado! Actualice la tabla para visualizar el cambio.")
            QMessageBox.information(self, "Eliminar proveedor", "¡Proveedor eliminado! Actualice la tabla para visualizar el cambio.")
        else:
            print("No ha seleccionado ningun proveedor a eliminar.")
            QMessageBox.warning(self, "Eliminar proveedor", "No ha seleccionado ningun proveedor a eliminar.")

    def setup_name_user(self, username):
        self.titulo = QLabel(f"Bienvenido {username}", alignment = Qt.AlignCenter)
        self.titulo.styleSheet = "color: gray; font-size: 21px; font-weight: bold;"

        self.titulo_layout = QVBoxLayout()
        self.titulo_layout.addWidget(self.titulo)

        self.fr_bienvenida.setLayout(self.titulo_layout)

    def aplicarFiltro(self):
        texto_filtro = self.filtro_edit.text
        if texto_filtro:
            num_filas = self.tabla_proveedores.rowCount
            for fila in range(num_filas):
                ocultar_fila = True
                for columna in range(self.tabla_proveedores.columnCount):
                    item = self.tabla_proveedores.item(fila, columna)
                    if texto_filtro == item.text():
                        ocultar_fila = False
                        break
                self.tabla_proveedores.setRowHidden(fila, ocultar_fila)
        else:
            num_filas = self.tabla_proveedores.rowCount
            for fila in range(num_filas):
                self.tabla_proveedores.setRowHidden(fila, False)