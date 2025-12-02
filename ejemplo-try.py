numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

try:
    division = numero1 / numero2
    print(f"El resultado de la división es: {division}")
except ValueError:
    print("Error. Debe ingresar un número entero")
except ZeroDivisionError:
    print("Error. No se puede dividir entre cero")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")