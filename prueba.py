from PySide6.QtWidgets import *
from PySide6.QtCore import *
from conexionDB import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.datosTotal = Registro_datos()
        self.setWindowTitle("Tabla de proveedores")
        self.setGeometry(100, 100, 900, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # tabla
        self.tabla_proveedores = QTableWidget()
        self.tabla_proveedores.setDragDropOverwriteMode(False)
        self.tabla_proveedores.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabla_proveedores.setSelectionMode(QTableWidget.SingleSelection)
        self.tabla_proveedores.setWordWrap(False)
        self.tabla_proveedores.setSortingEnabled(False)
        self.tabla_proveedores.setAlternatingRowColors(True)
        self.tabla_proveedores.setColumnCount(6)
        self.tabla_proveedores.setRowCount(0)
        nombreColumnas = ("Id", "Empresa", "Representante", "RUC", "Celular", "E-mail")
        self.tabla_proveedores.setHorizontalHeaderLabels(nombreColumnas)
        for indice, ancho in enumerate((80, 120, 120, 110, 150), start=0):
            self.tabla_proveedores.setColumnWidth(indice, ancho)
        header = self.tabla_proveedores.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.layout.addWidget(self.tabla_proveedores)

        # campo de filtrado
        self.filtro_edit = QLineEdit()
        self.filtro_edit.setPlaceholderText("Filtrar por empresa")
        self.layout.addWidget(self.filtro_edit)

        # botón mostrar datos
        self.boton_mostrar_proveedor = QPushButton("Mostrar datos")
        self.boton_mostrar_proveedor.setStyleSheet("background: white; font-size: 15px;")
        self.layout.addWidget(self.boton_mostrar_proveedor)

        self.boton_mostrar_proveedor.clicked.connect(self.datosTabla)

    def datosTabla(self):
        datos = self.datosTotal.buscar_proveedores()

        self.tabla_proveedores.clearContents()

        row = 0
        for endian in datos:
            self.tabla_proveedores.rowCount=row + 1
                
            idDato = QTableWidgetItem(str(endian[0]))
            #idDato.setTextAlignment(4)
                
            self.tabla_proveedores.setItem(row, 0, idDato)
            self.tabla_proveedores.setItem(row, 1, QTableWidgetItem(endian[1]))
            self.tabla_proveedores.setItem(row, 2, QTableWidgetItem(endian[2]))
            self.tabla_proveedores.setItem(row, 3, QTableWidgetItem(endian[3]))
            self.tabla_proveedores.setItem(row, 4, QTableWidgetItem(endian[4]))
            self.tabla_proveedores.setItem(row, 5, QTableWidgetItem(endian[5]))

            row += 1

app = QApplication([])
window = MainWindow()
window.show()
app.exec()


