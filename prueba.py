"""
Una compañia automovilistica le pide crear un programa para ordenar sus automoviles.
A usted se le otorga una serie de listas con varios automoviles
Las cuales son cargados al programa.
Cada vehiculo tiene los siguientes datos:

    <marca>
    <modelo>
    <año>
    <patente>
    <color>

Su programa debe mostrar un menu con las siguientes a continuación.

Buscar 1 auto por Modelo. << OBLIGATORIO
    Se puede buscar un auto por su "modelo".
    Se deben mostrar todos los datos del vehiculo.

Imprimir la lista
    El usuario podra escribir una llave y un parametro y
    el programa debe mostrar toda la lista de vehiculos que cumplan esa condicion

Imprimir Certificado
    El programa debe preguntar por el nombre del usuario y la fecha.
    Luego debe imprimir un certificado de la siguiente forma:

        <nombre_usuario> emite certificado que:
        El vehiculo <marca> <modelo> con patente <patente>
        De color <color>
        Queda registrado oficialmente a la fecha de <fecha>

Salir.
    El programa debe cerrarse y terminar. (se finaliza el programa)

Luego de realizar una accion, el programa debe volver al menu principal
(excepto por la opcion Salir).
"""

#------NO CAMBIAR ---------
from autoHerramientas import *
#---------------------------

#puede cargar cualquier archivo cambiando este parametro
nombre_archivo = "Autos1"

lista = obtenerAutos(nombre_archivo)


