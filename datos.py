import json

try:
    with open("inventario.json", "r") as archivo:
        datos_cargados = json.load(archivo)
    
    print("📖 ¡CONEXIÓN EXITOSA! Datos extraídos del disco duro correctamente.\n")
    
    print(f"Stock actual de Bujías: {datos_cargados['bujia']} unidades.")
    print(f"Stock actual de Pastillas: {datos_cargados['pastilla']} unidades.")

except FileNotFoundError:
    print("🚨 ALERTA PERIMETRAL: El archivo 'inventario.json' no existe en el servidor.")