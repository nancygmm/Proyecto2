import csv



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
