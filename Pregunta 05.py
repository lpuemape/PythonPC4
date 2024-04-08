def crear_tabla_multiplicacion(numero):
  """Crea la tabla de multiplicación del número dado y la guarda en un archivo."""
  tabla = ""
  for i in range(1, 11):
    tabla += f"{numero} x {i} = {numero * i}\n"
  with open(f"tabla-{numero}.txt", "w") as archivo:
    archivo.write(tabla)

def mostrar_tabla_multiplicacion(numero):
  """Lee la tabla de multiplicación del número dado desde un archivo y la muestra en pantalla."""
  try:
    with open(f"tabla-{numero}.txt", "r") as archivo:
      tabla = archivo.read()
      print(tabla)
  except FileNotFoundError:
    print(f"El archivo tabla-{numero}.txt no existe.")

def main():
  """Solicita el número al usuario y ejecuta las funciones correspondientes."""
  while True:
    try:
      numero = int(input("Ingrese un número entre 1 y 10 para crear su tabla de multiplicación (o 0 para salir): "))
      if numero == 0:
        break
      elif 1 <= numero <= 10:
        crear_tabla_multiplicacion(numero)
        print(f"La tabla del {numero} se ha creado en el archivo tabla-{numero}.txt")
      else:
        print("Error: El número debe estar entre 1 y 10.")
    except ValueError:
      print("Error: Ingrese un número válido.")

    while True:
      try:
        numero_a_mostrar = int(input("Ingrese un número entre 1 y 10 para mostrar su tabla de multiplicación (o 0 para salir): "))
        if numero_a_mostrar == 0:
          break
        elif 1 <= numero_a_mostrar <= 10:
          mostrar_tabla_multiplicacion(numero_a_mostrar)
        else:
          print("Error: El número debe estar entre 1 y 10.")
      except ValueError:
        print("Error: Ingrese un número válido.")

if __name__ == "__main__":
  main()
