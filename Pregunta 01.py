import requests
print("**Programa para calcular el costo de bitcoins**")

try:
    n = float(input("Digite la cantidad de bitcoins que posee: "))
    
    respuesta = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if respuesta.status_code == 200:
        datos = respuesta.json()
        precio_bitcoin = datos["bpi"]["USD"]["rate_float"]

        costo_total = n * precio_bitcoin

        print(f"\nEl costo actual de {n} bitcoins es: ${costo_total:,.4f}")
    else:
        print(f"\nError al consultar la API: {respuesta.status_code}")

except requests.RequestException as e:
    print(f"\nError al consultar la API: {e}")

except ValueError:
    print("\nError: La cantidad de bitcoins debe ser un numero.")
print("n\n**Gracias por usar este programa**")
