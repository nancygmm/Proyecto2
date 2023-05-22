import os
import usuarios
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
            input("opción 1")
        elif opcionMenu=="2":
            print ("")
            input("Has pulsado la opción 2")
        elif opcionMenu=="4":
            break
        else:
            print ("")
            input("Opción no válida")
    
    