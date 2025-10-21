# Hacer un programa que pida horas, minutos y segundos y los convierta a segundos

# Solicitar al usuario ingresar horas, minutos y segundos
horas = int(input("Ingresa las horas: "))
minutos = int(input("Ingresa los minutos: "))
segundos = int(input("Ingresa los segundos: "))

# Convertir todo a segundos
conversionASegundos = (horas * 3600) + (minutos * 60) + segundos

# Mostrar el resultado
print(f"El total en segundos de {horas} horas, {minutos} minutos y {segundos} segundos es: {conversionASegundos} segundos")