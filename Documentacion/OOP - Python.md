## Programacion Orientada a Objetos
    PILARES DE LA POO
    Abstraccion
        -> Desglozar el elemento {sus atributos}
        -> Ver una entidad para representarla como una clase.
        Siendo una clase:
            COMPARTE MISMOS ATRIBUTOS Y COMPARTAMIENTOS "una clase describe un tipo de objeto."

    Encapsulamiento
        -> Capacidad que tiene las clases para ocultar informacion que solo es vital para la misma clase. De esta forma se puede controlar el acceso y evitar en uso inadecuado. {public, private, protected, package}

    Herencia 
        -> Derivar de otra clase. Una clase derivada puede a;adir nuevas variavles y metodos y/o redefinir las variables y metodos heredados.

    Polimorfismo
        -> Una funcion para 2 objetos PERO hace diferentes cosas para los objetos
        -> Implementan una misma interface pueden tratarse de una forma general o individualizada, al mismo tiempo.
    
Los objetos es una instancia de la clase, tiene identidad propia y un estado.

## Representacion clase UML
    compuesto por:
    Nombre
    Atributo {Info del objeto}
    Metodos {acciones del objeto} Tambien puede ser privados.

## Puntero de instancia
    Se refiere a una variable que alamacena la direccion de memoria de un objeto o instancia de ua clase. 
        -> Objeto o instancia
            En programación orientada a objetos, un objeto o instancia es una representación concreta de una clase. Una clase es una plantilla o un plano que define cómo se deben crear objetos. Los objetos son instancias específicas de esa clase y contienen datos (atributos) y métodos (funciones) relacionados.

        -> Puntero
            Un puntero es una variable que almacena una dirección de memoria en lugar de un valor real. En otros términos, es una referencia a la ubicación de un objeto en la memoria del ordenador.
        
        -> Puntero de instancia
            Un puntero de instancia se utiliza para apuntar a un objeto o instancia específica de una clase en la memoria. Esto permite a los programadores manipular y acceder a los atributos y métodos de ese objeto.


## Variable de clase y de instancia
    -> VARIABLE DE INSTANCIA
    Una variable de instancia es una variabl que se declara en una clase y se asocia con cada instancia u objeto creado a partir de esa clase. Cada objeto tiene su propia copia de las variales de instancia, lo que significa que los valores de estas variables pueden variar entre diferentes objetos de las  misma clase.

    Uso: Las variables de instancia almacenan datos específicos para cada objeto creado a partir de la clase. Puedes acceder a ellas utilizando la notación de punto (objeto.variable) después de crear una instancia de la clase.

    class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # 'nombre' es una variable de instancia
        self.edad = edad      # 'edad' es una variable de instancia

    -> VARIAVLE DE CLASE
    Una variable de clase es una variable que se asocia con la propia clase, en lugar de con instancias individuales de la clase. Esto significa que todas las instancias comparten una única copia de la variable de clase, y cualquier cambio en esa variable afecta a todas las instancias de la clase.

    class Coche:
    cantidad_de_ruedas = 4  # 'cantidad_de_ruedas' es una variable de clase

    Las variables de clase se utilizan para almacenar datos que son comunes a todas las instancias de la clase. Puedes acceder a ellas a través de la clase misma, en lugar de través de instancias específicas.

    coche1 = Coche()
    coche2 = Coche()

    print(coche1.cantidad_de_ruedas)  # Accediendo a la variable de clase a través de coche1
    print(coche2.cantidad_de_ruedas)  # Accediendo a la variable de clase a través de coche2

    Coche.cantidad_de_ruedas = 6  # Cambiando la variable de clase a través de la clase
    print(coche1.cantidad_de_ruedas)  # Ahora ambas instancias reflejan el cambio
    print(coche2.cantidad_de_ruedas)

    
## Intancia




