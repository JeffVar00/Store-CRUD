
class producto:

    def __init__(self, ID, nombre, precio, IDtipo):
        self.ID = ID
        self.nombre = nombre
        self.precio = precio
        self.IDtipo = IDtipo

    def idTipo(self):
        return self.ID

    def precioP(self):
        return self.precio

    def toString(self):
        return "ID: " + self.ID + ", Descripcion: " + self.nombre + ", Precio: {}".format(self.precio)

