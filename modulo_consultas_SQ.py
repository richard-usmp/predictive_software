from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
from conexionDB import *
from __feature__ import true_property
import requests
import json
import jinja2
import pdfkit
from datetime import date
import math
import pandas as pd
from datetime import datetime

today = date.today()

class Window_consultas_SQ(QMainWindow):
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
        self.fr_contenedor_arriba.geometry=QRect(320, 10, 950, 700)
        self.fr_contenedor_arriba.styleSheet="background: white;"
        #texto del contenedor arriba
        self.texto_cont_arriba = QLabel(self.fr_contenedor_arriba)
        self.texto_cont_arriba.text = "Consultas SQ"  
        self.texto_cont_arriba.geometry = QRect(10,0, 850,35)
        self.texto_cont_arriba.alignment = Qt.AlignJustify
        self.texto_cont_arriba.styleSheet = "color: gray; font-size: 25px; font-weight: bold;"

        #texto del contenedor arriba
        self.texto_cont_abajo = QLabel(self.fr_contenedor_arriba)
        self.texto_cont_abajo.text = "DataSet"  
        self.texto_cont_abajo.geometry = QRect(10,0, 850,30)
        self.texto_cont_abajo.alignment = Qt.AlignJustify
        self.texto_cont_abajo.styleSheet = "color: blue; font-size: 25px;"
        #tabla
        self.tabla = QTableWidget(self.fr_contenedor_arriba)
        self.tabla.dragDropOverwriteMode=False
        self.tabla.selectionBehavior=QAbstractItemView.SelectRows
        self.tabla.selectionMode=QAbstractItemView.SingleSelection
        self.tabla.wordWrap=False
        self.tabla.isSortingEnabled=False
        self.tabla.alternatingRowColors=True
        self.tabla.columnCount= 7
        self.tabla.rowCount = 0
        nombreColumnas = ('Fecha', 'Venta Diaria', 'Sumatoria de cantidad total de Productos Vendidos', 'Mes', 'Dia', 'Año', 'Producto')
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)
        for indice, ancho in enumerate((80, 120, 120, 110, 150), start=0):
            self.tabla.setColumnWidth(indice, ancho)

        self.tabla.resize(800, 260)
        self.tabla.move(50, 50)
        #boton mostrar datos
        self.boton_mostrar_datos = QPushButton(self.fr_contenedor_arriba)
        self.boton_mostrar_datos.text = "Mostrar datos"
        self.boton_mostrar_datos.clicked.connect(self.datosTabla)
        self.boton_mostrar_datos.geometry = QRect(350, 0, 200,45)
        self.boton_mostrar_datos.styleSheet = "background: white; font-size: 15px;"

        #boton generar dataset
        self.boton_dataset = QPushButton(self.fr_contenedor_arriba)
        self.boton_dataset.text = "Generar dataset en excel"
        self.boton_dataset.clicked.connect(self.generar_dataset)
        self.boton_dataset.geometry = QRect(510, 380, 250,55)
        self.boton_dataset.styleSheet = "background: white; font-size: 15px;"

        #Texto Analisis predictivo
        self.texto_titulo = QLabel(self.fr_contenedor_arriba)
        self.texto_titulo.text = "Análisis Predictivo"  
        self.texto_titulo.geometry = QRect(10,350, 850,30)
        self.texto_titulo.alignment = Qt.AlignJustify
        self.texto_titulo.styleSheet = "color: blue; font-size: 25px;"
        #Formulario ana_predi
        self.fecha = QComboBox(self.fr_contenedor_arriba)
        self.fecha.placeholderText= "Fecha"
        self.fecha.geometry = QRect(10,400, 395,20)
        self.fecha.styleSheet = "color: gray; font-size: 15px;"
        self.fecha.addItems(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Setiembre", "Octubre", "Noviembre", "Diciembre"])

        self.producto = QComboBox(self.fr_contenedor_arriba)
        self.producto.placeholderText= "Producto"
        self.producto.geometry = QRect(10,450, 395,20)
        self.producto.styleSheet = "color: gray; font-size: 15px;"
        self.producto.addItems(['Todo', 'Cisternas de Combustible', 'Cisternas de Ácidos', 'Cisternas de Agua', 'Tolvas Volquetes', 'Semirremolques', 'Remolques', 'Cisternas de lacteos', 'Cisternas de GLP', 'Baranda de madera'])

        self.boton_analisis_predictivos = QPushButton(self.fr_contenedor_arriba)
        self.boton_analisis_predictivos.text = "Análisis predictivo"
        self.boton_analisis_predictivos.clicked.connect(self.rest_api)
        self.boton_analisis_predictivos.geometry = QRect(10, 540, 200,45)
        self.boton_analisis_predictivos.styleSheet = "background: white; font-size: 15px;"

    def datosTabla(self):
        datos = self.datosTotal.buscar_dataset()

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

            row += 1

    def setup_name_user(self, username):
        self.titulo = QLabel(f"Bienvenido {username}", alignment = Qt.AlignCenter)
        self.titulo.styleSheet = "color: gray; font-size: 21px; font-weight: bold;"

        self.titulo_layout = QVBoxLayout()
        self.titulo_layout.addWidget(self.titulo)

        self.fr_bienvenida.setLayout(self.titulo_layout)

    def generar_dataset(self):
        Mes = today.strftime("%m")
        Anio = today.strftime("%Y")
        Año_y_mes = str(Anio + "-" + Mes)
        filename = 'Dataset/dataset' + '_' + Año_y_mes + '.xlsx'
        dataset = self.datosTotal.generar_dataset()
        data_list = [[datetime.strptime(item[0], "%Y-%m-%d").strftime("%Y-%m-%d"), item[1], item[2], item[3], item[4], item[5], item[6]] for item in dataset]
        df = pd.DataFrame(data_list, columns=["Fechaa", "Cant_Total_Productos_Vendidos", "Total_Prod_Vendidos", "Mes", "Dia", "Anio", "Producto"])
        df.to_excel(filename, index=False)
        QMessageBox.information(self, "Excel", f"Se generó un excel con el dataset en {filename}")

    def rest_api(self):
        if(self.producto.currentIndex!=-1 or self.fecha.currentIndex!=-1):
            anio = today.strftime("%Y")
            mes_ = self.fecha.currentIndex + 1
            producto = self.producto.currentText
            QMessageBox.information(self, "Predicción...", f"La predicción se realizará para el mes de {self.fecha.currentText}.")
            #r = requests.post('https://api-tesis-usmp.herokuapp.com/prophetv3', json={'mes': mes_, 'producto': producto})
            r = requests.post('https://api-tesis-usmp2-0951b175bd55.herokuapp.com/prophetv3', json={'mes': mes_, 'producto': producto})
            #r = requests.post('http://127.0.0.1:4100/prophetv3', json={'mes': mes_, 'producto': producto})
            json_texto = r.text
            if producto =='Todo':
                jsondecoded = json.loads(json_texto) #para todo
                prediccion_ventas_total = jsondecoded["yhat"]
                
                datos_modificados = {}
                total_demanda = []
                for key, prediccion in prediccion_ventas_total.items():
                    nuevo_nombre = key.replace('Prophet_', '').replace('.pckl', '')
                    datos_modificados[nuevo_nombre] = prediccion
                
                for key, prediccion in datos_modificados.items():
                    print(f'{key}: {prediccion}')
                    if prediccion < 1:
                        prediccion = 0
                    if key == 'Cisternas de Combustible':
                        aluminio=1
                        pernosaluminio=3.5
                        combustible=1
                        pastaparametalesdura=2.61
                        pastaparametalessuave=2.01
                        pinturametalica=0.68
                        lijaparametalesn80=4.5
                        lijaparametalesn180=3.14
                        discocorteabl=3.38
                        trapometalesparapulir=1.29
                        petroleo=2.11
                        tiner=0.44
                        sacosparaproductosfinales=2.4
                        madera=1.5
                        pernoscobre=2.2
                        rafia=2.5
                        discocorteacl=3.35
                        jebesabl=2
                        jebesacl=3.5
                        tornillosaluminio=1.65
                        remachesaluminio=1.14
                        brocasparaaluminio=2.5
                        lijaparametalesn120=5.5
                        fajasmetalicas=2.45
                        pastaparametalesroja=3.5
                        lijaparametales60=2.5
                        acerosmicroaleados=1.5
                        acerosrefosforados=8.5
                        maderasintetica=1.1
                        pernosallenconcabezacilindrica=1.1
                        pernoprisionero=2.01
                        pernoenaceroinoxidable=1.5
                        acerosfasedoble=1.13
                        pernocabezaredonda=2
                        pernocabezahexagonalsaegrado5=1.1

                    elif key == 'Cisternas de Ácidos':
                        aluminio=1.5
                        pernosaluminio=3
                        combustible=1.5
                        pastaparametalesdura=2.47
                        pastaparametalessuave=3.05
                        pinturametalica=0.46
                        lijaparametalesn80=3.2
                        lijaparametalesn180=5.5
                        discocorteabl=2.31
                        trapometalesparapulir=0.6
                        petroleo=2.11
                        tiner=0.12
                        sacosparaproductosfinales=2.4
                        madera=1.7
                        pernoscobre=3.5
                        rafia=3
                        discocorteacl=3.35
                        jebesabl=3.2
                        jebesacl=3.24
                        tornillosaluminio=2.34
                        remachesaluminio=5
                        brocasparaaluminio=3.2
                        lijaparametalesn120=3.25
                        fajasmetalicas=1.8
                        pastaparametalesroja=3.5
                        lijaparametales60=2.1
                        acerosmicroaleados=2.5
                        acerosrefosforados=7.5
                        maderasintetica=1.35
                        pernosallenconcabezacilindrica=1.14
                        pernoprisionero=1.02
                        pernoenaceroinoxidable=1
                        acerosfasedoble=1.23
                        pernocabezaredonda=1.5
                        pernocabezahexagonalsaegrado5=1.2

                    elif key == 'Cisternas de Agua':
                        aluminio=1
                        pernosaluminio=3.2
                        combustible=1.5
                        pastaparametalesdura=2.79
                        pastaparametalessuave=4.08
                        pinturametalica=0.27
                        lijaparametalesn80=2.8
                        lijaparametalesn180=7.2
                        discocorteabl=2.21
                        trapometalesparapulir=1.18
                        petroleo=2.11
                        tiner=0.67
                        sacosparaproductosfinales=2.4
                        madera=0.6
                        pernoscobre=3.3
                        rafia=3.41
                        discocorteacl=2.06
                        jebesabl=2.12
                        jebesacl=3
                        tornillosaluminio=2.09
                        remachesaluminio=4.5
                        brocasparaaluminio=1.49
                        lijaparametalesn120=2.1
                        fajasmetalicas=3
                        pastaparametalesroja=1.49
                        lijaparametales60=1.7
                        acerosmicroaleados=0.5
                        acerosrefosforados=7.5
                        maderasintetica=0.75
                        pernosallenconcabezacilindrica=1.15
                        pernoprisionero=0.04
                        pernoenaceroinoxidable=1.2
                        acerosfasedoble=1.2
                        pernocabezaredonda=1
                        pernocabezahexagonalsaegrado5=1.3

                    elif key == 'Tolvas Volquetes':
                        aluminio=1
                        pernosaluminio=1.7
                        combustible=0.5
                        pastaparametalesdura=2.39
                        pastaparametalessuave=5.02
                        pinturametalica=0.68
                        lijaparametalesn80=1
                        lijaparametalesn180=2.4
                        discocorteabl=3.23
                        trapometalesparapulir=0.8
                        petroleo=2.11
                        tiner=0.48
                        sacosparaproductosfinales=1
                        madera=0.1
                        pernoscobre=2.6
                        rafia=2
                        discocorteacl=0.2
                        jebesabl=1.02
                        jebesacl=0
                        tornillosaluminio=1.09
                        remachesaluminio=3
                        brocasparaaluminio=1.2
                        lijaparametalesn120=1.2
                        fajasmetalicas=1.25
                        pastaparametalesroja=4.25
                        lijaparametales60=2.84
                        acerosmicroaleados=2
                        acerosrefosforados=6.5
                        maderasintetica=1.24
                        pernosallenconcabezacilindrica=0.56
                        pernoprisionero=1
                        pernoenaceroinoxidable=0.75
                        acerosfasedoble=1
                        pernocabezaredonda=2
                        pernocabezahexagonalsaegrado5=1

                    elif key == 'Semirremolques':
                        aluminio=1.5
                        pernosaluminio=7.1
                        combustible=2.5
                        pastaparametalesdura=2.69
                        pastaparametalessuave=1.5
                        pinturametalica=3.36
                        lijaparametalesn80=1.24
                        lijaparametalesn180=1.5
                        discocorteabl=1.5
                        trapometalesparapulir=0.41
                        petroleo=2.11
                        tiner=0.54
                        sacosparaproductosfinales=1.6
                        madera=1.4
                        pernoscobre=2.8
                        rafia=1.41
                        discocorteacl=0.1
                        jebesabl=4.2
                        jebesacl=2
                        tornillosaluminio=1.7
                        remachesaluminio=3
                        brocasparaaluminio=2.3
                        lijaparametalesn120=4
                        fajasmetalicas=1
                        pastaparametalesroja=1.75
                        lijaparametales60=1.2
                        acerosmicroaleados=1
                        acerosrefosforados=4.5
                        maderasintetica=1.25
                        pernosallenconcabezacilindrica=0.67
                        pernoprisionero=1
                        pernoenaceroinoxidable=2
                        acerosfasedoble=0.5
                        pernocabezaredonda=1
                        pernocabezahexagonalsaegrado5=0.8

                    elif key == 'Remolques':
                        aluminio=1
                        pernosaluminio=3.18
                        combustible=3.19
                        pastaparametalesdura=2.75
                        pastaparametalessuave=3.49
                        pinturametalica=5.62
                        lijaparametalesn80=6
                        lijaparametalesn180=2.9
                        discocorteabl=2.01
                        trapometalesparapulir=0.89
                        petroleo=2.11
                        tiner=0.5
                        sacosparaproductosfinales=5.07
                        madera=0.31
                        pernoscobre=3.9
                        rafia=5.18
                        discocorteacl=0.97
                        jebesabl=2
                        jebesacl=2
                        tornillosaluminio=4.5
                        remachesaluminio=2
                        brocasparaaluminio=0.5
                        lijaparametalesn120=1.64
                        fajasmetalicas=4.3
                        pastaparametalesroja=2.25
                        lijaparametales60=4.1
                        acerosmicroaleados=0.5
                        acerosrefosforados=5.5
                        maderasintetica=0.89
                        pernosallenconcabezacilindrica=1.78
                        pernoprisionero=2.06
                        pernoenaceroinoxidable=1
                        acerosfasedoble=1.5
                        pernocabezaredonda=1.21
                        pernocabezahexagonalsaegrado5=2.4

                    elif key == 'Cisternas de lacteos':
                        aluminio=1
                        pernosaluminio=0.9
                        combustible=1
                        pastaparametalesdura=2.8
                        pastaparametalessuave=1.99
                        pinturametalica=2.78
                        lijaparametalesn80=1.3
                        lijaparametalesn180=1.5
                        discocorteabl=1.35
                        trapometalesparapulir=0.6
                        petroleo=2.11
                        tiner=0.6
                        sacosparaproductosfinales=3.7
                        madera=0.2
                        pernoscobre=3
                        rafia=1.5
                        discocorteacl=3.35
                        jebesabl=2
                        jebesacl=3.5
                        tornillosaluminio=2.01
                        remachesaluminio=1
                        brocasparaaluminio=0.6
                        lijaparametalesn120=2
                        fajasmetalicas=2.2
                        pastaparametalesroja=0.75
                        lijaparametales60=2
                        acerosmicroaleados=0.5
                        acerosrefosforados=2.5
                        maderasintetica=1.05
                        pernosallenconcabezacilindrica=1.4
                        pernoprisionero=1.07
                        pernoenaceroinoxidable=1
                        acerosfasedoble=0.5
                        pernocabezaredonda=1
                        pernocabezahexagonalsaegrado5=1

                    elif key == 'Cisternas de Ácidos':
                        aluminio=1.5
                        pernosaluminio=3
                        combustible=1.5
                        pastaparametalesdura=2.47
                        pastaparametalessuave=3.05
                        pinturametalica=0.46
                        lijaparametalesn80=3.2
                        lijaparametalesn180=5.5
                        discocorteabl=2.31
                        trapometalesparapulir=0.6
                        petroleo=2.11
                        tiner=0.12
                        sacosparaproductosfinales=2.4
                        madera=1.7
                        pernoscobre=3.5
                        rafia=3
                        discocorteacl=3.35
                        jebesabl=3.2
                        jebesacl=3.24
                        tornillosaluminio=2.34
                        remachesaluminio=5
                        brocasparaaluminio=3.2
                        lijaparametalesn120=3.25
                        fajasmetalicas=1.8
                        pastaparametalesroja=3.5
                        lijaparametales60=2.1
                        acerosmicroaleados=2.5
                        acerosrefosforados=7.5
                        maderasintetica=1.35
                        pernosallenconcabezacilindrica=1.14
                        pernoprisionero=1.02
                        pernoenaceroinoxidable=1
                        acerosfasedoble=1.23
                        pernocabezaredonda=1.5
                        pernocabezahexagonalsaegrado5=1.2

                    elif key == 'Cisternas de GLP':
                        aluminio=1
                        pernosaluminio=1.81
                        combustible=4
                        pastaparametalesdura=2.29
                        pastaparametalessuave=1
                        pinturametalica=2.15
                        lijaparametalesn80=2.1
                        lijaparametalesn180=0.7
                        discocorteabl=2.45
                        trapometalesparapulir=0.62
                        petroleo=2.11
                        tiner=0.57
                        sacosparaproductosfinales=3.7
                        madera=0.13
                        pernoscobre=1.49
                        rafia=2.89
                        discocorteacl=3.35
                        jebesabl=2
                        jebesacl=4
                        tornillosaluminio=2.5
                        remachesaluminio=2
                        brocasparaaluminio=1.1
                        lijaparametalesn120=2
                        fajasmetalicas=1.54
                        pastaparametalesroja=1.5
                        lijaparametales60=1.2
                        acerosmicroaleados=0.5
                        acerosrefosforados=2.5
                        maderasintetica=1.26
                        pernosallenconcabezacilindrica=1.454
                        pernoprisionero=0.89
                        pernoenaceroinoxidable=0.5
                        acerosfasedoble=0.5
                        pernocabezaredonda=0.7
                        pernocabezahexagonalsaegrado5=1.1

                    elif key == 'Baranda de madera':
                        aluminio=0
                        pernosaluminio=0
                        combustible=2
                        pastaparametalesdura=0
                        pastaparametalessuave=0
                        pinturametalica=2.99
                        lijaparametalesn80=0
                        lijaparametalesn180=0
                        discocorteabl=1
                        trapometalesparapulir=0
                        petroleo=2.11
                        tiner=19.12
                        sacosparaproductosfinales=2.12
                        madera=45
                        pernoscobre=0.7
                        rafia=2.5
                        discocorteacl=0.46
                        jebesabl=0
                        jebesacl=0
                        tornillosaluminio=2.01
                        remachesaluminio=0.5
                        brocasparaaluminio=0
                        lijaparametalesn120=0
                        fajasmetalicas=0
                        pastaparametalesroja=0
                        lijaparametales60=0
                        acerosmicroaleados=0
                        acerosrefosforados=0
                        maderasintetica=1.1
                        pernosallenconcabezacilindrica=0
                        pernoprisionero=0
                        pernoenaceroinoxidable=0.5
                        acerosfasedoble=0
                        pernocabezaredonda=0.3
                        pernocabezahexagonalsaegrado5=0
                    
                    ####PDF_TODO
                    q_aluminio = round( aluminio * prediccion)
                    q_pernos_de_aluminio = round(pernosaluminio * prediccion)
                    q_combustible = round(combustible * prediccion)
                    q_pasta_para_metales_dura = round(pastaparametalesdura * prediccion)
                    q_pasta_para_metales_suave = round(pastaparametalessuave * prediccion)
                    q_pintura_metalica = round(pinturametalica * prediccion)
                    q_lija_para_metales_n80 = round(lijaparametalesn80 * prediccion)
                    q_lija_para_metales_n180 = round(lijaparametalesn180 * prediccion)
                    q_disco_de_corte_abl = round(discocorteabl * prediccion)
                    q_trapo_de_metales_para_pulir = round(trapometalesparapulir * prediccion)
                    q_petroleo = round(petroleo * prediccion)
                    q_tiner = round(tiner * prediccion)
                    q_sacos_para_productos_finales = round(sacosparaproductosfinales * prediccion)
                    q_madera = round(madera * prediccion)
                    q_pernos_de_cobre = round(pernoscobre * prediccion)
                    q_rafia = round(rafia * prediccion)
                    q_disco_de_corte_acl = round(discocorteacl * prediccion)
                    q_jebes_abl = round(jebesabl * prediccion)
                    q_jebes_acl = round(jebesacl * prediccion)
                    q_tornillos_de_aluminio = round(tornillosaluminio * prediccion)
                    q_remaches_de_aluminio = round(remachesaluminio * prediccion)
                    q_brocas_para_aluminio = round(brocasparaaluminio * prediccion)
                    q_lija_para_metales_n120 = round(lijaparametalesn120 * prediccion)
                    q_fajas_metalicas = round(fajasmetalicas * prediccion)
                    q_pasta_para_metales_roja = round(pastaparametalesroja * prediccion)
                    q_lija_para_metales_60 = round(lijaparametales60 * prediccion)
                    q_aceros_microaleados = round(acerosmicroaleados * prediccion)##
                    q_aceros_refosforados = round(acerosrefosforados * prediccion)
                    q_madera_sintetica = round(maderasintetica * prediccion)
                    q_pernos_allen_con_cabeza_cilindrica = round(pernosallenconcabezacilindrica * prediccion)
                    q_perno_prisionero = round(pernoprisionero * prediccion)
                    q_perno_en_acero_inoxidable = round(pernoenaceroinoxidable * prediccion)
                    q_aceros_de_fase_doble = round(acerosfasedoble * prediccion)
                    q_perno_cabeza_redonda = round(pernocabezaredonda * prediccion)
                    q_perno_cabeza_hexagonal_sae_grado_5 = round(pernocabezahexagonalsaegrado5 * prediccion)

                    #PDF
                    ruta_template = 'D:/Ricardo/Documents/predictive_software/template_todo.html'
                    info = {"mes":self.fecha.currentText, "producto": key, "prediccion_ventas": math.floor(prediccion) , "q_aluminio": q_aluminio, "q_pernos_aluminio": q_pernos_de_aluminio, "q_combustible": q_combustible, 
                            "q_pasta_para_metales_dura": q_pasta_para_metales_dura, "q_pasta_para_metales_suave": q_pasta_para_metales_suave, "q_pintura_metalica": q_pintura_metalica, "q_lija_para_metales_n80": q_lija_para_metales_n80, 
                            "q_lija_para_metales_n180": q_lija_para_metales_n180, "q_disco_corte_abl": q_disco_de_corte_abl, "q_trapo_metales_para_pulir": q_trapo_de_metales_para_pulir, "q_petroleo": q_petroleo, 
                            "q_tiner": q_tiner, "q_sacos_para_productos_finales": q_sacos_para_productos_finales, "q_madera": q_madera, "q_pernos_cobre": q_pernos_de_cobre, "q_rafia": q_rafia, 
                            "q_disco_corte_acl": q_disco_de_corte_acl, "q_jebes_abl": q_jebes_abl, "q_jebes_acl": q_jebes_acl, "q_tornillos_aluminio": q_tornillos_de_aluminio, "q_remaches_aluminio": q_remaches_de_aluminio, 
                            "q_brocas_para_aluminio": q_brocas_para_aluminio, "q_lija_para_metales_n120": q_lija_para_metales_n120, "q_fajas_metalicas": q_fajas_metalicas, "q_pasta_para_metales_roja": q_pasta_para_metales_roja, 
                            "q_lija_para_metales_60": q_lija_para_metales_60, "q_aceros_microaleados": q_aceros_microaleados, "q_aceros_refosforados": q_aceros_refosforados, "q_madera_sintetica": q_madera_sintetica, 
                            "q_pernos_allen_con_cabeza_cilindrica": q_pernos_allen_con_cabeza_cilindrica, "q_perno_prisionero": q_perno_prisionero, "q_perno_en_acero_inoxidable": q_perno_en_acero_inoxidable,
                            "q_aceros_de_fase_doble": q_aceros_de_fase_doble, "q_perno_cabeza_redonda": q_perno_cabeza_redonda, "q_perno_cabeza_hexagonal_sae_grado_5": q_perno_cabeza_hexagonal_sae_grado_5}
                    nombre_template = ruta_template.split('/')[-1]
                    ruta_template = ruta_template.replace(nombre_template,'')
                    
                    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
                    template=env.get_template(nombre_template)
                    html = template.render(info)
                    
                    options = { 'page-size': 'Letter', 'margin-top': '0.05in', 'margin-right': '0.05in', 'margin-bottom': '0.05in', 'margin-left': '0.05in', 'encoding':'UTF-8'}
                    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
                    ruta_salida = f'predictive_software_{key}_{self.fecha.currentText}-{anio}.pdf'
                    pdfkit.from_string(html, ruta_salida, options=options, configuration=config)
                    total_demanda.append(prediccion)
                total_demanda = round(sum(total_demanda),2)
                QMessageBox.information(self, "Predicción...", f"Se exportaron los PDF con los resultados. El total de demanda de carrocerias es {total_demanda}.")    

            else:
                jsondecoded = json.loads(json_texto[1:len(json_texto)-2])#quitar corchetes inicio y final
                prediccion_ventas = jsondecoded["yhat"]
                print(prediccion_ventas)
                if prediccion_ventas < 1:
                    prediccion_ventas = 0
                if producto == 'Cisternas de Combustible':
                    aluminio=1
                    pernosaluminio=3.5
                    combustible=1
                    pastaparametalesdura=2.61
                    pastaparametalessuave=2.01
                    pinturametalica=0.68
                    lijaparametalesn80=4.5
                    lijaparametalesn180=3.14
                    discocorteabl=3.38
                    trapometalesparapulir=1.29
                    petroleo=2.11
                    tiner=0.44
                    sacosparaproductosfinales=2.4
                    madera=1.5
                    pernoscobre=2.2
                    rafia=2.5
                    discocorteacl=3.35
                    jebesabl=2
                    jebesacl=3.5
                    tornillosaluminio=1.65
                    remachesaluminio=1.14
                    brocasparaaluminio=2.5
                    lijaparametalesn120=5.5
                    fajasmetalicas=2.45
                    pastaparametalesroja=3.5
                    lijaparametales60=2.5
                    acerosmicroaleados=1.5
                    acerosrefosforados=8.5
                    maderasintetica=1.1
                    pernosallenconcabezacilindrica=1.1
                    pernoprisionero=2.01
                    pernoenaceroinoxidable=1.5
                    acerosfasedoble=1.13
                    pernocabezaredonda=2
                    pernocabezahexagonalsaegrado5=1.1

                elif producto == 'Cisternas de Ácidos':
                    aluminio=1.5
                    pernosaluminio=3
                    combustible=1.5
                    pastaparametalesdura=2.47
                    pastaparametalessuave=3.05
                    pinturametalica=0.46
                    lijaparametalesn80=3.2
                    lijaparametalesn180=5.5
                    discocorteabl=2.31
                    trapometalesparapulir=0.6
                    petroleo=2.11
                    tiner=0.12
                    sacosparaproductosfinales=2.4
                    madera=1.7
                    pernoscobre=3.5
                    rafia=3
                    discocorteacl=3.35
                    jebesabl=3.2
                    jebesacl=3.24
                    tornillosaluminio=2.34
                    remachesaluminio=5
                    brocasparaaluminio=3.2
                    lijaparametalesn120=3.25
                    fajasmetalicas=1.8
                    pastaparametalesroja=3.5
                    lijaparametales60=2.1
                    acerosmicroaleados=2.5
                    acerosrefosforados=7.5
                    maderasintetica=1.35
                    pernosallenconcabezacilindrica=1.14
                    pernoprisionero=1.02
                    pernoenaceroinoxidable=1
                    acerosfasedoble=1.23
                    pernocabezaredonda=1.5
                    pernocabezahexagonalsaegrado5=1.2

                elif producto == 'Cisternas de Agua':
                    aluminio=1
                    pernosaluminio=3.2
                    combustible=1.5
                    pastaparametalesdura=2.79
                    pastaparametalessuave=4.08
                    pinturametalica=0.27
                    lijaparametalesn80=2.8
                    lijaparametalesn180=7.2
                    discocorteabl=2.21
                    trapometalesparapulir=1.18
                    petroleo=2.11
                    tiner=0.67
                    sacosparaproductosfinales=2.4
                    madera=0.6
                    pernoscobre=3.3
                    rafia=3.41
                    discocorteacl=2.06
                    jebesabl=2.12
                    jebesacl=3
                    tornillosaluminio=2.09
                    remachesaluminio=4.5
                    brocasparaaluminio=1.49
                    lijaparametalesn120=2.1
                    fajasmetalicas=3
                    pastaparametalesroja=1.49
                    lijaparametales60=1.7
                    acerosmicroaleados=0.5
                    acerosrefosforados=7.5
                    maderasintetica=0.75
                    pernosallenconcabezacilindrica=1.15
                    pernoprisionero=0.04
                    pernoenaceroinoxidable=1.2
                    acerosfasedoble=1.2
                    pernocabezaredonda=1
                    pernocabezahexagonalsaegrado5=1.3

                elif producto == 'Tolvas Volquetes':
                    aluminio=1
                    pernosaluminio=1.7
                    combustible=0.5
                    pastaparametalesdura=2.39
                    pastaparametalessuave=5.02
                    pinturametalica=0.68
                    lijaparametalesn80=1
                    lijaparametalesn180=2.4
                    discocorteabl=3.23
                    trapometalesparapulir=0.8
                    petroleo=2.11
                    tiner=0.48
                    sacosparaproductosfinales=1
                    madera=0.1
                    pernoscobre=2.6
                    rafia=2
                    discocorteacl=0.2
                    jebesabl=1.02
                    jebesacl=0
                    tornillosaluminio=1.09
                    remachesaluminio=3
                    brocasparaaluminio=1.2
                    lijaparametalesn120=1.2
                    fajasmetalicas=1.25
                    pastaparametalesroja=4.25
                    lijaparametales60=2.84
                    acerosmicroaleados=2
                    acerosrefosforados=6.5
                    maderasintetica=1.24
                    pernosallenconcabezacilindrica=0.56
                    pernoprisionero=1
                    pernoenaceroinoxidable=0.75
                    acerosfasedoble=1
                    pernocabezaredonda=2
                    pernocabezahexagonalsaegrado5=1

                elif producto == 'Semirremolques':
                    aluminio=1.5
                    pernosaluminio=7.1
                    combustible=2.5
                    pastaparametalesdura=2.69
                    pastaparametalessuave=1.5
                    pinturametalica=3.36
                    lijaparametalesn80=1.24
                    lijaparametalesn180=1.5
                    discocorteabl=1.5
                    trapometalesparapulir=0.41
                    petroleo=2.11
                    tiner=0.54
                    sacosparaproductosfinales=1.6
                    madera=1.4
                    pernoscobre=2.8
                    rafia=1.41
                    discocorteacl=0.1
                    jebesabl=4.2
                    jebesacl=2
                    tornillosaluminio=1.7
                    remachesaluminio=3
                    brocasparaaluminio=2.3
                    lijaparametalesn120=4
                    fajasmetalicas=1
                    pastaparametalesroja=1.75
                    lijaparametales60=1.2
                    acerosmicroaleados=1
                    acerosrefosforados=4.5
                    maderasintetica=1.25
                    pernosallenconcabezacilindrica=0.67
                    pernoprisionero=1
                    pernoenaceroinoxidable=2
                    acerosfasedoble=0.5
                    pernocabezaredonda=1
                    pernocabezahexagonalsaegrado5=0.8

                elif producto == 'Remolques':
                    aluminio=1
                    pernosaluminio=3.18
                    combustible=3.19
                    pastaparametalesdura=2.75
                    pastaparametalessuave=3.49
                    pinturametalica=5.62
                    lijaparametalesn80=6
                    lijaparametalesn180=2.9
                    discocorteabl=2.01
                    trapometalesparapulir=0.89
                    petroleo=2.11
                    tiner=0.5
                    sacosparaproductosfinales=5.07
                    madera=0.31
                    pernoscobre=3.9
                    rafia=5.18
                    discocorteacl=0.97
                    jebesabl=2
                    jebesacl=2
                    tornillosaluminio=4.5
                    remachesaluminio=2
                    brocasparaaluminio=0.5
                    lijaparametalesn120=1.64
                    fajasmetalicas=4.3
                    pastaparametalesroja=2.25
                    lijaparametales60=4.1
                    acerosmicroaleados=0.5
                    acerosrefosforados=5.5
                    maderasintetica=0.89
                    pernosallenconcabezacilindrica=1.78
                    pernoprisionero=2.06
                    pernoenaceroinoxidable=1
                    acerosfasedoble=1.5
                    pernocabezaredonda=1.21
                    pernocabezahexagonalsaegrado5=2.4

                elif producto == 'Cisternas de lacteos':
                    aluminio=1
                    pernosaluminio=0.9
                    combustible=1
                    pastaparametalesdura=2.8
                    pastaparametalessuave=1.99
                    pinturametalica=2.78
                    lijaparametalesn80=1.3
                    lijaparametalesn180=1.5
                    discocorteabl=1.35
                    trapometalesparapulir=0.6
                    petroleo=2.11
                    tiner=0.6
                    sacosparaproductosfinales=3.7
                    madera=0.2
                    pernoscobre=3
                    rafia=1.5
                    discocorteacl=3.35
                    jebesabl=2
                    jebesacl=3.5
                    tornillosaluminio=2.01
                    remachesaluminio=1
                    brocasparaaluminio=0.6
                    lijaparametalesn120=2
                    fajasmetalicas=2.2
                    pastaparametalesroja=0.75
                    lijaparametales60=2
                    acerosmicroaleados=0.5
                    acerosrefosforados=2.5
                    maderasintetica=1.05
                    pernosallenconcabezacilindrica=1.4
                    pernoprisionero=1.07
                    pernoenaceroinoxidable=1
                    acerosfasedoble=0.5
                    pernocabezaredonda=1
                    pernocabezahexagonalsaegrado5=1

                elif producto == 'Cisternas de Ácidos':
                    aluminio=1.5
                    pernosaluminio=3
                    combustible=1.5
                    pastaparametalesdura=2.47
                    pastaparametalessuave=3.05
                    pinturametalica=0.46
                    lijaparametalesn80=3.2
                    lijaparametalesn180=5.5
                    discocorteabl=2.31
                    trapometalesparapulir=0.6
                    petroleo=2.11
                    tiner=0.12
                    sacosparaproductosfinales=2.4
                    madera=1.7
                    pernoscobre=3.5
                    rafia=3
                    discocorteacl=3.35
                    jebesabl=3.2
                    jebesacl=3.24
                    tornillosaluminio=2.34
                    remachesaluminio=5
                    brocasparaaluminio=3.2
                    lijaparametalesn120=3.25
                    fajasmetalicas=1.8
                    pastaparametalesroja=3.5
                    lijaparametales60=2.1
                    acerosmicroaleados=2.5
                    acerosrefosforados=7.5
                    maderasintetica=1.35
                    pernosallenconcabezacilindrica=1.14
                    pernoprisionero=1.02
                    pernoenaceroinoxidable=1
                    acerosfasedoble=1.23
                    pernocabezaredonda=1.5
                    pernocabezahexagonalsaegrado5=1.2

                elif producto == 'Cisternas de GLP':
                    aluminio=1
                    pernosaluminio=1.81
                    combustible=4
                    pastaparametalesdura=2.29
                    pastaparametalessuave=1
                    pinturametalica=2.15
                    lijaparametalesn80=2.1
                    lijaparametalesn180=0.7
                    discocorteabl=2.45
                    trapometalesparapulir=0.62
                    petroleo=2.11
                    tiner=0.57
                    sacosparaproductosfinales=3.7
                    madera=0.13
                    pernoscobre=1.49
                    rafia=2.89
                    discocorteacl=3.35
                    jebesabl=2
                    jebesacl=4
                    tornillosaluminio=2.5
                    remachesaluminio=2
                    brocasparaaluminio=1.1
                    lijaparametalesn120=2
                    fajasmetalicas=1.54
                    pastaparametalesroja=1.5
                    lijaparametales60=1.2
                    acerosmicroaleados=0.5
                    acerosrefosforados=2.5
                    maderasintetica=1.26
                    pernosallenconcabezacilindrica=1.454
                    pernoprisionero=0.89
                    pernoenaceroinoxidable=0.5
                    acerosfasedoble=0.5
                    pernocabezaredonda=0.7
                    pernocabezahexagonalsaegrado5=1.1

                elif producto == 'Baranda de madera':
                    aluminio=0
                    pernosaluminio=0
                    combustible=2
                    pastaparametalesdura=0
                    pastaparametalessuave=0
                    pinturametalica=2.99
                    lijaparametalesn80=0
                    lijaparametalesn180=0
                    discocorteabl=1
                    trapometalesparapulir=0
                    petroleo=2.11
                    tiner=19.12
                    sacosparaproductosfinales=2.12
                    madera=45
                    pernoscobre=0.7
                    rafia=2.5
                    discocorteacl=0.46
                    jebesabl=0
                    jebesacl=0
                    tornillosaluminio=2.01
                    remachesaluminio=0.5
                    brocasparaaluminio=0
                    lijaparametalesn120=0
                    fajasmetalicas=0
                    pastaparametalesroja=0
                    lijaparametales60=0
                    acerosmicroaleados=0
                    acerosrefosforados=0
                    maderasintetica=1.1
                    pernosallenconcabezacilindrica=0
                    pernoprisionero=0
                    pernoenaceroinoxidable=0.5
                    acerosfasedoble=0
                    pernocabezaredonda=0.3
                    pernocabezahexagonalsaegrado5=0
                #----------------------------------------------------------------------
                q_aluminio = round( aluminio * prediccion_ventas)
                q_pernos_de_aluminio = round(pernosaluminio * prediccion_ventas)
                q_combustible = round(combustible * prediccion_ventas)
                q_pasta_para_metales_dura = round(pastaparametalesdura * prediccion_ventas)
                q_pasta_para_metales_suave = round(pastaparametalessuave * prediccion_ventas)
                q_pintura_metalica = round(pinturametalica * prediccion_ventas)
                q_lija_para_metales_n80 = round(lijaparametalesn80 * prediccion_ventas)
                q_lija_para_metales_n180 = round(lijaparametalesn180 * prediccion_ventas)
                q_disco_de_corte_abl = round(discocorteabl * prediccion_ventas)
                q_trapo_de_metales_para_pulir = round(trapometalesparapulir * prediccion_ventas)
                q_petroleo = round(petroleo * prediccion_ventas)
                q_tiner = round(tiner * prediccion_ventas)
                q_sacos_para_productos_finales = round(sacosparaproductosfinales * prediccion_ventas)
                q_madera = round(madera * prediccion_ventas)
                q_pernos_de_cobre = round(pernoscobre * prediccion_ventas)
                q_rafia = round(rafia * prediccion_ventas)
                q_disco_de_corte_acl = round(discocorteacl * prediccion_ventas)
                q_jebes_abl = round(jebesabl * prediccion_ventas)
                q_jebes_acl = round(jebesacl * prediccion_ventas)
                q_tornillos_de_aluminio = round(tornillosaluminio * prediccion_ventas)
                q_remaches_de_aluminio = round(remachesaluminio * prediccion_ventas)
                q_brocas_para_aluminio = round(brocasparaaluminio * prediccion_ventas)
                q_lija_para_metales_n120 = round(lijaparametalesn120 * prediccion_ventas)
                q_fajas_metalicas = round(fajasmetalicas * prediccion_ventas)
                q_pasta_para_metales_roja = round(pastaparametalesroja * prediccion_ventas)
                q_lija_para_metales_60 = round(lijaparametales60 * prediccion_ventas)
                q_aceros_microaleados = round(acerosmicroaleados * prediccion_ventas)##
                q_aceros_refosforados = round(acerosrefosforados * prediccion_ventas)
                q_madera_sintetica = round(maderasintetica * prediccion_ventas)
                q_pernos_allen_con_cabeza_cilindrica = round(pernosallenconcabezacilindrica * prediccion_ventas)
                q_perno_prisionero = round(pernoprisionero * prediccion_ventas)
                q_perno_en_acero_inoxidable = round(pernoenaceroinoxidable * prediccion_ventas)
                q_aceros_de_fase_doble = round(acerosfasedoble * prediccion_ventas)
                q_perno_cabeza_redonda = round(pernocabezaredonda * prediccion_ventas)
                q_perno_cabeza_hexagonal_sae_grado_5 = round(pernocabezahexagonalsaegrado5 * prediccion_ventas)

                # q_aluminio = round( 1 * prediccion_ventas)
                # q_pernos_de_aluminio = round(2.71 * prediccion_ventas)
                # q_combustible = round(1.91 * prediccion_ventas)
                # q_pasta_para_metales_dura = round(2.31 * prediccion_ventas)
                # q_pasta_para_metales_suave = round(2.46 * prediccion_ventas)
                # q_pintura_metalica = round(2.11 * prediccion_ventas)
                # q_lija_para_metales_n80 = round(1.6 * prediccion_ventas)
                # q_lija_para_metales_n180 = round(2.76 * prediccion_ventas)
                # q_disco_de_corte_abl = round(2.16 * prediccion_ventas)
                # q_trapo_de_metales_para_pulir = round(0.71 * prediccion_ventas)
                # q_petroleo = round(2.11 * prediccion_ventas)
                # q_tiner = round(2.56 * prediccion_ventas)
                # q_sacos_para_productos_finales = round(2.71 * prediccion_ventas)
                # q_madera = round(5.66 * prediccion_ventas)
                # q_pernos_de_cobre = round(2.61 * prediccion_ventas)
                # q_rafia = round(2.71 * prediccion_ventas)
                # q_disco_de_corte_acl = round(1.91 * prediccion_ventas)
                # q_jebes_abl = round(2.06 * prediccion_ventas)
                # q_jebes_acl = round(2.36 * prediccion_ventas)
                # q_tornillos_de_aluminio = round(2.21 * prediccion_ventas)
                # q_remaches_de_aluminio = round(2.46 * prediccion_ventas)
                # q_brocas_para_aluminio = round(1.41 * prediccion_ventas)
                # q_lija_para_metales_n120 = round(2.41 * prediccion_ventas)
                # q_fajas_metalicas = round(2.06 * prediccion_ventas)
                # q_pasta_para_metales_roja = round(2.11 * prediccion_ventas)
                # q_lija_para_metales_60 = round(1.96 * prediccion_ventas)
                # q_aceros_microaleados = round(1 * prediccion_ventas)##
                # q_aceros_refosforados = round(5 * prediccion_ventas)
                # q_madera_sintetica = round(1.11 * prediccion_ventas)
                # q_pernos_allen_con_cabeza_cilindrica = round(0.994 * prediccion_ventas)
                # q_perno_prisionero = round(1.01 * prediccion_ventas)
                # q_perno_en_acero_inoxidable = round(1.05 * prediccion_ventas)
                # q_aceros_de_fase_doble = round(0.84 * prediccion_ventas)
                # q_perno_cabeza_redonda = round(1.19 * prediccion_ventas)
                # q_perno_cabeza_hexagonal_sae_grado_5 = round(1.1 * prediccion_ventas)
                

                #PDF
                ruta_template = 'D:/Ricardo/Documents/predictive_software/template.html'
                info = {"mes":self.fecha.currentText, "producto": producto, "prediccion_ventas": math.floor(prediccion_ventas) , "q_aluminio": q_aluminio, "q_pernos_aluminio": q_pernos_de_aluminio, "q_combustible": q_combustible, 
                        "q_pasta_para_metales_dura": q_pasta_para_metales_dura, "q_pasta_para_metales_suave": q_pasta_para_metales_suave, "q_pintura_metalica": q_pintura_metalica, "q_lija_para_metales_n80": q_lija_para_metales_n80, 
                        "q_lija_para_metales_n180": q_lija_para_metales_n180, "q_disco_corte_abl": q_disco_de_corte_abl, "q_trapo_metales_para_pulir": q_trapo_de_metales_para_pulir, "q_petroleo": q_petroleo, 
                        "q_tiner": q_tiner, "q_sacos_para_productos_finales": q_sacos_para_productos_finales, "q_madera": q_madera, "q_pernos_cobre": q_pernos_de_cobre, "q_rafia": q_rafia, 
                        "q_disco_corte_acl": q_disco_de_corte_acl, "q_jebes_abl": q_jebes_abl, "q_jebes_acl": q_jebes_acl, "q_tornillos_aluminio": q_tornillos_de_aluminio, "q_remaches_aluminio": q_remaches_de_aluminio, 
                        "q_brocas_para_aluminio": q_brocas_para_aluminio, "q_lija_para_metales_n120": q_lija_para_metales_n120, "q_fajas_metalicas": q_fajas_metalicas, "q_pasta_para_metales_roja": q_pasta_para_metales_roja, 
                        "q_lija_para_metales_60": q_lija_para_metales_60, "q_aceros_microaleados": q_aceros_microaleados, "q_aceros_refosforados": q_aceros_refosforados, "q_madera_sintetica": q_madera_sintetica, 
                        "q_pernos_allen_con_cabeza_cilindrica": q_pernos_allen_con_cabeza_cilindrica, "q_perno_prisionero": q_perno_prisionero, "q_perno_en_acero_inoxidable": q_perno_en_acero_inoxidable,
                        "q_aceros_de_fase_doble": q_aceros_de_fase_doble, "q_perno_cabeza_redonda": q_perno_cabeza_redonda, "q_perno_cabeza_hexagonal_sae_grado_5": q_perno_cabeza_hexagonal_sae_grado_5}
                nombre_template = ruta_template.split('/')[-1]
                ruta_template = ruta_template.replace(nombre_template,'')
                
                env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
                template=env.get_template(nombre_template)
                html = template.render(info)
                
                options = { 'page-size': 'Letter', 'margin-top': '0.05in', 'margin-right': '0.05in', 'margin-bottom': '0.05in', 'margin-left': '0.05in', 'encoding':'UTF-8'}
                config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
                ruta_salida = f'predictive_software_{producto}_{self.fecha.currentText}-{anio}.pdf'
                pdfkit.from_string(html, ruta_salida, options=options, configuration=config)

                QMessageBox.information(self, "Predicción...", f"La predición de ventas para el mes {self.fecha.currentText} para {producto} es {prediccion_ventas}. Se exportó un pdf a {ruta_salida}.")
        else:
            print("No ha seleccionado ningún mes o producto para predecir.")
            QMessageBox.warning(self, "Predicción", "No ha seleccionado ningún mes o producto para predecir.")