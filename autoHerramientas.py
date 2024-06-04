def load_file (file_name:str="test",extension:str=".csv") -> list:
	lista = []
	file_name += extension
	file = open(file_name,"r")

	for count, line in enumerate(file):
		line = line.strip()
		aux = line.split(";")
		lista.append(aux)
	file.close()
	return lista

def obtenerAutos (nombre_archivo:str="Autos1",tipo_lista:str="diccionario") -> list:
	lista = load_file(nombre_archivo)
	if (tipo_lista.lower() == "lista"):
		return lista
	
	lista_autos = []
	for elemento in lista:
		aux = {
			"modelo":elemento[1],
			"marca":elemento[0],
			"año":int(elemento[2]),
			"patente":elemento[3],
			"color":elemento[4]
		}
		lista_autos.append(aux)
	return lista_autos

def pausa () -> None:
	import os
	os.system("pause")

def limpiarPantalla () -> None:
	import os
	os.system("cls")

def validar_seleccion (sel, lista:list) -> bool:
	if (str(sel).isnumeric()):
		if (int(sel) in range(len(lista)+1)):
			return True
	return False

def limpiarVidrios () -> None:
	print("vidrios limpios")