"""Realiza un programa que reciba una cantidad de minutos y 
muestre por pantalla a cuantas horas y minutos corresponde."""

a = int(input("ingresa minutos: "))
b = a // 60
c = a % 60
print(f"El resultado es: {b} horas con {c} minutos")
