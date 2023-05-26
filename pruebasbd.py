import ManejoBd
import numpy as np
import random
manejo=ManejoBd.manejoBd()
dicc=manejo.obtenerRelaciones()
diccionarioGeneros1={}







pelis=list(dicc.keys())

listaMeGusta=[]

contador=0
while contador<3:
    ra=random.randint(0,len(pelis)-1)
    print(f"Te gusta la pelicula {pelis[ra]}? ")
    seleccion=input("--> ")
    if seleccion=="si":
        listaMeGusta.append(pelis[ra])
        contador+=1
print(listaMeGusta)









def obtenerGeneroPelicula():
    diccionarioGenero={}
    rel=manejo.obtener_relaciones_pelicula_genero()
    for i in rel:
        laux=[]
        for j in rel[i]:
            laux.append(j['name'])
        diccionarioGenero[i[0][1]]=laux
    return diccionarioGenero
peliculasGeneros=obtenerGeneroPelicula()

def diccionarioInicialGeneros():
    xxx=manejo.obtenerGeneros()
    dic={}
    for i in xxx:
        dic[i]=0
    return dic

def puntaje10(diccionario,listaLiked):
    diccionarioMeGusta={}
    matriz=[]
    for i in listaLiked:
        diccionarioMeGusta[i]=diccionario[i]
        d=diccionarioInicialGeneros()
        for j in diccionarioMeGusta[i]:
            d[j]=1
        matriz.append(list(d.values()))
    return matriz
puntajes=[3,4,5]
def multiplicarPuntaje(puntajes):
    matrizAusar=puntaje10(peliculasGeneros,listaMeGusta)
    for i in range(len(puntajes)):
        for j in range(len(matrizAusar[0])):
            x=matrizAusar[i][j]
            matrizAusar[i][j]=puntajes[i]*x
    return matrizAusar

matrizValores=multiplicarPuntaje(puntajes)


def calcularPob(matriz):
    lista=[]
    for i in range(len(matriz[0])):
        suma=0
        suma=matriz[0][i]+matriz[1][i]+matriz[2][i]
        lista.append(round(suma/15,2))
    return lista

l=calcularPob(matrizValores)


def resultante (lista):
    matriz = puntaje10(peliculasGeneros, listaMeGusta)
    #lista = [0.3, 0.4, 0.2, 0.7, 0.6, 0.1, 0.9, 0.3, 0.7, 0.5, 0.4, 0.8, 0.3, 0.2]

    resp = np.zeros_like(matriz, dtype=float)

    for i in range(len(lista)):
        resp[:, i] = matriz[: i ] * lista[i]

    return resp




print(resultante(l))



    

