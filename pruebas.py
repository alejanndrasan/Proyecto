lista = []

for n in range(3):
    x = 500 // 3
    lista.append(x)
lista[1] += 1

print(lista)


#ARREGLAR:
artista = val_names('\nIngrese el nombre del artista o banda que desea buscar: ')
		index=-1
		for i in range(len(lista)):
			for j in range(len(lista[i].poster)):
				if lista[i].poster[j].title() == artista: #le a;ado el .title para que me generalize como estan escritos los nombres
					index=i
		if index==-1:
			print("Evento no encontrado\n")
			return 2
		else:
			return lista[index]