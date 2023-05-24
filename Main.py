import os
import usuarios
import cuentas
from neo4j import GraphDatabase

class Main: 
    
    def __init__(self):
        self.menu()
        self.banderaPrimeraVez=False
    def index(self):
        pass
    def menu(self):
        os.system("clear")
        print("############################       BIENVENIDO A UVG-FLIX          ########################")
        print("1. Ya tienes cuenta :D ")
        print("2. No tienes cuenta D: ")

        #PRUEBA
        lista=["prueba1@gmail.com","prueba2@gmail.com","prueba3@gmail.com","prueba4@gmail.com"]##<--Tiene que traerlo de la base de datos 
        seleccion=input("--> ")
        if seleccion=="1":
            correo=input("Ingresa el correo ")
            passw=input("Ingresa el password ")
            if correo in lista:
                print("Si existe ")
            else:
                print("La cuenta no existe, es necesario crear una ")

        elif seleccion=="2":
            nombre=input("Ingresa tu nombre ")
            apellido=input("Ingresa tu apellido ")
            edad=input("Ingresa tu edad ")
            tipo=""
            if int(edad)>=15 and int(edad)<=18:
                tipo="b"
            elif int(edad)>=18:
                tipo="a"
            else:
                tipo="c"
            
                

        else:
            print("Ingresa un valor correcto ")
Main()
    
    