"""
La empresa de transporte X requiere llevar un control de su flota 
de automoviles como de sus conductores, para lo cual requiere un 
sistema donde se puedan ingresar los datos de los automoviles como 
ser placa, marca, modelo, color y si es de transporte de personas o 
de cargas, asi mismo de los conductores se requiere su numero de identidad 
y sus nombres y apellidos, se requiere considerar que no se debera ingresar 
un automovil o un conductor si este ya fue ingresado, realizar el 
trabajo utlizando POO. 
"""

class Automovil():
    def __init__(self, placa, marca, modelo, color, tipo):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.tipo = tipo
        self.conductor = []

    def add_driver(self, conductor):
        self.conductor.append(conductor)

class Conductor():
    def __init__(self, nombre, apellido, identidad, telefono):
        self.nombre = nombre 
        self.apellido = apellido
        self.identidad = identidad
        self.telefono = telefono
    
class Menu():
    def __init__(self):
        self.automoviles = []

    def add_automovil(self):
        print("FAVOR DE INGRESAR DE MANERA CAUTELOSA LOS DATOS DEL PRODUCTO")
        print("V E H I C U L O ")

        placa = input("Placa del vehiculo: ")

        if any(automovil.placa == placa for automovil in self.automoviles):
            print("Este vehiculo ya fue ingresado")
            return
        
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        color = input("Color: ")
        tipo = input("Tipo de vehiculo: ")

        add_vehiculo = Automovil(placa, marca, modelo, color, tipo)
        self.automoviles.append(add_vehiculo)

    def add_conductor(self):
        if not self.automoviles:
            print("No hay vehiculos para asignar a un conductor")

        self.automoviles()
        select = int(input("Seleccione un vehiculo para asignarle al conductor: "))
        
        if 1 <= select <= len(self.automoviles):
            automovil_select = self.automoviles[select - 1]
            print("Ingrese los datos del conductor de manera cautelosa")
            nombre = input("Nombre del conductor: ")
            apellido = input("Apellido del conductor: ")
            identidad = int(input("Identidad: "))
            telefono = int(input("Telefono: "))

            if any(conductor.identidad == identidad for conductor in self.conductor):
                print("Este conductor ya existe")
                return
            
            conductor = Conductor(nombre, apellido, identidad, telefono)
            automovil_select.add_conductor(conductor)
            
