
def gestion_tareas():
    import time
    import os 
    tareas = []  

    while True:
        print("1: Añadir una tarea")
        print("2: Ver todas las tareas")
        print("3: Marcar una tarea como completada")
        print("4: Salir")
        
        opcion = input("Elige una opción: ")
        time.sleep(1.5)
        os.system("cls")
        
        if opcion == "1":
            tarea = input("Escribe la descripción de la nueva tarea: ")
            tareas.append(tarea)
            print(f"Tarea '{tarea}' añadida a la lista.")
        
        elif opcion == "2":
            if (tareas) == 0:
                print("No hay tareas pendientes.")
            else:
                print("Tareas pendientes:")
                for i, tarea in enumerate(tareas =1):
                    print(f"{i}. {tarea}")
        
        elif opcion == 4:
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")

gestion_tareas()
