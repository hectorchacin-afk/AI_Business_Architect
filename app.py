inventario_taller = {
    "bujia": 150,
    "pastilla": 20,
    "filtro": 85
}

while True:
    try:
        producto = input("Ingrese repuesto (bujia/pastilla/filtro), 'agregar' o 'salir': ").lower()
        
        if producto == 'salir':
            print("Cerrando sesión segura. ¡Hasta luego!")
            break
            
        if producto == 'agregar':
            nuevo_repuesto = input("Nombre del nuevo repuesto: ").lower()
            cantidad_nueva = int(input("Cantidad que ingresa al taller: "))
            inventario_taller[nuevo_repuesto] = cantidad_nueva
            print(f"✅ ÉXITO: Se registró '{nuevo_repuesto}' con {cantidad_nueva} unidades.\n")
            continue # Salta al inicio del while para seguir operando
            
        cantidad = inventario_taller[producto]
        
        if cantidad < 50:
            print(f"🚨 ALERT! El stock de '{producto}' es crítico: Solo quedan {cantidad} unidades.\n")
        else:
            print(f"✅ OK: El stock de '{producto}' es seguro: Hay {cantidad} unidades.\n")
            
    except KeyError:
        print("❌ ERROR: Ese producto no existe en el inventario actual. Intente de nuevo.\n")