## TIPO DE DATOS 
    """
    Mostrando los tipos de variables

    """

    def tipo_dato(dato):
        print (f"la variable es de tipo de dato {type(dato)}")

    entero = 1
    string = "esto es un string"
    float = 1.1
    boolean = True
    list = [entero, string, float]
    dict = {"entero" : entero, "string" : string}
    variable = input("ingrese cualquier tipo de valor : ")

    tipo_dato(entero)
    tipo_dato(string)
    tipo_dato(float)
    tipo_dato(boolean)
    tipo_dato(list)
    tipo_dato(dict)
    tipo_dato(variable)

## DICTIONARY
    """
    CREAR UN DICTIONARY PARA LA SIGUIENTE TABLA:
    SISTEMAS  MATEMATICAS  ELECTRONICA
    IS410     MM202        IE212
    IS513     MM312        IE2O7
    IS601     MM211        TEL201
    """ 

    tabla =[
        {"CARRERA":"SISTEMAS",
        "CLASES" : ['IS410', 'IS513', 'IS601']},
        
        {"CARRERA" : "MATEMATICAS",
        "CLASES" : ["MM202", "MM312", "MM211"]},

        {"CARRERA" : "ELECTRONICA",
        "CLASES" : ["IE212", "IE2O7", "TEL201"]}
    ]

    print(tabla)    

    for carrera in tabla:
        print("Estas son las carreras disponibles hasta el momento: " + carrera['CARRERA'])
        for clases in carrera['CLASES']:
            print(f"clases: {clases}")

## LISTA
    lista = []

    for item in range(0,10):
        lista.append(item + 1)
    
    for item in lista:
        print(item)
    
    lista.reverse()
    
    print(lista)

    print(len(lista))

    busqueda = int(input("Ingrese un numero a buscar: "))

    if lista.index(busqueda):
        print("valor encontrado")

## LISTAS 
    lista = []

    valor = ""

    while (valor != "Parar"):
        valor = input("Ingrese un valor para la lista : ")
        if (valor != "Parar" and len(valor) < 120):
            lista.append(valor)


    for elemento in lista:
        print(str(lista.index(elemento) + 1) + " " + elemento)

## String Upper n Lower
    texto = ""
    seguir = True

    while (seguir):
        texto = input("Ingresar texto para hacerlo mayusculas : ")
        
        if (not (len(texto) == 0 or texto == "" or texto == None or texto == "Parar")):
            print(texto.upper()+"\n")
        elif texto == "Parar":
            seguir = False
        

