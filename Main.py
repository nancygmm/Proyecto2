import os

class Main: 
    
    def menu():
        """
        Función que limpia la pantalla y muestra nuevamente el menu
        """
        os.system('clear') # NOTA para windows tienes que cambiar clear por cls
        print ("Bienvenido")
        print ("\t1 -> primera opción")
        print ("\t2 -> segunda opción")
        print ("\t3 -> tercera opción")
        print ("\t4 -> salir")
    
    
    while True:
        # Mostramos el menu
        menu()
    
        # solicituamos una opción al usuario
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