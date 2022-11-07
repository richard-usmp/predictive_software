from re import template
from tkinter.ttk import Separator
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
        self.tabla.columnCount= 3
        self.tabla.rowCount = 0
        nombreColumnas = ("Id_venta", "Fecha", "Sumatoria de cantidad total de Productos Vendidos")
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

        self.cant_venta_mes_pasado = QLineEdit(self.fr_contenedor_arriba)
        self.cant_venta_mes_pasado.placeholderText= "Ingrese cantidad de venta del mes seleccionado..."
        self.cant_venta_mes_pasado.geometry = QRect(10,450, 395,20)
        self.cant_venta_mes_pasado.alignment = Qt.AlignCenter
        self.cant_venta_mes_pasado.styleSheet = "color: gray; font-size: 15px;"

        self.boton_analisis_predictivos = QPushButton(self.fr_contenedor_arriba)
        self.boton_analisis_predictivos.text = "Análisis predictivo"
        self.boton_analisis_predictivos.clicked.connect(self.rest_api)
        self.boton_analisis_predictivos.geometry = QRect(10, 490, 200,45)
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

            row += 1

    def setup_name_user(self, username):
        self.titulo = QLabel(f"Bienvenido {username}", alignment = Qt.AlignCenter)
        self.titulo.styleSheet = "color: gray; font-size: 21px; font-weight: bold;"

        self.titulo_layout = QVBoxLayout()
        self.titulo_layout.addWidget(self.titulo)

        self.fr_bienvenida.setLayout(self.titulo_layout)

    def rest_api(self):
        anio = today.strftime("%Y")
        mes_ = self.fecha.currentIndex + 1
        cantidad_ventas_mes = self.cant_venta_mes_pasado.text
        QMessageBox.information(self, "Predicción...", f"La predicción se realizará para el mes de {self.fecha.currentText}.")
        r = requests.post('https://api-tesis-usmp.herokuapp.com/prophetv3', json={'mes':mes_})
        json_texto = r.text
        jsondecoded = json.loads(json_texto[1:len(json_texto)-2])#quitar corchetes inicio y final
        prediccion_ventas = jsondecoded["yhat_upper"]
        print(prediccion_ventas)
        q_aluminio = round(5 * prediccion_ventas)
        q_pernos_aluminio = round(2.71 * prediccion_ventas)
        q_combustible = round(1.91 * prediccion_ventas)
        q_pasta_para_metales_dura = round(2.31 * prediccion_ventas)
        q_pasta_para_metales_suave = round(2.46 * prediccion_ventas)
        q_pintura_metalica = round(2.11 * prediccion_ventas)
        q_lija_para_metales_n80 = round(2.46 * prediccion_ventas)
        q_lija_para_metales_n180 = round(2.76 * prediccion_ventas)
        q_disco_corte_abl = round(2.16 * prediccion_ventas)
        q_trapo_metales_para_pulir = round(0.71 * prediccion_ventas)
        q_petroleo = round(2.11 * prediccion_ventas)
        q_tiner = round(2.56 * prediccion_ventas)
        q_sacos_para_productos_finales = round(2.71 * prediccion_ventas)
        q_madera = round(5.66 * prediccion_ventas)
        q_pernos_cobre = round(2.61 * prediccion_ventas)
        q_rafia = round(2.71 * prediccion_ventas)
        q_disco_corte_acl = round(1.91 * prediccion_ventas)
        q_jebes_abl = round(2.06 * prediccion_ventas)
        q_jebes_acl = round(2.36 * prediccion_ventas)
        q_tornillos_aluminio = round(2.21 * prediccion_ventas)
        q_remaches_aluminio = round(2.46 * prediccion_ventas)
        q_brocas_para_aluminio = round(1.41 * prediccion_ventas)
        q_lija_para_metales_n120 = round(2.41 * prediccion_ventas)
        q_fajas_metalicas = round(2.06 * prediccion_ventas)
        q_pasta_para_metales_roja = round(2.11 * prediccion_ventas)
        q_lija_para_metales_60 = round(1.96 * prediccion_ventas)

        #PDF
        
        ruta_template = 'D:/QtDesigner/predictive_software/template.html'
        info = {"mes":self.fecha.currentText, "prediccion_ventas": math.floor(prediccion_ventas) , "q_aluminio": q_aluminio, "q_pernos_aluminio": q_pernos_aluminio, "q_combustible": q_combustible, "q_pasta_para_metales_dura": q_pasta_para_metales_dura, "q_pasta_para_metales_suave": q_pasta_para_metales_suave, "q_pintura_metalica": q_pintura_metalica, "q_lija_para_metales_n80": q_lija_para_metales_n80, "q_lija_para_metales_n180": q_lija_para_metales_n180, "q_disco_corte_abl": q_disco_corte_abl, "q_trapo_metales_para_pulir": q_trapo_metales_para_pulir, "q_petroleo": q_petroleo, "q_tiner": q_tiner, "q_sacos_para_productos_finales": q_sacos_para_productos_finales, "q_madera": q_madera, "q_pernos_cobre": q_pernos_cobre, "q_rafia": q_rafia, "q_disco_corte_acl": q_disco_corte_acl, "q_jebes_abl": q_jebes_abl, "q_jebes_acl": q_jebes_acl, "q_tornillos_aluminio": q_tornillos_aluminio, "q_remaches_aluminio": q_remaches_aluminio, "q_brocas_para_aluminio": q_brocas_para_aluminio, "q_lija_para_metales_n120": q_lija_para_metales_n120, "q_fajas_metalicas": q_fajas_metalicas, "q_pasta_para_metales_roja": q_pasta_para_metales_roja, "q_lija_para_metales_60": q_lija_para_metales_60}
        nombre_template = ruta_template.split('/')[-1]
        ruta_template = ruta_template.replace(nombre_template,'')
        
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
        template=env.get_template(nombre_template)
        html = template.render(info)
        
        options = { 'page-size': 'Letter', 'margin-top': '0.05in', 'margin-right': '0.05in', 'margin-bottom': '0.05in', 'margin-left': '0.05in', 'encoding':'UTF-8'}
        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
        ruta_salida = f'D:/QtDesigner/predictive_software/predictive_software_{self.fecha.currentText}-{anio}.pdf'
        pdfkit.from_string(html, ruta_salida, options=options, configuration=config)

        QMessageBox.information(self, "Predicción...", f"La predición de ventas para el mes {self.fecha.currentText} es {prediccion_ventas}. Se exportó un pdf a {ruta_salida}.")