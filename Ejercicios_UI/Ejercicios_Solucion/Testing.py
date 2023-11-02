"""
Las funciones deben estar arriba recordando que al ser lenguaje interpretado
lee linea por linea.
"""

def imprimir (parametro):
    print(parametro)

print("Hola Mundo")
## Comando "Es para imprimir en la CMD"

imprimir("Impresion II")

## Input recibe datos del usuario
input(" Label que va salir en la CMD ")

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


