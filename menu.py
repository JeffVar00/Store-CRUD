import os
from sucursal import sucursal
from random import randint
from seccion import seccion
from tipoProducto import tipoProducto
from producto import producto
from cliente import cliente
from pila import pila
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
        self.cliente = cliente
        self.colaClientes = queue.Queue(5)

    def cargar(self):
        sucursal1 = sucursal("{}".format(randint(0, 1000)), "Florida")
        sucursal2 = sucursal("{}".format(randint(0, 1000)), "Japon")
        sucursal3 = sucursal("{}".format(randint(0, 1000)), "Francia")

        pasillo1S1 = seccion("Pasillo Juguetes", 1)
        pasillo2S1 = seccion("Pasillo Tecnologia", 2)
        pasillo1S2 = seccion("Pasillo Ropa", 3)
        pasillo2S2 = seccion("Pasillo Zapatos", 4)
        pasillo1S3 = seccion("Pasillo Muebles", 5)
        pasillo2S3 = seccion("Pasillo Carnes", 6)

        tproducto1S1 = producto("{}".format(randint(0, 100)), "Taladro MECO", 12000)
        tproducto2S1 = producto("{}".format(randint(0, 100)), "Taladro ALPINOS", 34000)
        tproducto1S2 = producto("{}".format(randint(0, 100)), "Tornillos 1/2 Pulgada", 1000)
        tproducto2S2 = producto("{}".format(randint(0, 100)), "Tornillos 1/4 Pulgadas", 995)
        tproducto1S3 = producto("{}".format(randint(0, 100)), "Martillo Feliz", 53990)
        tproducto2S3 = producto("{}".format(randint(0, 100)), "Martillo Saiyajin", 75000)

        productoS1 = tipoProducto("{}".format(randint(0, 500)), "Taladros")
        productoS2 = tipoProducto("{}".format(randint(0, 500)), "Tornillos")
        productoS3 = tipoProducto("{}".format(randint(0, 500)), "Martillos")

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
                   "Nuestras Sucursales:\n"
                   "{}\n\n"
                   "Opciones:\n"
                   "1 - Abrir Nueva Sucursal\n"
                   "2 - Acceder a una Sucursal\n"
                   "0 - Salir\n").format("\n".join(self.mostrarFerreteria())))
            opcion = input("Opcion Elegida: ")
            if opcion.isnumeric() is True:
                opcion = int(opcion)
                if opcion == 1:
                    self.agregar_sucursal()
                if opcion == 2:
                    nSucursal = input("Digite el numero de sucursal a la cual desea acceder: ")
                    if nSucursal.isnumeric() is False or int(nSucursal) > len(self.ferreteria) or int(nSucursal) < 0:
                        print("No se digito una opcion valida")
                        os.system("pause")
                    elif nSucursal != "0":
                        self.menuSucursal(int(nSucursal))

    def agregar_sucursal(self):
        print("**********El martillazo Feliz**********\n\n"
              "Menu Agregar Sucursal\n\n")
        ubicacion = input("Digite la ubicacion de la sucursal la cual desea ingresar en el sistema: ")
        if ubicacion.isnumeric() is False:
            nueva_sucursal = sucursal("{}".format(randint(0, 1000)), ubicacion)
            agregar_secciones = True
            while agregar_secciones is True:
                nombre_seccion = input("Digite el nombre de la seccion: ")
                if nombre_seccion.isnumeric() is False:
                    numero_seccion = input("Digite el numero de la seccion: ")
                    if numero_seccion.isnumeric() is True:
                        nueva_seccion = seccion(nombre_seccion, int(numero_seccion))
                        agregar_tipos_producto = True
                        while agregar_tipos_producto is True:
                            nombre_tipo_producto = input("Digite el nombre del tipo del producto: ")
                            if nombre_tipo_producto.isnumeric() is False:
                                nuevo_tipo_producto = tipoProducto("{}".format(randint(0, 5000000)),
                                                                   nombre_tipo_producto)
                                agregar_productos = True
                                while agregar_productos is True:
                                    nombre_producto = input("Digite el nombre del Producto: ")
                                    if nombre_producto.isnumeric() is False:
                                        precio_producto = input(
                                            "Digite el precio (en colones) del producto " + nombre_producto + ": ")
                                        if precio_producto.isnumeric() is True:
                                            nuevo_producto = producto("{}".format(randint(0, 1000000)), nombre_producto,
                                                                      precio_producto)
                                            nuevo_tipo_producto.agregarPila(nuevo_producto)
                                            agregar = input("Desea agregar otro producto? (S = Si, Otra Tecla = No): ")
                                            if agregar != "S":
                                                agregar_productos = False
                                        else:
                                            print("El precio debe ser un numero")
                                    else:
                                        print("El nombre no debe ser un numero")
                                nueva_seccion.agregarProducto(nuevo_tipo_producto)
                                agregar = input("Desea agregar otro tipo de producto? (S = Si, Otra Tecla = No): ")
                                if agregar != "S":
                                    agregar_tipos_producto = False
                            else:
                                print("El nombre no debe ser un numero")
                        nueva_sucursal.Secciones.agregarInicio(nueva_seccion)
                        agregar = input("Desea agregar otra seccion? (S = Si, Otra Tecla = No): ")
                        if agregar != "S":
                            agregar_secciones = False
                    else:
                        print("El numero de seccion debe ser un numero")
                else:
                    print("El nombre de seccion no debe ser un numero")
            self.ferreteria.append(nueva_sucursal)
            print("La sucursal ha sido creada con exito")
        else:
            print("La ubicacion no debe ser un numero")

    def menuSucursal(self, nSucursal):
        opcion = None
        su = self.ferreteria[nSucursal - 1]
        while opcion != "0":
            os.system("cls")
            print("Sucursal: " + su.ubicacion())
            su.mostrar()
            print(("\n"
                   "1 - Mi carrito\n"
                   "2 - Entrar a una seccion\n"
                   "3 - Pasar a cajas\n"
                   "4 - Eliminar Seccion\n"
                   "5 - Eliminar esta sucursal\n"
                   "0 - Salir\n"))
            opcion = input("Digite la opcion que desea realizar: ")
            if opcion.isnumeric() is True:
                if opcion == "1":
                    self.menuCarrito()
                elif opcion == "2":
                    opcion = input("A que seccion se desea dirigir (Digite el # de seccion): ")
                    if opcion.isnumeric() is False or int(opcion) > su.CantidadSecciones() or int(opcion) < 0:
                        print("No se digito una opcion valida")
                        os.system("pause")
                    else:
                        self.dentroSeccion(su ,int(opcion))
                elif opcion == "3":
                    self.pagar()
                elif opcion == "4":
                    self.eliminarSeccion(su)
                elif opcion == "5":
                    self.eliminarSucursal(nSucursal)
                    if self.eliminarSucursal(nSucursal) is True:
                        break
                    else:
                        print("No se ha eliminado la sucursal")
                        os.system("pause")
                elif opcion == "0":
                    print("Gracias por visitarnos!")
                    os.system("pause")
                else:
                    print("No se digito una opcion valida")
                    os.system("pause")
            else:
                print("Solo se permite un digito numerico")
                os.system("pause")

    def dentroSeccion(self, sucursal, nSeccion):
        seccion = sucursal.manejarSeccion(nSeccion)
        opcion = None
        if seccion is False:
            print("Esta seccion no se encontro")
        else:
           while opcion != "0":
               os.system("cls")
               seccion.mostrarProductos()
               print(("\n"
                      "1 - Navegar producto\n"
                      "0 - Salir\n"))
               opcion = input("Digite la opcion que desea realizar: ")
               if opcion.isnumeric() is True:
                   if opcion == "1":
                       opcion = input("Digite el ID del producto: ")
                       tProductos = seccion.manejarProductos().buscar(opcion)
                       if tProductos is False:
                           print("No se encontro este producto")
                           os.system("pause")
                       else:
                           if tProductos.manejarPila().tamano() != 0:
                               print("Total de productos: {}".format(tProductos.manejarPila().tamano()))
                               print("Producto a la vista: " + tProductos.manejarPila().inspeccionar().toString())
                               opcion = input("Desea adiquirir este producto? 1 = si Otra tecla = no: ")
                               #pendiente array que se le agregen los productos que ignoro, si al final no agarro nada devolver
                               #a la pila original, y de igual forma si si selecciono uno, .pop a ese y devolver los otros
                               #no me salio xd
                               if opcion == "1":
                                   print("Gracias por adquirir: " + tProductos.manejarPila().inspeccionar().toString())
                                   print("Se ha agregado al carrito!!")
                                   self.cliente.carritoCliente().incluir(tProductos.manejarPila().inspeccionar())
                                   tProductos.manejarPila().extraer()
                                   os.system("pause")
                           else:
                               print("Ya no nos quedaron productos de este tipo")
                               os.system("pause")
                   elif opcion == "0":
                       os.system("pause")
                   else:
                       print("No se digito una opcion valida")
                       os.system("pause")
               else:
                   print("Solo se permite un digito numerico")
                   os.system("pause")

    def menuCarrito(self):
        if self.cliente.carritoCliente().tamano() != 0:
            print("Total de productos en el carrito: {}".format(self.cliente.carritoCliente().tamano()))
            self.cliente.carritoCliente().mostrar()
            os.system("pause")
        else:
            print("Carrito vacio")
            os.system("pause")

    def pagar(self):
        pass

    def eliminarSucursal(self, nSucursal):
        opcion = print("Seguro que desea eliminar esta seccion?: 1- Si Otra tecla- No: ")
        if opcion == "1":
            self.ferreteria.remove(nSucursal - 1)
            print("Se ha eliminado la sucursal")
            os.system("pause")
            return True
        else:
            os.system("pause")
            return False
    def eliminarSeccion(self, sucursal):
        numero = None
        while numero != "0":
            os.system("cls")
            sucursal.mostrar()
            print("**El martillazo Feliz**\n"
                  "Menu Eliminar Seccion\n\n"
                  "1 - Eliminar Primer Seccion\n"
                  "2 - Eliminar Ultima Seccion\n"
                  "3 - Eliminar Especifico\n"
                  "0 - Salir\n")
            numero = input("Digite la opcion que desea realizar: ")
            if numero.isnumeric() is True:
                if numero == "1":
                    sucursal.seccionesSucursal().eliminarInicio()
                    print("Se ha eliminado la seccion!")
                elif numero == "2":
                    sucursal.seccionesSucursal().eliminarFinal()
                    print("Se ha eliminado la seccion!")
                elif numero == "3":
                    opcion = input("Digite el numero de seccion que desea eliminar: ")
                    sucursal.seccionesSucursal().eliminar(int(opcion))
                    print("Se ha eliminado la seccion!")
                    os.system("pause")
                elif numero == "0":
                    os.system("pause")
                else:
                    print("No se digito una opcion valida")
                    os.system("pause")
            else:
                print("Solo se permite un digito numerico")
                os.system("pause")

    def mantenimientoSeccion(self, seccion): #recibe la seccion en la que esta, esto va dentro de menuSeccion
        #solo crear menu
        #aqui dentro va el eliminarSeccion()
        pass

    def mantenimientoSucursal(self, sucursal): #recibe la sucursal en la que esta, esto va dentro de menuSucursal
        #solo crear menu
        # aqui dentro va el eliminarSucursal()
        pass

    def mantenimientoProductos(self):
        pass

    def mantenimientoTProductos(self, producto):
        pass

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

