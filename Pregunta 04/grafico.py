import datetime
import matplotlib.pyplot as plt

def generar_grafico(nombre_archivo):
    # Leer los datos del archivo
    with open(nombre_archivo, "r") as archivo:
        datos = archivo.readlines()

    # Obtener las fechas y los precios
    fechas = [linea.split(",")[0] for linea in datos]
    precios = [linea.split(",")[1] for linea in datos]

    # Convertir las fechas a formato de fecha
    fechas = [datetime.strptime(fecha, "%Y-%m-%d") for fecha in fechas]

    # Generar el gráfico
    plt.plot(fechas, precios)
    plt.xlabel("Fecha")
    plt.ylabel("Precio (USD)")
    plt.show()

generar_grafico("precios_bitcoin_2024-04-08-16-25-00.txt")
