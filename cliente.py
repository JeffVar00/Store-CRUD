from pila import pila


class cliente:

    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = pila()

    def toString(self):
        return self.nombre

    def carritoCliente(self):
        return self.carrito

    def definirNombre(self, name):
        self.nombre = name
