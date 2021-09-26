class seccion:

    def __init__(self):
        self.nombre = None
        self.numero = None
        #self.productos = listaDoble()

    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        #self.productos = listaDoble()

    def nom(self):
        return(self.nombre)

    def toString(self):
        return self.nombre + self.numero