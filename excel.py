import openpyxl

try:
    libro = openpyxl.load_workbook("Inventario_Taller.xlsx")
    hoja = libro["Inventario Taller"]
    
    print("📖 ¡CONEXIÓN EXCEL EXITOSA! Extrayendo filas de producción...\n")
    
    registro_bujia = {
        "producto": hoja["A2"].value,
        "stock": hoja["B2"].value
    }
    
    prod_real = registro_bujia.get("producto")
    precio_seguro = registro_bujia.get("precio", "Precio No Registrado en Excel")
    
    print(f"Producto auditado: {prod_real}")
    print(f"Estatus del precio: {precio_seguro}")

except FileNotFoundError:
    print("🚨 ALERTA PERIMETRAL: El archivo 'Inventario_Taller.xlsx' no fue encontrado.")