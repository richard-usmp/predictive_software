import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_squared_error
import pickle

data = pd.read_csv('D:\Ricardo\Documents\predictive_software\Dataset\dataset.csv', sep=';')
data['Fechaa'] = pd.to_datetime(data['Fechaa'], dayfirst=True)
data = data[['Fechaa', 'Cant_Total_Productos_Vendidos', 'Producto']]
data.rename(columns={'Fechaa': 'ds', 'Cant_Total_Productos_Vendidos': 'y'}, inplace=True)
data['Mes_Anio_Producto'] = data['ds'].dt.strftime('%m%Y') + data['Producto']
predictions = []
validations = {
    'Producto': [],
    'Media': [],
    'MSE': [],
    'RMSE': []
}

for producto in data['Producto'].unique():
    # Filtrar los datos por producto
    product_data = data[data['Producto'] == producto]

    # Agrupar los datos por mes y calcular la suma de las ventas diarias para cada mes
    monthly_data = product_data.groupby(pd.Grouper(key='ds', freq='M')).sum().reset_index()

    # Verificar filas no nulas
    if not monthly_data.empty:
        # Renombrar las columnas a "ds" y "y"
        #monthly_data.rename(columns={'Fechaa': 'ds', 'Cant_Total_Productos_Vendidos': 'y'}, inplace=True)

        # Inicializar y ajustar el modelo Prophet con ajustes específicos
        model = Prophet(
            seasonality_mode='multiplicative',  # Multiplicativo para capturar mejor las estacionalidades
            weekly_seasonality=True,
            yearly_seasonality=True,
            seasonality_prior_scale=10.0,       # Ajustar el prior_scale para las estacionalidades
            holidays_prior_scale=20.0           # Ajustar el prior_scale para las vacaciones
        )
        model.fit(monthly_data)
        
        with open('Prophet_{}.pckl'.format(producto), 'wb') as f:
            pickle.dump(model, f)

        # Generar fechas futuras para predicción (12 meses a partir del último mes en los datos)
        future_dates = model.make_future_dataframe(periods=12, freq='M')
        
        # Generar predicciones mensuales forecast
        forecast = model.predict(future_dates)
        print("forecast")
        print(forecast)

        # Agregar la columna "producto" a la predicción
        forecast['Producto'] = producto

        # Agregar los pronósticos a la lista de predicción
        predictions.append(forecast[['Producto', 'ds', 'yhat', 'yhat_lower', 'yhat_upper']])

        # Validación con ventas reales y predichas
        merged_data = pd.merge(monthly_data, forecast[['ds', 'yhat']], on='ds', how='outer').dropna()
        real_data = merged_data['y']
        predicted_data = merged_data['yhat']

        # Calcular indicadores de desempeño
        mean_error = np.mean(real_data)
        mse = mean_squared_error(real_data, predicted_data)
        rmse = np.sqrt(mse)

        # Guardar resultados de validación en el diccionario
        validations['Producto'].append(producto)
        validations['Media'].append(mean_error)
        validations['MSE'].append(mse)
        validations['RMSE'].append(rmse)

print("predictions")
print(predictions)
result = pd.concat(predictions)