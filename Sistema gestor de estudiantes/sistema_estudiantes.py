from functions import *

# Función principal del sistema
def _main_():
    try:
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
                buscar_por_apellido(lista_estudiantes)
            elif opcion == '5':
                calcular_promedio(lista_estudiantes)
            elif opcion == '6':
                ordenar_por_promedio(lista_estudiantes)
            elif opcion == '7':
                eliminar_estudiante(lista_estudiantes)
            elif opcion == '8':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

_main_()