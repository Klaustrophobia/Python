'''
Una veterinaria desea realizar un programa para ingresar un control de consultas.
En el programa se ingresaran las mascotas identificadas por un nombre, tipo como perro gato etc, descripcion de porque viene a consulta,
estas mascotas seran atendidas por orden de llegada, el programa contara con un menu en el cual se contara con las opciones
ingresar mascotas, ver listado completo de las mascotas y visualizar el numero de mascota que sigue con su informacion y la opcion salir.
cada vez que se visualiza la mascota esta sera atendida por lo cual cuando se visualice una nuevamente sera la mascota siguiente.
'''
#Definir funcion {Mascota, Consulta}

class Mascota:
    def __init__(self, nombre, tipo, descripcion):
        self.nombre = nombre
        self.tipo = tipo
        self.descripcion = descripcion

class ConsultaVeterinaria:
    def __init__(self):
        self.mascotas = []
        self.indice_mascota_actual = 0

    def ingresar_mascota(self):
        nombre = input("Ingrese el nombre de la mascota: ")
        tipo = input("Ingrese el tipo de mascota (perro, gato, etc.): ")
        descripcion = input("Ingrese la descripción de la consulta: ")
        nueva_mascota = Mascota(nombre, tipo, descripcion)
        self.mascotas.append(nueva_mascota)
        print(f"{nombre} ha sido ingresado a la lista de consultas.")

    def ver_listado_completo(self):
        if not self.mascotas:
            print("No hay mascotas en la lista de consultas.")
            return

        print("Listado completo de mascotas en consulta:")
        for i, mascota in enumerate(self.mascotas, start=1):
            print(f"{i}. Nombre: {mascota.nombre}, Tipo: {mascota.tipo}, Descripción: {mascota.descripcion}")

    def visualizar_siguiente_mascota(self):
        if not self.mascotas:
            print("No hay mascotas en la lista de consultas.")
            return

        if self.indice_mascota_actual < len(self.mascotas):
            mascota_actual = self.mascotas[self.indice_mascota_actual]
            print(f"Número de mascota en consulta: {self.indice_mascota_actual + 1}")
            print(f"Nombre: {mascota_actual.nombre}, Tipo: {mascota_actual.tipo}, Descripción: {mascota_actual.descripcion}")
            self.indice_mascota_actual += 1
        else:
            print("No hay más mascotas en consulta en este momento.")

def main():
    consulta_veterinaria = ConsultaVeterinaria()

    while True:
        print("\nMenu:")
        print("1. Ingresar mascota")
        print("2. Ver listado completo de mascotas")
        print("3. Visualizar el número de mascota que sigue con su información")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consulta_veterinaria.ingresar_mascota()
        elif opcion == "2":
            consulta_veterinaria.ver_listado_completo()
        elif opcion == "3":
            consulta_veterinaria.visualizar_siguiente_mascota()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
