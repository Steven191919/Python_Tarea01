"""Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces,
 con espacios intermedios."""

a = input("ingresa una palabra: ")
b = "\n"
for i in range(1001):
    print(i,a,b)
