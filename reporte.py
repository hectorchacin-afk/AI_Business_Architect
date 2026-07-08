import csv

datos_taller = [
    ["Producto", "Cantidad", "Precio_USD"],
    ["Bujia Champion", "150", "30"],
    ["Pastilla Freno", "20", "45"],
    ["Filtro Aceite", "85", "12"]
]

with open("inventario.csv", "w", newline="") as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerows(datos_taller)

print("📊 ¡ÉXITO DE ARQUITECTURA! El archivo plano 'inventario.csv' ha sido grabado físicamente.")