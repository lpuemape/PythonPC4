import zipfile


def descomprimir_imagen(nombre_archivo_zip):
    with zipfile.ZipFile(nombre_archivo_zip, "r") as archivo_zip:
        archivo_zip.extractall()

descomprimir_imagen("imagen.zip")
