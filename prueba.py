#------NO CAMBIAR ---------
from autoHerramientas import *
import datetime
#---------------------------
#puede cargar cualquier archivo cambiando este parametro
nombre_archivo = "AutosTEST2"

#puede cambiar la forma de la lista entre:
#lista de diccionario -> tipo_lista = "diccionario"
#lista de listas -> tipo_lista = "lista"
tipo_lista = "diccionario"

lista_autos = obtenerAutos(nombre_archivo,tipo_lista)
"""for count,t in enumerate(lista_autos):
        try:
            print(count+1,"||",t["marca"]," ",t["modelo"]," ",t["año"]," ",t["patente"],t["color"],sep="")
        except Exception:
            continue"""
#------------
def buscarmodelo_marca_un_auto():
    x = str(input("ingrese modelo o marca del auto: \n>>> "))
    for marca_modelo in lista_autos:
        if x == marca_modelo["marca"] or x == marca_modelo["modelo"]:
            print(marca_modelo["marca"]," ",marca_modelo["modelo"]," ",marca_modelo["año"]," ",marca_modelo["patente"]," ",marca_modelo["color"],sep="")
            return
def imprimir_lista():
    x =str(input("ingrese un dato a investigar puede ser: \n[Marca \nModelo\nAño\nPatente\nColor]\n>>> "))
    for count,t in enumerate(lista_autos):
        if x == t["marca"] or x == t["modelo"] or x ==str( t["año"]) or x == t["color"] or  x == t["patente"]:
            print(count+1,"||",t["marca"]," ",t["modelo"]," ",str(t["año"])," ",str(t["patente"])," ",t["color"],sep="")
            continue
def imprimir_certificado():
    for count,t in enumerate(lista_autos):
        try:
            print(count+1,"||",t["marca"]," ",t["modelo"]," ",t["año"]," ",t["patente"],t["color"],sep="")
        except Exception:
            continue
    print("De la siguiente lista de auto eliga uno para hacer el certificado")
    x = input("ingrese numero de la patente:\n>>> ")
    for marca_modelo in lista_autos:
        if x == marca_modelo["patente"]:
            print(nombre_usuario," emite certificado que:\nEl vehiculo ",marca_modelo["marca"]," ",marca_modelo["modelo"]," con patente ",marca_modelo["patente"],"\nDe color ",marca_modelo["color"],"\nQueda registrado oficialmente a la fecha ",fecha_actual,sep="")
            continue
def buscar_patente():
    x = str(input("ingrese patente del auto: \n>>> "))
    for marca_modelo in lista_autos:
        if x == marca_modelo["patente"]:
            print(marca_modelo["marca"]," ",marca_modelo["modelo"]," ",marca_modelo["año"]," ",marca_modelo["patente"]," ",marca_modelo["color"],sep="")
            continue
def buscar_rango_año():
    x = int(input("ingrese año de inicio: \n>>> "))
    y = int(input("ingrese año de termino: \n>>> "))
    for marca_modelo in lista_autos:
        if x <= marca_modelo["año"] <= y:
            print(marca_modelo["marca"]," ",marca_modelo["modelo"]," ",marca_modelo["año"]," ",marca_modelo["patente"]," ",marca_modelo["color"],sep="")
            continue
def agregar_informacion():
    x = str(input("ingrese patente del auto: \n>>> "))
    for marca_modelo in lista_autos:
        if x == marca_modelo["patente"]:
            marca_modelo["nombre_propietario"] = input("ingrese nombre del dueño: \n>>> ")
            marca_modelo["apellido_propietario"] = input("ingrese apellido del dueño: \n>>> ")
            print(marca_modelo["marca"]," ",marca_modelo["modelo"]," ",marca_modelo["año"]," ",marca_modelo["patente"]," ",marca_modelo["color"],"\nEsta al nombre de ",marca_modelo["nombre"]," ",marca_modelo["apellido"],sep="")
            continue
def mostrar_autos_color():
    contador = 0
    for marca_modelo in lista_autos:
        if color_favorito == marca_modelo["color"]:
            print(marca_modelo["marca"]," ",marca_modelo["modelo"]," ",marca_modelo["año"]," ",marca_modelo["patente"]," ",marca_modelo["color"],sep="")
            contador += 1
    print("hay ",contador," autos de color ",color_favorito,sep="")
    pass

nombre_usuario = input("ingrese su nombre de usuario:\n>>> ")
fecha_actual = input("ingrese la fecha actual:\n>>> ")
color_favorito = input("ingrese su color favorito:\n>>> ")
while True:
    opciones_menu = [
        "Buscar 1 auto por Modelo / Marca.",
        "Imprimir la lista",
        "Imprimir Certificado",
        "Buscar por patente",
        "Buscar por rango de año",
        "Agregar informacion de Dueño al automovil",
        "Mostrar todos los automoviles del color favorito del usuario",
        ]
    opciones_menu.append("Salir")
    print(" \n")
    for count,t in enumerate(opciones_menu):
            try:
                print(count+1," - ",t,sep="")
            except Exception:
                continue

    menu = int(input(">>> "))

    if menu == 1:
        buscarmodelo_marca_un_auto()
        pass
    elif menu == 2:
        imprimir_lista()
        pass
    elif menu == 3:
        imprimir_certificado()
        pass
    elif menu == 4:
        buscar_patente()
        pass
    elif menu == 5:
        buscar_rango_año()
        pass
    elif menu == 6:
        agregar_informacion()
        pass
    elif menu == 7:
        mostrar_autos_color()
        pass
    elif menu == 8:
        break 
    else: 
        print("opcion incorrecta ")
        pass
