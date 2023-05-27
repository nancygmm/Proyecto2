# Importación de librerias a usar y objetos de otras clases 
import ManejoBd
import numpy as np
import random
import manejoCsv
manejo=ManejoBd.manejoBd()
dicc=manejo.obtenerRelaciones()
diccionarioGeneros1={}






#creación de variables
pelis=list(dicc.keys())
listaMeGusta=manejoCsv.abrirSeparar()[0]
listaPuntajes=manejoCsv.abrirSeparar()[1]

#funcion que ontiene los generos de las peliculas
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

#funcion que retorna un diccionario con los generos
def diccionarioInicialGeneros():
    xxx=manejo.obtenerGeneros()
    dic={}
    for i in xxx:
        dic[i]=0.0
    return dic

#funcion que retorna una matriz de 1 y 0 dependiendo de los generos de las peliculas seleccionadas
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

#retorna la matriz multiplicada con los puntajes del usuario
def multiplicarPuntaje(puntajes):
    matrizAusar=puntaje10(peliculasGeneros,listaMeGusta)
    for i in range(len(puntajes)):
        for j in range(len(matrizAusar[0])):
            x=matrizAusar[i][j]
            matrizAusar[i][j]=puntajes[i]*x
    return matrizAusar

matrizValores=multiplicarPuntaje(listaPuntajes)

#funcion que suma los valores de las columnas y los convierte en valores entre 0 y 1 y retorna una lista con esos valores
def calcularPob(matriz):
    lista=[]
    for i in range(len(matriz[0])):
        suma=0
        suma=matriz[0][i]+matriz[1][i]+matriz[2][i]
        lista.append(round(suma/15,2))
        
    return lista

l=calcularPob(matrizValores)

#multiplica los valores de la lista previa con cada columna de la matriz de las posibles recomendaciones
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

#se muestran los resultados de la multiplicacion
r=resultante(l)[0]

#se muestran las posibles recomendaciones
listaOpciones=resultante(l)[1]

#funcion que suma la fila para obtener los puntajes finales de cada posible recomendacion 
def sumaFila(matriz):
    listaSumas=[]
    for i in matriz:
        listaSumas.append(sum(i))
    return listaSumas
t=sumaFila(r)
print(t)
print(listaOpciones)

#se muestra la recomendacion
print("\n#######################  RESULTADO  #######################")
pos=t.index(max(t))
print(f"La pelicula que te recomendamos ver es: {listaOpciones[pos]}")

#manda al front la posicion de la pelicula recomendada
def mandarFront(lista,posicion):
    posicionNueva=0
    if (len(lista)-1)==posicion:
        posicionNueva=0
    else:
        posicionNueva=posicion+1
    return posicionNueva
    



