#crearemos un programa que verifica si un número ingresado por el usuario es positivo, negativo o cero, y también si es un número par o impar.

numero = int(input("ingresa un numero: "))

if numero > 0:
    print("es positivo")
elif numero < 0:
    print("es negativo")
else:
    print("cero")

if numero % 2 == 0:
    print("par")
else:
    print("impar")