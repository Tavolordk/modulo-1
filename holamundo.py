"""Este programa fue hecho en atexIT gracias por tomar el curso
sdkfjsdjfñkjsfd
sdfskgkjdg
"""
#Esto fue hecho por ATEXIT

print('HOLA MUNDO DESDE ATEX IT')

nombre_completo=input('Inserte nombre')
print('Tu nombre es ' + str(nombre_completo))
print(f"Hola, {nombre_completo}")
print(f'5/2 pero dame el entero solamente: {5//2}')
print(f'5/2 pero dame con todo el decimal: {5/2}')
print(f'residuo de 5/2: {5%2}')
print(f'Doble asterisco: representa una potencia {5**3}')
def imprimeSaludo():
 print('Hola soy una funcion')

def esMayorDeEdad(edad):
 if edad>=18 and  edad<65:
  print('Aun no te toca 60 y mas')
 elif edad>=18 and not edad<65:
  print('Ya puedes cobrar tus 60 y mas')
 else:
  print('Eres menor de edad')


esMayorDeEdad(7)

contador=0
contador=1