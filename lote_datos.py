import openpyxl
from openpyxl.styles import Font, PatternFill

nombre_archivo = "Reporte_Masivo.xlsx"

lote_repuestos = [
    {"producto": "Bomba de Agua", "cantidad": 45, "estatus": "OK"},
    {"producto": "Kit de Tiempo", "cantidad": 12, "estatus": "CRITICO"},
    {"producto": "Liga de Freno", "cantidad": 80, "estatus": "OK"}
]

libro = openpyxl.Workbook()
hoja = libro.active
hoja.title = "Lote Produccion"

fuente_header = Font(name="Arial", size=11, bold=True, color="FFFFFF")
fondo_header = PatternFill(start_color="2C3E50", end_color="2C3E50", fill_type="solid")

headers = ["Nombre del Repuesto", "Stock Actual", "Alerta de Sistema"]
hoja.append(headers)

for celda in hoja[1]:
    celda.font = fuente_header
    celda.fill = fondo_header

print("📊 Procesando lote de diccionarios en la RAM...")

for repuesto in lote_repuestos:
    nombre = repuesto.get("producto")
    stock = repuesto.get("cantidad")
    alerta = repuesto.get("estatus")
    
    hoja.append([nombre, stock, alerta])

libro.save(nombre_archivo)
print(f"✅ ¡HITO CONQUISTADO! Se procesó el lote y se creó '{nombre_archivo}' con éxito.")