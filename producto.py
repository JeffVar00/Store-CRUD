from pila import pila
from tipoProducto import tipoProducto

class producto:

    def __init__(self, ID, nombre):
        self.ID = ID
        self.nombre = nombre

    def cargarProductos(self, productos):
        self.productos = productos

    def identificacion(self):
        return (self.ID)

    def toString(self):
        return self.ID + self.nombre + "{}".format(self.precio)