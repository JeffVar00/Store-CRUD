from listaProducto import listaDoble

class seccion:

    def __init__(self, nombre=None, numero=None):
        self.nombre = nombre
        self.numero = numero
        self.productos = listaDoble()

    def nom(self):
        return self.nombre

    def num(self):
        return self.numero

    def mostrarProductos(self):
        self.productos.mostrar()

    def manejarProductos(self):
        return self.productos

    def toString(self):
        return "# Pasillo: {}".format(self.numero) + ", " + self.nombre

    def agregarProducto(self, dato):
        self.productos.agregarInicio(dato)