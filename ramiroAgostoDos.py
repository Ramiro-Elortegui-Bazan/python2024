import time
import os

def gestion_tareas():
    tareas = []

    while True:
        print("1: Añadir una tarea")
        print("2: Ver todas las tareas")
        print("3: Marcar una tarea como completada")
        print("4: Salir")
        
        opcion = input("Elige una opción: ")
        time.sleep(1.5)
        os.system("cls" if os.name == "nt" else "clear")
        
        if opcion == "1":
            tarea = input("Escribe la descripción de la nueva tarea: ")
            tareas.append(tarea)
            print(f"Tarea '{tarea}' añadida a la lista.")
        
        elif opcion == "2":
            if len(tareas) == 0:
                print("No hay tareas pendientes.")
            else:
                print("Tareas pendientes:")
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea}")
        
        elif opcion == "3":
            if len(tareas) == 0:
                print("No hay tareas para completar.")
            else:
                print("Tareas pendientes:")
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea}")
                
                num_tarea = int(input("Elige el número de la tarea a marcar como completada: "))
                if 1 <= num_tarea <= len(tareas):
                    tarea_completada = tareas.pop(num_tarea - 1)
                    print(f"Tarea '{tarea_completada}' completada y eliminada de la lista.")
                else:
                    print("Número de tarea inválido.")
        
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")

gestion_tareas()
