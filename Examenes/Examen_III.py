from abc import ABC, abstractmethod

class Contacto(ABC):
    def __init__(self, nombre, numeros, correos, tipo):
        self.nombre = nombre
        self.numeros = numeros 
        self.correos = correos
        self.tipo = tipo

        self.numeros = []
        self.correos = []

    @abstractmethod
    def generar_key(self):
        pass

class Empresarial(Contacto):
    def __init__(self, nombre, numeros, correos, tipo, rtn ,casaMatriz):
        super().__init__(nombre, numeros, correos, tipo)
        self.rtn = rtn
        self.casaMatriz = casaMatriz

    def generar_key(self):
        return f"{self.rtn}-{self.numeros[0]}"  # Se asume que hay al menos un número


class Familiar(Contacto):
    def __init__(self, nombre, numeros, correos, tipo, tipoFamiliar):
        super().__init__(nombre, numeros, correos, tipo)
        self.tipoFamiliar = tipoFamiliar

    def generar_key(self):
        return f"{self.tipoFamiliar}-{self.nombre}"

class Personal(Contacto):
    def __init__(self, nombre, numeros, correos, tipo, titulo, nickname):
        super().__init__(nombre, numeros, correos, tipo)
        self.titulo = titulo
        self.nickname = nickname

    def generar_key(self):
        if self.correos:
            return f"{self.nickname}-{self.correos[0]}"
        elif self.numeros:
            return f"{self.nickname}-{self.numeros[0][:3]}"
        else:
            return f"{self.nickname}-NoKey"  # Definir un valor predeterminado si no hay correo ni número
class Agenda():
    def __init__(self):
        self.contactos = []

    def add_empresarial (self):
        print("E M P R E S A R I A L")
        nombre = input("Nombre de la empresa: ")
        rtn = input("RTN de la empresa: ")
        casaMatriz = input("Casa Matriz: ")

        numeros = []
        while True:
            numero = input("Numero de telefono (o '0' para detenerse): ")
            if numero == '0':
                break
            numeros.append(numero)

        correos = []
        while True:
            correo = input("Correo electronico (o 'stop' para detenerse): ")
            if correo == 'stop':
                break
            correos.append(correo)

        tipo = "Empresarial" 
        new_empresarial = Empresarial(nombre, numeros, correos, tipo, rtn ,casaMatriz)
        new_empresarial.numeros = numeros       #Almacena los numeros en la lista numeros
        new_empresarial.correos = correos       #Almacena los numeros en la lista de correos
        self.contactos.append(new_empresarial)
        print(f"Contacto {nombre} ha sido ingresado de manera exitosa!")
    
    def lista_contactos(self):
        if not self.contactos:
            print("No hay contactos registrados")
        else:
            total = len(self.contactos)
            print(f"Cantidad total de contactos registrados: {total}")
            for i, contacto in enumerate(self.contactos, start=1):
                key = contacto.generar_key()
                print(f"{i}.    Nombre: {contacto.nombre}       Numeros: {contacto.numeros}     Correos: {contacto.correos}     KEY:{key}")

    def add_familiar (self):
        print("F A M I L I A R")
        nombre = input("Nombre: ")
        tipoFamiliar = input("Tipo Familiar: ")

        numeros = []
        while True:
            numero = input("Numero de telefono (o '0' para detenerse): ")
            if numero == '0':
                break
            numeros.append(numero)

        correos = []
        while True:
            correo = input("Correo electronico (o 'stop' para detenerse): ")
            if correo == 'stop':
                break
            correos.append(correo)

        tipo = "Familiar"

        new_familiar = Familiar(nombre, numeros, correos, tipo, tipoFamiliar)
        new_familiar.numeros = numeros
        new_familiar.correos = correos
        self.contactos.append(new_familiar)
        print(f"Contacto {nombre} ha sido ingresado de manera exitosa!")

    def add_personal (self):
        print("P E R S O N A L")
        nombre = input("Nombre: ")
        titulo = input("Titulo: ")
        nickname = input("NickName: ")

        numeros = []
        while True:
            numero = input("Numero de telefono (o '0' para detenerse): ")
            if numero == '0':
                break
            numeros.append(numero)

        correos = []
        while True:
            correo = input("Correo electronico (o 'stop' para detenerse): ")
            if correo == 'stop':
                break
            correos.append(correo)

        tipo = "Personal"

        new_personal = Personal(nombre, numeros, correos, tipo, titulo, nickname)
        new_personal.numeros = numeros
        new_personal.correos = correos
        self.contactos.append(new_personal)
        print(f"Contacto {nombre} ha sido ingresado de manera exitosa!")


    def eliminar_contactos(self):
        pass

    def details_contactos(self):
        pass
                


def main():
    agenda = Agenda()
    
    while True:
        try:
            
            print("A G E N D A")
            print("Ingresar un contacto")
            print("1. Empresarial")
            print("2. Familiar")
            print("3. Personal")
            print("4. Lista de contactos")
            print("5. Salir")

            option = int(input("Option: "))

            match option:
                case 1:
                    agenda.add_empresarial()
                case 2:
                    agenda.add_familiar()
                case 3:
                    agenda.add_personal()
                case 4:
                    agenda.lista_contactos()
                case 5:
                    break
                case default:
                    print("OPCION NO VALIDA")
        except ValueError:
            print("ERROR, OPCION NO VALIDA")

if __name__ == '__main__':
    main()