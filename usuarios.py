class usuarios:
    def __init__(self,nombre,apellido,edad,cuenta):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.cuenta=cuenta
        self.listaGustos=[]
        self.playList=[]
    # GETS
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getEdad(self):
        return self.edad
    def getCuenta(self):
        return self.cuenta
    def getListaGustos(self):
        return self.listaGustos
    def getPlayList(self):
        return self.playList
    # SETS
    def setNombre(self,nombre):
        self.nombre=nombre
    def setApellido(self,apellido):
        self.apellido=apellido
    def setEdad(self,edad):
        self.edad=edad
    def setCuenta(self,cuenta):
        self.cuenta=cuenta
    def SetListaGustos(self,listaGustos):
        self.listaGustos=listaGustos
    # METODOS 
    def agregarPlayList(self,pelicula):
        self.playList.append(pelicula)
    def quitarPlayList(self,pelicula):
        self.playList.remove(pelicula)
    


