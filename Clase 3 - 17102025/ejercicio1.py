# Ejercicio 1: Haz un programa que solicite al usuario ingresar 5 calificaciones y calcula el promedio

# Solicitar al usuario ingresar las 5 calificaciones
calificacion1 = float(input("Ingresa la calificación 1: "))
calificacion2 = float(input("Ingresa la calificación 2: "))
calificacion3 = float(input("Ingresa la calificación 3: "))
calificacion4 = float(input("Ingresa la calificación 4: "))
calificacion5 = float(input("Ingresa la calificación 5: "))

# Calcular el promedio
promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5) / 5

# Mostrar el promedio
print(f"El promedio de calificaciones es: {promedio}")
