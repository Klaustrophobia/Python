"""
Una empresa desea realizar un sistema para manejar sus productos, estos productos pueden ser de tres tipos, 
Refrigeradoras, Televisores y Celulares, todos los productos tendrán que calcular su precio  de venta para 
el cual se tomara el costo del producto más un porcentaje sobre ese costo por cada caso detallado continuación : 

refrigeradoras un 70% si son de dos puertas verticales caso contrario será de un 65%, 
en el caso de los televisores un 100% si el televisor es de más de 75 pulgadas, si es de 60 a 74 pulgadas 
será de un 80% y menores a 60 será de 75%, 
en el caso de los Celulares tendrá un estándar de 150%. 
de cada producto se requieren al menos 5 características propias, de manera general todos los productos tendrán 
un código único que no se repite, así mismo una marca, modelo, costo y existencia.

De cada producto también se requiere un label o string donde se describan todas las características del 
producto (no usar el método __str__() ).

En cada producto se calculará también el impuesto el cual será de 15% de su precio total, 
también se requiere un cálculo de descuento en el cual se ingresará el producto y el porcentaje 
de descuento en el producto ingresado.

Se deberán poder ingresar productos validando que el código no se repita y mostrar todos 
los productos y aplicación de descuento a un producto ingresando el código del producto y 
el porcentaje a aplicar mostrando el precio actual y el precio con descuento.

 
Se requiere aplicar Programación Orientada a Objetos y se evaluara de la siguiente manera :

·         Herencia (6%)

·         Uso del constructor de la clase padre (1%)

·         Clases abstractas (2%)

·         Métodos Abstractos (2%)

·         Métodos estáticos (1.5%)

·         Atributos Privados y públicos. (1.5%)

·         Ingreso de productos (2%)

·         Mostrado de productos (2%)

·         Ingreso de descuentos (2%)
"""

"""
SOLUCION
PRODUCTO {marca, modelo, costo, existencia} CLASE PADRE I
"""

from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, codigo, marca, modelo, costo, existencia, tipo):
        self.codigo = codigo
        self.marca = marca
        self.modelo = modelo
        self.costo = costo
        self.existencia = existencia
        self.tipo = tipo

    @abstractmethod
    def precio_venta(self):
        pass
    
    @abstractmethod
    def detalles_productos(self):
        pass
    
    @staticmethod
    def impuesto(self):
        return 0.15 * self.costo
    
class Televisor(Producto):
    def __init__(self, pulgadas, smart, led, resolucion, consumo, codigo, marca, modelo, costo, existencia, tipo):
        super().__init__(codigo, marca, modelo, costo, existencia, tipo)
        self.pulgadas = pulgadas
        self.smart = smart 
        self.led = led
        self.resolucion = resolucion
        self.consumo = consumo
    
    def precio_venta(self):
        if self.pulgadas > 75:
            return 1 * self.costo
        elif 74 > self.pulgadas > 60:
            return 0.8 * self.costo
        elif self.pulgadas < 60:
            return 0.75 * self.costo
        
    def detalles_productos(self):

        precio_venta = self.precio_venta()
        impuesto = self.impuesto()
        total = self.impuesto() + self.precio_venta() + self.costo

        print("D E T A L L E S")
        print(f"Codigo: {self.codigo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Costo: {self.costo}")
        print(f"Existencia: {self.existencia}")
        print(f"Tipo: {self.tipo}")
        print(f"Pulgadas: {self.pulgadas}")
        print(f"Smart: {self.smart}")
        print(f"Led: {self.led}")
        print(f"Resolucion: {self.resolucion}")
        print(f"Consumo: {self.consumo}")
        print(f"Total: {total}")

        
        
class Refrigerador(Producto):
    def __init__(self, cant_puertas, congelador, dispensador, capacidad, smart, codigo, marca, modelo, costo, existencia, tipo):
        super().__init__(codigo, marca, modelo, costo, existencia, tipo)
        self.cant_puertas = cant_puertas
        self.congelador = congelador
        self.dispensador = dispensador
        self.capacidad = capacidad
        self.smart = smart

    def precio_venta(self):
        if self.cant_puertas > 2:
            return 0.7 * self.costo
        else:
            return 0.6 * self.costo
        
    def detalles_productos(self):

        precio_venta = self.precio_venta()
        impuesto = self.impuesto()
        total = self.impuesto() + self.precio_venta() + self.costo

        print("D E T A L L E S")
        print(f"Codigo: {self.codigo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Costo: {self.costo}")
        print(f"Existencia: {self.existencia}")
        print(f"Tipo: {self.tipo}")
        print(f"Cantidad de puertas: {self.cant_puertas}")
        print(f"Congelador: {self.congelador}")
        print(f"Dispensador: {self.dispensador}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Smart: {self.smart}")
        print(f"Total: {total}")

        
        
class Celular(Producto):
    def __init__(self, cant_camaras, ram, almacenamiento, bateria, sistema, codigo, marca, modelo, costo, existencia, tipo):
        super().__init__(codigo, marca, modelo, costo, existencia, tipo)
        self.cant_camaras = cant_camaras
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.bateria = bateria
        self.sistema = sistema
    
    def precio_venta(self):
        return 1.5 * self.costo
    
    def detalles_productos(self):

        precio_venta = self.precio_venta()
        impuesto = self.impuesto()
        total = self.impuesto() + self.precio_venta() + self.costo

        print("D E T A L L E S")
        print(f"Codigo: {self.codigo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Costo: {self.costo}")
        print(f"Existencia: {self.existencia}")
        print(f"Tipo: {self.tipo}")
        print(f"Cantidad de camaras: {self.cant_camaras}")
        print(f"RAM: {self.ram}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"Bateria: {self.bateria}")
        print(f"Sistema Operativo: {self.sistema}")
        print(f"Total: {total}")

    
    
        
class Menu():

    def __init__(self):
        self.lista_productos = []

    def add_televisor(self):
        print("FAVOR DE INGRESAR DE MANERA CAUTELOSA LOS DATOS DEL PRODUCTO")
        print("T E L E V I S O R ")
        try:
            codigo = int(input("Codigo: "))

            if any(producto.codigo == codigo for producto in self.lista_productos):
                print("Este código ya está asignado a otro producto, vuelva a intentarlo \n")
                return
            
            pulgadas = int(input("Pulgadas: "))
            smart = input("Es smart (si/no): ").lower()
            led = input("La pantalla es led (si/no): ").lower()
            resolucion = input("La resolucion de la pantalla: ")
            consumo = int(input("Consumo en KWatts: "))
            marca = input("Marca: ")            
            modelo = input("Modelo: ")
            costo = int(input("Costo: "))
            existencia = int(input("Existencia: "))
            new_tv = Televisor(pulgadas, smart, led, resolucion, consumo, codigo, marca, modelo, costo, existencia, tipo = "televisor")
            self.lista_productos.append(new_tv)

            print(f"El producto {new_tv.codigo} con existencia de {new_tv.existencia} ha sido ingresado al sistema \n")

        except ValueError:
            print("Un tipo de dato no fue ingresado de manera correcta, intenta de nuevo \n")

    def add_refri(self):
        print("FAVOR DE INGRESAR DE MANERA CAUTELOSA LOS DATOS DEL PRODUCTO")
        print("R E F R I G E R A D O R ")
        try:
            codigo = int(input("Codigo: "))

            if any(producto.codigo == codigo for producto in self.lista_productos):
                print("Este código ya está asignado a otro producto, vuelva a intentarlo \n")
                return

            
            cant_puertas = int(input("Cantidad de puertas: "))
            congelador = input("Tiene congelador (si/no): ").lower()
            dispensador = input("Tiene dispensador (si/no): ").lower()
            capacidad = int(input("Capacidad que soporta: "))
            smart = input("Es smart(si/no): ").lower()
            marca = input("Marca: ")            
            modelo = input("Modelo: ")
            costo = int(input("Costo: "))
            existencia = int(input("Existencia: "))
            new_refri = Refrigerador(cant_puertas, congelador, dispensador, capacidad, smart, codigo, marca, modelo, costo, existencia, tipo = "refrigerador")
            self.lista_productos.append(new_refri)

            print(f"El producto {new_refri.codigo} con existencia de {new_refri.existencia} ha sido ingresado al sistema \n")

        except ValueError:
            print("Un tipo de dato no fue ingresado de manera correcta, intenta de nuevo \n")
    
    def add_phone(self):
        print("FAVOR DE INGRESAR DE MANERA CAUTELOSA LOS DATOS DEL PRODUCTO")
        print("C E L U L A R ")
        try: 
            codigo = int(input("Codigo: "))

            if any(producto.codigo == codigo for producto in self.lista_productos):
                print("Este código ya está asignado a otro producto, vuelva a intentarlo \n")
                return

            
            cant_camaras = int(input("Cantidad de camaras: "))
            ram = int(input("Cantidad de memoria RAM: "))
            almacenamiento = int(input("Almacenamiento: "))
            bateria = int(input("Capacidad de la bateria (KWh): "))
            sistema = input("Sistema Operativo: ")
            marca = input("Marca: ")            
            modelo = input("Modelo: ")
            costo = int(input("Costo: "))
            existencia = int(input("Existencia: "))
            new_phone = Celular(cant_camaras, ram, almacenamiento, bateria, sistema, codigo, marca, modelo, costo, existencia, tipo = "celular")
            self.lista_productos.append(new_phone)

            print(f"El producto {new_phone.codigo} con existencia de {new_phone.existencia} ha sido ingresado al sistema \n")
        except ValueError:
            print("Un tipo de dato no fue ingresado de manera correcta, intenta de nuevo \n")
    
    def menu_sencundario(self):
        try:
            print("Seleccione la categoría del producto: ")
            print("1. Refrigerador")
            print("2. Televisor")
            print("3. Celular")
            print("4. Regresar al menú principal")

            selection = int(input("Opción: "))
            print()

            match selection:
                case 1:
                    Menu.add_refri(self)
                case 2:
                    Menu.add_televisor(self)
                case 3:
                    Menu.add_phone(self)
                case 4:
                    return True
                case default:
                    print("ERROR, FAVOR DE INTENTARLO DE NUEVO \n")
        
        except ValueError:
            print("ERROR, FAVOR DE INTENTARLO DE NUEVO \n")


    def menu_terceario(self,  tipo_producto = None):
            try:
                print("Seleccione la categoría del producto: ")
                print("1. Refrigerador")
                print("2. Televisor")
                print("3. Celular")
                print("4. Regresar al menú principal")

                select = int(input("Opción: "))
                
                print()
                match select:
                    case 1:
                        tipo_producto = "refrigerador"
                        for i, producto in enumerate(self.lista_productos, start=1):
                            if producto.tipo.lower() == tipo_producto:
                                print(f"{i}. Tipo: {producto.tipo}, Código: {producto.codigo}")

                        select_producto = int(input("Seleccione el producto que desea ver sus detalles: "))
                        if 0 <= select_producto < len(self.lista_productos):
                            producto_seleccionado = self.lista_productos[select_producto - 1]
                            print(producto_seleccionado.detalles_productos())

                    case 2:
                        tipo_producto = "televisor"
                        for i, producto in enumerate(self.lista_productos, start = 1):
                            if tipo_producto == "refrigerador" or producto.tipo.lower():
                                print(f"{i}. Tipo: {producto.tipo}, Código: {producto.codigo}")
                        
                        select_producto = int(input("Seleccione el producto que desea ver sus detalles: "))
                        if 0 <= select_producto < len(self.lista_productos):
                            producto_seleccionado = self.lista_productos[select_producto - 1]
                            print(producto_seleccionado.detalles_productos())
                    case 3:
                        tipo_producto = "celular"
                        for i, producto in enumerate(self.lista_productos, start = 1):
                            if tipo_producto == "refrigerador" or producto.tipo.lower():
                                print(f"{i}. Tipo: {producto.tipo}, Código: {producto.codigo}")
                        
                        select_producto = int(input("Seleccione el producto que desea ver sus detalles: "))
                        if 0 <= select_producto < len(self.lista_productos):
                            producto_seleccionado = self.lista_productos[select_producto - 1]
                            print(producto_seleccionado.detalles_productos())
                    case 4:
                        return True
            except ValueError:
                print("ERROR, FAVOR DE INTENTARLO DE NUEVO")



def main():

    menu_principal = Menu()

    while True:
        try:
                print("B I E N V E N I D O")
                print("Elegir una opcion a trabajar: ")
                print("1. Agregar Producto")
                print("2. Precio de un producto")
                print("3. Salir")

                option = int(input("Opcion: "))
                print()

                match option:
                    case 1:
                        menu_principal.menu_sencundario()
                    case 2:
                        menu_principal.menu_terceario()
                    case 3:
                        return True
                    case default: 
                        print("Error, favor de eligir otra opcion")
                        
        except ValueError:
                print("ERROR DE INGRESO DE DATOS, POR FAVOR VOLVER A INTENTAR")


if __name__ == "__main__":
    main()