from functions import *

# Función principal del sistema
def _main_():
    lista_estudiantes = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_estudiante(lista_estudiantes)
        elif opcion == '2':
            mostrar_estudiantes(lista_estudiantes)
        elif opcion == '3':
            buscar_estudiante(lista_estudiantes)
        elif opcion == '4':
            eliminar_estudiante(lista_estudiantes)
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

_main_()