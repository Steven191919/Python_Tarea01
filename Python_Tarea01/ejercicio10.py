"""Escribe un programa que pida un nombre de usuario y una contraseña 
y si se ha introducido “pepe” y “passwd#” 
se indica “Has entrado al sistema”, sino se da un error."""

Nombredeusuario= input("Ingresa nombre de usuario: ")
Contraseña = input("Ingresa la contraseña: ")

if Nombredeusuario == "pepe" and Contraseña == "passwd#":
    print("Has entrado al sistema")
else:
    print("Error")

