import openpyxl

libro = openpyxl.Workbook()
hoja = libro.active
hoja.title = "Calculos Taller"

hoja["A1"] = "Repuesto"
hoja["B1"] = "Cantidad Stock"

hoja["A2"] = "Bujia Champion"
hoja["B2"] = 150

hoja["A3"] = "Filtro de Aire"
hoja["B3"] = 85

hoja["A4"] = "Pastilla Freno"
hoja["B4"] = 20

hoja["A5"] = "TOTAL INVENTARIO:"
hoja["B5"] = "=SUM(B2:B4)"

libro.save("Reporte_Matematico.xlsx")

print("📊 ¡ÉXITO DE AUTOMATIZACIÓN! El archivo 'Reporte_Matematico.xlsx' ha sido creado con fórmulas activas.")