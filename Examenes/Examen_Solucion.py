"""
Ejercicio:

Una empresa de Aseo y Mantenimientos requiere un programa para el manejo de sus contratos, 
para esto se requiere que se ingrese la información de cada contrato la cual contiene, el empleado responsable, 
la cantidad de metro cuadrados en los que se realizara el aseo, el cliente del cual se requerirá su nombre completo 
y la identidad, y por último el precio por el cual se realiza el contrato.

Cada contrato podrá ir cambiando de estado por lo tanto el programa tendrá una opción para cambiar de estado el 
contrato, el estado solo puede ser de tres tipos “En Espera”, “En Proceso” y “Finalizado”.

Se tendrá una opción para visualizar cada contrato y para visualizar todos los contratos ingresados.

También una opción para que busque los contratos en un estado en especifico.

Se evaluará de la siguiente manera :

1- Diccionarios 1%

2- Arreglos 1%

3- Aplicación correcta de validaciones para evitar error en segmentos de código 2%

5- Aplicación correcta de Condicionales 2%

6- Aplicación correcta de Loops 2%

7- Funciones 2%

8- Funcionalidad del programa 10%
"""

"""
1. Clase Cliente {Nombre, Identidad} fun{Agregar contratos}
2. Clase Contrato {Empleado, metros, precio, status}
3. Mostar listados de contrato con nombre de cliente
4. Mostrar de manera detallada un contrato seleccionado
5. Buscar contratos por Status
6. Modificar Status de contrato
7. Factura del servicio contratado
"""

class Cliente():
    def __init__(self, nombre, identidad):
        self.nombre = nombre
        self.identidad = identidad

        self.contratos = []

    def agregar_contrato(self, contrato):
        self.contratos.append(contrato)

class Contrato():
    def __init__(self, empleado, metros, precio, status):
        self.empleado = empleado
        self.metros = metros
        self.precio = precio
        self.status = status

class Menu():
    def __init__(self):
        self.clientes = {}

    def agregar_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        identidad = int(input("Ingrese el numero de identidad del cliente: "))
        nuevo_cliente = Cliente(nombre, identidad)
        self.clientes.append(nuevo_cliente)
        print(f"El cliente '{nombre}' ha sido agregado de manera exitosa!\n")
    
    def listado_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados para agregarles un contrato")
        
        for i, cliente in enumerate(self.clientes):
            print(f"N{i}. Nombre: {cliente.nombre}, Identidad: {cliente.identidad}")


    def agregar_contrato(self):
        if not self.clientes:
            print("No hay clientes registrados para agregarles un contrato")
        
        self.listado_clientes()
        seleccion = int(input("Seleccione el numero de cliente que desea agregarle un contrato: "))

        if 1 <= seleccion <= len(self.clientes):
            cliente_seleccionado = self.clientes[seleccion - 1]
            empleado = input("Cual es el nombre del empleado asignado: ")
            metros = int(input("Cuantos son los metros asigandos a trabajar: "))
            precio = int(input("Ingrese el precio por metro: "))
            status = input("Ingrese el estado del contrato: ")
            contrato = Contrato(empleado, metros, precio, status)
            cliente_seleccionado.agregar_contrato(contrato)
            print("El contrato ha sido agregado de manera exitosa!\n")
    
    def listado_contrato(self):
        if not self.cliente:
            print("No hay clientes ingresados!")
        
        self.listado_clientes()
        seleccion = int(input("Seleccione el numero del cliente que desea ver su contrato: "))

        if 1 <= seleccion <= len(self.clientes):
            cliente_seleccionado = self.clientes[seleccion - 1]

            if not cliente_seleccionado.contratos:
                print(f"No hay contratos registrados para el cliente '{cliente_seleccionado.nombre}'")
            else:
                print(f"Contratos del cliente '{cliente_seleccionado.nombre}':")
                for i, contrato in enumerate(cliente_seleccionado.contratos, start=1):
                    print(f"Contrato {i}:")
                    print(f"Empleado: {contrato.empleado}")
                    print(f"Metros: {contrato.metros}")
                    print(f"Precio por metro: ${contrato.precio:.2f}")
                    print(f"Estado del contrato: {contrato.status}\n")
        else:
            print("Selección inválida. Intente nuevamente.")
    
    def detalle_contrato(self):
        if not self.clientes:
            print("No hay clientes registrados para mostrar contratos.")
            return

        self.listado_clientes()
        seleccion_cliente = int(input("Seleccione el número del cliente cuyos contratos desea ver: "))

        if 1 <= seleccion_cliente <= len(self.clientes):
            cliente_seleccionado = self.clientes[seleccion_cliente - 1]

            if not cliente_seleccionado.contratos:
                print(f"No hay contratos registrados para el cliente '{cliente_seleccionado.nombre}'")
                return

            print(f"Contratos del cliente '{cliente_seleccionado.nombre}':")
            for i, contrato in enumerate(cliente_seleccionado.contratos, start=1):
                print(f"Contrato {i}:")
                print(f"Empleado: {contrato.empleado}")
                print(f"Metros: {contrato.metros}")
                print(f"Precio por metro: ${contrato.precio:.2f}")
                print(f"Estado del contrato: {contrato.status}\n")
            
            seleccion_contrato = int(input("Seleccione el número del contrato que desea ver en detalle: "))

            if 1 <= seleccion_contrato <= len(cliente_seleccionado.contratos):
                contrato_seleccionado = cliente_seleccionado.contratos[seleccion_contrato - 1]
                print("Detalles del contrato seleccionado:")
                print(f"Empleado: {contrato_seleccionado.empleado}")
                print(f"Metros: {contrato_seleccionado.metros}")
                print(f"Precio por metro: ${contrato_seleccionado.precio:.2f}")
                print(f"Estado del contrato: {contrato_seleccionado.status}")
            else:
                print("Selección de contrato inválida. Intente nuevamente.")
        else:
            print("Selección de cliente inválida. Intente nuevamente.")
    
    def contrato_status(self):
        if not self.clientes:
            print("No hay clientes registrados para buscar contratos.")
            return

        estado_buscado = input("Ingrese el estado del contrato que desea buscar (En Espera o Finalizado): ")
        contratos_encontrados = []

        for cliente in self.clientes:
            for contrato in cliente.contratos:
                if contrato.status.lower() == estado_buscado.lower():
                    contratos_encontrados.append((cliente, contrato))
        
        if not contratos_encontrados:
            print(f"No se encontraron contratos con el estado '{estado_buscado}'.")
            return

        print(f"Contratos con estado '{estado_buscado}':")
        for i, (cliente, contrato) in enumerate(contratos_encontrados, start=1):
            print(f"Contrato {i}:")
            print(f"Cliente: {cliente.nombre}, Identidad: {cliente.identidad}")
            print(f"Empleado: {contrato.empleado}")
            print(f"Metros: {contrato.metros}")
            print(f"Precio por metro: ${contrato.precio:.2f}")
            print(f"Estado del contrato: {contrato.status}\n")
    
    def cambiar_status(self):
        if not self.clientes:
            print("No hay clientes registrados para cambiar el estado de contratos.")
            return

        self.listado_clientes()
        seleccion_cliente = int(input("Seleccione el número de cliente cuyo contrato desea modificar: "))

        if 1 <= seleccion_cliente <= len(self.clientes):
            cliente_seleccionado = self.clientes[seleccion_cliente - 1]
            self.listado_contratos(cliente_seleccionado)
            seleccion_contrato = int(input("Seleccione el número del contrato que desea modificar: "))

            if 1 <= seleccion_contrato <= len(cliente_seleccionado.contratos):
                contrato_seleccionado = cliente_seleccionado.contratos[seleccion_contrato - 1]
                nuevo_estado = input("Ingrese el nuevo estado del contrato: ")
                contrato_seleccionado.status = nuevo_estado
                print(f"El estado del contrato ha sido modificado a '{nuevo_estado}'.")
            else:
                print("Selección de contrato inválida. Intente nuevamente.")
        else:
            print("Selección de cliente inválida. Intente nuevamente.")
    
    def factura_contrato(self):
        
        precio_total = 0 
        for contrato in self.contrato:
            precio_total += contrato.costo * contrato.metros

        return precio_total