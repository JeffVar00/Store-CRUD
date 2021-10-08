from listaSeccion import listaDobleC
from listaProducto import listaDoble
from tipoProducto import tipoProducto
from producto import producto
from seccion import seccion
from sucursal import sucursal
import csv

class archivos:

    def __init__(self):
        self.listaSucursales = []
        self.listaSecciones = []
        self.listaTProductos = []
        self.listaProductos = []

    def guardarFacturas(self, facturas):
        headers = ('Fecha y hora de salida', 'Productos comprados')
        with open('facturas.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for i in range(0, len(facturas)):
                fecha = ({'Fecha y hora de salida': facturas[i].fecha()})
                writer.writerow(fecha)
                aux = facturas[i].misProductos()
                for x in range(0, len(aux)):
                    producto = ({'Productos comprados' : aux[x].toString()})
                    writer.writerow(producto)

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
            return self.listaSucursales

    def cargarTProductos(self, new_seccion):
        with open('tProductos.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if new_seccion.idpropio() == row['ID Seccion']:
                    new_producto = tipoProducto(row['ID producto'], row['Nombre'], row['ID Seccion'])
                    self.cargarProductos(new_producto)
                    new_seccion.manejarProductos().agregarInicio(new_producto)

    def guardarTProductos(self):
        headers = ('ID producto', 'Nombre', 'ID Seccion')
        with open('tProductos.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            aux = self.listaTProductos
            for i in range(0, len(aux)):
                aux2 = aux[i].manejarPila().devolverPagar()
                for x in range(0, len(aux2)):
                    self.listaProductos.append(aux2[x])
                datos = ({'ID producto': aux[i].identificacion(), 'Nombre': aux[i].nom(), 'ID Seccion': aux[i].idSeccion()})
                writer.writerow(datos)
            self.guardarProductos()

    def cargarSecciones(self, new_sucursal):
        with open('secciones.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if new_sucursal.myID() == row['ID Sucursal']:
                    new_seccion = seccion(row['ID Sucursal'] , row['Nombre'], int(row['Numero de Seccion']), row['ID Seccion'])
                    self.cargarTProductos(new_seccion)
                    new_sucursal.seccionesSucursal().agregarFinal(new_seccion)

    def guardarSecciones(self):
        headers = ('ID Sucursal', 'Nombre', 'Numero de Seccion', 'ID Seccion')
        with open('secciones.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            aux = self.listaSecciones
            for i in range(0, len(aux)):
                aux2 = aux[i].manejarProductos().devolverGuardar()
                for x in range(0, len(aux2)):
                    self.listaTProductos.append(aux2[x])
                datos = ({'ID Sucursal': aux[i].id(), 'Nombre': aux[i].nom(), 'Numero de Seccion' : aux[i].num(), 'ID Seccion' : aux[i].idpropio()})
                writer.writerow(datos)
            self.guardarTProductos()

    def cargarProductos(self, tProducto):
        with open('productos.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if tProducto.identificacion() == row['ID tipoProducto']:
                    new_producto = producto(row['ID producto'], row['Nombre'], int(row['Precio']) , row['ID tipoProducto'])
                    tProducto.agregarPila(new_producto)

    def guardarProductos(self):
        headers = ('ID producto', 'Nombre', 'Precio' , 'ID tipoProducto')
        with open('productos.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            aux = self.listaProductos
            for i in range(0, len(aux)):
                datos = ({'ID producto': aux[i].idPropio(), 'Nombre': aux[i].nom(), 'Precio' : aux[i].precioP() , 'ID tipoProducto' : aux[i].idTipo()})
                writer.writerow(datos)

