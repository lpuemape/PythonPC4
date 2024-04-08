import zipfile

def comprimir_imagen(nombre_imagen):
    with zipfile.ZipFile("imagen.zip", "w") as archivo_zip:
        archivo_zip.write(nombre_imagen)

comprimir_imagen("imagen.jpg")
