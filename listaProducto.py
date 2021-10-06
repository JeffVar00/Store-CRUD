# doblemente enlazada
from nodo import Nodo


class listaDoble:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregarInicio(self, dato):
        # Si la lista esta vacia, primero y ultimo apuntarán al mismo nodo
        if self.primero is None:
            self.primero = self.ultimo = Nodo(dato)
        # En caso contrario, se añadirá un nodo en donde el siguiente de este será el primero y
        # el primero tendra como anterior el nuevo nodo. Por ultimo el nuevo nodo pasa a ser el
        # primero.
        else:
            nuevo_nodo = Nodo(dato)
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo

    def agregarFinal(self, dato):
        # Si la lista esta vacia, primero y ultimo apuntarán al mismo nodo
        if self.primero is None:
            self.primero = self.ultimo = Nodo(dato)
        # En caso contrario, el nuevo nodo pasará a ser el ultimo nodo en la lista y el que era
        # el ultimo nodo, pasará a ser el penultimo.
        else:
            nuevo_nodo = self.ultimo
            self.ultimo = nuevo_nodo.siguiente = Nodo(dato)
            self.ultimo.anterior = nuevo_nodo

    def mostrar(self):
        # Si la lista está vacia se muestra al usuario que esta vacia la lista
        if self.primero is None:
            print("La Lista de Productos se encuentra Vacia")
        # En caso contrario, se recorre la lista y se va mostrando cada dato de la lista
        else:
            temporal = self.primero
            while temporal is not None:
                print(temporal.MostrarDato())
                temporal = temporal.siguiente

    def eliminarInicio(self):
        # Si la lista está vacia, muestra al usuario que está vacia
        if self.primero is None:
            print("La Lista de Productos se encuentra Vacia")
        # En caso contrario, si solo tiene un elemento en la lista, borra el primer elemento
        elif self.primero.siguiente is None:
            self.primero = None
        # Si la lista posee más de un nodo, el segundo nodo pasa a ser el primero.
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None

    def eliminarFinal(self):
        # Si la lista está vacia, muestra al usuario que está vacia
        if self.primero is None:
            print("La Lista de Productos se encuentra Vacia")
        # En Caso Contrario, si solo hay un Nodo en la lista, se borra el primer y ultimo nodo
        elif self.primero.siguiente is None:
            self.primero = None
        # Si la lista posee más de un Nodo,
        else:
            """temporal = self.primero
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.anterior.siguiente = None"""
            self.ultimo.anterior.siguiente = None

    def buscar(self, id):
        aux = self.primero
        while aux:
            if aux.dato.identificacion() == id:
                return aux.dato
            else:
                aux = aux.siguiente
                if aux == None:
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


# https://www.youtube.com/watch?v=c27dIMT9kLE De aqui se obtuvieron la mayoria de metodos, a excepcion de eliminar final, inicio y eliminar por posicion
# https://pharos.sh/lista-doblemente-enlazada-con-ejemplos-de-python/ Metodos eliminar final, inicio y eliminar por posicion