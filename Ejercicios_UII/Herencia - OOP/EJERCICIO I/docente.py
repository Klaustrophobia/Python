from persona import Persona

## INSTANCIAS LA DATOS DE DOCENTE

class Docente (Persona):
    def __init__(self, nombre, apellido, identidad, numCuenta, departamento, area, clase):
        super().__init__(nombre, apellido, identidad, numCuenta)
        self.departamento = departamento
        self.area = area
        self.clase = clase 