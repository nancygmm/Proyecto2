import os
import usuarios
import cuentas
from neo4j import GraphDatabase

class Main: 
    
    def menu():
        
        os.system('clear')
        print ("Bienvenido a teleflix")
        print("¿Ya tienes una cuenta?")
        print ("\t1 -> Si :) ")
        print ("\t2 -> No :( ")
        print ("\t4 -> salir")
    
    while True:
        menu()
        opcionMenu = input("Elige una opción ")
        if opcionMenu=="1":
            print ("Por favor ingrese sus credenciales")
            cuentaE = cuentas(correo,contraseña,telefono,tipo)
            correo = input("Por favor ingrese su correo electrónico ->   ")
            contraseña = input("Por favor ingrese su contraseña ->   ")
            telefono = input("Por favor ingrese su número de teléfono ->   ")
            tipo = input("Por favor ingrese el tipo ->   ")
            
        elif opcionMenu=="2":
            print ("")
            input("Has pulsado la opción 2")
        elif opcionMenu=="4":
            break
        else:
            print ("")
            input("Opción no válida")
    
    