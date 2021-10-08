from listaProducto import listaDoble

class seccion:

    def __init__(self, ID = None, nombre=None, numero=None, IDseccion = None):
        self.ID = ID
        self.nombre = nombre
        self.numero = numero
        self.IDseccion = IDseccion
        self.productos = listaDoble()

    def nom(self):
        return self.nombre

    def num(self):
        return self.numero

    def id(self):
        return self.ID

    def idpropio(self):
        return self.IDseccion

    def actualizar(self, nombre, num):
        self.nombre = nombre
        self.numero = num

    def mostrarProductos(self):
        self.productos.mostrar()

    def manejarProductos(self):
        return self.productos

    def toString(self):
        return "# Pasillo: {}".format(self.numero) + ", " + self.nombre

    def agregarProducto(self, dato):
        self.productos.agregarInicio(dato)