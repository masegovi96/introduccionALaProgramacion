# Sintaxis condicionales

# if condicion:
#     instrucciones si la condicion es verdadera
# elif otra_condicion:
#     instrucciones si la otra condicion es verdadera
# else:
#     instrucciones si ninguna condicion es verdadera

# Ejercicio 1: Programa que pida un número y muestre si es positivo, negativo o cero.
# numero = float(input("Ingrese un número: "))

if numero > 0:
    print("Bloque if ejecutado.")
    print("El número es positivo.")
elif numero < 0:
    print("Bloque elif ejecutado.")
    print("El número es negativo.")
else:
    print("Bloque else ejecutado.")
    print("El número es cero.")
    
print("-------------------------")

# if condicion:
#     if condicion_anidada:
#         instrucciones si la condicion_anidada es verdadera
#     else:
#         instrucciones si la condicion_anidada es falsa

# Ejercicio 2: Programa que pida dos números y muestre cuál es mayor o si son iguales.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 > num2:
    print("El primer número es mayor.")
elif num1 < num2: # num2 > num1
    print("El segundo número es mayor.")
else:
    print("Ambos números son iguales.")
    
print("-------------------------")

# Ejercicio 3: Haz un programa que pida una calificación del 0 al 10 y muestre si está aprobado o reprobado. Toma en cuenta una calificación mayor o igual a 6 como aprobatoria.

nombreAlumno = input("Ingrese el nombre del alumno: ")
calificacion = float(input("Ingrese la calificación del alumno (0 - 10): "))

if calificacion >= 6:
    print(f"El alumno {nombreAlumno} está aprobado.")
else:
    print(f"El alumno {nombreAlumno} está reprobado.")
    
print("-------------------------")

# Ejercicio 4: Haz un programa que pida la edad de una persona y muestre si puede votar (mayor o igual a 18 años) o no

nombre = input("Ingrese el nombre de la persona: ")
edadPersona = int(input("Ingrese su edad: "))

if edadPersona >= 18:
    print(f"{nombre} tiene {edadPersona} años y puede votar.")
else:
    print(f"{nombre} tiene {edadPersona} años y no puede votar.")