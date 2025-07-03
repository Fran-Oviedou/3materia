# Integrador: Escribe un programa que permita a un usuario crear una lista de nombres. El programa continuará pidiendo nombres hasta que el usuario ingrese "fin".
# Luego, el programa mostrará la lista de nombres en orden alfabético, indicará cuántos nombres empiezan con la letra 'A' o 'E', y mostrará si un nombre específico está en la lista.

nombres = []

while True:
    nombre = input("ingresa nombres (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    nombres.append(nombre)

nombres.sort()
print("lista ordenada:", nombres)

contador = 0
for n in nombres:
    if n.lower().startswith(("a", "e")):
        contador += 1
print("nombres que comienzan con 'a' o 'e':", contador)

verificar = input("ingresa un nombre para buscar en la lista: ")
if verificar in nombres:
    print(verificar, "esta en la lista.")
else:
    print(verificar, "no esta en la lista.")
