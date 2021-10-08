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
        self.listaSecciones = []

    def guardarFacturas(self):
        pass

    def guardarSucursales(self, sucursales):
        headers = ('ID', 'Ubicacion')
        with open('sucursales.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for i in range(0, len(sucursales)):
                aux = sucursales[i].seccionesSucursal().devolverGuardar()
                for x in range(0, len(aux)):
                    self.listaSecciones.append(aux[x])
                datos = ({'ID': sucursales[i].myID(), 'Ubicacion': sucursales[i].ubicacion()})
                writer.writerow(datos)
            self.guardarSecciones()

    def cargarSucursales(self):
        with open('sucursales.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_sucursal = sucursal(row['ID'], row['Ubicacion'])
                self.cargarSecciones(new_sucursal)
                self.listaSucursales.append(new_sucursal)
                print(new_sucursal.toString())
                new_sucursal.mostrar()

    def cargarProductos(self):
        pass

    def guardarProductos(self):
        pass

    def cargarSecciones(self, new_sucursal):
        with open('secciones.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if new_sucursal.myID() == row['ID Sucursal']:
                    new_seccion = seccion(row['ID Sucursal'] , row['Nombre'], row['Numero de Seccion'], row['ID Seccion'])
                    new_sucursal.seccionesSucursal().agregarFinal(new_seccion)

    def guardarSecciones(self):
        headers = ('ID Sucursal', 'Nombre', 'Numero de Seccion', 'ID Seccion')
        with open('secciones.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            aux = self.listaSecciones
            for i in range(0, len(aux)):
                datos = ({'ID Sucursal': aux[i].id(), 'Nombre': aux[i].nom(), 'Numero de Seccion' : aux[i].num(), 'ID Seccion' : aux[i].idpropio()})
                writer.writerow(datos)

    def cargarTiposProductos(self):
        pass

    def guardarTiposProductos(self):
        pass

