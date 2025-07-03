#Escribe un programa que recorra una lista de números y muestre si cada número es par o impar.


numeros = [3, 8, 5, 10, 1]
for num in numeros:
    if num % 2 == 0:
        print(num, "es par")
    else:
        print(num, "es impar")