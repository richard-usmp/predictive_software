from ctypes import alignment
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtCharts import *
from conexionDB import *
import sys
from __feature__ import true_property

class Window_main_admin(QMainWindow):
    def setupUi(self):
        self.datosTotal = Registro_datos()

        self.setFixedSize(1280, 720)
        self.styleSheet="background: gray;"
        self.setWindowTitle("JR Group SAC - Predictive Software_admin")

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
        self.boton6.text = "Crear usuario"
        self.boton6.geometry = QRect(80, 420, 200,45)
        self.boton6.styleSheet = "background: white; font-size: 25px;"

        self.boton7 = QPushButton(self.fr_titulo)
        self.boton7.text = "Perfil"
        self.boton7.geometry = QRect(80, 490, 200,45)
        self.boton7.styleSheet = "background: white; font-size: 25px;"

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
        self.line_charts_cont = QGridLayout(self.fr_contenedor_arriba)
        self.create_line_chart()
        
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

    def create_line_chart(self):
        self.lineSeries = QLineSeries()
        #Q_ventas
        a=1
        for x in self.datosTotal.grafico_ventas_cantidad():
            self.lineSeries.append(a,x)
            a = a + 1

        #grafico de barras = 0; sirve para colocar categoria al eje X
        for x in range(len(self.datosTotal.grafico_ventas())): 
            self.set0 = QBarSet(f"{x}")
        i = 0
        while i <=len(self.datosTotal.grafico_ventas()):
            j=0
            self.set0.append([j])
            i = i + 1

        self.barSeries = QBarSeries()
        self.barSeries.append(self.set0)

        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.barSeries)
        self.chart.addSeries(self.lineSeries)
        self.chart.createDefaultAxes()
        self.chart.zoom
        self.chart.title="Cantidad de ventas mensuales"

        self.categories = self.datosTotal.grafico_ventas()
        self.axisX = QBarCategoryAxis()
        self.axisX.append(self.categories)
        self.chart.setAxisX(self.axisX, self.lineSeries)
        self.chart.setAxisX(self.axisX, self.barSeries)
        self.chart.style = "font-size: 5px;"

        self.axisY = QValueAxis()
        self.chart.setAxisY(self.axisY, self.lineSeries)
        self.chart.setAxisY(self.axisY, self.barSeries)
        self.axisY.setRange(0, 50)

        self.chartView = QChartView(self.chart)

        #self.chart.animationOptions=QChart.AllAnimations

        self.chartView.chart().theme=QChart.ChartThemeDark
        self.line_charts_cont.addWidget(self.chartView)

    def keyPressEvent(self,event):
        if(event.key() == Qt.Key_Plus):
            self.chart.zoomIn()
        elif(event.key() == Qt.Key_Minus):
            self.chart.zoomOut()
        elif(event.key() == Qt.Key_D):
            self.chart.scroll(15,0)
        elif(event.key() == Qt.Key_A):
            self.chart.scroll(-15,0)
        elif(event.key() == Qt.Key_W):
            self.chart.scroll(0,10)
        elif(event.key() == Qt.Key_S):
            self.chart.scroll(0,-10)
        elif(event.key() == Qt.Key_R):
            self.chart.zoomReset()