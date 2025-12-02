# Función para mostrar las opciones del menu
def mostrar_menu():
    print("Sistema de Gestión de Estudiantes")
    print("1. Agregar estudiante")
    print("2. Mostrar lista completa de estudiantes")
    print("3. Buscar estudiante por nombre")
    print("4. Buscar estudiante por apellido")
    print("5. Calcular promedio del grupo")
    print("6. Ordenar estudiantes por promedio")
    print("7. Eliminar estudiante")
    print("8. Salir")
    
# Función para buscar estudiante por medio del apellido
def buscar_por_apellido(lista_estudiantes, apellido):
    for estudiante in lista_estudiantes:
        if estudiante['apellido'].lower() == apellido.lower():
            return estudiante
    return None    

# Función para calcular el promedio del grupo
def calcular_promedio(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes en la lista para calcular el promedio.")
        return
    try:
        suma_promedios = sum(estudiante['promedio'] for estudiante in lista_estudiantes)
        promedio_general = suma_promedios / len(lista_estudiantes)
        print(f"El promedio general del grupo es: {promedio_general:.2f}")
    except ZeroDivisionError:
        print("Error: División por cero al calcular el promedio.")

# Función para ordenar estudiantes por promedio (De la calificación más alta a la más baja)
def ordenar_por_promedio(lista_estudiantes):
    lista_ordenada = sorted(lista_estudiantes, key=lambda x: x['promedio'], reverse=True)
    print("Estudiantes ordenados por promedio (de mayor a menor):")
    for estudiante in lista_ordenada:
        print(f"{estudiante['nombre']} {estudiante['apellido']} - Promedio: {estudiante['promedio']}")

# Función para agregar un estudiante
def agregar_estudiante(lista_estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    
    try:
        promedio = float(input("Ingrese el promedio del estudiante: "))
    except ValueError:
        print("Promedio inválido. Debes ingresar un valor numérico.")
        return    
    
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
        
# Función para buscar estudiante por nombre
def buscar_estudiante(lista_estudiantes):
    nombre_buscar = input("Ingrese el nombre del estudiante que desea buscar: ")
    for estudiante in lista_estudiantes:
        if estudiante['nombre'].lower() == nombre_buscar.lower():
            print(f"Estudiante encontrado: {estudiante['nombre']} {estudiante['apellido']} - Promedio: {estudiante['promedio']}")
            return
    print("Estudiante no encontrado.")
    
# Función para eliminar estudiante
def eliminar_estudiante(lista_estudiantes):
    nombre_eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
    for estudiante in lista_estudiantes:
        if estudiante['nombre'].lower() == nombre_eliminar.lower():
            lista_estudiantes.remove(estudiante)
            print(f"Estudiante {estudiante['nombre']} {estudiante['apellido']} dado de baja exitosamente.")
            return
    print("Estudiante no encontrado.")