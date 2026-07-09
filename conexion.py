import requests

try:
    print("🌐 Iniciando petición HTTP al servidor remoto...")
    respuesta = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    
    if respuesta.status_code == 200:
        print("✅ CONEXIÓN EXITOSA: El servidor internacional respondió correctamente.")
        datos_servidor = respuesta.json()
        print(f"Datos recibidos en vivo: {datos_servidor}")
    else:
        print(f"⚠️ ALERTA DE RED: Código de estado inesperado: {respuesta.status_code}")

except requests.exceptions.ConnectionError:
    print("🚨 ERROR CRÍTICO: No se pudo establecer la conexión física a internet.")