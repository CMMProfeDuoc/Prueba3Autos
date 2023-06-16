"""
Una compañia automovilistica le pide crear un programa para ordenar sus automoviles.
A usted se le otorga una serie de listas con varios automoviles
Las cuales son cargados al programa.
Cada vehiculo tiene los siguientes datos:

    <nombre_vehiculo>
    <marca>
    <año>
    <precio>
    <patente_vehiculo>

Su programa debe mostrar un menu con las siguientes a continuación.

1. Buscar 1 auto.
    Se puede buscar un auto por su "nombre/modelo" , "marca" o "año".
    Se deben mostrar todos los datos del vehiculo.

2. Imprimir Certificado
    El programa debe preguntar por el nombre del usuario y la fecha.
    Luego debe imprimir un certificado de la siguiente forma:

        <nombre_usuario> emite certificado que:
        El vehiculo <marca> <nombre_vehiculo> con patente <patente_vehiculo>
        Con valor : $ <precio>
        Queda registrado oficialmente a la fecha de <fecha>

3. Agregar vehiculo
    El programa debe preguntar los datos del vehiculo y guardarlos.

    Y luego guardar estos datos en la lista.
    (Esto se verificara si el dato es accesible o buscable usando el punto 1)
    
4. Salir.
    El programa debe cerrarse y terminar. (se finaliza el programa)

Luego de realizar una accion, el programa debe volver al menu principal (excepto por la opcion 4).
"""