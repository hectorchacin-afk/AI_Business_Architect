import openpyxl
from datetime import datetime

nombre_reporte = "Control_Acceso_Gimnasio.xlsx"
nombre_log_errores = "Log_Errores_Infraestructura.txt"

def validar_membresia_gym(nombre_socio, dias_restantes=0):
    if dias_restantes > 0:
        estatus = "ACTIVO"
        mensaje = f"🟩 ACCESO PERMITIDO - Socio: '{nombre_socio}' | Días: {dias_restantes}"
    else:
        estatus = "VENCIDO"
        mensaje = f"🟥 ACCESO DENEGADO - Socio: '{nombre_socio}' | Membresía Expirada"
    return estatus, mensaje

try:
    print("🔐 1. Activando escudo de resiliencia perimetral sobre 'Gym Flow'...")
    
    raise FileNotFoundError("Conexión perdida con la base de datos central de Salesforce.")

    lote_clientes = [
        {"nombre": "Héctor Chacón", "dias_membresia": 15},
        {"nombre": "Carlos Mendoza", "dias_membresia": 0},
        {"nombre": "Operador Incompleto"}
    ]
    
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

    for columna in hoja.columns:
        letra_columna = columna.column_letter
        largo_maximo = max(len(str(celda.value or '')) for celda in columna)
        hoja.column_dimensions[letra_columna].width = largo_maximo + 4

    libro.save(nombre_reporte)

except Exception as error_inesperado:
    print("\n🚨 ALERTA CRÍTICA: Se interceptó una falla operativa en el gimnasio.")
    print(f"-> Diagnóstico técnico capturado: {error_inesperado}")
    
    momento_exacto = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(nombre_log_errores, mode="a", encoding="utf-8") as archivo_log:
        archivo_log.write(f"[{momento_exacto}] FALLA EN VIVO: {error_inesperado}\n")
    print(f"💾 Registro de ciberseguridad guardado en '{nombre_log_errores}'.")

finally:
    print("\n🧹 2. [Protocolo Finally] Recursos liberados y entorno estabilizado.")
    print("✅ El software de la recepción sigue encendido protegiendo el torniquete.")