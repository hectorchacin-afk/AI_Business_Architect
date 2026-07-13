import openpyxl

nombre_archivo = "Reporte_Continuo.xlsx"

try:
    libro = openpyxl.load_workbook(nombre_archivo)
    hoja = libro.active
except FileNotFoundError:
    libro = openpyxl.Workbook()
    hoja = libro.active
    hoja.title = "Ingresos Taller"
    hoja.append(["Producto", "Cantidad"])

print("🚀 CENTRAL DE CAPTURA EN VIVO ACTIVADA")
print("-> Escriba la palabra 'salir' en el nombre del producto para cerrar el programa.\n")

while True:
    producto = input("Nombre del repuesto: ").strip()
    
    if producto.lower() == "salir":
        print("\n💾 Guardando base de datos física en el disco duro...")
        libro.save(nombre_archivo)
        print("🔌 Sistema cerrado de forma segura. ¡Buen trabajo!")
        break 
        
    cantidad = input(f"Cantidad para {producto} (Solo números): ").strip()
    
    if cantidad.isdigit():
        hoja.append([producto, int(cantidad)])
        print(f"✅ Fila acoplada temporalmente: [{producto} | {cantidad}]")
    else:
        print("🚨 CANTIDAD INVÁLIDA: Fila descartada para proteger el Excel. Intente de nuevo.\n")