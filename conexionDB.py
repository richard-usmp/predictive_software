import pyodbc
import pandas as pd
server = 'predictive-app.database.windows.net'
database = 'predictiveapp'
username = 'administrador'
password = '{sql_proyecto2}'   
driver= '{ODBC Driver 17 for SQL Server}'

class Registro_datos():
    def __init__(self):
        self.conexion = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

    #material
    def buscar_material(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM dbo.Material" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def buscar_material_cmb(self):
        cursor = self.conexion.cursor()
        sql = "SELECT Descripcion FROM dbo.Material" 
        cursor.execute(sql)
        row = [item[0] for item in cursor.fetchall()]
        return row

    def inserta_material(self, Descripcion, Unid_medida,Precio_compra_unit, Stock, Mes, Anio):
        cur = self.conexion.cursor()
        sql='''INSERT INTO dbo.Material 
        VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(Descripcion, Unid_medida, Stock, Precio_compra_unit,  Mes, Anio)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def insertar_log_material(self, ID_material, Descripcion, Stock, Precio_compra_unit, Dia, Mes, Anio, Estado):
        cur = self.conexion.cursor()
        sql='''INSERT INTO dbo.Material_log
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(ID_material, Descripcion, Stock, Precio_compra_unit, Dia, Mes, Anio, Estado)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def getMaterial(self, descripcion):
        descripcion_=""
        cursor = self.conexion.cursor()
        sql = "SELECT Descripcion FROM dbo.Material where Descripcion = {}".format(descripcion) 
        cursor.execute(sql)
        descripcion_fetch = cursor.fetchall()
        for row in descripcion_fetch:
            descripcion_ = row[0]
        return descripcion_

    def getID_Material(self, descripcion):
        id_=""
        cursor = self.conexion.cursor()
        sql = "SELECT ID_material FROM dbo.Material where Descripcion = {}".format(descripcion) 
        cursor.execute(sql)
        id_fetch = cursor.fetchall()
        for row in id_fetch:
            id_ = row[0]
        return id_
    
    def actualizar_stock_material(self, stock, desc):
        cur = self.conexion.cursor()
        sql ='''UPDATE dbo.Material SET Stock ='{}'
        WHERE Descripcion = '{}' '''.format(stock, desc)
        cur.execute(sql)
        act = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return act  

    def actualizar_precio_material(self, desc, precio):
        cur = self.conexion.cursor()
        sql ='''UPDATE dbo.Material SET Precio_compra_unit = '{}'
        WHERE Descripcion = '{}' '''.format(precio, desc)
        cur.execute(sql)
        act = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return act 

    def getStock(self, descripcion):
        stock_=""
        cursor = self.conexion.cursor()
        sql = "SELECT Stock FROM dbo.Material where Descripcion = {}".format(descripcion) 
        cursor.execute(sql)
        stock_fetch = cursor.fetchall()
        for row in stock_fetch:
            stock_ = row[0]
        return stock_

    def buscar_Material_log(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM dbo.Material_log" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro  
    

    #proveedores
    def buscar_proveedores(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM dbo.Proveedor" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def inserta_proveedor(self, empresa, representante, ruc, celular, email, tipo):
        cur = self.conexion.cursor()
        sql='''INSERT INTO dbo.Proveedor (Nombre_empresa, Representante, RUC, Celular, Email, Tipo) 
        VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(empresa, representante, ruc, celular, email, tipo)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def buscar_proveedor_cmb(self):
        cursor = self.conexion.cursor()
        sql = "SELECT Nombre_empresa FROM dbo.Proveedor"
        cursor.execute(sql)
        row = [item[0] for item in cursor.fetchall()]
        return row
    
    
    def elimina_proveedor(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM dbo.Proveedor WHERE Nombre_empresa = {} '''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close() 

    #ventas
    def buscar_ventas(self):
        cursor = self.conexion.cursor()
        sql = "SELECT ID_Venta,DNI_cliente,Cant_Total_Productos_Vendidos,Dia,Mes,Anio FROM dbo.Ventas" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def inserta_ventas(self, dni, cantidad, Dia, Mes, Anio, total_prod_vendidos, fecha):
        cur = self.conexion.cursor()
        sql='''INSERT INTO dbo.Ventas
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(dni, cantidad, Dia, Mes, Anio, total_prod_vendidos, fecha)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def get_total_productos_vendidos(self, Año_y_mes):
        total_productos_vendidos=""
        cursor = self.conexion.cursor()
        sql = "SELECT top 1 (Total_Prod_Vendidos) FROM dbo.Ventas WHERE Fecha='{}' ORDER BY Total_Prod_Vendidos DESC".format(Año_y_mes) 
        cursor.execute(sql)
        total_productos_vendidos_fetch = cursor.fetchall()
        for row in total_productos_vendidos_fetch:
            total_productos_vendidos = row[0]
        return total_productos_vendidos


    def getUser(self, user):
        usuario=""
        cursor = self.conexion.cursor()
        sql = "SELECT usuario FROM dbo.login where usuario= {}".format(user) 
        cursor.execute(sql)
        usuario_fetch = cursor.fetchall()
        for row in usuario_fetch:
            usuario = row[0]
        return usuario

    def getPass(self, passw):
        contra=""
        cursor = self.conexion.cursor()
        sql = "SELECT Password FROM dbo.login where Password= {}".format(passw)
        cursor.execute(sql)
        contra_fetch = cursor.fetchall()
        for row in contra_fetch:
            contra = row[0]
        return contra
    
    def importCSV(self, ruta_de_csv):
        data = pd.read_csv(f"{ruta_de_csv}")   
        df = pd.DataFrame(data)
        
        cursor = self.conexion.cursor()
        #format(dni, cantidad, Dia, Mes, Anio, total_prod_vendidos, fecha)

        for row in df.itertuples():
            cursor.execute('''
                INSERT INTO dbo.Ventas
                VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')''',
                row.DNI_cliente, 
                row.CANT_TOTAL_PRODUCTOS_VENDIDOS, 
                row.Dia, 
                row.Mes, 
                row.Anio, 
                row.total_prod_vendidos, 
                row.fecha
            )
        self.conexion.commit() 


