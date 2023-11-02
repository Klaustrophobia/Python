from docente import Docente
from alumno import Alumno

## PROCESA EL INGRESO DE DATOS DE DOCENTES Y ALUMNOS

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
        print(f"El alumno '{nombre} {apellido}'ha sido ingresado en la carrera '{carrera}' ! \n")
     
    def list_student(self):
        if not self.alumnos:
            print("No hay Alumnos registrados \n")
        
        for j, alumno in enumerate(self.alumnos, start = 1):
            print(f"{j}. Nombre:{alumno.nombre}, NumCuenta:{alumno.numCuenta}, Carrera:{alumno.carrera}, Clases:{alumno.clase}")
            print (" \n")
        
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
        print(f"El docente '{nombre}' del departamento '{departamento}' ha sido registrado! \n")
    
    def list_teacher(self):
        if not self.docentes:
            print("NO HAY DOCENTES REGISTRADOS \n")
        
        for i, docente in enumerate(self.docentes, start = 1):
            print (f"{i}. Nombre: {docente.nombre}, NumCuenta:{docente.numCuenta}, Departamento:{docente.departamento}, Area: {docente.area}, Clases:{docente.clase}")
            print (" \n")