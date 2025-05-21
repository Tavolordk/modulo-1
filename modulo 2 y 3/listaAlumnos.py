"""
Ejercicio Práctico: Registro de Calificaciones de Alumnos
Objetivo:
Practicar el uso de variables, operadores, estructuras de datos como listas y diccionarios, y entrada/salida básica.

Enunciado:
Desarrolla un programa en Python que permita registrar alumnos y sus calificaciones, y luego calcular el promedio de cada alumno y mostrar su estatus (Aprobado/Reprobado).

Requisitos:
Solicitar al usuario el número total de alumnos a registrar.

Para cada alumno:

Pedir su nombre.

Pedir tres calificaciones (valores entre 0 y 10).

Guardar la información en un diccionario, donde la clave sea el nombre del alumno y el valor sea una lista de sus tres calificaciones.

Al finalizar, mostrar un reporte así:

REPORTE FINAL:
Alumno: Juan Pérez
Calificaciones: [8.0, 9.0, 7.5]
Promedio: 8.2
Estatus: Aprobado

Alumno: Ana López
Calificaciones: [6.0, 5.5, 6.0]
Promedio: 5.8
Estatus: Reprobado

"""
numeroDeAlumnos=int(input('Inserte número de estudiantes a registrar: '))
status='Reprobado'
objetoAlumno={}
for alumno in range (numeroDeAlumnos):
    calificaciones=[]
    promedio=0
    nombre=str(input('Inserta nombre del alumno: '))
    for calificacion in range (3):
        numeroCalificacion=float(input('Inserte calificacion: '))
        calificaciones.append(numeroCalificacion)
        promedio=round(sum(calificaciones) / 3, 1)
    if promedio >=6:
        status='Aprobado'
    else:
        status=status
    objetoAlumno[nombre]={'calificaciones':calificaciones,'promedio':promedio,'status':status}
print("\nREPORTE FINAL:")
for nombre, datos in objetoAlumno.items():
    print(f"Alumno: {nombre}")
    print(f"Calificaciones: {datos['calificaciones']}")
    print(f"Promedio: {datos['promedio']}")
    print(f"Estatus: {datos['status']}\n")
