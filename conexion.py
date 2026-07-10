import requests

try:
    print("🚀 Iniciando envío de datos (Petición POST) al servidor remoto...")
    
    alerta_inventario = {
        "repuesto": "Bujia Champion",
        "estatus": "CRITICO",
        "cantidad": 20
    }
    
    respuesta = requests.post("https://jsonplaceholder.typicode.com/posts", json=alerta_inventario)
    
    if respuesta.status_code == 201:
        print("✅ ENVÍO EXITOSO: El servidor remoto recibió y procesó la alerta.")
        print(f"Respuesta oficial de la nube: {respuesta.json()}")
    else:
        print(f"⚠️ ALERTA DE RED: El servidor respondió con código {respuesta.status_code}")

except requests.exceptions.ConnectionError:
    print("🚨 ERROR CRÍTICO: No se pudo establecer la conexión física a internet.")