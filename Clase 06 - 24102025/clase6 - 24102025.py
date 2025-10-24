# for variable in iterable:
#     bloque de código


# funcion range(inicio, fin, paso)

# Ejemplo usando range, se imprimirán todos los pares del 0 al 10
for i in range(0, 11, 2):
    print(i)
    
# Ejercicio 1: Haz un programa que muestro los números del 1 al 20
print("Números del 1 al 20:")
for numero in range(1, 21):
    print(numero)

print("---------------------")

# Ejercicio 2: Haz un programa que muestre la tabla de multiplicar de un número dado por el usuario (del 1 al 10)
numero_usuario = int(input("Introduce un número: "))
print(f"Tabla de multiplicar del {numero_usuario}: ")
for i in range(1, 11):
    resultado = numero_usuario * i
    print(f'{numero_usuario} x {i} = {resultado}')