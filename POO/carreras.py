from Personaje_cl import Personaje
# nombre, altura, velocidad, resistencia, fuerza

menu = '''
_____________________________
*    1 Crear personaje      *
*    2 Jugar carrera        *
*    3 Salir                *
_____________________________
       '''

cantidadPersonaje = 0

while True:
    print(menu)
    try:
        opcion = int(input("Elegir una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        nombre = input("")
    
    elif opcion == 2:
        p2 = Personaje("Superman", 190, 100, 100, 100)
        print(f"El personaje se llama {p2.nombre}")
    
    elif opcion == 3:
        print("chau")
        break
    else:
        print("Opción incorrecta.")
