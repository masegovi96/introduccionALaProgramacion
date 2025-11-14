# Sistema de Gestión de Estudiantes

# Función para mostrar las opciones del menu
def mostrar_menu():
    print("Sistema de Gestión de Estudiantes")
    print("1. Agregar estudiante")
    print("2. Mostrar lista completa de estudiantes")
    print("3. Buscar estudiante por nombre")
    print("4. Eliminar estudiante")
    print("5. Salir")
    
# Función para agregar un estudiante
def agregar_estudiante(lista_estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    promedio = float(input("Ingrese el promedio del estudiante: "))
    
    lista_estudiantes.append({"nombre": nombre, "apellido": apellido, "promedio": promedio})
    
    print(f"Estudiante {nombre} {apellido} agregado exitosamente.")

# Función para mostrar lista de estudiantes
def mostrar_estudiantes(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes en la lista")
        return
    print("Lista de estudiantes")
    for estudiante in lista_estudiantes:
        print(f"{estudiante['nombre']} {estudiante['apellido']} -  Promedio: {estudiante['promedio']}")