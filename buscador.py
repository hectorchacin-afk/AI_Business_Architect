import openpyxl

producto_a_buscar = "Pastilla Freno"

try:
    print(f"🔍 Iniciando motor de búsqueda para: '{producto_a_buscar}'...")
    libro = openpyxl.load_workbook("Reporte_Matematico.xlsx")
    hoja = libro["Calculos Taller"]
    
    encontrado = False
    
    for fila in hoja.iter_rows(min_row=2, max_row=4, values_only=True):
        nombre_repuesto = fila[0]
        cantidad_stock = fila[1]
        
        if nombre_repuesto == producto_a_buscar:
            print(f"🎯 ¡PRODUCTO ENCONTRADO EN LA BASE DE DATOS!")
            print(f"-> Repuesto: {nombre_repuesto} | Stock Disponible: {cantidad_stock} unidades.")
            encontrado = True
            break 
            
    if not encontrado:
        print(f"❌ ERROR: El producto '{producto_a_buscar}' no existe en este reporte.")

except FileNotFoundError:
    print("🚨 ALERTA PERIMETRAL: El archivo 'Reporte_Matematico.xlsx' no existe en el disco duro.")