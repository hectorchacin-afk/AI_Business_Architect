import openpyxl

nombre_archivo = "Inventario_Taller.xlsx"

try:
    print("📂 Intentando conectar con el archivo físico de Excel...")
    libro = openpyxl.load_workbook(nombre_archivo)
    hoja = libro.active
    print(f"✅ CONEXIÓN EXITOSA: El archivo '{nombre_archivo}' fue leído correctamente.")
    print(f"Dato actual en la celda A2: {hoja['A2'].value}")

except FileNotFoundError:
    print(f"🚨 ALERTA DE INFRAESTRUCTURA: El archivo '{nombre_archivo}' no existe.")
    print("🛠️ Iniciando protocolo de recuperación: Creando un archivo nuevo automatizado...")
    
    nuevo_libro = openpyxl.Workbook()
    nueva_hoja = nuevo_libro.active
    nueva_hoja.title = "Inventario Taller"
    nueva_hoja["A1"] = "Repuesto"
    nueva_hoja["A2"] = "Bujia Automática"
    
    nuevo_libro.save(nombre_archivo)
    print(f"💾 ¡SISTEMA RECUPERADO! Se generó un nuevo '{nombre_archivo}' de respaldo seguro.")