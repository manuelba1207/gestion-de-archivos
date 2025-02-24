metodo = input("Ingrese el metodo de pago: ").strip()
contador = 0

with open("files/SalesJan2009.csv", "r", encoding="utf-8") as f:

  for linea in f:
      datos = linea.strip().split(",") 
      if len(datos) > 3 and datos[3].strip() == metodo:
          contador += 1

print(f"{metodo}: {contador}")