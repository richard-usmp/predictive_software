from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
from conexionDB import *
from datetime import date
from __feature__ import true_property

today = date.today()

class Window_material_log(QMainWindow):
    def setupUi(self):
        self.datosTotal = Registro_datos()

        self.setFixedSize(1330, 380)
        self.styleSheet="background: gray;"
        self.setWindowTitle("JR Group SAC - Predictive Software")

        self.fr_frame_tabla = QFrame(self)
        self.fr_frame_tabla.geometry=QRect(20, 20, 1290, 340)
        self.fr_frame_tabla.styleSheet="background: white;"

        #texto del contenedor arriba
        self.texto_cont = QLabel(self.fr_frame_tabla)
        self.texto_cont.text = "Historial de materia prima"  
        self.texto_cont.geometry = QRect(10,0, 850,30)
        self.texto_cont.alignment = Qt.AlignJustify
        self.texto_cont.styleSheet = "color: blue; font-size: 25px; font-weight: bold;"

        #tabla
        self.tabla = QTableWidget(self.fr_frame_tabla)
        self.tabla.dragDropOverwriteMode=False
        self.tabla.selectionBehavior=QAbstractItemView.SelectRows
        self.tabla.selectionMode=QAbstractItemView.SingleSelection
        self.tabla.wordWrap=False
        self.tabla.isSortingEnabled=False
        self.tabla.alternatingRowColors=True
        self.tabla.columnCount= 9
        self.tabla.rowCount = 0
        nombreColumnas = ("ID_material", "Descripción", "Stock","Precio de compra unitario", "Día", "Mes", "Año", "Estado", "Usuario modificador")
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)
        for indice, ancho in enumerate((80, 120, 120, 110, 150), start=0):
            self.tabla.setColumnWidth(indice, ancho)

        self.tabla.resize(1175, 260)
        self.tabla.move(50, 50)
        #boton mostrar datos
        self.boton_mostrar_datos = QPushButton(self.fr_frame_tabla)
        self.boton_mostrar_datos.text = "Mostrar datos"
        self.boton_mostrar_datos.clicked.connect(self.datosTabla)
        self.boton_mostrar_datos.geometry = QRect(450, 0, 200,45)
        self.boton_mostrar_datos.styleSheet = "background: white; font-size: 15px;"

        #boton generar reporte
        self.boton_mostrar_datos = QPushButton(self.fr_frame_tabla)
        self.boton_mostrar_datos.text = "Exportar a excel"
        self.boton_mostrar_datos.clicked.connect(self.generarReporteExcel)
        self.boton_mostrar_datos.geometry = QRect(660, 0, 200,45)
        self.boton_mostrar_datos.styleSheet = "background: white; font-size: 15px;"

    def generarReporteExcel(self):
        dia = today.strftime("%d")
        mes = today.strftime("%m")
        anio = today.strftime("%Y")
        fecha = str(anio + "-" + mes + "-" + dia)
        filename = 'Reportes/historial_recursos' + '_' + fecha + '.xlsx'
        data_list = self.datosTotal.buscar_Material_log()
        data_list = [[item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8]] for item in data_list]
        df = pd.DataFrame(data_list, columns=["ID_material", "Descripción", "Stock","Precio de compra unitario", "Día", "Mes", "Año", "Estado", "Usuario modificador"])
        df.to_excel(filename, index=False)
        QMessageBox.information(self, "Excel", f"Se generó un excel con el historial de recursos en {filename}")

    def datosTabla(self):
        datos = self.datosTotal.buscar_Material_log()

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
            self.tabla.setItem(row, 6, QTableWidgetItem(str(endian[6])))
            self.tabla.setItem(row, 7, QTableWidgetItem(str(endian[7])))
            self.tabla.setItem(row, 8, QTableWidgetItem(str(endian[8])))
            #self.tabla.setItem(row, 9, QTableWidgetItem(str(endian[9])))

            row += 1