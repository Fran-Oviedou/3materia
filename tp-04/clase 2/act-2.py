#2. Escribe un programa que muestre los números del 0 al 4 usando un ciclo while. 
#2.1. Escribe un programa que solicita al usuario que ingrese números enteros positivos y muestre la suma de esos números. La entrada de números continuará hasta que el usuario ingrese un número negativo, momento en el que el programa mostrará la suma total.

i = 0
while i < 5:
    print(i)
    i += 1
suma = 0

while True:
    numero = int(input("ingresa un numero: "))
    if numero < 0:
        break
    suma += numero
print("suma total:", suma)