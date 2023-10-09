'''

Gestión de Tareas Pendientes

Crea un programa en Python que permita a un usuario gestionar una lista de tareas pendientes. Debes utilizar un diccionario para representar cada tarea con las siguientes propiedades:

descripcion: Una breve descripción de la tarea.
completada: Un valor booleano que indica si la tarea está completada o no.
El programa debe ofrecer las siguientes opciones al usuario:

Agregacar como cr Tarea: Permite al usuario agregar una nueva tarea a la lista. El usuario debe ingresar la descripción de la tarea.

Marcar Tarea como Completada: El usuario puede marcar una tarea como completada. Deberías mostrar una lista numerada de tareas pendientes y permitir al usuario seleccionar la tarea que desea marompletada.

Listar Tareas: Muestra una lista de todas las tareas, indicando si están completadas o no.

Eliminar Tarea: Permite al usuario eliminar una tarea de la lista. Deberías mostrar una lista numerada de tareas pendientes y permitir al usuario seleccionar la tarea que desea eliminar.

Salir: Termina el programa.

'''

## Funciones

class Tarea:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

class ListaTarea:
    def __init__(self):
        self.tareas = []
        self.indice_tarea = 0

    def agregar_tarea(self):
        nombre = input(f"Ingrese el titulo de la tarea a realizar: ")
        descripcion = input(f"Ingrese la descripcion de la tarea a realizar: ")
        nueva_tarea = Tarea(nombre, descripcion)
        self.tareas.append(nueva_tarea)
        print(f"\n ******** La tarea {nombre} fue agregada de manera exitosa! ******** \n")

    def listar_tareas(self):
        if not self.tareas:
            print(f"1No hay tareas registradas")
            return 
        
        print(f"Listado de las tareas agregadas")
        for i, tarea in enumerate(self.tareas, start = 1):
            print(f"\n {i}. Tarea: {tarea.nombre}, Descripcion: {tarea.descripcion} \n")

    def marcar_completada(self, indice):
        if indice >= 1 and indice <= len(self.tareas):
            tarea = self.tareas[indice-1]
            tarea.completada = True
            tarea.completada = self.tareas.pop(indice -1)
            print(f"Tarea {tarea.nombre} fue marcada como completada! ")
        else:
            print("Índice no válido. Por favor, seleccione un número válido de tarea.")

    def tarea_completada(self):
        tareas_completadas = [tarea for tarea in self.tareas if hasattr(tarea, 'completada') and tarea.completada]
        if not tareas_completadas:
            print("No hay tareas completadas.")
        else:
            print("Listado de tareas completadas:")
            for i, tarea in enumerate(tareas_completadas, start=1):
                print(f"\n {i}. Tarea: {tarea.nombre}, Descripción: {tarea.descripcion} \n")

    def eliminar_tarea(self, indice):
        print(f"Que tarea desea eliminar: ")
        for i, tarea in enumerate(self.tareas, start = 1):
            print(f"\n {i}. Tarea: {tarea.nombre}, Descripcion: {tarea.descripcion} \n")
        
        if indice >= 1 and indice <= len(self.tareas):
            tarea_eliminada = self.tareas.pop(indice -1)
            print(f"\n Tarea eliminada: {tarea_eliminada.nombre} \n")
        else:
            print("\n Índice no válido. Por favor, seleccione un número válido de tarea. \n")

def main():

    listado_tareas =ListaTarea()
    while True:
        print("Opciones:")
        print("1. Agregar Tarea")
        print("2. Listar Tareas agregadas")
        print("3. Marcar Tarea como completada")
        print("4. Listado de Tareas completadas")
        print("5. Eliminar Tarea")
        print("6. Salir")

        option = input("Seleccione una opcion: ")

        if option == "1":
            listado_tareas.agregar_tarea()
        elif option == "2":
            listado_tareas.listar_tareas()
        elif option == "3":
            if not listado_tareas.tareas:
                print("\n No hay tareas para completar \n")
            else:
                listado_tareas.listar_tareas()
                indice = int(input("Seleccione el numero de la tarea para marcar como completada: "))
                listado_tareas.marcar_completada(indice)
        elif option == "4":
            listado_tareas.tarea_completada()
        elif option == "5":
            if not listado_tareas.tareas:
                print("No hay tareas registradas para eliminar.")
            else:
                listado_tareas.listar_tareas()
                indice = int(input("Seleccione el número de la tarea a eliminar: "))
                listado_tareas.eliminar_tarea(indice)
        elif option == "6":
            print("\n ****** EXIT ******* \n")
            break
        else:
            print("\n ********* Opción no válida. Por favor, seleccione una opción válida. ********* \n")

if __name__=="__main__":
       main()