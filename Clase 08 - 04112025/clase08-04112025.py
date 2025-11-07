nombre = "Mario Alonso Segovia Gutierrez"
cadena2 = "hola a todos mi nombre es mario alonso segovia gutierrez"
cadena3 = "          Hola mundo          "
cadena4 = "Esto es una cadena"
cadena5 = "Esto es otra cadena"

print(len(nombre)) # Imprime la longitud de la cadena

print(nombre.upper()) # Convierte la cadena a mayúsculas

print(nombre.lower()) # Convierte la cadena a minúsculas

print(cadena2.capitalize()) # Convierte el primer carácter a mayúscula y el resto a minúsculas

print(cadena2.title()) # Convierte la primera letra de cada palabra a mayúscula

print(cadena3)
print(cadena3.strip()) # Elimina los espacios en blanco al inicio y al final de la cadena

cadenaNueva = cadena4 + " " + cadena5
print(cadenaNueva) # Concatenación de cadenas

cadenaMultiplicada = cadena4 * 5
print(cadenaMultiplicada) # Multiplicación de cadenas

print(cadena4.replace("a", "s")) # Reemplaza todas las apariciones de "a" por "s"

cadena6 = "Hola, ¿cómo estás? ¿Estás bien?"
indice = cadena6.find("¿") # Busca la posición de la primera aparición de "¿"
print(indice) # Imprime la posición de la primera aparición de "¿"

indiceUltimo = cadena6.rfind("¿") # Busca la posición de la última aparición de "¿"
print(indiceUltimo) # Imprime la posición de la última aparición de "¿"

cadena7 = "anita lava la tina"
conteo = cadena7.count("a") # Cuenta cuántas veces aparece "a" en la cadena
print(conteo) # Imprime el conteo de "a"

print(cadena7.startswith("anita")) # Verifica si la cadena comienza con "anita"
print(cadena7.endswith("tina")) # Verifica si la cadena termina con "tina"

# Sintaxis de Slicing cadena[inicio:fin:paso]

cadena8 = "Hola a todos"
print(cadena8[0:4]) # Imprime "Hola"
print(cadena8[:4]) # Imprime "Hola"
print(cadena8[4:9]) # Imprime " a to"
print(cadena8[5:]) # Imprime "a todos"
print(cadena8[-2:]) # Imprime "os"
print(cadena8[::2]) # Imprime "Hl atds"
print(cadena8[::-1]) # Imprime la cadena al revés "sodot a aloH"

#Ejercicio 1: Pide una frase y muestra la misma frase sin espacios al inicio y al final con todas las letras en minúscula
frase = input("Escribe una frase: ")
fraseLimpia = frase.strip().lower()
print(fraseLimpia)

#Ejercicio 2: Pide una palabra y comprueba si es un palíndromo
palabra = input("Escribe una palabra: ")
palabra_invertida = palabra[::-1]
if palabra.lower() == palabra_invertida.lower():
    print("La palabra es un palíndromo")
else:
    print("La palabra no es un palíndromo")