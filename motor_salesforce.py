from app_gym import validar_membresia_gym

print("🌐 CONECTANDO CON EL API GATEWAY DE SALESFORCE...")
print("🛡️ Reutilizando módulos de ciberseguridad locales...\n")

socio_vip = "Director Corporativo"
estatus_red = 30

resultado_estatus, texto_consola = validar_membresia_gym(socio_vip, estatus_red)

print("📋 Resultado del escaneo externo:")
print(texto_consola)

print("\n✅ Conexión con Salesforce finalizada con éxito modular.")