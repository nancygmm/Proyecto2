from neo4j import GraphDatabase
class manejoBd:
    def __init__(self):
        self.conectar()
    def conectar(self):
        driver=GraphDatabase.driver("bolt://localhost:7687",auth=("neo4j","douglasdouglas"))
        def execute_query(query):
            with driver.session() as session:
                result = session.run(query)
                return list(result)

# Ejemplo de consulta
        query = "MATCH (n) RETURN n"
        result = execute_query(query)

        for i in result:
            nodo=i["n"]
            print(nodo)
            print(nodo["name"])


        driver.close()
app=manejoBd()
