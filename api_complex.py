import requests
import openpyxl

nombre_archivo = "Reporte_Clientes_API.xlsx"

try:
    print("🌐 Conectando con el servidor remoto para extraer datos de usuarios...")
    respuesta = requests.get("https://jsonplaceholder.typicode.com/users")
    
    if respuesta.status_code == 200:
        print("✅ Datos recibidos. Analizando estructura anidada en la RAM...")
        lista_usuarios = respuesta.json()
        
        libro = openpyxl.Workbook()
        hoja = libro.active
        hoja.title = "Directorio Clientes"
        hoja.append(["Nombre", "Email", "Ciudad", "Empresa"])
        
        for usuario in lista_usuarios:
            nombre = usuario.get("name")
            email = usuario.get("email")
            
            direccion = usuario.get("address", {})
            ciudad = direccion.get("city")
            
            compania = usuario.get("company", {}).get("name")
            
            hoja.append([nombre, email, ciudad, compania])
            
        for columna in hoja.columns:
            letra = columna[0].column_letter
            largo_max = max(len(str(celda.value or '')) for celda in columna)
            hoja.column_dimensions[letra].width = largo_max + 4
            
        libro.save(nombre_archivo)
        print(f"💾 ¡ÉXITO DE INFRAESTRUCTURA! Se ha generado '{nombre_archivo}' con datos anidados.")
    else:
        print(f"⚠️ Alerta de servidor: Código {respuesta.status_code}")

except requests.exceptions.ConnectionError:
    print("🚨 ERROR CRÍTICO: Bloqueo perimetral o falla física de internet.")