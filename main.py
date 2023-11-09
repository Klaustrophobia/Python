"""
Clases
    Contratos {Clase}
    AseoDomicilio {Clase}
    AseoEmpresarial{Clase}
    AseoAreaVerde{Clase}
    Personas {Clase} -> Heredar -> Empleados {Clase}    
"""
from abc import ABC, abstractclassmethod

class Persona:
    nombre = None
    salario = None
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
         

## Una clase abstracta puede heredar de otra clase abstracta
class Contrato(ABC):
    empleado = None
    metros = None
    cliente = None
    fecha_init = None
    fecha_end = None
    estado = None
    empleados = None
    
    ## CONSTRUCTOR
    def __init__(self, empleado, metros, cliente, fecha_init, fecha_end, estado, empleados):
        self.empleado = empleado
        self.metros = metros    
        self.cliente = cliente
        self.fecha_init = fecha_init
        self.fecha_end = fecha_end
        self.estado = estado
        self.empleados = empleados
        
    ##CLASE CONSTRUCTIR
    @abstractclassmethod
    def set_precio(self):
        pass

class AseoDomicilio(Contrato):
    lavado_planchado = None
    cocinar = None
    cant_banos = None
    cant_habitaciones = None
    
    def __init__(self, lavado_planchado, cocinar, cant_banos, cant_habitaciones, empleado, metros, cliente, fecha_init, fecha_end, estado, empleados):
        super().__init__(empleado, metros, cliente, fecha_init, fecha_end, estado, empleados)
        self.lavado_planchado = lavado_planchado
        self.cocinar = cocinar
        self.cant_banos = cant_banos
        self.cant_habitaciones = cant_habitaciones
    
    def set_precio(self):
        pass
    
    def add_contrato(self):
        print("Ingrese los datos solicitados para el contrato: ")
        empleado = input("Nombre: ")
        metros = int(input("Metros: "))
        cliente = input("Nombre del cliente: ")
        fecha_init = input("Fecha Inicio: ")
        fecha_end = input("Fecha Final: ")
        estado = input("Estado: ")
        empleados = input("")
        
        
        

    