"""
Ejercicio: Sistema de Gestión de Inventario de Tienda

Crear un sistema de gestión de inventario para una tienda. El sistema debe permitir a los usuarios realizar las siguientes operaciones:

1- Agregar un producto al inventario.
2- Modificar la cantidad de un producto en el inventario.
3- Eliminar un producto del inventario.
4- Mostrar la lista de productos en el inventario.
5- Calcular el valor total del inventario (basado en la cantidad y el precio de cada producto).

Para implementar esto, debes crear una clase Producto con las siguientes propiedades:

1- Nombre del producto.
2- Código del producto (debe ser único para cada producto).
3- Precio del producto.
4- Cantidad en stock.

Luego, crea una clase Inventario que maneje una lista de productos. Debe tener los siguientes métodos:

- agregar_producto: Agrega un nuevo producto al inventario.
- modificar_cantidad: Modifica la cantidad de un producto existente en el inventario.
- eliminar_producto: Elimina un producto del inventario por su código.
- mostrar_inventario: Muestra la lista de productos en el inventario, incluyendo nombre, código, precio y cantidad en stock.
- calcular_valor_total: Calcula el valor total del inventario multiplicando el precio por la cantidad de cada producto 
y sumando estos valores.

Crea un programa principal que permita a los usuarios interactuar con el sistema de gestión de inventario. Los usuarios deben 
poder agregar productos, modificar cantidades, eliminar productos, ver el inventario y calcular el valor total.
"""

class Producto():
    def __init__(self, nombre, codigo, precio, stock):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.stock = stock

class Inventario():
    def __init__(self):
        self.productos = []

    def agregar_producto(self):
        nombre = input("Ingrese el nombre del producto: ")
        codigo = int(input("Ingrese el codigo del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el numero de unidades en stock del producto: "))
        nuevo_producto = Producto(nombre, codigo, precio, stock)
        self.productos.append(nuevo_producto)
        print(f"El producto {nombre} ha sido registado de manera exitosa!\n")

    def mostrar_inventario(self):
        if not self.productos:
            print("No hay productos registrados.")
            return
        
        for i, producto in enumerate(self.productos, start = 1):
            print(f"{i}.  Nombre: {producto.nombre}, Codigo: {producto.codigo}, Precio:{producto.precio}, Stock: {producto.stock}")



    def modificar_cantidad(self):
        if not self.productos:
            print("No hay productos registrados.")
            return
        
        self.mostrar_inventario()
        seleccion = int(input("Ingresa el numero del producto que desea modificar cantidad: "))

        if 1 <= seleccion <= len(self.productos):
            producto_seleccionado = self.productos[seleccion - 1]
            while True:
                print(" ******** Modificar Producto ******** ")
                print("1. Aumentar cantidad de un producto")
                print("2. Disminuir cantidad de un producto")
                print("3. Volver al menú anterior")

                option = int(input("Que accion desea realizar: "))

                match option:

                    case 1:
                        cantidad_aumentar = int(input("Ingrese la cantidad que desea aumentar: "))
                        producto_seleccionado.stock += cantidad_aumentar
                        print(f"El producto '{producto_seleccionado.nombre}' ha sido aumentada {cantidad_aumentar}. Nueva Cantidad {producto_seleccionado.stock}")
                    
                    case 2:
                        cantidad_disminuir = int(input("Ingrese la cantidad que desea disminuir: "))
                        producto_seleccionado.stock -= cantidad_disminuir
                        print(f"El producto '{producto_seleccionado.nombre}' ha sido disminuido {cantidad_disminuir}. Nueva Cantidad {producto_seleccionado.stock}")
                    
                    case 3:
                        break

                    case default:
                        print("XXXXX Opcion no valida XXXXX")

    def eliminar_producto(self):
        if not self.productos:
            print("No hay productos ingresados")

        self.mostrar_inventario()
        seleccion = int(input("Ingresa el numero del producto que desea modificar cantidad: "))

        if 1 <= seleccion <= len(self.productos):
            producto_eliminado = self.productos.pop(seleccion - 1)
            print(f"Producto eliminado: {producto_eliminado.nombre} \n")
    
    def costo_producto(self):
        costo_total = 0
        for producto in self.productos:
            costo_total += producto.precio * producto.stock
        
        return costo_total
    
    

def main():

    inventario = Inventario()

    while True:
        print("MENU")
        print("1. Ingresar Producto")
        print("2. Listado del inventario")
        print("3. Modificar cantidad de un producto")
        print("4. Eliminar un producto")
        print("5. Salir")

        option = int(input("Que opcion desea realizar: "))

        match option:

            case 1:
                inventario.agregar_producto()
            case 2:
                inventario.mostrar_inventario()
            case 3:
                inventario.modificar_cantidad()
            case 4:
                inventario.eliminar_producto()
            case 5: 
                 print("****** Hasta Luego ******")
                 break
            




if __name__ == "__main__":
    main()            



           
