# # Ejercicio 3: Pide 6 nombres y muestra la lista numerada (1. Nombre1, 2. Nombre2, etc.)-
# lista_nombres = []
# for i in range(6):
#     nombre = input("Introduce un nombre: ")
#     lista_nombres.append(nombre)

# lista_nombres.sort()
    
# for i, nombre in enumerate(lista_nombres, start=1):
#     print(f"{i}. {nombre}")

# # Ejercicio 4: Pide 8 números, elimina las repeticiones y muestra la lista sin duplicados ordenados de menor a mayor
# lista_numeros = []

# for i in range(8):
#     numero = int(input("Introduce un número: "))
#     lista_numeros.append(numero)

# lista_numeros_ordenada = list(set(lista_numeros))
# lista_numeros_ordenada.sort()
# print(lista_numeros_ordenada)

# # Ejercicio 5: Pide 10 calificaciones entre 0 y 10. Si alguna es menor que 6, añade al conteo de reprobados. Al final, muestra cuantos aprobaron y cantos reprobraron.
# lista_aprobados = []
# lista_reprobados = []

# for i in range(10):
#     calificacion = float(input("Introduce una calificación entre 0 y 10: "))
#     while(calificacion < 0 or calificacion > 10):
#         calificacion = float(input("Calificación inválida. Introduce una calificación entre 0 y 10: "))
#     if calificacion < 6:
#         lista_reprobados.append(calificacion)
#     else:
#         lista_aprobados.append(calificacion)

# print(f"Cantidad de aprobados: {len(lista_aprobados)}")
# print(f"Cantidad de reprobados: {len(lista_reprobados)}")

# Diccionarios
# nombre : "Mario"

# diccionario = {
#     "nombre": "Mario",
#     "apellido": "Segovia",
#     "edad": 29,
#     "licenciatura": "Ingeniero en Sistemas Computacionales",
#     "isEmpleado": True
# }

# print(diccionario.keys()) # Devuelve las claves del diccionario
# print(diccionario.values()) # Devuelve los valores del diccionario
# print(diccionario.items()) # Devuelve agrupados en conjuntos la clave y el valor
# print(diccionario["isEmpleado"]) # Acceder a la clave deseada
# diccionario.pop("edad") # Eliminar una clave junto con su valor
# print(diccionario)
# print(len(diccionario)) # Devuelve el largo del diccionario

# diccionario["edad"] = 29 # Agregar o actualizar un valor
# print(diccionario)

# # Recorrer un diccionario
# for clave, valor in diccionario.items():
#     print(f"{clave}: {valor}")


# # Ejercicio 1: Crea un diccionario vacío. Pide nombres y calificaciones de 5 alumnos y guárdalos en el diccionario. Luego muestra su promedio.
# diccionario_alumnos = {}
# for i in range(5):
#     nombre = input("Introduce el nombre del alumno: ")
#     calificacion = float(input(f"Introduce la calificación de {nombre}: "))
#     while(calificacion < 0 or calificacion > 10):
#         calificacion = float(input(f"Calificación inválida. Introduce la calificación de {nombre} entre 0 y 10: "))
#     diccionario_alumnos[nombre] = calificacion

# print(diccionario_alumnos)

# for clave, valor in diccionario_alumnos.items():
#     print(f"La calificación de {clave} es: {valor}")

# suma_calificaciones = sum(diccionario_alumnos.values())
# promedio = suma_calificaciones / len(diccionario_alumnos)
# print(f"El promedio de las calificaciones es: {promedio}")


# # Ejercicio 2: Crea un diccionario con 5 productos y precios, pide un producto y muestra su precio.
# diccionario_productos = {
#     "Cloro": 20,
#     "Detergente": 35,
#     "Jabón": 15,
#     "Papel sanitario": 40,
#     "Limpiador multiusos": 60
# }
# producto_buscado = input("Introduce el nombre del producto: ")
# if producto_buscado in diccionario_productos:
#     print(f"El precio de: {producto_buscado} es: ${diccionario_productos[producto_buscado]}.")
# else:
#     print("El producto no se encuentra en el inventario.")

# Ejercicio 3: Crea un diccionario con 5 países y sus capitales. Pide un país y muestra su capital.

pais_buscado = input("Introduce el nombre del país o 'Salir' para terminar: ")
diccionario_paises = {
    "México": "Ciudad de México",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo",
    "Argentina": "Buenos Aires",
    "Estados Unidos": "Washington D.C."
}
while pais_buscado != "Salir":
    if pais_buscado in diccionario_paises:
        print(f"La capital del pais {pais_buscado} es: {diccionario_paises[pais_buscado]}.")
    else:
        capital_pais = input("El país no se encuentra en el diccionario. Introduce la capital de ese país para agregarlo: ")
        diccionario_paises[pais_buscado] = capital_pais
    pais_buscado = input("Introduce el nombre del país o 'Salir' para terminar: ")