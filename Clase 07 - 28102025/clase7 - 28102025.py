# Ejercicio 3: Haz un programa en Python que pida un número entero y muestre cuántos números pares hay desde 1 hasta ese número (incluyéndolo si es par)

# conteo_pares = 0
# #Solicitar al usuario que ingrese un número entero
# numero = int(input("Ingrese un número entero: "))

# for i in range(1, numero + 1):
#     if i % 2 == 0:
#         conteo_pares += 1
#     print(i)

# print(f"Hay {conteo_pares} números pares desde 1 hasta {numero}.")

#Ejercicio 4: Haz un programa en Python que pida un número y calcule el factorial de ese número utilizando un ciclo for.

# numero = int(input("Ingrese un número para calcular su factorial: "))
# factorial = 1
# for i in range(1, numero + 1):
#     factorial *= i
# print(f"El factorial de {numero} es {factorial}.")

# Bucle While
# while condicion:
#     bloque de código

#Ejercicio 1: Haz un programa que pida al usuario ingresar una contraseña hasta que ingrese la correcta, y que tenga máximo 5 intentos.

# Definir la contraseña correcta  
# contrasena_correcta = "Credinalga"
# intentos = 0
# max_intentos = 5
# contrasena = input("Ingrese la contraseña: ")

# while (intentos < max_intentos) and (contrasena != contrasena_correcta):
#     print("Contraseña incorrecta. Intente de nuevo.")
#     intentos += 1
#     contrasena = input("Ingrese la contraseña: ")

# if intentos == max_intentos:
#     print("Has excedido el número máximo de intentos. Acceso denegado.")
# else:
#     print(f"Contraseña correcta. Acceso concedido. Intentos realizados {intentos}.")
    
#Ejercicio 2: Haz un programa que pida al usuario ingresar números positivos y que se detenga hasta que ingrese un número negativo.

# numero = float(input("Ingrese un número positivo (o un número negativo para salir): "))

# while numero >= 0:
#     numero = float(input("Ingrese un número positivo (o un número negativo para salir): "))
    
# print("Número negativo ingresado. Programa terminado.")

# Ejercicio 3: Haz un programa que sume todos los números que ingrese el usuario hasta que ingrese un 0.
suma = 0
numero = float(input("Ingrese un número para sumar (o 0 para salir):  "))

while numero != 0:
    suma += numero
    numero = float(input("Ingrese un número para sumar (o 0 para salir):  "))
    
print(f"La suma total de los números ingresados es: {suma}.")