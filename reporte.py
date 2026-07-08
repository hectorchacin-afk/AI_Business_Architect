import csv

try:
    with open("inventario.csv", "r", newline="") as archivo_csv:
        lector_datos = csv.reader(archivo_csv)
        
        print("📊 ¡CONEXIÓN TABULAR EXITOSA! Leyendo las filas del taller:\n")
        
        for fila in lector_datos:
            print(f"Producto: {fila[0]} | Stock: {fila[1]} | Precio: ${fila[2]} USD")

except FileNotFoundError:
    print("🚨 ALERTA DE SEGURIDAD: El archivo 'inventario.csv' no existe en el disco duro.")