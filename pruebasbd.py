import ManejoBd

manejo=ManejoBd.manejoBd()


query = "MATCH (n) RETURN n"
result = manejo.execute_query(query)
for i in result:
    nodo=i["n"]
    print(nodo)
    print(nodo["name"])
