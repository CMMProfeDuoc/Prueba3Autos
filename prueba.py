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

Buscar 1 auto. << OBLIGATORIO
    Se puede buscar un auto por su "modelo" , "marca" o "año".
    Se deben mostrar todos los datos del vehiculo.

Imprimir la lista
    El usuario podra escribir una llave y un parametro y
    el programa debe mostrar toda la lista de vehiculos que cumplan esa condicion

Filtrar por parametros
    Cree una funcion que permita filtrar por una llave y un valor ingresado por el usuario
    La funcion debe devolver una sublista con los parametros filtrados

Imprimir Certificado
    El programa debe preguntar por el nombre del usuario y la fecha.
    Luego debe imprimir un certificado de la siguiente forma:

        <nombre_usuario> emite certificado que:
        El vehiculo <marca> <modelo> con patente <patente>
        De color <color>
        Queda registrado oficialmente a la fecha de <fecha>

Agregar vehiculo
    El programa debe preguntar los datos del vehiculo y guardarlos.

    Y luego guardar estos datos en la lista.
    (Esto se verificara si el dato es accesible)

Asignar dueño
    Debe poder agregar la opcion de asignarle un dueño a un vehiculo
    Para esto su programa debe añadir el dato a su diccionario (o lista)
    como lo estime conveniente
    
Salir.
    El programa debe cerrarse y terminar. (se finaliza el programa)

Luego de realizar una accion, el programa debe volver al menu principal
(excepto por la opcion Salir).
"""

from autoHerramientas import *

