from py2neo import Graph
import pandas as pd
import ManejoBd

manejo=ManejoBd.manejoBd()

driver=manejo.conectar()

query="""
MATCH (n)
OPTIONAL MATCH (n)-[r]->(m)
RETURN n,r,m
"""
result=driver.execute_query(query)

resultado=result.data()

data=[]
for i in resultado:
    nodo=i['n']
    relacion=i['r']
    nodoRelacionado=i['m']
    data.append({
        "nodo":nodo['name'],
        "relacion":relacion['name'],
        'Nodo relacionado':nodoRelacionado['name']
    })

    df=pd.DataFrame(data,columns=['Nodo',"Relacion","Nodo relacionado "])
    df.to_csv("prueba.csv",index=False)
