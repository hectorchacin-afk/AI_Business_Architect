import openpyxl

try:
    print("🔍 Cargando base de datos maestra para filtrado perimetral...")
    libro_maestro = openpyxl.load_workbook("Reporte_Masivo.xlsx")
    hoja_maestra = libro_maestro["Lote Produccion"]
    
    libro_alerta = openpyxl.Workbook()
    hoja_alerta = libro_alerta.active
    hoja_alerta.title = "PRODUCTOS EN CRITICO"
    
    hoja_alerta.append(["Repuesto de Emergencia", "Stock Actual"])
    
    print("⚡ Analizando celdas en tiempo real...")
    
    for fila in hoja_maestra.iter_rows(min_row=2, max_row=4, values_only=True):
        nombre = fila[0]
        stock = fila[1]
        estatus = fila[2]
        
        if estatus == "CRITICO":
            hoja_alerta.append([nombre, stock])
            print(f"🚨 Alerta detectada y aislada: {nombre} ({stock} unidades)")
            
    libro_alerta.save("Lista_Compras_Urgentes.xlsx")
    print("\n💾 ¡OPERACIÓN EXITOSA! Se ha generado el reporte 'Lista_Compras_Urgentes.xlsx'.")

except FileNotFoundError:
    print("🚨 ERROR: No se encontró el archivo 'Reporte_Masivo.xlsx' para realizar el filtro.")