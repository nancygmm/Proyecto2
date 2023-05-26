import ManejoBd
import random
manejo=ManejoBd.manejoBd()
dicc=manejo.obtenerRelaciones()
diccionarioGeneros1={}
diccionarioGeneros2={}
diccionarioGeneros3={}
xxx=manejo.obtenerGeneros()
for i in xxx:
    diccionarioGeneros1[i]=0
    diccionarioGeneros2[i]=0
    diccionarioGeneros3[i]=0





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



def resultante (lista):
    matrizF = []
    matriz = puntaje10(peliculasGeneros, listaMeGusta)
    lista = [0.3, 0.4, 0.2, 0.7, 0.6, 0.1, 0.9, 0.3, 0.7, 0.5, 0.4, 0.8, 0.3, 0.2]

    for decimal in lista:
        resp = []
        for columna in range(len(matriz[0])):
            respC = []
            for fila in range(len(matriz)):
                respC.append(decimal*matriz[fila][columna])
            resp.append(respC)
        matrizF.append(resp)
    return matrizF











    

    
    

