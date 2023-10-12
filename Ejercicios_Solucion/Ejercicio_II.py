"""     INCISO 
Ejercicio : Una empresa desea realizar un sistema donde el usuario ingrese productos, 
con el codigo, nombre, precio de venta, costo, cantidad en inventario, asi mismo 
podra realizar consultas sobre productos para lo cual ingresara el nombre del producto 
y el sistema le mostrara todos los datos de este producto, luego el usuario podra 
realizar entradas al inventario y salidas del inventario de cada producto, entonces 
cuando sea una entrada este valor se sumara a la cantidad en inventario y cuando sea 
una salida se restara la cantidad del inventario, el usuario podra realizar n cantidad 
de transacciones en el sistema 
"""

"""  ESTRUCTURA 
1. Estructura de la clase producto, con su funcion, metodo init y parametros que recibirira {nombre, codigo
precio, costo, cantidad}.
2. Consulta de la lista de productos disponibles con todos sus atributos.
3. Consulta de un unico producto en especifico.
4. Agregar o eliminar cantidad del inventario.
5. Crear el menu y llamar las funciones.
"""

class Producto():

    def __init__(self, nombre, codigo, precio, costo, cantidad):
        self.nombre = nombre #Esta línea asigna el valor del parámetro nombre a un atributo llamado nombre en la instancia actual 
                             #(representada por self). Esto significa que cuando creas una instancia de la clase y proporcionas un 
                             # valor para nombre, ese valor se almacena en el atributo nombre de esa instancia.
        self.codigo = codigo
        self.precio = precio
        self.costo = costo
        self.cantidad = cantidad


class Menu():

    def __init__(self):
        self.productos = []
        self.index_productos = 0
    
    def agregar_producto(self):
        nombre = input(f"Ingrese el nombre del producto: ")
        codigo = int(input("Ingrese el codigo del producto: "))
        precio = float(input("Ingrese el precio de compra del producto: "))
        costo = float(input("Ingrese el costo por unidad del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        nuevo_producto = Producto(nombre, codigo, precio, costo, cantidad)
        self.productos.append(nuevo_producto)
        print(f"\nProducto {nombre} ingresado de manera exitosa!\n")


    def lista_producto(self):
        if not self.productos:
            print(f"No hay productos registrados")
        else:
            print(f"Listado de productos: ")
            for i, producto in enumerate(self.productos, start = 1):
                print(f"{i}. Nombre:{producto.nombre}, Codigo:{producto.codigo}, Precio:{producto.precio}, Costo:{producto.costo}, Cantidad:{producto.cantidad}")
    
    def detalle_producto(self):
        while True:
            nombre_producto = input(f"\nIngrese el nombre del producto que desea visualizar: \n")
            encontrado =  False

            for producto in self.productos:
                if producto.nombre == nombre_producto:
                    print(f"Producto encontrado: Nombre: {producto.nombre}, Codigo: {producto.codigo}, Precio: {producto.precio}, Costo: {producto.costo}, Cantidad: {producto.cantidad}")
                    encontrado = True
                    break

            if not encontrado:
                 print(f"El producto con nombre '{nombre_producto}' no se encontró en la lista. Intente nuevamente.")
                 continue
            
            break

    def aumentar_producto(self):
        if not self.productos:
            print("No hay productos registrados.")
            return
        
        self.lista_producto()
        seleccion = int(input(f"Seleccione el numero del producto al que desea aumentar las cantidades: "))

        if 1<= seleccion <= len(self.productos):
            producto_seleccionado = self.productos[seleccion - 1]
            cantidad_aumentar = int(input(f"Ingrese la cantidad que desea aumentar: "))
            producto_seleccionado.cantidad += cantidad_aumentar
            print(f"La cantidad de '{producto_seleccionado.nombre}' ha sido aumentada en {cantidad_aumentar}. Nueva cantidad: {producto_seleccionado.cantidad}")
        else:
            print("Seleccion Invalido. Intente nuevamente")
    
    def disminuir_producto(self):
        if not self.productos:
            print("No hay productos registrados.")
            return
        
        self.lista_producto()
        seleccion = int(input(f"Seleccione el numero del producto al que desea disminuir las cantidades: "))
        
        if 1<= seleccion <= len(self.productos):
            producto_seleccionado = self.productos[seleccion - 1]
            cantidad_disminuir = int(input(f"Ingrese la cantidad que desea disminuir: \n"))
            producto_seleccionado.cantidad -= cantidad_disminuir
            print(f"La cantidad de '{producto_seleccionado.nombre}' ha sido disminuida en {cantidad_disminuir}. Nueva cantidad: {producto_seleccionado.cantidad}")
        else:
            print("Seleccion Invalido. Intente nuevamente")

def main():

    listado_producto = Menu()

    while True:
        print(" ******** MENU ******** ")
        print("1. Agregar producto")
        print("2. Listado de productos registrados")
        print("3. Detalles de un producto")
        print("4. Aumentar cantidades de un producto")
        print("5. Disminuir cantidades de un producto")
        print("6. Salir")

        option = input(f"\nSeleccione una opcion a trabajar: ")

        if option == "1":
            listado_producto.agregar_producto()
        elif option == "2":
            listado_producto.lista_producto()
        elif option == "3":
            listado_producto.detalle_producto()
        elif option == "4":
            listado_producto.aumentar_producto()
        elif option == "5":
            listado_producto.disminuir_producto()
        elif option == "6":
            print("\n ****** EXIT ******* \n")
            break
        else:
            print("\n ********* Opción no válida. Por favor, seleccione una opción válida. ********* \n")


if __name__ == "__main__":
        main()
