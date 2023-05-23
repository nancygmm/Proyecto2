import ManejoBd

manejo=ManejoBd.manejoBd()


#query = "MATCH (n) RETURN n"
#query="Gaby"
#manejo.crearUsuario(query)

genero="Titanes del pacifica "
manejo.crearPelicula(genero)
#for i in result:
#    nodo=i["n"]
#    print(nodo)
#    print(nodo["name"])
