#4 - Crear una lista de frutas y mostrar en consola algunas frutas de la lista, también por rebanadas.
#5 - 5. Escribe un programa que recorra una lista de frutas y muestre cada fruta.
#5.1 Agregar otras frutas a la lista.
#5.2 Escribe un programa verifique si una fruta específica está en una lista de frutas y muestra un mensaje correspondiente.


# lista inicial
frutas = ["manzana", "banana", "pera", "uva", "kiwi"]

# mostrar algunas frutas por rebanada
print("algunas frutas (del indice 1 al 3):", frutas[1:4])  # banana, pera, uva

# recorrer la lista
print("\nlista completa de frutas:")
for fruta in frutas:
    print("-", fruta)

# agregar mas frutas
frutas.append("melon")
frutas += ["mango", "frutilla"]

print("\nlista actualizada:")
for fruta in frutas:
    print("-", fruta)

# verificar si una fruta esta en la lista
buscar = input("\ningresa una fruta para buscar: ").lower()
if buscar in frutas:
    print("la fruta esta en la lista.")
else:
    print("la fruta no esta en la lista.")