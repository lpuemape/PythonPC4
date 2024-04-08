from multiprocessing import connection
import requests
import datetime

def obtener_tipo_cambio_pen():
  url = "https://api.sunat.gob.pe/v1/tipo-cambio/dia?fecha=2024-04-08"
  respuesta = requests.get(url)
  if respuesta.status_code == 200:
    datos = respuesta.json()
    return datos["venta"][0]["cambio"]
  else:
    print("Error al obtener el tipo de cambio.")
    return None

def insertar_datos(fecha, precio_usd):
  precio_gbp = precio_usd * 0.79
  precio_eur = precio_usd * 0.83
  precio_pen = precio_usd * obtener_tipo_cambio_pen()

  # Insertar datos en la tabla
  sql = "INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen) VALUES (?, ?, ?, ?, ?)"
  valores = (fecha, precio_usd, precio_gbp, precio_eur, precio_pen)
  cursor.execute(sql, valores)

fecha = datetime.date.today()
precio_usd = float(input("Ingrese el precio de Bitcoin en USD: "))

insertar_datos(fecha, precio_usd)

# Conexión a la base de datos
# ...

# Crear cursor
cursor = connection.cursor()
