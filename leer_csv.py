import csv

nombre_archivo = "Carga_Masiva_Salesforce.csv"

try:
    print(f"📖 1. Abriendo la base de datos de texto plano '{nombre_archivo}'...")
    
    with open(nombre_archivo, mode="r", encoding="utf-8") as archivo_csv:
        lector_inteligente = csv.DictReader(archivo_csv)
        
        print("⚡ 2. Absorbiendo y procesando filas en la memoria RAM...")
        print("-" * 50)
        
        for fila in lector_inteligente:
            cliente = fila.get("nombre")
            compania = fila.get("empresa")
            nivel_plan = fila.get("plan")
            
            print(f"👤 Cliente: {cliente} | 🏢 Empresa: {compania} | 💎 Plan: {nivel_plan}")
            
        print("-" * 50)
    print("✅ 3. ¡HITO CONQUISTADO! Todo el reporte CSV de Salesforce fue leído con éxito.")

except FileNotFoundError:
    print(f"🚨 ERROR: El archivo '{nombre_archivo}' no existe en este directorio.")