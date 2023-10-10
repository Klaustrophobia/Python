## Condiciones
    """
    if else, is elif else, if if else else

    en el caso de switch se puede programar una funcion con el uso de if o usar el match

    """

    numero1 = int(input("Ingrese numero1 :"))
    numero2 = int(input("Ingrese numero2 :"))

    if numero1 > numero2:
        print("El numero1 es mayor al numero2")
    else : 
        print("El numero2 es igual o mayor al numero1")


    if numero1 > numero2:
        print("El numero1 es mayor que el numero2")
    elif numero1 == numero2: 
        print("El numero1 es igual al numero2")
    else :
        print("El numero2 es mayor al numero1")


    if numero1 > numero2:
        print("El numero1 es mayor que el numero2")
    else :
        if numero1 == numero2: 
            print("El numero1 es igual al numero2")
        else :
            print("El numero2 es mayor al numero1")

    match numero1:
        case 0:
            print("el numero ingresado es 0")
        case 1:
            print("el numero ingresado es 1")
        case 5:
            print("el numero ingresado es 5")        
        case default:
            print("no hay una opcion para el numero igresado, opciones 0,1,5")        

## Condiciones Encadenadas
    Las condiciones encadenadas en Python se refieren a una serie de declaraciones if, elif, y 
    else que se utilizan para evaluar múltiples condiciones en secuencia. 
    Estas condiciones se evalúan de arriba a abajo, y la primera que sea verdadera ejecutará 
    el bloque de código asociado. Si ninguna de las condiciones es verdadera y se proporciona 
    una cláusula else, se ejecutará su bloque de código.

## Condiciones Anidadas
    Las condiciones anidadas se refieren a la práctica de colocar estructuras condicionales 
    dentro de otras estructuras condicionales. Esto se hace utilizando declaraciones 
    if, elif y else dentro de bloques de código ya condicionales. Permite evaluar múltiples 
    condiciones de manera jerárquica.
## Exception Handling
    {try except finally}
    La excepcion finally siempre se va a ejecutar

    El manejo de excepciones en Python se realiza con las cláusulas try, except, y finally. 
    La cláusula try se utiliza para rodear el código que podría generar una excepción. 
    La cláusula except se utiliza para manejar excepciones específicas o genéricas. 
    La cláusula finally es opcional y se ejecuta siempre, independientemente de si se produjo 
    una excepción o no.

## Cortocircuito de expresiones logicas
    El cortocircuito de expresiones lógicas en Python se refiere al comportamiento de las 
    expresiones and y or. Cuando se utiliza and, si la primera condición es falsa, 
    la segunda ni siquiera se evalúa porque la expresión completa será falsa de todas formas. 
    Con or, si la primera condición es verdadera, la segunda ni siquiera se evalúa porque 
    la expresión completa será verdadera de todas formas.

## Guardianes (Warden)
    Un guardian es una expresion que garantiza las evaluaciones 
    de las funciones.

    En Python, los guardianes son expresiones que se utilizan para garantizar 
    que ciertas evaluaciones sean válidas antes de realizar operaciones adicionales. 
    Ayudan a prevenir errores o excepciones en el código. Pueden ser utilizados en 
    combinación con estructuras condicionales como if y elif.

## Funciones {Internas, agregadas por el programador, lambda/Anonymous function}
    Las funciones lambda estan definidas en una linea.

    Comportamientos {Productivas, esteriles}

    En Python, las funciones pueden ser internas (built-in), agregadas por el programador 
    o funciones lambda (también conocidas como funciones anónimas). Las funciones lambda 
    se definen en una sola línea y son útiles para tareas simples y rápidas. Las funciones 
    pueden tener comportamientos productivos (que devuelven un valor) o estériles (que no devuelven un valor).

## Sustentabilidad del codigo
    La sustentabilidad del código se refiere a la capacidad de un programa o proyecto 
    de software para mantenerse y evolucionar con el tiempo. Implica escribir código limpio, 
    bien documentado, modular y fácil de mantener. La sustentabilidad del código es esencial 
    para garantizar que un proyecto siga siendo eficiente y efectivo a medida que crece y cambia.

## Iteraciones
    Las iteraciones en Python se utilizan para repetir un bloque de código varias veces. 
    Pueden implementarse con bucles como for y while. Las iteraciones permiten realizar 
    tareas repetitivas, como procesar elementos de una lista, leer líneas de un archivo o 
    ejecutar un bloque de código hasta que se cumpla una condición específica.
    