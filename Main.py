import os

class Main: 
    
    def menu():
        """
        Función que limpia la pantalla y muestra nuevamente el menu
        """
        os.system('clear')
        print ("Bienvenido")
        print ("\t1 -> primera opción")
        print ("\t2 -> segunda opción")
        print ("\t3 -> tercera opción")
        print ("\t4 -> salir")
    
    
    while True:
        menu()

        opcionMenu = input("Elige una opción ")
        if opcionMenu=="1":
            print ("")
            input("opción 1")
        elif opcionMenu=="2":
            print ("")
            input("Has pulsado la opción 2")
        elif opcionMenu=="3":
            print ("")
            input("Has pulsado la opción 3")
        elif opcionMenu=="4":
            break
        else:
            print ("")
            input("Opción no válida")