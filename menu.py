import queue
from cliente import cliente

"""
from seccion import seccion
from listaSeccion import listaDobleC
"""

"""
from producto import producto
from listaProducto import listaDoble
"""

class menu:

    def cargar():
        pass

    def menuPrincipal():
        pass

"""prueba lista doblemente enlazada
        productos = listaDoble()
        producto1 = producto("1","uno",1)
        producto2 = producto("2", "dos", 2)
        producto3 = producto("3", "tres", 3)
        producto4 = producto("4", "cuatro", 4)

        productos.agregarInicio(producto1)
        productos.agregarInicio(producto2)
        productos.agregarInicio(producto3)
        productos.agregarInicio(producto4)

        x = productos.buscar("2")
        productos.mostrar()
        print(x.toString())
        productos.eliminarInicio()
        productos.mostrar()
"""

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



"""prueba lista doblemente enlazada circular
        secciones = listaDobleC()
        seccion1 = seccion("uno", "1")
        seccion2 = seccion("dos", "2")
        seccion3 = seccion("tres", "3")
        seccion4 = seccion("cuatro", "4")

        secciones.agregarFinal(seccion1)
        secciones.agregarFinal(seccion2)
        secciones.agregarFinal(seccion3)
        secciones.agregarFinal(seccion4)

        x = secciones.buscar("dos")
        secciones.mostrar()
        print(x.toString())
        secciones.eliminar("uno")
        secciones.mostrar()
"""


