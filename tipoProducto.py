class tipoProducto:

    def __init__(self, ID, nombre, precio):
        self.ID = ID
        self.nombre = nombre
        self.precio = precio

    def idTipo(self):
        return self.ID