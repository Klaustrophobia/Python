"""
class Persona:
    def __init__(self, nombre, apellido, identidad, numCuenta):
        self.nombre = nombre 
        self.apellido = apellido
        self.identidad = identidad
        self.numCuenta = numCuenta

class Docente (Persona):
    def __init__(self, nombre, apellido, identidad, numCuenta, departamento, area, clase):
        super().__init__(nombre, apellido, identidad, numCuenta)
        self.departamento = departamento
        self.area = area
        self.clase = clase

class Alumno(Persona):
    def __init__(self, nombre, apellido, identidad, numCuenta, carrera, clase):
        super().__init__(nombre, apellido, identidad, numCuenta)
        self.carrera = carrera
        self.clase = clase

class Universidad:
    def __init__(self):
        self.docentes = []
        self.alumnos = []

    ##APARTADO DE AGREGAR ESTUDIANTES
    def add_student(self):
        print("Ingrese los datos del estudiante")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        identidad = int(input("Identidad: "))
        numCuenta = int(input("Numero de Cuenta: "))
        carrera = input("Carrera: ")
        clase = input("Clases: ")
        new_student = Alumno(nombre, apellido, identidad, numCuenta, carrera, clase)
        self.alumnos.append(new_student)
        print(f"El alumno '{nombre} {apellido}'ha sido ingresado en la carrera '{carrera}' !")
     
    def list_student(self):
        if not self.alumnos:
            print("No hay Alumnos registrados")
        
        for j, alumno in enumerate(self.alumnos, start = 1):
            print(f"{j}. Nombre:{alumno.nombre}, NumCuenta:{alumno.numCuenta}, Carrera:{alumno.carrera}, Clases:{alumno.clase}")

    ##APARTADO DE AGREGAR DOCENTES
    def add_teacher(self):
        print("Ingrese los datos del docente")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        identidad = int(input("Identidad: "))
        numCuenta = int(input("Numero de Cuenta: "))
        departamento = input("Departamento donde trabaja: ")
        area = input("Area de trabajo: ")
        clase = input("Ingrese las clases que imparte: ")
        new_teacher = Docente(nombre, apellido, identidad, numCuenta, departamento, area, clase)
        self.docentes.append(new_teacher)
        print(f"El docente '{nombre}' del departamento {departamento} ha sido registrado!")
    
    def list_teacher(self):
        if not self.docentes:
            print("NO HAY DOCENTES REGISTRADOS")
        
        for i, docente in enumerate(self.docentes, start = 1):
            print (f"{i}. Nombre: {docente.nombre}, NumCuenta:{docente.numCuenta}, Departamento:{docente.departamento}, Area: {docente.area}, Clases:{docente.clase}")
"""

from universidad import Universidad

def main():

    university = Universidad()

    while True:
        print(" **** M E N U **** ")
        print("1. Agregar Docente")
        print("2. Agregar Alumno")
        print("3. Listado Docente")
        print("4. Listado Alumno")
        print("5. Salir")

        option = int(input("Opcion a trabajar: "))

        match option:
            case 1:
                university.add_teacher()
            case 2:
                university.add_student()
            case 3:
                university.list_teacher()
            case 4:
                university.list_student()
            case 4:
                break
            case default:
                return "ERROR"

if __name__ == "__main__":
    main()