from listaSeccion import listaDobleC
from listaProducto import listaDoble
from tipoProducto import tipoProducto
from seccion import seccion
from sucursal import sucursal
import csv

class archivos:

    #sucursal tiene un ID, seccion hereda ese ID y crea uno propio que se hereda a los tipos de productos de esta seccion
    #cada tipo de producto genera un ID propio que hereda a sus tipos de productos, estos crearn su propio ID pero es solo
    #para identificarlos

    def __init__(self):
        self.listaSucursales = []

    def guardarFacturas(self):
        pass

    def guardarSucursales(self, sucursales):
        headers = ('ID', 'Ubicacion')
        with open('sucursales.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for i in range(0, len(sucursales)):
                datos = ({'ID': sucursales[i].myID(), 'Ubicacion': sucursales[i].ubicacion()})
                writer.writerow(datos)

    def cargarSucursales(self):
        with open('sucursales.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_sucursal = sucursal(row['ID'] , row['Ubicacion'])
                self.cargarSecciones()
                self.listaSucursales.append(new_sucursal)
                print(new_sucursal.toString())

    def cargarProductos(self):
        pass

    def guardarProductos(self):
        pass

    def cargarSecciones(self):
        pass

    def guardarSecciones(self):
        pass

    def cargarTiposProductos(self):
        pass

    def guardarTiposProductos(self):
        pass

