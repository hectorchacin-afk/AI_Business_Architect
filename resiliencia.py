import openpyxl

nombre_archivo = "Inventario_Taller.xlsx"

try:
    print("📂 Accediendo al archivo de Excel en el disco duro...")
    libro = openpyxl.load_workbook(nombre_archivo)
    hoja = libro.active
    
    nuevo_registro = ["Filtro de Aire", 85]
    
    hoja.append(nuevo_registro)
    
    libro.save(nombre_archivo)
    print(f"✅ MODIFICACIÓN EXITOSA: Se agregó '{nuevo_registro[0]}' al final de la tabla.")

except FileNotFoundError:
    print(f"🚨 ALERTA: El archivo '{nombre_archivo}' no existe. Creando base de datos inicial...")
    libro = openpyxl.Workbook()
    hoja = libro.active
    hoja.title = "Inventario Taller"
    hoja.append(["Producto", "Cantidad"]) # Encabezados de la tabla
    hoja.append(["Bujia Champion", 150]) # Fila inicial
    libro.save(nombre_archivo)
    print(f"💾 Base de datos '{nombre_archivo}' restaurada con éxito. Vuelve a ejecutar el script.")