## CLASE PLANTILLA
class Empleado:
    def __init__(self, nombre, apellido, identidad, numEmpleado, salario):
        self.nombre = nombre 
        self.apellido = apellido
        self.identidad = identidad
        self.numEmpleado = numEmpleado
        self.salario = salario

## CLASES CON HERENCIA 
class Docente(Empleado):
    def __init__(self, nombre, apellido, identidad, numEmpleado, salario, departamento, horario):
        super().__init__( nombre, apellido, identidad, numEmpleado, salario)
        self.departamento = departamento 
        self.horario = horario

class Administrativo(Empleado):
    def __init__(self, nombre, apellido, identidad, numEmpleado, salario, puesto, oficina):
        super().__init__( nombre, apellido, identidad, numEmpleado, salario)
        self.puesto = puesto
        self.oficina = oficina

## CLASE CON HERENCIA MULTIPLE
"""class Jefe(Docente, Administrativo):
    class Jefe(Docente, Administrativo):
        def __init__(self, nombre, apellido, identidad, numEmpleado, salario, oficina, departamento, horario, fechaInit, fechaEnd, bono, salarioNeto):
            super().__init__( nombre, apellido, identidad, numEmpleado, salario)
            # Inicializa las propiedades específicas de Jefe
            self.oficina = oficina
            self.departamento = departamento
            self.horario = horario
            self.fechaInit = fechaInit
            self.fechaEnd = fechaEnd
            self.bono = bono
            self.salarioNeto = salarioNeto
"""
class Jefe(Docente, Administrativo):
    def __init__(self, nombre, apellido, identidad, numEmpleado, salario, puesto, oficina, departamento, horario, fechaInit, fechaEnd, bono):
        Docente.__init__(self, nombre, apellido, identidad, numEmpleado, salario, departamento, horario)
        Administrativo.__init__(self, nombre, apellido, identidad, numEmpleado, salario, puesto, oficina)
        self.fechaInit = fechaInit
        self.fechaEnd = fechaEnd
        self.bono = bono
        # Calcula el salario neto como el salario base más el bono
        self.salarioNeto = salario + bono




## CLASE PROCESADORA DE INFORMACION
class Universidad:
    def __init__(self):
        ##INICIALIZAR LISTAS
        self.docentes = []
        self.admins = []
        self.jefes = []

    ##INGRESAR DATOS DEL PERSONAL
    def add_teacher(self):
        print("Ingrese los datos del personal docente")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        identidad = int(input("Identidad: "))
        numEmpleado = int(input("Numero de Empleado: "))
        salario = int(input("Salario: "))
        departamento = input("Departamento: ")
        horario = input("Horario: ")
        new_teacher = Docente(nombre, apellido, identidad, numEmpleado, salario, departamento, horario)
        self.docentes.append(new_teacher)
        print(f"El personal docente '{nombre}' del dpto '{departamento}' ha sido ingresado! \n")

    
    def add_admin(self):
        print("Ingrese los datos del personal administrativo")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        identidad = int(input("Identidad: "))
        numEmpleado = int(input("Numero de Empleado: "))
        salario = int(input("Salario: "))
        puesto = input("Puesto que ejerce: ")
        oficina = input("Oficina: ")
        new_admin = Administrativo(nombre, apellido, identidad, numEmpleado, salario, puesto, oficina)
        self.admins.append(new_admin)
        print(f"El personal administrativo '{nombre}' del puesto '{puesto}' ha sido ingresado! \n")

    def add_boss(self):
        print("Ingrese los datos de los jefes de departamento")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        identidad = int(input("Identidad: "))
        numEmpleado = int(input("Numero de Empleado: "))
        salario = int(input("Salario: "))
        oficina = input("Oficina: ")
        departamento = input("Departamento: ")
        horario = input("Horario: ")
        fechaInit = input("Fecha Inicial como jefe: ")
        fechaEnd = input("Fecha Final como jefe: ")
        bono = salario*0.30
        ## salarioNeto = bono + salario
        new_boss = Jefe(nombre, apellido, identidad, numEmpleado, salario, oficina, departamento, horario, fechaInit, fechaEnd, bono)
        self.jefes.append(new_boss)
        print(f"El jefe '{nombre}' del departamento '{departamento}' ha sido ingresado! \n")

    ## IMPRIMIR LISTADO DEL PERSONAL
    def list_teacher(self):
        if not self.docentes:
            print("NO HAY DOCENTES REGISTRADOS \n")
         
        for i, docente in enumerate (self.docentes, start = 1):
            print(f"{i}. Nombre: {docente.nombre}   NumEmpleado: {docente.numEmpleado}  Departamento: {docente.departamento}    Horario: {docente.horario}")

    def list_admin(self):
        if not self.admins:
            print("NO HAY PERSONAL ADMINSTRATIVO REGISTRADOS \n")
         
        for i, admin in enumerate (self.admins, start = 1):
            print(f"{i}. Nombre: {admin.nombre}   NumEmpleado: {admin.numEmpleado}  Puesto: {admin.puesto}    Oficina: {admin.oficina}")         
    
    def list_boss(self):
        if not self.jefes:
            print("NO HAY JEFES REGISTRADOS \n")
         
        for i, jefe in enumerate (self.jefes, start = 1):
            print(f"{i}. Nombre: {jefe.nombre}   NumEmpleado: {jefe.numEmpleado}  departamento: {jefe.departamento}    Oficina: {jefe.oficina}  Horario: {jefe.horario}     FechaInit: {jefe.fechaInit}     FechaEnd: {jefe.fechaEnd}   Salario: {jefe.salario}     Bono: {jefe.bono}   SalarioNeto: {jefe.salarioNeto}")         

## MAIN
def main():
    university = Universidad()

    while True:
        print(" **** M E N U **** ")
        print("1. Agregar Docente")
        print("2. Agregar Administrativo")
        print("3. Agregar Jefe de departamento")
        print("4. Listado personal docente")
        print("5. Listado personal administrativo")
        print("6. Listado de Jefes de departamento")
        print("7. Salir")

        option = int(input("Opcion a ejercer: "))

        match option:
            case 1:
                university.add_teacher()
            case 2:
                university.add_admin()
            case 3:
                university.add_boss()
            case 4:
                university.list_teacher()
            case 5: 
                university.list_admin()
            case 6:
                university.list_boss()
            case 7:
                break
            case default:
                print("ERROR DE OPCION")

if __name__ == "__main__":
    main()


