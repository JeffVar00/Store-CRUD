import queue
import os
from cliente import cliente
from sucursal import sucursal

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
        self.sucursales = []

    def cargar(self):
        sucursal1 = sucursal("1","Florida")
        sucursal2 = sucursal("2","Japon")
        sucursal3 = sucursal("3","Francia")

        self.sucursales.append(sucursal1)
        self.sucursales.append(sucursal2)
        self.sucursales.append(sucursal3)

    def menuPrincipal(self):
        self.cargar()
        nSucursal = None
        while nSucursal != 0:

            os.system("cls")
            print("""        El martillazo Feliz
Bienvenido al martillazo Feliz!
Ingrese el numero de sucursal al que desea acceder
Digite 0 para salir
            """)

            nSucursal = input("Sucursal: ")
            if nSucursal.isnumeric() == False or int(nSucursal) > 3 or int(nSucursal) < 0:
                print("No se digito una opcion valida")
                os.system("pause")
            elif nSucursal != 0:
                self.menuSucursal(int(nSucursal))

    def menuSucursal(self, nSucursal):
        x = None
        while(x != 0):
            os.system("cls")
            if nSucursal == 1:
                print("Sucursal: " + self.sucursales[0].ubicacion())
                os.system("pause")
                x = 0

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

