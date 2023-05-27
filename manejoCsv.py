#importar la libreria a usar

import csv


#funcion que abre, lee, recorre y guarda los datos de un csv en una lista
def abrirSeparar():
    archivo=open("archivo.csv",'r',encoding='UTF-8')
    leer=csv.reader(archivo)
    l=[]
    for i in leer:
        l.append(i)
    listaPeliculas=[]
    listaPuntajes=[]
    for i in l:
        listaPeliculas.append(i[0])
        listaPuntajes.append(int(i[1]))
    print(listaPeliculas)
    print(listaPuntajes)
    return listaPeliculas,listaPuntajes
