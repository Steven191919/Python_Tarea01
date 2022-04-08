""" Pedir un número por teclado y mostrar la tabla de multiplicar"""

num = int(input("Ingresa un numero: "))

for i in range(0,13):
    y = num * i 
    print(num, "x", i,"=" ,y)





