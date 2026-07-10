import os
from dotenv import load_dotenv

load_dotenv()

print("🔐 Iniciando bóveda de ciberseguridad...")

clave_invisible = os.getenv("TOKEN_SECRETORIO")

print(f"Token de Salesforce cargado en la RAM: {clave_invisible}")