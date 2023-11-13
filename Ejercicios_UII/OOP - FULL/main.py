"""
Clases
    Contratos {Clase}
    AseoDomicilio {Clase}
    AseoEmpresarial{Clase}
    AseoAreaVerde{Clase}
    Empleados {Clase}
    Utilidad {Clase}    
"""
from abc import ABC, abstractmethod

class Utilidad:
    @staticmethod
    def calcular_impuesto(salario):
        if salario > 5000:
            return salario * 0.12
        else:
            return 500

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Contrato(ABC):
    def __init__(self, empleado, metros, cliente, fecha_init, fecha_end, estado, cant_empleados):
        self.empleado = empleado
        self.metros = metros
        self.cliente = cliente
        self.fecha_init = fecha_init
        self.fecha_end = fecha_end
        self.estado = estado
        self.cant_empleados = cant_empleados

    @abstractmethod
    def set_precio(self):
        pass


class AseoDomicilio(Contrato):
    def __init__(self, empleado, metros, cliente, fecha_init, fecha_end, estado, cant_empleados, lavado_planchado, cocinar, cant_banos, cant_habitaciones):
        super().__init__(empleado, metros, cliente, fecha_init, fecha_end, estado, cant_empleados)
        self.lavado_planchado = lavado_planchado
        self.cocinar = cocinar
        self.cant_banos = cant_banos
        self.cant_habitaciones = cant_habitaciones

    def set_precio(self):
        total = 0
        for empleado in self.empleados:
            total += empleado.salario
        
        self.precio= (self.emp_responsable.salario + total) * 2 + Utilidad
        return self.precio

class AseoEmpresarial(Contrato):
    def __init__(self, empleado, metros, cliente, fecha_init, fecha_end, estado, cant_empleados, mesero, cant_meseros, cant_banos, cant_habitaciones, quimicos):
        super().__init__(empleado, metros, cliente, fecha_init, fecha_end, estado, cant_empleados)
        self.mesero = mesero
        self.cant_meseros = cant_meseros
        self.cant_banos = cant_banos
        self.cant_habitaciones = cant_habitaciones
        self.quimicos = quimicos

    def set_precio(self):
        total = 0
        for empleado in self.empleados:
            total += empleado.salario
        
        self.precio= (self.emp_responsable.salario + total) * 2 + Utilidad
        return self.precio

class AseoAreaVerde(Contrato):
    def __init__(self, quimicos, talado, jardineria, empleado, metros, cliente, fecha_init, fecha_end, estado, cant_empleados):
        super().__init__(empleado, metros, cliente, fecha_init, fecha_end, estado, cant_empleados)
        self.quimicos = quimicos 
        self.talado = talado
        self.jardineria = jardineria

    def set_precio(self):
        total = 0
        for empleado in self.empleados:
            total += empleado.salario
        
        self.precio= (self.emp_responsable.salario + total) * 2 + Utilidad
        return self.precio

class Menu:
    def __init__(self):
        self.contratoDomicilio = []
        self.contratoEmpresarial = []
        self.contratoAreaVerde = []

    def add_contrato_domicilio(self):
        print("Ingrese los datos solicitados para el contrato: ")
        empleado = input("Nombre del empleado-lider: ")
        metros = int(input("Metros: "))
        cliente = input("Nombre del cliente: ")
        fecha_init = input("Fecha Inicio: ")
        fecha_end = input("Fecha Final: ")
        estado = input("Estado: ")
        cant_empleados = input("Cantidad de empleados a trabajar: ")
        lavado_planchado = input("¿Lavado y planchado incluido? (si/no): ").lower() == 'si'
        cocinar = input("Requiere cocinar (si/no): ").lower() == 'si'
        cant_banos = int(input("Ingrese la cantidad de banos: "))
        cant_habitaciones = int(input("Ingrese la cantidad de habitaciones: "))
        new_contrato = AseoDomicilio(empleado, metros, cliente, fecha_init, fecha_end, estado, cant_empleados, lavado_planchado, cocinar, cant_banos, cant_habitaciones)
        self.contratoDomicilio.append(new_contrato)
        print("Contrato de aseo a domicilio registrado de manera exitosa")

    def add_contrato_empresarial(self):
        print("Ingrese los datos solicitados para el contrato: ")
        empleado = input("Nombre del empleado-lider: ")
        metros = int(input("Metros: "))
        cliente = input("Nombre del cliente: ")
        fecha_init = input("Fecha Inicio: ")
        fecha_end = input("Fecha Final: ")
        estado = input("Estado: ")
        cant_empleados = input("Cantidad de empleados a trabajar: ")

        mesero = input("Requiere mesero (si/no): ").lower() == 'si'
        if mesero:
            cant_meseros = int(input("Ingrese la cantidad de meseros necesarios: "))
        else:
            cant_meseros = 0

        cant_banos = int(input("Ingrese la cantidad de banos: "))
        cant_habitaciones = int(input("Ingrese la cantidad de habitaciones: "))

        quimicos = input("Requiere uso de quimicos (si/no): ").lower() == "si"

        new_contrato = AseoEmpresarial(empleado, metros, cliente, fecha_init, fecha_end, estado, cant_empleados, mesero, cant_meseros, cant_banos, cant_habitaciones, quimicos)
        self.contratoEmpresarial.append(new_contrato)

    def add_contrato_AreaVerde(self):
        print("Ingrese los datos solicitados para el contrato: ")
        empleado = input("Nombre del empleado-lider: ")
        metros = int(input("Metros: "))
        cliente = input("Nombre del cliente: ")
        fecha_init = input("Fecha Inicio: ")
        fecha_end = input("Fecha Final: ")
        estado = input("Estado: ")
        cant_empleados = input("Cantidad de empleados a trabajar: ")
        quimicos = input("Requiere uso de quimicos (si/no): ").lower() == "si"
        talado = input("Requiere talado de arboles(si/no): ").lower() == "si"
        jardineria = input("Requiere uso de servicio de jardineria (si/no): ").lower() == "si"

        new_contrato = AseoAreaVerde(empleado, metros, cliente, fecha_init, fecha_end, estado, cant_empleados, quimicos, talado, jardineria)
        self.contratoAreaVerde.append(new_contrato)

    def cambiar_estado(self):
        tipo_contrato = input("Ingrese el tipo de contrato (domicilio/empresarial/areaverde): ").lower()

        if tipo_contrato == "domicilio":
            contratos = self.contratoDomicilio
        elif tipo_contrato == "empresarial":
            contratos = self.contratoEmpresarial
        elif tipo_contrato == "areaverde":
            contratos = self.contratoAreaVerde
        else: 
            print("Tipo de contrato no válido.")
            return
        
        if not contratos:
            print("No hay contratos de este tipo para cambiar estado.")
            return

        print("Contratos disponibles:")
        for i, contrato in enumerate(contratos):
            print(f"{i + 1}. {contrato.cliente} - Estado: {contrato.estado}")

        try:
            indice_contrato = int(input("Ingrese el numero del contrato: "))
            if 0 <= indice_contrato < len(contratos):
                nuevo_estado = input("Ingrese el nuevo estado del contrato: ")
                contratos[indice_contrato].estado = nuevo_estado
                print("Estado del contrato modificado exitosamente")
            else:
                print("Numero de contrato no valido")
        except ValueError:
            print("Entrada no valida. Ingrese un numero valido.")

    def precio_contrato(self):
        tipo_contrato = input("Ingrese el tipo de contrato (domicilio/empresarial/areaverde): ").lower()

        if tipo_contrato == "domicilio":
            contratos = self.contratoDomicilio
        elif tipo_contrato == "empresarial":
            contratos = self.contratoEmpresarial
        elif contratos == "areaverde":
            contratos = self.contratoAreaVerde
        else: 
            print("Tipo de contrato no válido.")
            return
        
        if not contratos:
            print("No hay contratos de este tipo para cambiar estado.")
            return

        print("Contratos disponibles:")
        for i, contrato in enumerate(contratos):
            print(f"{i + 1}. {contrato.cliente} - Estado: {contrato.estado}")

        try:
            indice_contrato = int(input("Ingrese el numero del contrato: "))
            if 0 <= indice_contrato < len(contratos):
                nuevo_estado = input("Ingrese el nuevo estado del contrato: ")
                contratos[indice_contrato].estado = nuevo_estado
                print("Estado del contrato modificado exitosamente")
            else:
                print("Numero de contrato no valido")
        except ValueError:
            print("Entrada no valida. Ingrese un numero valido.")





def main():
    menu = Menu()

    while True:
        try:
            print(" **** MENU PRINCIPAL **** ")
            print("1. Agregar un contrato de aseo domiciliario")
            print("2. Agregar un contrato de aseo empresarial")
            print("3. Agregar un contrato de aseo de area verde")
            print("4. Cambiar el estado de un contrato")
            print("5. Precio Total de un contrato")
            print("6. Salir")
        
        except:
            print("ERROR")

        else: 
            option = int(input("Ingrese la opcion: "))

            match option:
                case 1:
                    menu.add_contrato_domicilio()
                case 2:
                    menu.add_contrato_empresarial()
                case 3:
                    menu.add_contrato_AreaVerde()
                case 4:
                    menu.cambiar_estado()
                case 5:
                    menu.precio_contrato()
                case 6:
                    break
                case default:
                    print("OPCION NO VALIDA")


if __name__ == "__main__":
    main()