class pila:

    def __init__(self):
        self.items = []

    def incluir(self, item):
        self.items.append(item)

    def extraer(self):
        return self.items.pop()

    def inspeccionar(self):
        return self.items[len(self.items) - 1]

    def tamano(self):
        return len(self.items)

    def mostrar(self):
        pilaAux = self.items
        for i in range(0, self.tamano()):
            print(pilaAux[-1].toString())
            pilaAux.pop()

#pila productos y pila carrito
#pila