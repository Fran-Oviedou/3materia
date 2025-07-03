#crear un programa que le pida al usuario nombre, edad y ciudad de residencia, realizar cálculos basados en la edad, y luego mostrará la información en pantalla (# Pedir al usuario que ingrese su nombre # Pedir al usuario que ingrese su edad # Pedir al usuario que ingrese su ciudad de residencia # Calcular el año de nacimiento # Saludar al usuario y mostrar la información # Comprobar si la edad es mayor de 18 años # Comprobar si la edad es un múltiplo de 5).

nombre = input("Nombre: ")
edad = int(input("Edad: "))
ciudad = input("Ciudad: ")

año_actual = 2025
año_nacimiento = año_actual - edad

print(f"\nHola {nombre}, vivis en {ciudad} y naciste en {año_nacimiento}.")

if edad > 18:
    print("sos mayor de edad.")
else:
    print("sso menor de edad.")

if edad % 5 == 0:
    print("tu edad es mnultiplo de 5.")
else:
    print("tu edad NO es multiplo de 5.")
