class cuentas:
    def __init__(self, correo, contraseña, telefono, tipo): #creación del constructor de la clase con sus variables
        self.correo = correo
        self.contraseña = contraseña
        self.telefono = telefono
        self.tipo = tipo
    
    #gets y sets de cada variable
    
    def getCorreo (self):
        return self.correo
    
    def setCorreo (self,correo):
        self.correo = correo
    
    def getContraseña (self):
        return self.contraseña
    
    def setContraseña (self,contraseña):
        self.contraseña = contraseña

    def getTelefono (self):
        return self.telefono
    
    def setTelefono (self,telefono):
        self.telefono = telefono
    
    def getTipo (self):
        return self.tipo
    
    def setTipo (self,tipo):
        self.tipo = tipo
    

