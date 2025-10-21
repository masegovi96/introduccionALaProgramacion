# Programa que pida un número entero positivo y muestre su raiz cuadrada, raiz cúbica
# potencia al cuadrado y potencia al cubo

import math

numero = int(input("Ingrese un número entero positivo: "))

raizCuadrada = math.sqrt(numero)
raizCubica = numero ** (1/3)
potenciaCuadrado = pow(numero, 2) # numero ** 2
potenciaCubica = pow(numero, 3) # numero ** 3

print(f'La raíz cuadrada de {numero} es: {raizCuadrada}.')
print(f'La raíz cúbica de {numero} es: {raizCubica}.')
print(f'La potencia al cuadrado de {numero} es: {potenciaCuadrado}.')
print(f'La potencia al cubo de {numero} es: {potenciaCubica}.')