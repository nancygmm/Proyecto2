from neo4j import GraphDatabase
import csv
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
    def exportarCSV(self):
       with self.driver.session() as session:
        # Consulta para obtener todos los nodos y relaciones
        consulta = '''
        
        MATCH (p)-[PERTENECE]->(g) "
                "WHERE ID(p) = $nodo_id_1 AND ID(g) = $nodo_id_2 "
                "RETURN p,PERTENECE, g
           '''

        # Ejecutar la consulta
        resultados = session.run(consulta)

        with open("archivo.csv", 'w', newline='') as archivo:
            writer = csv.writer(archivo)

            # Escribir encabezados de columnas
            writer.writerow(['Tipo', 'Propiedades'])

            # Escribir nodos y propiedades
            for registro in resultados:
                nodo = registro['g']
                tipo = list(nodo.labels)[0]  # Obtener el tipo del nodo
                propiedades = dict(nodo)  # Obtener las propiedades del nodo
                writer.writerow([tipo, propiedades])

                # Escribir relaciones y propiedades
                #for relacion in registro['p']:
                #    tipo_relacion = relacion.type
                #    propiedades_relacion = dict(relacion)
                #    writer.writerow([tipo_relacion, propiedades_relacion])

    print("Exportación a CSV completada.")
app=manejoBd()
app.exportarCSV()
       
            




