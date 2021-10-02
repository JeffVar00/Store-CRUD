
class producto:

    def __init__(self, ID, nombre, precio):
        self.ID = ID
        self.nombre = nombre
        self.precio = precio

    def idTipo(self):
        return self.ID

    def toString(self):
        return "ID: " + self.ID + ", Descripcion: " + self.nombre + ", Precio: {}".format(self.precio)

