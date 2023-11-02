""" INCISO
Un restaurante desea un sistema para almacenar  la comida que prepara,.
de la comida se desea el nombre del plato, el tipo de plato que puede ser ensalada, 
carnes, hamburguesas etc., así mismo la comida tendrá una lista de ingredientes y las cantidades 
que se usa de cada ingrediente la unidad de medida y el costo por unidad de medida.
de cada comida se desea saber la receta, en la cual se describe paso a paso la preparación,
para lo cual se desea el orden en el que se realizan los pasos y la descripción de este.
la forma de ingreso de los datos es que primero ingresan la comida luego, a esta comida 
se le ingresaran los ingredientes mediante otro item del menu, de igual forma se realiza con la receta,
se debera mostrar el listado de todas las comidas y poder ver una comida en especifico
"""

"""
1. Crear tres clases {Comida, Ingredientes, Recetas}
2. Clase Comida con funcion init {nombre, tipo}
3. Clase de Ingredientes contiene una lista {nombre, cantidad, costo, unidad}
4. Clase Receta, seleccionar comida y agregar pasos para hacer la comida
5. Menu de trabajo
"""

class Comida():
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.ingredientes = []  # Agregar una lista para ingredientes
        self.receta = Receta()  # Inicializar la receta

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

class Ingredientes():
    def __init__(self, nombre, cantidad, costo, unidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo
        self.unidad = unidad

class Receta():
    def __init__(self):
        self.pasos = []

    def agregar_pasos(self, orden, descripcion):
        self.pasos.append((orden, descripcion))

class Menu(): 
    def __init__(self):
        self.comidas = []

    def agregar_comida(self):
        nombre = input("Ingrese el nombre del platillo: ")
        tipo = input("Ingrese el tipo de platillo: ")
        nueva_comida = Comida(nombre, tipo)
        self.comidas.append(nueva_comida)
        print(f"El platillo '{nombre}' ha sido registrado de manera exitosa!\n")

    def lista_comidas(self):
        if not self.comidas:
            print(f"No hay platillos registrados")
        else:
            print(f"Listado de platillos: ")
            for i, comida in enumerate(self.comidas, start = 1):
                print(f"{i}. Nombre:{comida.nombre}, Tipo:{comida.tipo}\n")
    
    def agregar_ingredientes(self):
        if not self.comidas:
            print("No hay platillos registrados. Agregue un platillo primero. ")
            return
        
        self.lista_comidas()
        seleccion = int(input("Seleccione el número del platillo al que desea agregar ingredientes: "))

        if 1 <= seleccion <= len(self.comidas):
            comida_seleccionada = self.comidas[seleccion - 1]
            while True:
                nombre = input("Ingrese el nombre del ingrediente (o 'fin' para detenerse): ")
                if nombre.lower() == 'fin':
                    break
                cantidad = float(input("Ingrese la cantidad del ingrediente: "))
                costo = float(input("Ingrese el costo del ingrediente: "))
                unidad = input("Ingrese la unidad de medida del ingrediente: ")
                ingrediente = Ingredientes(nombre, cantidad, costo, unidad)
                comida_seleccionada.agregar_ingrediente(ingrediente)
                print(f"Ingrediente '{nombre}' agregado al platillo '{comida_seleccionada.nombre}'.")

        else:
            print("Selección inválida. Intente nuevamente.")

    def detalle_comida(self):
        if not self.comidas:
            print("No hay platillos registrados.")
            return

        self.lista_comidas()
        seleccion = int(input("Seleccione el número del platillo del que desea ver información detallada: "))

        if 1 <= seleccion <= len(self.comidas):
            comida_seleccionada = self.comidas[seleccion - 1]
            print(f"Información detallada del platillo '{comida_seleccionada.nombre}':")
            print(f"Tipo: {comida_seleccionada.tipo}")
            print("Ingredientes:")
            for ingrediente in comida_seleccionada.ingredientes:
                print(f"- Nombre: {ingrediente.nombre}, Cantidad: {ingrediente.cantidad} por {ingrediente.unidad} unidad, Costo: ${ingrediente.costo} por {ingrediente.unidad} Unidad")
                
            print("\nReceta:")
            for paso in comida_seleccionada.receta.pasos:
                print(f"Paso {paso[0]}: {paso[1]}")

        else:
            print("Selección inválida. Intente nuevamente.")

    def pasos_receta(self):
        if not self.comidas:
            print("No hay platillos registrados. Agregue un platillo primero.")
            return

        self.lista_comidas()
        seleccion = int(input("Seleccione el número del platillo al que desea agregar pasos a la receta: "))

        if 1 <= seleccion <= len(self.comidas):
            comida_seleccionada = self.comidas[seleccion - 1]
            while True:
                orden = int(input("Ingrese el orden del paso (número entero) o '0' para detenerse: "))
                if orden == 0:
                    break
                descripcion = input("Ingrese la descripción del paso: ")
                comida_seleccionada.receta.agregar_pasos(orden, descripcion)
                print(f"Paso {orden} agregado a la receta de '{comida_seleccionada.nombre}'.")
        else:
            print("Selección inválida. Intente nuevamente.")

def main():
    listado_comida = Menu()

    while True:
        print(" ******** MENU ******** ")
        print("1. Agregar platillo")
        print("2. Listado de platillos registrados")
        print("3. Agregar ingrediente a un platillo")
        print("4. Agregar receta para un platillo")
        print("5. Detalles de un platillo")
        print("6. Salir")

        option = input(f"\nSeleccione una opcion a trabajar: ")

        if option == "1":
            listado_comida.agregar_comida()
        elif option == "2":
            listado_comida.lista_comidas()
        elif option == "3":
            listado_comida.agregar_ingredientes()
        elif option == "4":
            listado_comida.pasos_receta()
        elif option == "5":
            listado_comida.detalle_comida()
        elif option == "6":
            print("\n ****** EXIT ******* \n")
            break
        else:
            print("\n ********* Opción no válida. Por favor, seleccione una opción válida. ********* \n")



if __name__ == "__main__":
    main()


