def es_primo(numero):
  """
  Esta función verifica si el número dado es primo.

  Parámetros:
    numero: El número a verificar.

  Devuelve:
    True si el número es primo, False si no lo es.
  """
  if numero <= 1:
    return False
  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      return False
  return True

def main():
  """
  Esta función solicita al usuario un número y luego verifica si es primo.
  """
  while True:
    try:
      numero = int(input("Ingrese un número entero positivo (o 0 para salir): "))
      if numero == 0:
        break
      elif numero < 0:
        print("Error: El número debe ser positivo.")
      else:
        if es_primo(numero):
          print(f"El número {numero} es primo.")
        else:
          print(f"El número {numero} no es primo.")
    except ValueError:
      print("Error: Ingrese un número válido.")

if __name__ == "__main__":
  main()
