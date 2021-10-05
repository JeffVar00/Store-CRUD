# lista normal en el menu
from listaSeccion import listaDobleC
from seccion import seccion


class sucursal:

    def __init__(self, ID=None, ubicacion=None):
        self.ID = ID
        self.Ubicacion = ubicacion
        self.Secciones = listaDobleC()

    def ubicacion(self):
        return self.Ubicacion

    def myID(self):
        return self.ID

    def mostrar(self):
        self.Secciones.mostrar()

    def seccionesSucursal(self):
        return self.Secciones

    def manejarSeccion(self, nSeccion):
        return self.Secciones.buscar(nSeccion)

    def CantidadSecciones(self):
        return self.Secciones.ReturnCantidad()

    def toString(self):
        return "Sucursal: " + self.Ubicacion + ", ID: " + self.ID
