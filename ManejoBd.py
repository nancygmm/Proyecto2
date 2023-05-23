from neo4j import GraphDatabase
class manejoBd:
    def __init__(self):
        self.driver=self.conectar()
    def conectar(self):
        driver=GraphDatabase.driver("bolt://localhost:7687",auth=("neo4j","douglasdouglas"))
        return driver
    def execute_query(self,query):
        with self.driver.session() as session:
            result = session.run(query)
            return list(result)
    def crearUsuario(self,nombre):
        with self.driver.session() as sesion:
            result=sesion.write_transaction(
                lambda tx: tx.run("CREATE (n:nombre {name: $nombre}) RETURN n", nombre=nombre)
            )
    def crearGenero(self,genero):
       with self.driver.session() as session:
        result = session.write_transaction(
            lambda tx: tx.run("CREATE (g:Genero {name: $genero}) RETURN g", genero=genero)
        )
    def crearPelicula(self,pelicula):
       with self.driver.session() as session:
        result = session.write_transaction(
            lambda tx: tx.run("CREATE (p:Pelicula {name: $pelicula}) RETURN p", pelicula=pelicula)
        )
            




