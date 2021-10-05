# doblemente enlazada circular
from nodo import Nodo


class listaDobleC:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cantidad = 0

    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False

    def agregarInicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unirNodos() #las hace circulares
        self.cantidad += 1

    def agregarFinal(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.__unirNodos() #las hace circulares
        self.cantidad += 1

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
        self.cantidad -= 1

    def eliminarFinal(self):
        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
        self.__unirNodos()
        self.cantidad -= 1

    def buscar(self, numero):

        if self.vacia() is True:
            return False

        aux = self.primero
        while aux:
            if aux.MostrarNumero() == numero:
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
            if self.primero.dato.num() == x:
                self.eliminarInicio()
            else:
                print("dato not found")
            return

        if self.primero.dato.num() == x:
            self.eliminarInicio()
            return

        n = self.primero
        while n.siguiente is not self.primero:
            if n.dato.num() == x:
                break
            n = n.siguiente
        if n.siguiente is not self.primero:
            n.anterior.siguiente = n.siguiente
            n.siguiente.anterior = n.anterior
        else:
            if n.dato.num() == x:
                self.eliminarFinal()
            else:
                print("Element not found")

    def ReturnCantidad(self):
        return self.cantidad

# https://www.youtube.com/watch?v=c27dIMT9kLE De aqui se obtuvieron la mayoria de metodos, a excepcion de eliminar por posicion
# https://pharos.sh/lista-doblemente-enlazada-con-ejemplos-de-python/ Metodo eliminar por posicion