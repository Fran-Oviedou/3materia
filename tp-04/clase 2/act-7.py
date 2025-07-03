#Escribe un programa que recorra una cadena de  texto y cuente cuántas veces aparece la letra 'a' en la cadena.

cadena = input("ingresa un texto: ").lower()
contador = cadena.count("a")
print("la letra 'a' aparece", contador, "veces")