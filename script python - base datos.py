import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from IPython.display import display
import sqlite3 as sq
print("Librerías cargadas con éxito.")

#Función para procesar los registros meteorológicos y contaminantes desde el año 2010
def procesar_datos_quito(ruta, columna_estacion, nuevo_nombre):
  # Cargamos saltando la fila 1 de encabezados de unidades
  df = pd.read_excel(ruta, skiprows=[1])

  # renombramos la primera columna a Fecha
  df.rename(columns={df.columns[0] : 'Fecha'}, inplace = True)

  #Convertimos al formato de fecha DateTime para hacer un filtrado por los años
  df['Fecha'] = pd.to_datetime(df['Fecha'])

  #Filtramos solo desde el 1 de enero de 2010
  df = df[df['Fecha'] >= '2010-01-01']

  # Seleccionamos solo la fecha y la estación (Belisario)
  df = df[['Fecha', columna_estacion]].copy()
  df.columns = ['Fecha', nuevo_nombre]

  return df


#=================PROCESAMIENTO DE ARCHIVOS HISTÓRICOS================================
try:
  df_pm25 = procesar_datos_quito('https://raw.github.com/LuisNepas/proyecto-aplicado-ciencia-datos-uide/main/data/PM2.5.xlsx', 'BELISARIO', 'PM25')
  df_lluvia = procesar_datos_quito('https://raw.github.com/LuisNepas/proyecto-aplicado-ciencia-datos-uide/main/data/LLU.xlsx', 'Belisario', 'Lluvia')
  df_viento = procesar_datos_quito('https://raw.github.com/LuisNepas/proyecto-aplicado-ciencia-datos-uide/main/data/VEL.xlsx', 'Belisario', 'Viento')
  df_hum = procesar_datos_quito('https://raw.github.com/LuisNepas/proyecto-aplicado-ciencia-datos-uide/main/data/HUM.xlsx', 'Belisario', 'Humedad')
  df_no2 = procesar_datos_quito('https://raw.github.com/LuisNepas/proyecto-aplicado-ciencia-datos-uide/main/data/NO2.xlsx', 'BELISARIO', 'NO2')
  df_tmp = procesar_datos_quito('https://raw.github.com/LuisNepas/proyecto-aplicado-ciencia-datos-uide/main/data/TMP.xlsx', 'Belisario', 'Temperatura')
  print("Datos procesados y filtrados desde el años 2010")

except Exception as e:
  print(f"Error al cargar archivos: {e}. Asegurarse de haber subido los archivos a la carpeta Colab")


#=================CREACIÓN DE TABLA MAESTRA================================
try:
  #unir en un df_maestro
  df_maestro = df_pm25.merge(df_lluvia, on='Fecha')\
                        .merge(df_viento, on='Fecha')\
                        .merge(df_hum, on='Fecha')\
                        .merge(df_no2, on='Fecha')\
                        .merge(df_tmp, on='Fecha')
  #crear variables de tiempo
  df_maestro['Hora'] = df_maestro['Fecha'].dt.hour
  df_maestro['Dia_Semana'] = df_maestro['Fecha'].dt.day_of_week

  #limpieza y conversoin
  columnas_finales = ['PM25', 'Lluvia', 'Viento', 'Humedad', 'NO2', 'Temperatura']
  for col in columnas_finales:
    df_maestro[col] = pd.to_numeric(df_maestro[col], errors = 'coerce')

  #limpieza de nulos
  df_maestro = df_maestro.dropna().reset_index(drop = True)

  #convertimos todo
  print("Tabla maestra creada con éxito")
  print(f"Registros totales: {len(df_maestro)}")
  display(df_maestro.head(10))
except Exception as e:
  print(f"Error al integrar: {e}")
  print("Revisa que los archivos .xlsx esten en la ruta")



#=================Almacenamiento en una base de datos SQlite================================
#agregamos un id
df_maestro.insert(0, 'id_medicion', range(1, 1+ len(df_maestro)))

#crear la conexion
try:
  conn = sq.connect('calidad_aire_quito.db')
  cursor = conn.cursor()
  print("Conexión a la base de datos establecida con éxito")
  #guardamos el dataframe maestro en una tabla llamada monitoreo_belisario
  df_maestro.to_sql('monitoreo_belisario', conn, if_exists='replace', index=False)
  print("Tabla monitoreo_belisario creada con éxito")

  #verificamos que los datos esten correctamente almacenados
  query = "SELECT * FROM monitoreo_belisario LIMIT 10"
  verificacion = pd.read_sql_query(query, conn)
  print("Verificación de los datos almacenados en la tabla monitoreo_belisario:")
  display(verificacion)
  conn.close()
except Exception as e:
  print(f"Error al crear la base de datos: {e}")
