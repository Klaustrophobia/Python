## PROPUESTA
La universidad desea realizar un sistema para poder llevar el control 
de sus empleados para esto se requiera almacenar los datos generales 
de cada uno mas el numero de empleado, cada empleado puede ser administrativo 
o docente, en caso de ser administrativo tendra un puesto asignado y una oficina, 
en el caso de los docentes tendran un departamento asignado y un horario, 
asi mismo se requiere ingresar a los jefes de cada departamento por lo cual 
este jefe tendra que ser un administrativo y docente al mismo tiempo, en el 
jefe se requiere una fecha de inicio como jefe y una fecha fin, asi como un 
valor que almacenara el bono extra de salario que el tendra, se desean ingresar 
los empleados asi como consultar informacion por departamento e individual por 
numero de empleado.

Empleado {Clase Padre} [Nombre, Apellido, Identidad, NumEmpleado, Salario]
Docente {Clase Hijo I} [DptAsign, Horario]  
Administrativo {Clase Hijo I} [Puesto, Oficina]
Jefe {Clase Hijo II} [FechaInit, FechaEnd, Bono]
Universidad {Clase procesadora}
Main {Clase principal de ejecucion}

## Ejemplo Herencia Multiple

# Clase base Cliente
class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def comprar(self, producto):
        print(f"{self.nombre} ha comprado {producto}")

# Clase base Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f"{self.nombre}: ${self.precio}")

# Clase base Empleado
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def trabajar(self):
        print(f"{self.nombre} está trabajando.")

# Clase derivada Gerente que hereda de Cliente, Producto y Empleado
class Gerente(Cliente, Producto, Empleado):
    def __init__(self, nombre, telefono, salario):
        # Llama a los constructores de las clases base
        Cliente.__init__(self, nombre, telefono)
        Producto.__init__(self, "Producto genérico", 0)
        Empleado.__init__(self, nombre, salario)

    def promocionar(self, producto, descuento):
        producto.precio -= descuento
        print(f"{self.nombre} ha promocionado {producto.nombre}. Ahora cuesta ${producto.precio}")

    def vender(self, cliente, producto):
        print(f"{self.nombre} ha vendido {producto.nombre} a {cliente.nombre} por ${producto.precio}")
        cliente.comprar(producto)

# Crear un cliente
cliente1 = Cliente("Cliente 1", "123-456-7890")

# Crear un producto
producto1 = Producto("Producto 1", 100)

# Crear un empleado
empleado1 = Empleado("Empleado 1", 2500)

# Crear un gerente
gerente1 = Gerente("Gerente 1", "555-123-4567", 5000)

# El gerente promociona un producto
gerente1.promocionar(producto1, 30)

# El cliente compra un producto
cliente1.comprar(producto1)

# El gerente vende un producto al cliente
gerente1.vender(cliente1, producto1)
