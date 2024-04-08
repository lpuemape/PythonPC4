import pyfiglet # type: ignore
import random

# Lista de fuentes
fuentes = pyfiglet.getFonts()

def mostrar_menu():
    print("**Opciones:**")
    print("1. Elegir una fuente")
    print("2. Ver la lista de fuentes")
    print("3. Salir del programa")

def elegir_fuente():
    while True:
        opcion = input("Seleccione una opción: ")
        if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            print("Error: La opción debe ser un número entre 1 y 3.")
            continue
        return int(opcion)

def mostrar_fuentes():
    print("**Lista de fuentes:**")
    for fuente in fuentes:
        print(f"- {fuente}")

def previsualizar_texto(texto, fuente):
    figlet = pyfiglet.Figlet(font=fuente)
    print(figlet.renderText(texto))

def guardar_resultado(texto, fuente, formato):
    if formato == "txt":
        with open("resultado.txt", "w") as archivo:
            archivo.write(texto)
    elif formato == "png":
        figlet = pyfiglet.Figlet(font=fuente)
        figlet.writeText(texto, "resultado.png")
    else:
        print(f"Error: Formato no válido: '{formato}'.")

# Bucle principal
while True:
    mostrar_menu()
    opcion = elegir_fuente()

    if opcion == 1:
        nombre_fuente = input("Ingrese el nombre de la fuente (o presione Enter para aleatoria): ")
        if not nombre_fuente:
            nombre_fuente = random.choice(fuentes)
        if nombre_fuente not in fuentes:
            print(f"Error: La fuente '{nombre_fuente}' no existe.")
            continue
    elif opcion == 2:
        mostrar_fuentes()
        continue
    elif opcion == 3:
        break

    texto = input("Ingrese el texto a imprimir: ")
    previsualizar_texto(texto, nombre_fuente)

    respuesta = input("¿Desea imprimir el texto? (s/n): ")
    if respuesta.lower() == "s":
        print(texto)

    respuesta = input("¿Desea guardar el resultado? (txt/png/n): ")
    if respuesta.lower() in ("txt", "png"):
        guardar_resultado(texto, nombre_fuente, respuesta.lower())

print("**Gracias por usar este programa**")

