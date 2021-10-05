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

    def vaciar(self):
        for i in range(0, self.tamano()):
            self.items.pop()

    def mostrar(self):
        pilaAux = []
        for i in range(0, self.tamano()):
            print(self.items[len(self.items) - 1].toString())
            pilaAux.append(self.items.pop())
        for i in range(0, len(pilaAux)):
            self.items.append(pilaAux.pop())

#pila productos y pila carrito
#pila