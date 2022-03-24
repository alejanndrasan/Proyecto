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
			concert_n = Music(db["events"][event]["title"], db["events"][event]["cartel"],fix_layout(db["events"][event]["layout"]), fix_layout_vip(db["events"][event]["layout"]),  db["events"][event]["prices"], db["events"][event]["date"], db["events"][event]["bands"], True)
			lista.append(concert_n)
	return lista

def objectify_data_plays(db, lista): #Esta funcion transforma los datos de la API en objetos, y crea la lista para los objetos tipo Teatro.
	for event in range(len(db["events"])):         
		if db["events"][event]["type"] == 2:
			play_n = Theater(db["events"][event]["title"], db["events"][event]["cartel"],fix_layout(db["events"][event]["layout"]), fix_layout_vip(db["events"][event]["layout"]), db["events"][event]["prices"], db["events"][event]["date"], db["events"][event]["synopsis"], True)
			lista.append(play_n)
	return lista

#Esto debo hacerlo SOLO 1 VEZ, y cuando se quiera reiniciar, esta aca mientras.
lista1 = objectify_data_concerts(db, [])
lista2 = objectify_data_plays(db, []) #1, 2 y 3 de notas.


def buscar_evento():
	tipo = val_int('\nIngrese el tipo de evento que busca: \n1.Tipo musical. \n2.Tipo teatral. \n==> ', 3)
	while True:
		filtro = val_int('''\nIngrese el filtro por los que desea buscarlo:
		1. Titulo
		2. Artista o banda.
		3. Fecha.
		==> ''', 4)
		otro = val_int('\nIngrese 1 para agregar otro filtro, 2 para finaliza: ', 3)
		if otro == 1:
			continue
		else:
			break

def busqueda_lineal_play(filtro, lista):	
	if filtro == 1:
		titulo = val_str('\nIngrese el nombre del evento que desea buscar: ')
		print(f'Titulo que ingreso: {titulo}')
		for i in range(len(lista)):
			if lista[i].title == titulo:
				lista[i].show_whole_play() 
				break
			elif lista[i].title != titulo:
				print('Evento no encontrado\n')
	elif filtro == 2:
		artista = val_names('\nIngrese el nombre del artista que desea buscar: ')
		index=-1
		print(f'Artista que ingreso: {artista}')
		for i in range(len(lista)):
			for j in range(len(lista[i].poster)):
				if lista[i].poster[j] == artista:
					index=i
		if index==-1:
			print("Evento no encontrado\n")
		else:
			lista[index].show_whole_play()
	elif filtro == 3:
		index=-1
		dia = val_int('\nIngresa el dia del evento que deseas buscar: ', 32)
		dia = str(dia)
		if len(dia) == 1:
			dia = '0'+dia
		mes = val_int('\nIngresa el mes del evento que deseas buscar (en numero): ', 12)
		mes = str(mes)
		if len(mes) == 1:
			mes = '0'+mes
		fecha = '2022-'+mes+'-'+dia
		print(f'Fecha que ingreso: {fecha}')
		for i in range(len(lista)):
			if lista[i].date == fecha:
				index = i
		if index==-1:
			print("Evento no encontrado\n")
		else:
			lista[index].show_whole_play()

		
busqueda_lineal_play(3, lista2)







	







