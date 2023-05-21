#Se crea la clase de persona
class pelicula:
    #Aquí se definen los atributos de esta clase,  los atributos son: nombre, director, actores, generos, saga
    def __init__(self,nombre,director,actores,generos,saga):
        self.nombre=nombre
        self.director=director
        self.actores=actores
        self.generos=generos
        self.saga=saga

    #Get y Set para cada atributo
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre

    def getDirector(self):
        return self.director
    def setDirector(self,director):
        self.director=director

    def getActores(self):
        return self.actores
    def setActores(self,actores):
        self.actores=actores

    def getGeneros(self):
        return self.generos
    def setGeneros(self,generos):
        self.generos=generos

    def getSaga(self):
        return self.saga
    def setSaga(self,saga):
        self.saga=saga