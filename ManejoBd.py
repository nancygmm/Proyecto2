#se importan las librerias a usar

from neo4j import GraphDatabase
import csv
class manejoBd:

    #constructor
    def __init__(self):
        self.driver=self.conectar()
    
    #funcion para conectar con la base de datos local
    def conectar(self):
        driver=GraphDatabase.driver("bolt://localhost:7687",auth=("neo4j","douglasdouglas"))
        return driver
    
    #funcion que recibe los querys y los corre
    def execute_query(self,query):
        with self.driver.session() as session:
            result = session.run(query)
            return list(result)
        
    #funcion que crea un usuario y tambien crea los nodos y relaciones necesarias en la base de datos
    def crearUsuario(self,nombre):
        with self.driver.session() as sesion:
            result=sesion.write_transaction(
                lambda tx: tx.run("CREATE (n:nombre {name: $nombre}) RETURN n", nombre=nombre)
            )
     #funcion que crea un generp y tambien crea los nodos y relaciones necesarias en la base de datos
    def crearGenero(self,genero):
       with self.driver.session() as session:
        result = session.write_transaction(
            lambda tx: tx.run("CREATE (g:Genero {name: $genero}) RETURN g", genero=genero)
        )
     #funcion que crea una pelicula y tambien crea los nodos y relaciones necesarias en la base de datos
    def crearPelicula(self,pelicula):
       with self.driver.session() as session:
        result = session.write_transaction(
            lambda tx: tx.run("CREATE (p:Pelicula {name: $pelicula}) RETURN p", pelicula=pelicula)
        )
    
    #funcion que obtiene las relaciones de las peliculas en la clase de datos
    def obtener_relaciones_pelicula_genero(self):
        driver = self.conectar()
        
        with driver.session() as session:
            query = "MATCH (p:pelicula)-[:PERTENECE]->(g:Genero) RETURN p, collect(g) AS generos"
            result = session.run(query)

            relaciones = {}
            for record in result:
                pelicula = tuple(record["p"].items())
                generos = [dict(g) for g in record["generos"]]
                relaciones[pelicula] = generos

            return relaciones
    def obtenerGeneros(self):
      driver=self.conectar()

      with driver.session() as session:
            # Ejecutar una consulta Cypher para obtener los nodos de tipo pelicula
            query = "MATCH (g:Genero) RETURN g"
            result = session.run(query)

            # Recorrer los resultados y obtener los nodos de tipo pelicula
            generos = []
            for record in result:
                pelicula = record["g"]
                generos.append(pelicula['name'])

            return generos
    def obtenerPeliculas(self):
      driver=self.conectar()

      with driver.session() as session:
            # Ejecutar una consulta Cypher para obtener los nodos de tipo pelicula
            query = "MATCH (p:pelicula) RETURN p"
            result = session.run(query)

            # Recorrer los resultados y obtener los nodos de tipo pelicula
            peliculas = []
            for record in result:
                pelicula = record["p"]
                peliculas.append(pelicula['name'])

            return peliculas

    #obtiene las relaciones de cualquier nodo
    def obtenerRelaciones(self):
       diccionario_relaciones = self.obtener_relaciones_pelicula_genero()
       diccionarioPeliculaGenero={}
       for pelicula, generos in diccionario_relaciones.items():
            dicciAuxi=dict(pelicula)
            peli=dicciAuxi['name']
            listaGeneros=[]
            for i in generos:
                listaGeneros.append(i['name'])
                diccionarioPeliculaGenero[peli]=listaGeneros   
       return diccionarioPeliculaGenero
    

    #funcion para obtener los usuarios
    def obtenerUsuarios(self):
      driver=self.conectar()

      with driver.session() as session:
            # Ejecutar una consulta Cypher para obtener los nodos de tipo usuario
            query = "MATCH (u:Usuario) RETURN u"
            result = session.run(query)

            # Recorrer los resultados y obtener los nodos de tipo usuario
            usuarios = []
            for record in result:
                usuario = record["u"]
                usuarios.append(usuario['name'])
            
            
