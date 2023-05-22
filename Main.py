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
        print ("\t3 -> salir")
    
    while True:
        menu()
        opcionMenu = input("Elige una opción ")
        if opcionMenu=="1":
            print ("Por favor ingrese sus credenciales")
            correo = input("Por favor ingrese su correo electrónico ->   ")
            contraseña = input("Por favor ingrese su contraseña ->   ")
            telefono = input("Por favor ingrese su número de teléfono ->   ")
            tipo = input("Por favor ingrese el tipo ->   ")
            Ncuenta=cuentas(correo, contraseña, telefono, tipo)
            
        elif opcionMenu=="2":
            print ("Ingresa la información que se te solicita")
            
        elif opcionMenu=="4":
            break
        else:
            print ("")
            input("Opción no válida")
    
    