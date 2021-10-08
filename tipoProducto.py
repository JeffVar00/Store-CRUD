from pila import pila
from producto import producto

class tipoProducto:

    def __init__(self, ID, nombre, IDseccion):
        self.ID = ID
        self.nombre = nombre
        self.IDseccion = IDseccion
        self.pilaProductos = pila()

    def identificacion(self):
        return (self.ID)

    def toString(self):
        return "ID: " + self.ID + ", Nombre: " + self.nombre

    def agregarPila(self, dato):
        self.pilaProductos.incluir(dato)

    def manejarPila(self):
        return self.pilaProductos

    def productos(self):
        return self.pilaProductos