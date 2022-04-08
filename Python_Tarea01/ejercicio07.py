"""Realiza un programa que pida dos números a y b 
e indique si su suma es positiva, negativa o cero."""

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c= a+b
if c > 0:
    print(f"{c}  La suma es postiva")
elif c < 0:
    print(f"{c}  La suma es negativa ")
else:
    print(f"{c}  La suma es cero")






