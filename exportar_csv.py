import csv

nombre_archivo = "Carga_Masiva_Salesforce.csv"

lote_clientes = [
    {"nombre": "Alejandro Gomez", "empresa": "Taller Central", "plan": "Premium"},
    {"nombre": "Maria Rodriguez", "empresa": "Inversiones Merida", "plan": "Basico"},
    {"nombre": "Carlos Mendoza", "empresa": "Autopartes Global", "plan": "Premium"}
]

try:
    print("📝 1. Inicializando archivo de texto plano CSV...")
    
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo_csv:
        campos = ["nombre", "empresa", "plan"]
        
        escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
        
        escritor.writeheader()
        
        print("⚡ 2. Inyectando lote de diccionarios en caliente...")
        escritor.writerows(lote_clientes)
        
    print(f"✅ 3. ¡HITO CONQUISTADO! Se ha grabado físicamente '{nombre_archivo}'.")

except IOError:
    print("🚨 ERROR CRÍTICO: No se pudo escribir en el disco duro por falta de permisos.")