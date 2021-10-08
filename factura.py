
class factura:

    def __init__(self, fechayhora, productos):
        self.fechayhora = fechayhora
        self.productos = productos

    def fecha(self):
        return self.fechayhora

    def misProductos(self):
        return self.productos