#Escribe un programa que muestra la primer, última u otra letra de una cadena de carcateres, inclusive una rebanada

texto = input("ingresa una palabra: ")
print("primera letra:", texto[0])
print("ultima letra:", texto[-1])
print("rebanada (2 a 5):", texto[2:6])