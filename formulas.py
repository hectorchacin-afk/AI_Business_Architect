import openpyxl
from datetime import datetime

momento_actual = datetime.now()
fecha_formateada = momento_actual.strftime("%Y-%m-%d %H:%M:%S")

nombre_archivo = "Reporte_Cronologico.xlsx"

libro = openpyxl.Workbook()
hoja = libro.active
hoja.title = "Auditoria Temporal"

hoja["A1"] = "Fecha y Hora de Operación"
hoja["B1"] = "Repuesto Registrado"
hoja["C1"] = "Stock"

hoja["A2"] = fecha_formateada
hoja["B2"] = "Filtro Aceite"
hoja["C2"] = 85

libro.save(nombre_archivo)

print(f"📊 ¡ÉXITO DE INFRAESTRUCTURA! Se creó '{nombre_archivo}' con estampa de tiempo real.")