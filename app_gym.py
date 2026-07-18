import openpyxl

nombre_reporte = "Control_Acceso_Gimnasio.xlsx"

def validar_membresia_gym(nombre_socio, dias_restantes=0):
    if dias_restantes > 0:
        estatus = "ACTIVO"
        mensaje = f"🟩 ACCESO PERMITIDO - Socio: '{nombre_socio}' | Días: {dias_restantes}"
    else:
        estatus = "VENCIDO"
        mensaje = f"🟥 ACCESO DENEGADO - Socio: '{nombre_socio}' | Membresía Expirada"
    return estatus, mensaje

lote_clientes = [
    {"nombre": "Héctor Chacón", "dias_membresia": 15},
    {"nombre": "Carlos Mendoza", "dias_membresia": 0},
    {"nombre": "Alejandro Gomez", "dias_membresia": 3},
    {"nombre": "Operador Incompleto"}
]

print("🛡️ Iniciando Consola Inteligente 'Gym Flow' de Alta Gama...\n")

libro = openpyxl.Workbook()
hoja = libro.active
hoja.title = "Log de Accesos"
hoja.append(["Nombre del Cliente", "Estatus de Membresía"])

for cliente in lote_clientes:
    nombre = cliente.get("nombre", "Usuario Anónimo")
    dias = cliente.get("dias_membresia")
    
    if dias is None:
        estatus, texto_consola = validar_membresia_gym(nombre)
    else:
        estatus, texto_consola = validar_membresia_gym(nombre, dias)
        
    print(texto_consola)
    
    hoja.append([nombre, estatus])

print("\n📐 Calculando dimensiones geométricas de celdas en la RAM...")
for columna in hoja.columns:
    letra_columna = columna[0].column_letter
    largo_maximo = max(len(str(celda.value or '')) for celda in columna)
    hoja.column_dimensions[letra_columna].width = largo_maximo + 4

libro.save(nombre_reporte)
print(f"\n💾 ¡SISTEMA INTEGRADO CON ÉXITO! Archivo '{nombre_reporte}' consolidado.")