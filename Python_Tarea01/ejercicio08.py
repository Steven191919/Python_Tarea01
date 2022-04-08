"""Escribe un programa que lea un número
 e indique si es par o impar."""

a = int(input("Ingresa un numero: "))

if a % 2 == 0:
    print(f"{a} es un numero par")
elif a % 3 == 0:
    print(f"{a} es numero impar")
else:
    print("Es primo")
    





