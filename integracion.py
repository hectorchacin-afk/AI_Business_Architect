import requests
import openpyxl

try:
    print("🌐 1. Solicitando datos en vivo a la nube...")
    respuesta = requests.get("https://jsonplaceholder.typicode.com/todos/2")
    
    if respuesta.status_code == 200:
        print("✅ 2. Datos recibidos. Procesando e inyectando en Excel...")
        datos = respuesta.json()
        
        libro = openpyxl.Workbook()
        hoja = libro.active
        hoja.title = "Datos Remotos"
        
        hoja["A1"] = "ID_Usuario"
        hoja["B1"] = "Titulo_Tarea"
        hoja["C1"] = "Estatus_Completado"
        
        hoja["A2"] = datos.get("userId")
        hoja["B2"] = datos.get("title")
        hoja["C2"] = str(datos.get("completed")) # Convertimos el booleano a texto seguro
        
        libro.save("Reporte_Nube.xlsx")
        print("💾 3. ¡ÉXITO TOTAL! El archivo físico 'Reporte_Nube.xlsx' ha sido creado con datos reales.")
    else:
        print(f"⚠️ Alerta de red: Código {respuesta.status_code}")

except requests.exceptions.ConnectionError:
    print("🚨 ERROR CRÍTICO: Bloqueo perimetral o falla física de internet.")