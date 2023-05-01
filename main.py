from ctypes import alignment
from PySide6.QtWidgets import *
from PySide6.QtCore import *
#from PySide6.QtCharts import *
from conexionDB import *
import sys
from __feature__ import true_property
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class Window_main(QMainWindow):
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

        self.boton6 = QPushButton(self.fr_titulo)
        self.boton6.text = "Perfil"
        self.boton6.geometry = QRect(80, 420, 200,45)
        self.boton6.styleSheet = "background: white; font-size: 25px;"

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
        #grafico
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title('Cantidad de ventas por mes')
        self.ax.set_xlabel('Mes')
        self.ax.set_ylabel('Cantidad')
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas, self)#
        layout = QVBoxLayout(self.fr_contenedor_arriba)
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)#

        #x = np.arange(1, 73)
        y = self.datosTotal.grafico_ventas_cantidad()
        #self.ax.plot(x, y)

        categories = self.datosTotal.grafico_ventas()
        x_bars = np.arange(len(categories))
        width = 0.35
        self.ax.bar(x_bars, y, width, label='Cantidad de ventas')

        self.ax.set_xticks(x_bars)
        self.ax.set_xticklabels(categories)
        self.ax.legend()
        self.fig.tight_layout()

        self.toolbar.update()#
        self.canvas.draw()
        
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
        self.tabla.columnCount= 7
        self.tabla.rowCount = 0
        nombreColumnas = ("Id","Nombre", "Unidad de medida", "Stock", "Precio de compra unitario", "Mes", "Año")
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)
        for indice, ancho in enumerate((80, 120, 120, 110, 150), start=0):
            self.tabla.setColumnWidth(indice, ancho)

        self.tabla.resize(800, 260)
        self.tabla.move(50, 50)
        #boton mostrar datos
        self.boton_mostrar_datos = QPushButton(self.fr_contenedor_abajo)
        self.boton_mostrar_datos.text = "Mostrar datos"
        self.boton_mostrar_datos.clicked.connect(self.datosTabla)
        self.boton_mostrar_datos.geometry = QRect(190, 0, 200,45)
        self.boton_mostrar_datos.styleSheet = "background: white; font-size: 15px;"
    
    def datosTabla(self):
        datos = self.datosTotal.buscar_material()

        self.tabla.clearContents()

        row = 0
        for endian in datos:
            self.tabla.rowCount=row + 1
            
            idDato = QTableWidgetItem(str(endian[0]))
            idDato.setTextAlignment(4)
            
            self.tabla.setItem(row, 0, idDato)
            self.tabla.setItem(row, 1, QTableWidgetItem(endian[1]))
            self.tabla.setItem(row, 2, QTableWidgetItem(endian[2]))
            self.tabla.setItem(row, 3, QTableWidgetItem(str(endian[3])))
            self.tabla.setItem(row, 4, QTableWidgetItem(str(endian[4])))
            self.tabla.setItem(row, 5, QTableWidgetItem(endian[5]))
            self.tabla.setItem(row, 6, QTableWidgetItem(endian[6]))

            row += 1

    def setup_name_user(self, username):
        self.titulo = QLabel(f"Bienvenido {username}", alignment = Qt.AlignCenter)
        self.titulo.styleSheet = "color: gray; font-size: 21px; font-weight: bold;"

        self.titulo_layout = QVBoxLayout()
        self.titulo_layout.addWidget(self.titulo)

        self.fr_bienvenida.setLayout(self.titulo_layout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Plus:
            self.toolbar.zoom(1.1) # Aumentar el zoom en un 10%
        elif event.key() == Qt.Key_Minus:
            self.toolbar.zoom(0.9) # Disminuir el zoom en un 10%

