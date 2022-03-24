from Event import *
from tools import*

db = get_json()


def fix_layout(layout): #Esta funcion organiza la matriz del layout (general y VIP), con los datos de cada objeto.
	x = layout['general'][0]
	y = layout['general'][1]
	abcdf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	matriz = ['A'] * x
	for i in range (x):
		matriz[i] = [f'{abcdf[i]}'] * y
	for j in range(x):
		a = matriz[j]
		for i in range(y):
			a[i] = a[i]+str(i)
	matriz_final = matriz.append(fix_layout_vip(layout))
	return matriz

def fix_layout_vip(layout): #Esta funcion organiza los puestos de la zona VIP.
	x = layout['vip'][0]
	y = layout['vip'][1]
	matrix = ['V'] * x
	for i in range (x):
		matrix[i] = ['V'] * y
	for j in range(x):
		a = matrix[j]
		for i in range(y):
			a[i] = a[i]+str(i)
	return matrix

def objectify_data_concerts(db, lista): #Esta funcion transforma los datos de la API en objetos, y crea la lista para los objetos tipo Musica.
	for event in range(len(db["events"])):         
		if db["events"][event]["type"] == 1:
			concert_n = Music(db["events"][event]["title"], db["events"][event]["cartel"],fix_layout(db["events"][event]["layout"]), db["events"][event]["prices"], db["events"][event]["date"], db["events"][event]["bands"], True)
			lista.append(concert_n)
	return lista

def objectify_data_plays(db, lista): #Esta funcion transforma los datos de la API en objetos, y crea la lista para los objetos tipo Teatro.
	for event in range(len(db["events"])):         
		if db["events"][event]["type"] == 2:
			play_n = Theater(db["events"][event]["title"], db["events"][event]["cartel"],fix_layout(db["events"][event]["layout"]), db["events"][event]["prices"], db["events"][event]["date"], db["events"][event]["synopsis"], True)
			lista.append(play_n)
	return lista

#Esto debo hacerlo en el main, esta aca mientras.
lista1 = objectify_data_concerts(db, [])
lista2 = objectify_data_plays(db, [])

def buscar_evento():
	tipo = val_int('\nIngrese el tipo de evento que busca: \n1.Tipo musical. \n2.Tipo teatral. \n==> ', 3)
	filtros = []
	while True:
		filtro = val_int('''\nIngrese el filtro por los que desea buscarlo:
		1. Titulo
		2. Artista o banda.
		3. Fecha.
		==> ''', 4)
		filtros.append(filtro)
		otro = val_int('\nIngrese 1 para agregar otro filtro, 2 para finaliza: ', 3)
		if otro == 1:
			continue
		else:
			break

def busqueda_lineal_play(filtro, lista):	
	if filtro == 1:
		while True:
			titulo = val_str('\nIngrese el nombre del evento que desea buscar: ')
			for i in lista:
				print(i.title)
				if titulo == i.title:
					print(i.show_whole_play()) #Me esta imprimiendo unas cosas extra
					break
				else:
					otro = val_int('\nEvento no encontrado, para volver a buscar, ingrese 1, para salir ingrese 1: ', 3)
					if otro == 1:
						continue
					else:
						break
	elif filtro == 2:
		while True:
			artista = val_names('\nIngrese el nombre del artista que desea buscar: ')
			for i in lista:
				print(i.poster)
				for j in i.poster:
					if artista == j:
						print(i.show_whole_play())
						break
					'''else:
						otro = val_int('\nEvento no encontrado, para volver a buscar, ingrese 1, para salir ingrese 1: ', 3)
						if otro == 1:
							continue
						else:
							break'''
	'''elif filtro == 3:
		while True:
			mes = val_int('\nIngrese el mes del evento que desea buscar: ')
			for i in lista:
				for j in i.date.split('-'):
					if mes == j[1]:
						print(i.show_whole_play())
					else:
						otro = val_int('\nEvento no encontrado, para volver a buscar, ingrese 1, para salir ingrese 1: ', 3)
						if otro == 1:
							continue
						else:
							break'''

busqueda_lineal_play(2, lista2)





	







