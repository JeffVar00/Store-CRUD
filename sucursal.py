#lista normal en el menu
from listaSeccion import listaDobleC

class sucursal:

    def __init__(self):
        self.ID = None
        self.Ubicacion = None
        self.Secciones = listaDobleC()

    def __init__(self, ID, ubicacion):
        self.ID = ID
        self.Ubicacion = ubicacion
        self.Secciones = listaDobleC()

    def ubicacion(self):
        return self.Ubicacion