import openpyxl
from openpyxl.styles import Font, PatternFill

nombre_archivo = "Reporte_Masivo.xlsx"

lote_repuestos = [
    {"producto": "Bomba de Agua de Alta Presión", "cantidad": 45, "estatus": "OK"},
    {"producto": "Kit de Tiempo Completo Gate", "cantidad": 12, "estatus": "CRITICO"},
    {"producto": "Liga de Freno Wagner", "cantidad": 80, "estatus": "OK"}
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

for repuesto in lote_repuestos:
    hoja.append([repuesto.get("producto"), repuesto.get("cantidad"), repuesto.get("estatus")])

print("📐 Iniciando cálculo geométrico de columnas en la RAM...")

for columna in hoja.columns:
    letra_columna = columna[0].column_letter
    
    largo_maximo = 0
    for celda in columna:
        if celda.value:
            largo_celda = len(str(celda.value))
            if largo_celda > largo_maximo:
                largo_maximo = largo_celda
                
    hoja.column_dimensions[letra_columna].width = largo_maximo + 4


libro.save(nombre_archivo)
print(f"✅ ¡HITO CONQUISTADO! Columnas auto-ajustadas y archivo '{nombre_archivo}' grabado.")