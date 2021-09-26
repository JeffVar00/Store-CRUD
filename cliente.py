from pila import pila
from producto import producto

class cliente:

    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = pila()

    def toString(self):
        return self.nombre