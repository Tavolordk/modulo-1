# Proyecto: Calculadora de Edad
# Autor: Octavio Olea
# Fecha: 9 de mayo de 2025

from datetime import datetime

# Bienvenida
print("Bienvenido a la Calculadora de Edad 🎂")

# Solicitar datos al usuario
nombre = input("¿Cuál es tu nombre? ")
anio = int(input("Ingresa tu año de nacimiento (YYYY): "))
mes = int(input("Ingresa tu mes de nacimiento (1-12): "))
dia = int(input("Ingresa tu día de nacimiento (1-31): "))

# Obtener fecha actual
hoy = datetime.now()
print('fecha de hoy ' + str(hoy))
fecha_nacimiento = datetime(anio, mes, dia)
print('fecha de nacimiento ' + str(fecha_nacimiento))

# Calcular diferencia
diferencia = hoy - fecha_nacimiento
edad_dias = diferencia.days
edad_anios = edad_dias // 365
edad_meses = (edad_dias % 365) // 30
dias_restantes = (edad_dias % 365) % 30

# Mostrar resultado
print("\nHola", nombre + "!")
print(f"Tienes aproximadamente {edad_anios} años, {edad_meses} meses y {dias_restantes} días de edad.")