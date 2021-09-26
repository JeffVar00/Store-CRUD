#doblemente enlazada
from producto import producto

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class listaDoble:

    def __init__(self):
        self.primero = None
        self.ultimo = None

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

    def agregarFinal(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux

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
        if self.vacia():
            print("Vacio")
        elif self.primero.siguiente is None:
            self.primero = None
            return
        self.primero = self.primero.siguiente
        self.primero.anterior = None

    def eliminarFinal(self):
        if self.vacia():
            print("Vacio")
        elif self.primero.siguiente is None:
            self.primero = None
            return
        n = self.primero
        while n.siguiente is not None:
            n = n.siguiente
        n.anterior.siguiente = None

    def buscar(self, id):
        aux = self.primero
        while aux:
            if aux.dato.identificacion() == id:
                return aux.dato
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return False

    def eliminar(self, id):
        if self.primero is None:
            print("The list has no element to delete")
            return
        
        if self.primero.siguiente is None:
            if self.primero.dato.identificacion() == id:
                self.primero = None
            else:
                print("dato not found")
            return

        if self.primero.dato.identificacion() == id:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            return

        n = self.primero
        while n.siguiente is not None:
            if n.dato.identificacion() == id:
                break;
            n = n.siguiente
        if n.siguiente is not None:
            n.anterior.siguiente = n.siguiente
            n.siguiente.anterior = n.anterior
        else:
            if n.dato.identificacion() == id:
                n.anterior.siguiente = None
            else:
                print("Element not found")


#https://www.youtube.com/watch?v=c27dIMT9kLE De aqui se obtuvieron la mayoria de metodos, a excepcion de eliminar final, inicio y eliminar por posicion
#https://pharos.sh/lista-doblemente-enlazada-con-ejemplos-de-python/ Metodos eliminar final, inicio y eliminar por posicion