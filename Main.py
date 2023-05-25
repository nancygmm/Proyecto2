import os
import usuarios
import cuentas
import ManejoBd
from neo4j import GraphDatabase

class Main: 
    
    def __init__(self):
        self.menu()
        self.banderaPrimeraVez=False
    def menu(self):
        os.system("clear")
        print("############################       BIENVENIDO A UVG-FLIX          ########################")
        print("1. Iniciar sesion")
        print("2. Crear cuenta")

        BD = ManejoBd.manejoBd()

        contraseñas = []
        
        seleccion=input("--> ")
        if seleccion=="1":

            usuario = BD.obtenerUsuarios()
            nombre=input("Ingresa el nombre del usuario ")
            passw=input("Ingresa el password ")
            
            if nombre in usuario:
                print("Bienvenido a UVG-FLIX")
            else:
                print("La cuenta no existe, es necesario crear una ")
            
            for i in contraseñas:
                if passw != contraseñas[i]:
                    print("Contraseña incorrecta, intente de nuevo")
                else:
                    print("Bienvenido")

        elif seleccion=="2":
            nombre=input("Ingresa el nombre del nuevo usuario: ")
            passwN=input("Ingresa la nueva contraseña: ")
            BD.crearUsuario(self,nombre)
            contraseñas.append(passwN)
            
                

        else:
            print("Ingresa un valor correcto ")
            
Main()
    
    