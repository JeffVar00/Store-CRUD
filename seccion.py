from listaSeccion import listaDobleC

class seccion:

    def __init__(self, nombre=None, numero=None):
        self.nombre = nombre
        self.numero = numero
        self.productos = listaDobleC()

    def nom(self):
        return self.nombre

    def num(self):
        return self.numero

    def toString(self):
        return self.nombre + self.numero

    def agregarProducto(self, dato):
        self.productos.agregarInicio(dato)