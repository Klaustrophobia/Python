"""
Aplicar clases abstractas
Calcular areas de Cuadrado {Lado * Lado}, 
rectangulos {Base x Altura}, 
Circulo {Pi x Radio^2}
"""
from abc import ABC, abstractmethod
import math

class Figura(ABC):
    
    @abstractmethod    
    def calcular_area(self):
        pass
        
    
class Cuadrado(Figura):
    
    def calcular_area(self):
        
        print("Ingrese los datos solicitados del cuadrado en cm: ")
        lado = int(input("Lado: "))
        area = lado * lado 
        print(f"El area del cuadrado es: '{area}'cm \n")

class Rectangulo(Figura):
    
    def calcular_area(self):
        
        print("Ingrese los datos solicitados del Rectangulo en cm: ")
        base = int(input("Base :"))
        altura = int(input("Altura: "))
        area = base * altura
        print(f" El area del rectangulo es '{area}' cm \n")

class Circulo(Figura):
    
    def calcular_area(self):
         
        print("Ingrese los datos solicitados del Circulo en cm: ")
        radio = int(input("Radio: "))
        area = math.pi * radio * radio
        print(f"El area del Circulo es '{area}' cm \n")
        
        
def main():
    cuadrado = Cuadrado()
    rectangulo = Rectangulo()
    circulo = Circulo()
    
    while True:
        try:
            print(" *** MENU *** ")
            print("1. Calcular area de un cuadrado")
            print("2. Calcular area de un rectangulo")
            print("3. Calcular area de un circulo")
            print("4. Salir")
        except:
            print("ERROR DE OPCION")
        else:
            option = int(input("Ingrese la opcion a trabajar: "))
            
            match option:
                case 1:
                    cuadrado.calcular_area()
                case 2:
                    rectangulo.calcular_area()
                case 3:
                    circulo.calcular_area()
                case 4:
                    break
                case default:
                    print("ERROR")
            
    
if __name__ == "__main__":
    main()
    
    
    

        
        