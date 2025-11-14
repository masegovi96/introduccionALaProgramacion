# Funciones en Python

# Definición
def saludar():
    print("¡Hola, bienvenido a la clase de Python!")
    
# Llamada a la función
saludar()
saludar()
saludar()

# Función con parámetros
def saludar_persona(nombre, apellido, edad):
    print(f"¡Hola {nombre} {apellido}, tienes {edad} años!")
    
# Llamada a la función con argumentos
saludar_persona("Mario", "Segovia", 29)
saludar_persona("Jorge", "Ramirez", 39)
saludar_persona("Jorge", "Zuñiga", 29)

# Función con valor de retorno
def sumar(a, b):
    return a + b

print(sumar(3, 5))
resultado = sumar(10,20)
print("El resultado de la suma es:", resultado)
