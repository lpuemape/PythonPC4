def suma_numeros(numero):
  suma = 0
  for i in range(1, numero + 1):
    suma += i
  return suma

def main():
  """
  Esta función solicita al usuario un número y luego calcula la suma de todos los números desde 1 hasta el número ingresado.
  """
  while True:
    try:
      numero = int(input("Ingrese un número entero (o 0 para salir): "))
      if numero == 0:
        break
      else:
        suma = suma_numeros(numero)
        print(f"La suma de todos los números desde 1 hasta {numero} es {suma}.")
    except ValueError:
      print("Error: Ingrese un número válido.")

if __name__ == "__main__":
  main()
