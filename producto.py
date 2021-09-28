from pila import pila
from tipoProducto import tipoProducto


class producto:

    def __init__(self, ID, nombre):
        self.ID = ID
        self.nombre = nombre
        self.pilaProductos = pila()

    def identificacion(self):
        return (self.ID)

    def toString(self):
        return self.ID + self.nombre

    def agregarPila(self, dato):
        self.pilaProductos.incluir(dato)
