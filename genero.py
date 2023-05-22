class Genero:
    #Aquí se definen los atributos de esta clase, los atributos son: nombre y compatibilidad
    def __init__(self, nombre, compatibilidad):
        self._nombre = nombre
        self._compatibilidad = compatibilidad

    #Get y Set para cada atributo   
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_compatibilidad(self):
        return self._compatibilidad
    def set_compatibilidad(self, compatibilidad):
        self._compatibilidad = compatibilidad