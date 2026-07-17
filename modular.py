import openpyxl

nombre_reporte = "Auditoria_Acceso_Gym.xlsx"

def validar_acceso_gym(nombre_cliente, dias_restantes=0):
    if dias_restantes > 0:
        estatus = "PERMITIDO"
        mensaje = f"🟩 ACCESO PERMITIDO - '{nombre_cliente}'"
    else:
        estatus = "DENEGADO"
        mensaje = f"🟥 ACCESO DENEGADO - '{nombre_cliente}'"
    return estatus, mensaje

def registrar_auditoria_excel(nombre_cliente, estatus_resultado):
    try:
        libro = openpyxl.load_workbook(nombre_reporte)
        hoja = libro.active
    except FileNotFoundError:
        libro = openpyxl.Workbook()
        hoja = libro.active
        hoja.title = "Log Acceso"
        hoja.append(["Nombre Socio", "Resultado Acceso"])
        
    hoja.append([nombre_cliente, estatus_resultado])
    libro.save(nombre_reporte)

lote_socios = [
    {"socio": "Héctor Chacón", "dias": 15},
    {"socio": "Carlos Mendoza", "dias": 0},
    {"socio": "Alejandro Gomez", "dias": 3}
]

print("🛡️ Iniciando Sistema de Auditoría Modular...\n")

for persona in lote_socios:
    nombre = persona.get("socio")
    dias = persona.get("dias")
    
    estatus_final, texto_terminal = validar_acceso_gym(nombre, dias)
    print(texto_terminal)
    
    registrar_auditoria_excel(nombre, estatus_final)
    print("💾 Fila de auditoría respaldada en el disco duro.")
    print("-" * 55)

print("\n✅ ¡SISTEMA MODULAR COMPLETO! Archivo 'Auditoria_Acceso_Gym.xlsx' actualizado.")