pais = input("Ingrese el nombre del país en ingles: ").strip()
contador = 0

with open("files/SalesJan2009.csv", "r", encoding="utf-8") as f:

  for linea in f:
      datos = linea.strip().split(",") 
      if len(datos) > 7 and datos[7].strip() == pais:
          contador += 1

print(f"{pais}: {contador}")