print("🛡️ Iniciando escudo de sanitización perimetral...")

entrada_usuario = input("Ingrese el nombre del repuesto a registrar: ")

datos_limpios = entrada_usuario.strip().replace("'", "").replace('"', "").replace(";", "")

producto_seguro = datos_limpios.lower()

if producto_seguro == "":
    print("❌ ERROR DE CIBERSEGURIDAD: El ingreso no puede estar vacío o contener solo caracteres inválidos.")
else:
    print(f"✅ DATO SANITIZADO Y SEGURO: '{producto_seguro}' listo para ser enviado a la nube.")