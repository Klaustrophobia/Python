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
1. Clase Contrato {Empleado, metros, precio , status}
2. Clase Cliente {Nombre, Identidad}
3. Clase Menu:
    Agregar Contrato
    Agregar Cliente a un contrato
    
"""

class Contrato():
    def __init__(self, empleado, metros, precio, status):
        self.empleado = empleado
        self.metros = metros
        self.precio = precio
        self.status = status
        self.cliente = []

    
    def add_client(self, cliente):
        self.cliente.append(cliente)


class Cliente():
    def __init__(self, nombre, identidad, telefono, correo):
        self.nombre = nombre 
        self.identidad = identidad
        self.telefono = telefono
        self.correo = correo

class Menu():

    def __init__(self):
        self.contratos = []
       
    def list_contract(self):
        if not self.contratos:
            print("No hay contratos registrados")
            return
        for i, contrato in enumerate(self.contratos, start = 1):
            print(f"{i}. Empleado asignado:{contrato.empleado}   Precio:{contrato.precio}")

    def add_contract(self):
        print("POR FAVOR INGRESAR LOS DATOS DE MANERA CAUTELOSA \n")
        print("INFORMACION BASE DEL CONTRATO, LLENAR DE MANERA CAUTELOSA \n")
        empleado = input("Empleado a cargo: ")
        metros = int(input("Metros a trabajar: "))
        precio = int(input("Precio: "))
        status = "En espera"
        new_contract = Contrato(empleado, metros, precio, status)
        self.contratos.append(new_contract)
        print("Contrato asignado de manera exitosa \n")

    def add_cliente(self):
        if not self.contratos:
            print("No hay contratos para asignar a un cliente")
        
        self.list_contract()
        select = int(input("Numero del contrato que desea seleccionar: "))
        if 1 <= select <= len(self.contratos):
            contrato_seleccionado = self.contratos[select - 1]
            print("POR FAVOR INGRESAR LOS DATOS DE MANERA CAUTELOSA \n")
            print("INFORMACION BASE DEL CLIENTE, LLENAR DE MANERA CAUTELOSA \n")
            nombre = input("Nombre del cliente: ")
            identidad = int(input("Identidad: "))
            telefono = int(input("Telefono: "))
            correo = input("Correo: ")
            cliente = Cliente(nombre, identidad, telefono, correo)
            contrato_seleccionado.add_client(cliente)
            print(f"El cliente {nombre} ha sido asignado a su contrato \n")

    def detalle_contrato(self):
        if not self.contratos:
            print("No hay contratos registrados")
        
        self.list_contract()
        selection = int(input("Numero del contrato que desea visualizar: "))
        if 1 <= selection <= len(self.contratos):
            contrato_select = self.contratos [selection - 1]
            print(f"Nombre del empleado encargado: {contrato_select.empleado}")
            print(f"Nombre del cliente: {contrato_select.nombre}")
            print(f"Precio: {contrato_select.precio}")

    def change_status(self):
        if not self.contratos:
            print("No hay contratos registrados")
        
        self.list_contract()
        selection = int(input("Numero del contrato que desea cambiar el estado: "))
        if 1 <= selection <= len(self.contratos):
            contrato_select = self.contratos [selection - 1]
            nuevo_status = input("Estado nuevo: ")
            contrato_select.estado == nuevo_status
            print("Estado cambiado de manera exitosa! \n")

def main():
    menu = Menu()

    while True:
        try:
            print(" +++++++ MENU +++++++ ")
            print("1. Agregar contrato")
            print("2. Agregar cliente")
            print("3. Listado de contratos")
            print("4. Contrato detallado")
            print("5. Cambiar Status")
            print("6. Salir")

            option = int(input("Opcion a realizar: "))

            match option:
                case 1:
                    menu.add_contract()
                case 2:
                    menu.add_cliente()
                case 3:
                    menu.list_contract()
                case 4:
                    menu.detalle_contrato()
                case 5:
                    menu.change_status()
                case 6:
                    break
                case default:
                    print("OPCION NO VALIDA, FAVOR DE VOLVERLO A INTENTAR")

        except ValueError:
            print("OPCION NO VALIDA, FAVOR DE VOLVERLO A INTENTAR")

if __name__ == "__main__":
    main()
