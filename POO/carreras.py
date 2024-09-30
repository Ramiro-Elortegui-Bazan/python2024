from Personaje_cl import Personaje
import time
import os

def pedir_datos_personaje(num):
    print(f"Introduce los datos para el personaje {num}:")
    nombre = input("Nombre: ")
    altura = float(input("Altura: "))
    velocidad = float(input("Velocidad: "))
    resistencia = float(input("Resistencia: "))
    fuerza = float(input("Fuerza: "))
    return Personaje(nombre, altura, velocidad, resistencia, fuerza)

def mostrar_menu():
    print("--- Menú ---")
    print("1. Crear o recrear personajes")
    print("2. Mostrar información de ambos personajes")
    print("3. Personaje 1 ataca a Personaje 2")
    print("4. Personaje 2 ataca a Personaje 1")
    print("5. Salir")
    return input("Elige una opción: ")
 
           
personaje1 = None
personaje2 = None

opcion = ''
while opcion != '5':
    opcion = mostrar_menu()

    if opcion == '1':
        print("Creando personajes...")
        personaje1 = pedir_datos_personaje(1)
        personaje2 = pedir_datos_personaje(2)
        print("Personajes creados exitosamente.")
        
        time.sleep(1.5)
        os.system("cls")    

    elif opcion == '2':
        if personaje1 and personaje2:
            print("Información de los personajes:")
            personaje1.mostrar_info()
            personaje2.mostrar_info()
        else:
            print("Primero debes crear los personajes (opción 1).")
            
            time.sleep(1.5)
            os.system("cls") 

    elif opcion == '3':
        if personaje1 and personaje2:
            print("Personaje 1 ataca a Personaje 2:")
            personaje1.atacar(personaje2)
            time.sleep(7.0)
            os.system("cls")
        else:
            print("Primero debes crear los personajes (opción 1).")
            
            time.sleep(7.0)
            os.system("cls")

    elif opcion == '4':
       if personaje2 and personaje1:
            print("Personaje 1 ataca a Personaje 2:")
            personaje1.atacar(personaje2)
            time.sleep(7.0)
            os.system("cls")
   