import requests

def descargar_imagen(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        with open("imagen.jpg", "wb") as archivo:
            archivo.write(respuesta.content)
    else:
        print(f"Error al descargar la imagen: {respuesta.status_code}")

url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

descargar_imagen(url)
