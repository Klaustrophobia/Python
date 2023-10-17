"""
Ejercicio: Sistema de Gestión de Recetas de un Restaurante

Un restaurante desea desarrollar un sistema de gestión de recetas para sus platos. Cada plato tiene los siguientes atributos:

-Nombre del plato.
-Tipo de plato (ensalada, carnes, hamburguesas, etc.).
-Lista de ingredientes con cantidades, unidad de medida y costo por unidad de medida.
-Receta que describe paso a paso la preparación, con el orden y la descripción de cada paso.

Tu tarea es crear un programa en Python que permita al restaurante:

- Registrar nuevos platos con sus respectivos ingredientes y recetas.
- Ver un listado de todos los platos registrados.
- Ver los detalles de un plato específico, incluyendo ingredientes y la receta.
- Modificar o eliminar platos existentes.
- Calcular el costo total de un plato basado en los costos de los ingredientes.
- Exportar la información de los platos a un archivo para su respaldo.

Consideraciones adicionales:

- Debes utilizar clases y objetos para representar platos, ingredientes y recetas.
- Implementa un menú que permita al usuario seleccionar las acciones a realizar.
- Utiliza estructuras de datos adecuadas para almacenar la información de los platos, ingredientes y recetas.
- Asegúrate de gestionar los datos de manera eficiente y manejar posibles errores del usuario.
- Proporciona una opción para guardar la información en un archivo (por ejemplo, en formato JSON) y cargarla cuando se inicie el programa nuevamente.
"""

class Platillo():
    def __init__(self, nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
        # Lista de ingredientes
        self.ingredientes = []
        # Recetas
        self.receta = Receta()

    # Agregar los ingredientes al platillo
    def agregar_ingrediente(self, ingrediente): #Esta función nos permite agregar ingredientes a la lista de ingredientes del plato. 
        self.ingredientes.append(ingrediente)    #Cuando la llamamos y le damos un ingrediente, lo guardará en la lista de ingredientes.


class Ingredientes():
    def __init__(self, nombre, cantidad, unidad, costo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad = unidad
        self.costo = costo

class Receta():
    def __init__(self):
        self.pasos = [] #Lista que registra los pasos

    def agregar_pasos(self, paso, descripcion):
        self.pasos.append(paso, descripcion) 

class Menu():
    # Inicializar una lista donde se almacenaran las comidas ingresadas
    def __init__(self):
        self.comidas = []
    
    def agregar_comidas(self): 
        nombre = input("Por favor ingresar el nombre del platillo: ")
        tipo = input("Ingresar el tipo de platillo: ")
        nueva_comida = Platillo(nombre, tipo)
        self.comidas.append(nueva_comida)
        print(f"El platillo '{nombre}' fue registado de manera exitosa!\n")
    
    def lista_comidas(self):
        if not self.comidas:
            print("No hay platillos registrados, volver a intentar.")
            return 
        for i, comida in enumerate(self.comidas, start = 1 ):
            print(f"{i}. Nombre:{comida.nombre}, Tipo:{comida.tipo}\n")

    
    def agregar_ingredientes(self):
        if not self.comidas:
            print("No hay platillos registrados, volver a intentar.")
            return

        self.lista_comidas()
        seleccion = int(input("Seleccione el platillo que desea agregar ingredientes: ")) 
        
        if 1 <= seleccion <= len(self.comidas):
            comida_seleccionada = self.comidas[seleccion - 1]
            while True:
                nombre = input("Ingresar el nombre del ingrediente [Escribir 'fin' para detenerse]: ")
                if nombre.lower() =='fin':
                    break
                cantidad = float(input("Ingrese la cantidad a utilizar: "))
                unidad = input("Ingrese la unidades a utilizar 'Ejemplo : 2 tazas, 1/4 de taza': ")
                costo = float(input("Ingrese el costo por unidad del ingrediente: "))
                ingrediente = Ingredientes(nombre, cantidad, unidad, costo)
                comida_seleccionada.agregar_ingrediente(ingrediente)
                print(f"Ingrediente '{nombre}' agregado al platillo \n")
    
    def agregar_receta(self):
        if not self.comidas:
            print("No hay platillos registrados. Agregue un platillo")
            return
        
        self.lista_comidas()
        seleccion = int(input("Seleccione el platillo que desea agregar una receta: "))

        if 1 <= seleccion <= len(self.comidas):
            comida_seleccionada = self.comidas[seleccion - 1]
            orden = 1 #Inicializa el orden de pasos en 1
            while True:
                descripcion = input(f"Ingrese la descripción del paso {orden} (o 'parar' para detenerse): ")
                if descripcion.lower() == 'parar':
                    break
                comida_seleccionada.receta.agregar_pasos(orden, descripcion)
            print(f"Paso {orden} agregado a la receta de '{comida_seleccionada.nombre}'.")
            orden += 1  # Incrementa el orden para el próximo paso
        else:
            print("Selección inválida. Intente nuevamente.")

    def detalle_comida(self):
        if not self.comidas:
            print("No hay platillos registrados!")

        self.lista_comidas()
        seleccion = int(input("Seleccione el platillo que desea ver sus detalles: "))

        if 1 <= seleccion <= len(self.comidas):
            comida_seleccionada = self.comidas[seleccion-1]
            print(f"Informacion detallada del platillo '{comida_seleccionada.nombre}' ")
            print(f"Tipo: {comida_seleccionada.tipo}")
            print("Ingredientes: ")
            for ingrediente in comida_seleccionada.ingredientes:
                print(f"- Nombre: {ingrediente.nombre},  Cantidad: {ingrediente.cantidad}, Unidades: {ingrediente.unidad}, Costo: {ingrediente.costo}\n") 
                
            print("Receta:\n")
            for orden, descripcion in comida_seleccionada.receta.pasos:
                print(f"Paso {orden}: {descripcion} \n")


    def eliminar_comida(self):
        if not self.comidas:
            print("No hay platillos registrados!")
        
        self.lista_comidas()
        seleccion = int(input("Seleccione el platillo que desea eliminar: "))

        if seleccion >= 1 and seleccion <= len(self.comidas):
            comida_seleccionada = self.comidas.pop(seleccion - 1)
            print(f" El platillo '{comida_seleccionada.nombre}' ha sido eliminada con exito!\n")

        else:
            print("Opcion no valida. Seleccione un numero valido de platillo!\n")

    ## MODIFICACIONES ##
    def modificar_comida(self):
        self.lista_comidas()
        seleccion = int(input("seleccione el platillo que desea modificar: "))

        if 1 <= seleccion <= len(self.comidas):
            comida_seleccionada = self.comidas[seleccion - 1]
            print(f"Modificando el platillo '{comida_seleccionada.nombre}':")
            while True:
                print(" ******** Modificar Platillo ******** ")
                print("1. Modificar nombre del platillo")
                print("2. Modificar tipo del platillo")
                print("3. Modificar ingredientes")
                print("4. Modificar receta")
                print("5. Volver al menú principal")
                
                option = int(input("Seleccione una opción: "))

                match option:
                    case 1:
                        nuevo_nombre = input("Ingrese el nuevo nombre del platillo: ")
                        comida_seleccionada.nombre =  nuevo_nombre
                    case 2:
                        nuevo_tipo = input("Ingrese el nuevo tipo de platillo: ")
                        comida_seleccionada.tipo = nuevo_tipo
                    case 3:
                        self.modificar_ingrediente(comida_seleccionada)

    def modificar_ingrediente(self, platillo):
        print(f"Modificando ingredientes del platillo '{platillo.nombre}':")
        
        while True:
            print(" ******** Modificar Ingredientes ******** ")
            print("1. Agregar un ingrediente")
            print("2. Eliminar un ingrediente")
            print("3. Volver al menú anterior")
            
            option = input("Seleccione una opción: ")

            match option:
                case 1:
                    nombre = input("Ingrese el nombre del nuevo ingrediente: ")
                    cantidad = float(input("Ingrese la cantidad del ingrediente: "))
                    costo = float(input("Ingrese el costo del ingrediente: "))
                    unidad = input("Ingrese la unidad de medida del ingrediente: ")
                    nuevo_ingrediente = Ingredientes(nombre, cantidad, costo, unidad)
                    platillo.agregar_ingrediente(nuevo_ingrediente)
                    print(f"Ingrediente '{nombre}' agregado al platillo '{platillo.nombre}'.")
                    
                case 2:
                    if platillo.ingredientes:
                        print("Seleccione el ingrediente a eliminar:")
                        for i, ingrediente in enumerate(platillo.ingredientes, start=1):
                            print(f"{i}. Nombre: {ingrediente.nombre}, Cantidad: {ingrediente.cantidad} {ingrediente.unidad}, Costo: ${ingrediente.costo} por {ingrediente.unidad}")
                        seleccion = int(input("Seleccione el número del ingrediente a eliminar: "))
                        if 1 <= seleccion <= len(platillo.ingredientes):
                            ingrediente_eliminado = platillo.ingredientes.pop(seleccion - 1)
                            print(f"Ingrediente '{ingrediente_eliminado.nombre}' eliminado del platillo '{platillo.nombre}'.")
                        else:
                            print("Selección inválida. Intente nuevamente.")
                    else:
                       print("El platillo no tiene ingredientes para eliminar.") 
                
                case 3:
                    break

                case default:
                     print("XXXXX Opcion no valida XXXXX")
        
    def modificar_receta(self, platillo):
        print(f"Modificando la receta del platillo '{platillo.nombre}'")
        
        while True:
            print(" ******** Modificar Receta ******** ")
            print("1. Agregar un paso")
            print("2. Eliminar un paso")
            print("3. Modificar un paso")
            print("4. Volver al menú anterior")

            option = int(input("Seleccione una opcion: "))

            match option:
                case 1:
                    orden = len(platillo.receta.pasos) + 1
                    descripcion = input("Ingrese la descripción del nuevo paso: ")
                    platillo.receta.agregar_pasos(orden, descripcion)
                    print(f"Paso {orden} agregado a la receta del platillo '{platillo.nombre}'.")
                case 2:
                    if platillo.receta.pasos:
                        print("Seleccione el paso a eliminar:")
                        for orden, descripcion in platillo.receta.pasos:
                            print(f"{orden}. {descripcion}")
                        seleccion = int(input("Seleccione el número del paso a eliminar: "))
                        if 1 <= seleccion <= len(platillo.receta.pasos):
                            platillo.receta.pasos = [(o, d) for o, d in platillo.receta.pasos if o != seleccion]
                            print(f"Paso {seleccion} eliminado de la receta del platillo '{platillo.nombre}'.")
                        else:
                            print("Selección inválida. Intente nuevamente.")
                    else:
                        print("La receta del platillo no tiene pasos para eliminar.")

                case 3: 
                    if platillo.receta.pasos:
                        print("Seleccione el paso a modificar:")
                        for orden, descripcion in platillo.receta.pasos:
                            print(f"{orden}. {descripcion}")
                        seleccion = int(input("Seleccione el número del paso a modificar: "))
                        if 1 <= seleccion <= len(platillo.receta.pasos):
                            nueva_descripcion = input("Ingrese la nueva descripción para el paso: ")
                            platillo.receta.pasos = [(o, d) if o != seleccion else (o, nueva_descripcion) for o, d in platillo.receta.pasos]
                            print(f"Paso {seleccion} modificado en la receta del platillo '{platillo.nombre}'.")
                        else:
                            print("Selección inválida. Intente nuevamente.")
                    else:
                        print("La receta del platillo no tiene pasos para modificar.")
                
                case 4:
                    break

                case default:
                    print("XXXXX Opcion no valida XXXXX")


    def costo_comida(self):
         if not self.comidas:
            print("No hay platillos registrados.")
            return

         for comida in self.comidas:
            costo_comida = 0
            print(f"Costo de '{comida.nombre}':")

            for ingrediente in comida.ingredientes:
                costo_ingrediente = ingrediente.cantidad * ingrediente.costo
                print(f"- {ingrediente.nombre}: ${costo_ingrediente:.2f}") #:.2f se utiliza para formatear el costo como un número decimal con dos decimales.
                costo_comida += costo_ingrediente

            print(f"Costo total de '{comida.nombre}': ${costo_comida:.2f}\n")

    # Exoortar informacion a un excel:

def main():
    menu = Menu()

    while True:
        print(" +++++++ MENU +++++++ ")
        print("1. Ingresar un platillo")
        print("2. Agregar ingredientes a un platillo")
        print("3. Agregar recetas a un platillo")
        print("4. Listado de todos los platillos")
        print("5. Detalle de un platillo")
        print("6. Eliminar un platillo")
        print("7. Modificar un platillo")
        print("8. Costo de un platillo")
        print("9. Exportar listado de un platillo a un excel")
        print("10. Salir")

        option = int(input("Elija un opcion: "))

        match option:
            case 1:
                menu.agregar_comidas()
            case 2: 
                menu.agregar_ingredientes()
            case 3:
                menu.agregar_receta()
            case 4:
                menu.lista_comidas()
            case 5:
                menu.detalle_comida()
            case 6: 
                menu.eliminar_comida()
            case 7:
                menu.modificar_comida()
            case 8:
                menu.costo_comida()
            case 10:
                print("****** Hasta Luego ******")
                break
            case default:
                print("XXXXX Opcion no valida XXXXX")

            



if __name__ == "__main__":
    main()
