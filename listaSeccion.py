#doblemente enlazada circular
from seccion import seccion

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class listaDobleC:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False

    #metodo agregar falta

    def agregarInicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unirNodos() #las hace circulares

    def agregarFinal(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.__unirNodos() #las hace circulares

    def __unirNodos(self):
        if self.primero != None:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero

    def mostrar(self):
        aux = self.primero
        if self.vacia():
            print("Vacio")
        else:
            while aux:
                print(aux.dato.toString())
                aux = aux.siguiente
                if aux == self.primero:
                    break

    def eliminarInicio(self):
        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
        self.__unirNodos()

    def eliminarFinal(self):
        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
        self.__unirNodos()

    def buscar(self, nombre):
        aux = self.primero
        while aux:
            if aux.dato.nom() == nombre:
                return aux.dato
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return False

    def eliminar(self, x):

        if self.primero is None:
            print("The list has no element to delete")
            return

        if self.primero.siguiente is None:
            if self.primero.dato.nom() == x:
                self.eliminarInicio()
            else:
                print("dato not found")
            return

        if self.primero.dato.nom() == x:
            self.eliminarInicio()
            return

        n = self.primero
        while n.siguiente is not self.primero:
            if n.dato.nom() == x:
                break;
            n = n.siguiente
        if n.siguiente is not self.primero:
            n.anterior.siguiente = n.siguiente
            n.siguiente.anterior = n.anterior
        else:
            if n.dato.nom() == x:
                self.eliminarFinal()
            else:
                print("Element not found")

#https://www.youtube.com/watch?v=c27dIMT9kLE De aqui se obtuvieron la mayoria de metodos, a excepcion de eliminar por posicion
#https://pharos.sh/lista-doblemente-enlazada-con-ejemplos-de-python/ Metodo eliminar por posicion