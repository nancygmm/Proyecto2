import ManejoBd
import numpy as np
import random
import manejoCsv
manejo=ManejoBd.manejoBd()
dicc=manejo.obtenerRelaciones()
diccionarioGeneros1={}







pelis=list(dicc.keys())
listaMeGusta=manejoCsv.abrirSeparar()[0]
listaPuntajes=manejoCsv.abrirSeparar()[1]
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
        dic[i]=0.0
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

def multiplicarPuntaje(puntajes):
    matrizAusar=puntaje10(peliculasGeneros,listaMeGusta)
    for i in range(len(puntajes)):
        for j in range(len(matrizAusar[0])):
            x=matrizAusar[i][j]
            matrizAusar[i][j]=puntajes[i]*x
    return matrizAusar

matrizValores=multiplicarPuntaje(listaPuntajes)


def calcularPob(matriz):
    lista=[]
    for i in range(len(matriz[0])):
        suma=0
        suma=matriz[0][i]+matriz[1][i]+matriz[2][i]
        lista.append(round(suma/15,2))
        
    return lista

l=calcularPob(matrizValores)


def resultante (lista):
    xxx=manejo.obtenerPeliculas()
    p1=xxx[random.randint(0,len(xxx)-1)]
    p2=xxx[random.randint(0,len(xxx)-1)]
    p3=xxx[random.randint(0,len(xxx)-1)]
    listaP=[p1,p2,p3]

    matriz = puntaje10(peliculasGeneros, xxx)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            val=matriz[i][j]
            matriz[i][j]=lista[j]*val


    return matriz,xxx


r=resultante(l)[0]


listaOpciones=resultante(l)[1]

def sumaFila(matriz):
    listaSumas=[]
    for i in matriz:
        listaSumas.append(sum(i))
    return listaSumas
t=sumaFila(r)
print(t)
print(listaOpciones)


print("\n#######################  RESULTADO  #######################")
pos=t.index(max(t))
print(f"La pelicula que te recomendamos ver es: {listaOpciones[pos]}")

def mandarFront(lista,posicion):
    posicionNueva=0
    if (len(lista)-1)==posicion:
        posicionNueva=0
    else:
        posicionNueva=posicion+1
    return posicionNueva
    



