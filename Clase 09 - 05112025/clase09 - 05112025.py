palabra = "Palabra ejemplo"

for letra in palabra:
    print(letra)

# Ejercicio 3: Haz un programa que pida nombre y apellido. Muestra en pantalla en formato Apellido, Nombre con cada palabra iniciando en mayúscula
nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
nombre_completo = apellido + ", " + nombre # Concatenación de cadenas

print(f"{apellido.capitalize()}, {nombre.capitalize()}") #Aquí usamos cadenas formateadas para mostrar el resultado, todo el trato de mayusculas se hace en esta linea
print(nombre_completo.title()) # Aquí usamos tittle para convertir la primera letra de cada palabra en mayúsculas, trabajamos con la variable creada anteriormente

# Ejercicio 4: Pide una frase y una letra. Muestra cuantas veces aparece esa letra en la frase sin distinguir entre mayúsculas y minúsculas
frase = input("Escribe una frase: ")
letra = input("Escribe la letra que deseas buscar: ")

frase_formateada = frase.strip().lower() # Limpiamos espacios y convertimos a minúsculas
letra_formateada = letra.strip().lower() # Limpiamos espacios y convertimos a minúsculas

conteo_letra = frase_formateada.count(letra_formateada) # Contar las apariciones de la letra ingresada por el usuario en la frase

print(f"La letra '{letra}' aparece {conteo_letra} veces en la frase: '{frase}'.")

# Ejercicio 5: Pide una frase y reemplaza todas las vocales 'a' por '@' y muestra el resultado.
frase = input("Escribe una frase: ")
frase_formateada = frase.strip().lower() # Limpiamos espacios y convertimos a minúsculas|
frase_modificada = frase_formateada.replace("a", "@") # Reemplazamos todas las 'a' por '@'
print("Frase modificada:", frase_modificada)

# Ejercicio 6: Pide un texto y extrae los primeros 10 caracteres. Si el texto tiene menos de 10 caracteres, muestra el texto completo.
texto = input("Escribe un texto o frase: ")
if len(texto) <= 10:
    print(f"El texto completo es: '{texto}'")
else:
    texto_diez_caracteres = texto[:10]
    print(f"Los primeros 10 caracteres son: '{texto_diez_caracteres}'")

##############################################################
#                     LISTAS EN PYTHON                       #
##############################################################
lista1 = [10, 30, 20, 50, 5, 15] # Lista
lista2 = ["manzana", "banana", "fresa", "pera", "naranja", 4, 6.6, True] # Lista con diferentes tipos de datos

print(lista1)
print(lista2)

# Recorrido de listas
for elemento in lista1:
    print(elemento)
    
for elemento in lista2:
    print(elemento)

# Llenado de listas vacías
list3 = [] # Lista vacía

# Llenar la lista con datos ingresados por el usuario
for i in range(11):
    numero = int(input("Ingresa un número entero: "))
    list3.append(numero) # Agregar el número ingresado a la lista (append agrega un elemento al final de la lista)
    
print("Lista llena:", list3)

print(len(list3)) # Imprime la longitud de la lista

print(sum(list3)) # Imprime la suma de todos los elementos de la lista

list3.reverse() # Invierte el orden de los elementos en la lista
print("Lista invertida:", list3)

list3.sort() # Ordena los elementos de la lista en orden ascendente
print("Lista ordenada:", list3)

