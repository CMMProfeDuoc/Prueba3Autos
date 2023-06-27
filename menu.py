#ejemplo Menu
#Puede copiar esto si estima conveniente

from autoHerramientas import *

#Con esto puede llamar a cualquier funcion creada en prueba.py
from prueba import *

#lista de autos
lista_autos = obtenerAutos("Autos2")

opciones_menu = [
    "Opcion 1",
    "Opcion 2",
    "Opcion 3",
    "Opcion 4",
#agregar más opciones de forma similar
]
opciones_menu.append("Salir")

while (True):
    #Mostrar Menu
    for i, opcion in enumerate(opciones_menu):
        print(i+1,". ",opcion, sep="")

    #Seleccionar
    while (True):
        seleccion = input(">> ")
        if (validar_seleccion(seleccion,opciones_menu)):
            seleccion = int(seleccion)-1
            break
    
    #MOSTRAR OPCION --------------------
    print(opciones_menu[seleccion])

    #HACER ACCIONES ---------------------
    if (seleccion == 0):
        #opcion 1
        pass

    if (seleccion == 1):
        #opcion 2
        pass

    if (seleccion == 2):
        #opcion 3
        pass

    if (seleccion == 3):
        #opcion 4
        pass

    if (seleccion == len(opciones_menu)-1):
        #SALIR
        pass