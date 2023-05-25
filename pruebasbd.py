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






def creacionMatriz(lista):
    l=[]
    for i in range(len(lista)):
        f=[]
        for j in range(len(xxx)):
            f.append(0)
        l.append(f)
    print(l)
matriz=creacionMatriz(listaMeGusta)

