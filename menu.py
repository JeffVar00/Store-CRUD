import os
from sucursal import sucursal
from random import randint
from seccion import seccion
from tipoProducto import tipoProducto
from producto import producto
from cliente import cliente
import queue


"""
from seccion import seccion
from listaSeccion import listaDobleC
"""

"""
from producto import producto
from listaProducto import listaDoble
"""


class menu:

    def __init__(self):
        self.ferreteria = []

    def cargar(self):
        sucursal1 = sucursal("{}".format(randint(0, 1000)), "Florida")
        sucursal2 = sucursal("{}".format(randint(0, 1000)), "Japon")
        sucursal3 = sucursal("{}".format(randint(0, 1000)), "Francia")

        pasillo1S1 = seccion("Pasillo Juguetes", "#1")
        pasillo2S1 = seccion("Pasillo Tecnologia", "#2")
        pasillo1S2 = seccion("Pasillo Ropa", "#1")
        pasillo2S2 = seccion("Pasillo Zapatos", "#2")
        pasillo1S3 = seccion("Pasillo Muebles", "#1")
        pasillo2S3 = seccion("Pasillo Carnes", "#2")

        tproducto1S1 = tipoProducto("{}".format(randint(0, 1000000)), "Taladro MECO", 12000)
        tproducto2S1 = tipoProducto("{}".format(randint(0, 1000000)), "Taladro ALPINOS", 34000)
        tproducto1S2 = tipoProducto("{}".format(randint(0, 1000000)), "Tornillos 1/2 Pulgada", 1000)
        tproducto2S2 = tipoProducto("{}".format(randint(0, 1000000)), "Tornillos 1/4 Pulgadas", 995)
        tproducto1S3 = tipoProducto("{}".format(randint(0, 1000000)), "Martillo Feliz", 53990)
        tproducto2S3 = tipoProducto("{}".format(randint(0, 1000000)), "Martillo Saiyajin", 75000)

        productoS1 = producto("{}".format(randint(0, 5000000)), "Taladros")
        productoS2 = producto("{}".format(randint(0, 5000000)), "Tornillos")
        productoS3 = producto("{}".format(randint(0, 5000000)), "Martillos")

        productoS1.agregarPila(tproducto1S1)
        productoS1.agregarPila(tproducto2S1)
        productoS2.agregarPila(tproducto1S2)
        productoS2.agregarPila(tproducto2S2)
        productoS3.agregarPila(tproducto1S3)
        productoS3.agregarPila(tproducto2S3)

        pasillo1S1.agregarProducto(productoS1)
        pasillo2S1.agregarProducto(productoS1)
        pasillo1S2.agregarProducto(productoS2)
        pasillo2S2.agregarProducto(productoS2)
        pasillo1S3.agregarProducto(productoS3)
        pasillo2S3.agregarProducto(productoS3)

        sucursal1.Secciones.agregarInicio(pasillo1S1)
        sucursal1.Secciones.agregarInicio(pasillo2S1)
        sucursal1.Secciones.agregarInicio(pasillo1S2)
        sucursal1.Secciones.agregarInicio(pasillo2S2)
        sucursal1.Secciones.agregarInicio(pasillo1S3)
        sucursal1.Secciones.agregarInicio(pasillo2S3)

        self.ferreteria.append(sucursal1)
        self.ferreteria.append(sucursal2)
        self.ferreteria.append(sucursal3)

    def menuPrincipal(self):
        self.cargar()
        opcion = None
        while opcion != 0:
            os.system("cls")
            print(("\n"
                   "**********El martillazo Feliz**********\n"
                   "Bienvenido al martillazo Feliz!\n\n"
                   "Nuestras Sucursales:\n\n"
                   "{}\n\n"
                   "Opciones:\n"
                   "1 - Abrir Nueva Sucursal (Disponible en la siguiente actualizacion (BETA NO ENTRE!!!))\n"
                   "2 - Acceder a una Sucursal\n"
                   "0 - Salir\n").format("\n".join(self.mostrarFerreteria())))
            opcion = input("Opcion Elegida: ")
            if opcion.isnumeric() is True:
                opcion = int(opcion)
                if opcion == 2:
                    nSucursal = input("\nDigite la posicion del sucursal a la cual desea acceder: ")
                    if nSucursal.isnumeric() is False or int(nSucursal) > len(self.ferreteria) or int(nSucursal) < 0:
                        print("No se digito una opcion valida")
                        os.system("pause")
                    elif nSucursal != "0":
                        self.menuSucursal(int(nSucursal))

    def menuSucursal(self, nSucursal):
        x = None
        su = self.ferreteria[nSucursal - 1]
        while x != 0:
            os.system("cls")
            print("Sucursal: " + su.ubicacion())
            su.mostrar()
            opcion = input("A que seccion se desea dirigir: ")
            if opcion.isnumeric() is False or int(opcion) > su.CantidadSecciones() or int(opcion) < 0:
                print("No se digito una opcion valida")
                os.system("pause")
            x = 0

    def mostrarFerreteria(self):
        sucursales = []
        """for i in self.ferreteria:
            sucursales.append(i.toString())"""
        for i in range(0, len(self.ferreteria)):
            sucursales.append("{}- {}".format(i + 1, self.ferreteria[i].toString()))
        return sucursales

"""prueba cola

#_get() obtener de la cola
#get() sacar de la cola

        colClientes = queue.Queue(5)

        cliente1 = cliente("Jeff")
        cliente2 = cliente("Ramses")
        cliente3 = cliente("Caleb")

        colClientes.put(cliente1)
        colClientes.put(cliente2)
        colClientes.put(cliente3)

        print(colClientes.qsize())
        x =  colClientes.get()
        print(x.toString())

        print(colClientes.qsize())
        x = colClientes.get()
        print(x.toString())

        print(colClientes.qsize())
        x = colClientes.get()
        print(x.toString())

"""

