import time
import os
import sqlite3
from CLSEstudiante import Estudiante
from CLSCurso import Curso
from CLSMaestro import Profesor
from CLSMaterias import Materia
from CLSCaleficacion import Calificacion



def conectar_db():
    conn = sqlite3.connect("escuela.db")
    return conn

# Función para agregar estudiante
def agregar_estudiante(conn):
    legajo_id = int(input("Ingrese el ID del estudiante: "))
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del estudiante (YYYY-MM-DD): ")
    dni = input("Ingrese el DNI del estudiante: ")
    curso = input("Ingrese el curso del estudiante: ")
    
    conn = sqlite3.connect('escolar.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO estudiantes (id, nombre, edad, fecha_nacimiento, dni, curso) 
        VALUES (?, ?, ?, ?, ?, ?)
    """, (legajo_id, nombre, edad, fecha_nacimiento, dni, curso))
    
    conn.commit()
    print("Estudiante agregado correctamente.")


# Función para agregar profesor
def agregar_profesor(conn):
    nombre = input("Ingrese el nombre del profesor: ")
    asignatura = input("Ingrese la asignatura del profesor: ")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO profesores (nombre, asignatura) VALUES (?, ?)", (nombre, asignatura))
    conn.commit()
    print("Profesor agregado correctamente.")

# Función para agregar materia
def agregar_materia(conn):
    nombre = input("Ingrese el nombre de la materia: ")
    codigo = input("Ingrese el código de la materia: ")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO materias (nombre, codigo) VALUES (?, ?)", (nombre, codigo))
    conn.commit()
    print("Materia agregada correctamente.")

# Función para agregar calificación
def agregar_calificacion(conn):
    estudiante_id = int(input("Ingrese el ID del estudiante: "))
    materia_id = int(input("Ingrese el ID de la materia: "))
    calificacion = float(input("Ingrese la calificación: "))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO calificaciones (estudiante_id, materia_id, calificacion) VALUES (?, ?, ?)", (estudiante_id, materia_id, calificacion))
    conn.commit()
    print("Calificación agregada correctamente.")

# Función para mostrar estudiantes
def mostrar_estudiantes(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()
    for estudiante in estudiantes:
        print(f"ID: {estudiante[0]}, Nombre: {estudiante[1]}, Edad: {estudiante[2]}")

# Función para mostrar profesores
def mostrar_profesores(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profesores")
    profesores = cursor.fetchall()
    for profesor in profesores:
        print(f"ID: {profesor[0]}, Nombre: {profesor[1]}, Asignatura: {profesor[2]}")

# Función para mostrar materias
def mostrar_materias(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM materias")
    materias = cursor.fetchall()
    for materia in materias:
        print(f"ID: {materia[0]}, Nombre: {materia[1]}, Código: {materia[2]}")

# Función para mostrar calificaciones
def mostrar_calificaciones(conn):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT c.id, e.nombre, m.nombre, c.calificacion
        FROM calificaciones c
        JOIN estudiantes e ON c.estudiante_id = e.id
        JOIN materias m ON c.materia_id = m.id
    ''')
    calificaciones = cursor.fetchall()
    for calificacion in calificaciones:
        print(f"ID: {calificacion[0]}, Estudiante: {calificacion[1]}, Materia: {calificacion[2]}, Calificación: {calificacion[3]}")


def main():
    conn = conectar_db()
    while True:
        print("Sistema de Gestión Escolar")
        print("1. Agregar estudiante")
        print("2. Agregar profesor")
        print("3. Agregar materia")
        print("4. Agregar calificación")
        print("5. Mostrar estudiantes")
        print("6. Mostrar profesores")
        print("7. Mostrar materias")
        print("8. Mostrar calificaciones")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")
        time.sleep(1.5)
        os.system("cls" if os.name == "nt" else "clear")

        if opcion == '1':
            agregar_estudiante(conn)
        elif opcion == '2':
            agregar_profesor(conn)
        elif opcion == '3':
            agregar_materia(conn)
        elif opcion == '4':
            agregar_calificacion(conn)
        elif opcion == '5':
            mostrar_estudiantes(conn)
            time.sleep(1.5)
        elif opcion == '6':
            mostrar_profesores(conn)
            time.sleep(1.5)
        elif opcion == '7':
            mostrar_materias(conn)
            time.sleep(1.5)
        elif opcion == '8':
            mostrar_calificaciones(conn)
            time.sleep(1.5)
        elif opcion == '9':
            print("Saliendo del sistema.")
            conn.close()
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    
    
    time.sleep(1.5)
    os.system("cls" if os.name == "nt" else "clear")            

if __name__ == "__main__":
    main()
