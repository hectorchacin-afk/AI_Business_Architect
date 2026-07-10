import os
import requests
import openpyxl
from dotenv import load_dotenv

load_dotenv()
token_acceso = os.getenv("TOKEN_SECRETORIO")

try:
    print("🔐 1. Validando credenciales de ciberseguridad en la RAM...")
    
    reporte_operacion = {
        "origen": "Taller_Repuestos",
        "auth_token": token_acceso,
        "estatus_sistema": "OPERATIVO"
    }
    
    print("🌐 2. Transmitiendo reporte de ventas (POST) a internet...")
    respuesta = requests.post("https://jsonplaceholder.typicode.com/posts", json=reporte_operacion)
    
    if respuesta.status_code == 201:
        print("✅ 3. Servidor remoto conectado. Generando registro físico en Excel...")
        datos_recibidos = respuesta.json()
        
        libro = openpyxl.Workbook()
        hoja = libro.active
        hoja.title = "Auditoria Ventas"
        
        hoja["A1"] = "Parametro_Seguridad"
        hoja["B1"] = "ID_Registro_Nube"
        
        hoja["A2"] = reporte_operacion.get("estatus_sistema")
        hoja["B2"] = datos_recibidos.get("id")
        
        libro.save("Auditoria_Taller.xlsx")
        print("💾 4. ¡SISTEMA COMPLETADO CON ÉXITO! Archivo 'Auditoria_Taller.xlsx' grabado físicamente.")
    else:
        print(f"⚠️ Alerta de red: Código inesperado {respuesta.status_code}")

except requests.exceptions.ConnectionError:
    print("🚨 ERROR CRÍTICO: Bloqueo de red o falla física de internet.")