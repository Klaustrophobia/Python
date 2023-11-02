"""
class Nombre_Clase <- Definicion de una clase
puntero self <-

Arfinar atributos clases y de instancia
Constructor y destructor
Metodos y Metodos estaticos
Metodos y clases abstractos
Decorador clase
Setters n Getters
Atributos publicos, privados y protegidos
    
"""


## Clase 
class Automovil:
    puertas = 5
    ruedas = 4

    ## Constructor <- Inicializar valores
    def __init__(self, placa, color, marca, modelo):
        self.placa = placa ## <- A la instancia 'self.placa' agregale la variable 'placa'
        self.color = color
        self.marca = marca
        self.modelo = modelo
        
    def setpuertas(self, puertas):
        self.puertas = puertas
        
    def setruedas(self, ruedas):
         self.ruedas = ruedas
        
    ## Destructor 
    def __del__(self):
        print("Objeto destruido\n")
        
## Clase
class Metodos: 
    ## Constructor 
    def __init__(self, nombre):
        self.nombre = nombre
        
    def metodoinstancia(self):
        print("Este es un metodo de la instancia")
        
        ##La instancia guarda el estado de un objeto ##
        
        
        """
        DECORADOR CLASE
        No pueden acceder a los atributos de la instancia.
        Pero si pueden modificar los atributos de la clase
        """
        
        @classmethod
        def metodoclase(cls):
            print("Metodo de la clase")
        
        """
        DECORADOR ESTATICO
        No pueden modificar el estado ni de la clase ni de la instancia
        """           
        
        @staticmethod
        def metodostatic():
            print("Este es un metodo estatico")
            
        ## Destructor
        def __del__(self):
            print("Objeto destruido")
            
            """
                variable -> publica
                __variable -> privada
                _variable -> protected
            """
            
            