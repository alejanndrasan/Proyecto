from Event import *
from tools import*


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
	abcdf = ['AV', 'BV', 'CV', 'DV', 'EV', 'FV', 'GV', 'HV', 'IV', 'JV', 'KV', 'LV', 'MV', 'NV', 'OV', 'PV', 'QV', 'RV', 'SV', 'TV', 'UV', 'VV', 'WV', 'XV', 'YV', 'ZV']
	matrix = ['V'] * x
	for i in range (x):
		matrix[i] = [f'{abcdf[i]}'] * y
	for j in range(x):
		a = matrix[j]
		for i in range(y):
			a[i] = a[i]+str(i)
	return matrix

def seats_quantity_general(layout): #Esta funcion es para tener la cantidad de asientos de cada evento.
	x = layout['general'][0]
	y = layout['general'][1]
	q = x*y
	return q

def seats_quantity_vip(layout): #Esta funcion es para tener la cantidad de asientos de cada evento.
	x = layout['vip'][0]
	y = layout['vip'][1]
	q = x*y
	return q
	
def objectify_data_concerts(db, lista): #Esta funcion transforma los datos de la API en objetos, y crea la lista para los objetos tipo Musica.
	for event in range(len(db["events"])):         
		if db["events"][event]["type"] == 1:
			concert_n = Music(db["events"][event]["title"], db["events"][event]["cartel"],fix_layout(db["events"][event]["layout"]), fix_layout_vip(db["events"][event]["layout"]), seats_quantity_general(db["events"][event]["layout"]), seats_quantity_vip(db["events"][event]["layout"]), db["events"][event]["prices"], db["events"][event]["date"], db["events"][event]["bands"], True)
			lista.append(concert_n)
	return lista

def objectify_data_plays(db, lista): #Esta funcion transforma los datos de la API en objetos, y crea la lista para los objetos tipo Teatro.
	for event in range(len(db["events"])):         
		if db["events"][event]["type"] == 2:
			play_n = Theater(db["events"][event]["title"], db["events"][event]["cartel"],fix_layout(db["events"][event]["layout"]), fix_layout_vip(db["events"][event]["layout"]), seats_quantity_general(db["events"][event]["layout"]), seats_quantity_vip(db["events"][event]["layout"]), db["events"][event]["prices"], db["events"][event]["date"], db["events"][event]["synopsis"], True)
			lista.append(play_n)
	return lista

def buscar_evento(lista): #Esta funcion sirve para buscar conciertos, retorna resultado.
	filtro = val_int('''\nIngrese el filtro por el que desea buscarlo:
	1. Titulo
	2. Artista o banda.
	3. Fecha.
	==> ''', 4)
	resultado = busqueda_lineal(filtro, lista)
	return resultado

def busqueda_lineal(filtro, lista): #Esta funcion auxilia la funcion anterior de busqueda. TEATRO
	if filtro == 1:
		index = -1
		titulo = val_names('\nIngrese el nombre del evento que desea buscar: ')
		for i in range(len(lista)):
			if lista[i].title.title() == titulo:
				index=i
		if index==-1:
			print("Evento no encontrado\n")
		else:
			return lista[index]
	elif filtro == 2:
		artista = val_names('\nIngrese el nombre del artista o banda que desea buscar: ')
		index=-1
		for i in range(len(lista)):
			for j in range(len(lista[i].poster)):
				if lista[i].poster[j] == artista:
					index=i
		if index==-1:
			print("Evento no encontrado\n")
		else:
			return lista[index]
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
			return lista[index]

def abrir_cerrar(lista1, lista2): #Altera el estado de disponibilidad de los eventos.
	tipo = val_int('\nIngrese el tipo de evento que busca: \n1.Tipo musical. \n2.Tipo teatral. \n==> ', 3)
	if tipo == 1:
		resultado = buscar_evento(lista1)
	if tipo == 2:
		resultado = buscar_evento(lista2)
	print(f'Evento seleccionado: {resultado.title}')
	msg = val_int('1.Abrir venta de tickets. \n2.Cerrar venta de tickets. \n==> ', 3)
	resultado.open_close(msg)
	if resultado.opened == True:
		print(f'Venta del evento {resultado.title} abierta')
	else:
		print(f'Venta del evento {resultado.title} cerrada')

def ver_evento(lista1, lista2): #Esta funcion muestra los eventos en su forma default.
	print('\n ------------------------------------------------------------- Eventos musicales -------------------------------------------------------------\n')
	for i in lista1:
		i.show_concert()
		print('\n******************************************************************************************************************************************\n')
	print('\n ------------------------------------------------------------- Eventos teatrales -------------------------------------------------------------\n')
	for i in lista2:
		i.show_play()
		print('\n******************************************************************************************************************************************\n')

def subir_cambios(lista1, lista2): #Esta funcion actualiza lis archivos de texto despues de cambiar datos de los eventos
	subir_datos('C:\\Users\\Jsantos\\Desktop\\PROYECTO\\Conciertos_DB.txt', lista1)
	subir_datos('C:\\Users\\Jsantos\\Desktop\\PROYECTO\\Obras_Teatro_DB.txt', lista2)

db = get_json()

'''En estos comentarios subi la info inicial de la API a los archivos de texto, esto no se vuelve hacer, sino en la funcion de resetear la info.'''
#conciertos = objectify_data_concerts(db, [])
#obras_teatro = objectify_data_plays(db, [])
#subir_datos('C:\\Users\\Alejandra\\Documents\\Unimet Ale\\PROYECTO\\Conciertos_DB.txt', conciertos)
#subir_datos('C:\\Users\\Alejandra\\Documents\\Unimet Ale\\PROYECTO\\Obras_Teatro_DB.txt', obras_teatro)











