print("🛡️ Iniciando escudo de validación numérica perimetral...")

entrada_stock = input("Ingrese la cantidad exacta de repuestos (Solo números): ")

stock_limpio = entrada_stock.strip()

if stock_limpio.isdigit():
    cantidad_segura = int(stock_limpio)
    print(f"✅ VALIDACIÓN EXITOSA: El número {cantidad_segura} es seguro para meterlo a Excel.")
else:
    print("🚨 ERROR CRÍTICO DE ENTRADA: Se detectaron letras o caracteres inválidos. Operación bloqueada.")