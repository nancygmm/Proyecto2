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


app=manejoBd()
