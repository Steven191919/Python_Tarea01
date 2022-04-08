"""Crea una aplicación que permita adivinar un número. 
En primer lugar la aplicación solicita un número entero por teclado. 
A continuación va pidiendo números y va respondiendo 
si el número a adivinar es mayor o menor que el introducido.
El programa termina cuando se acierta el número."""


a = "ADIVINA EL NUMERO"
print(a) 
num = int(input("Ingresa un numero entero: "))

while num > 5:
    num = int(input("El numero es menor.Intentalo de nuevo: "))

while num < 5:
    num = int(input("El numero es mayor.Intentalo de nuevo: "))
        
else:
    print("¡¡¡ACERTASTE!!!")






    
    

   
    
 

