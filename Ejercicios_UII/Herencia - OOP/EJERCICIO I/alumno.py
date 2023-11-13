from persona import Persona

## INSTANCIA LOS DATOS DE ALUMNOS

class Alumno(Persona):
    def __init__(self, nombre, apellido, identidad, numCuenta, carrera, clase):
        super().__init__(nombre, apellido, identidad, numCuenta)
        self.carrera = carrera
        self.clase = clase
