from Food_court import *
from tools import *
db = get_json()

def fix_stock_drinks(amount): #Esta funcion divide la cnatidad de bebidas en tres partes, es una division entera, si la cantidad no es multiplo de tres, le suma el residuo al elemento del medio (seria el precio para las bebidas medianas).
    lista = []
    c = amount
    for n in range(3):
        x = amount // 3
        lista.append(x)
        c -= x

    if amount%3 != 0:
        lista[1] += c
    return lista

def fix_price(price):
    x = price
    y = price * 0.16
    new_price = x + y
    return new_price

def fix_price_drinks(prices):
    for i in range(len(prices)):
        x = prices[i]
        y = x * 0.16
        prices[i] = x + y
    return prices

def objectify_data_foods(db, lista): #Esta funcion transforma los datos de la API en objetos, y crea la lista para los objetos tipo comida.
	for food in range(len(db["food_fair_inventory"])):         
		if db["food_fair_inventory"][food]["type"] == 1:
			food_n = Food(db["food_fair_inventory"][food]["name"], fix_price(db["food_fair_inventory"][food]["price"]),(db["food_fair_inventory"][food]["amount"]), (db["food_fair_inventory"][food]["presentation"]))
			lista.append(food_n)
	return lista

def objectify_data_drinks(db, lista): #Esta funcion transforma los datos de la API en objetos, y crea la lista para los objetos tipo bebida.
	for drink in range(len(db["food_fair_inventory"])):         
		if db["food_fair_inventory"][drink]["type"] == 2:
			drink_n = Drink(db["food_fair_inventory"][drink]["name"], fix_price_drinks(db["food_fair_inventory"][drink]["price"]),fix_stock_drinks(db["food_fair_inventory"][drink]["amount"]), (['P', 'M', 'G']))
			lista.append(drink_n)
	return lista

def buscar_producto(lista1, lista2): #Esta funcion sirve para buscar conciertos, retorna resultado.
    tipo = val_int('\nTipo de producto que buscar: \n1. Comidas. \n2. Bebidas. \n==> ', 3)
    if tipo == 1:
        print('\n---------------------------------\n')
        for i in lista1:
            i.show_food()
            print('\n---------------------------------\n')
        filtro = val_int('''\nIngrese el filtro por el que desea buscarlo:
        1. Nombre del producto
        2. Rango de precio.
        ==> ''', 3)
        if filtro == 1:
            resultado = busqueda_lineal(lista1)
            return resultado
        else:
            resultado=busqueda_precio_comida(lista1)
            return resultado
    else:
        print('\n---------------------------------\n')
        for i in lista2:
            i.show_drink()
            print('\n---------------------------------\n')
        filtro = val_int('''\nIngrese el filtro por el que desea buscarlo:
        1. Nombre del producto
        2. Rango de precio.
        ==> ''', 3)
        if filtro == 1:
            resultado = busqueda_lineal(lista2)
            return resultado
        else:
            resultado=busqueda_precio_bebida(lista2)
            return resultado

def busqueda_lineal(lista): #Esta funcion auxilia la funcion anterior de busqueda. 
    index = -1
    titulo = val_names('\nIngrese el nombre del producto que desea buscar: ')
    for i in range(len(lista)):
        if lista[i].product_name.title() == titulo:
            index=i
    if index==-1:
        print("Producto no encontrado\n")
        return 2
    else:
        return lista[index]

def busqueda_precio_bebida(lista):
    productos=[]
    print('\nIngrese el rango de precio que busca: ')
    n = val_int('Ingresa el precio minimo: ', 100)
    m = val_int('Ingresa el precio maximo: ', 100)
    for i in range(len(lista)):
        for j in range(len(lista[i].price)):
            if n <= lista[i].price[j] <= m:
                productos.append(lista[i].product_name)
    print(productos)
    resultado = busqueda_lineal(lista)
    return resultado

def busqueda_precio_comida(lista):
    print('\nIngrese el rango de precio que busca: ')
    n = val_int('Ingresa el precio minimo: ', 100)
    m = val_int('Ingresa el precio maximo: ', 100)
    for i in range(len(lista)):
        if n <= lista[i].price <= m:
            print(lista[i].product_name)
    resultado = busqueda_lineal(lista)
    return resultado

def eliminar_producto(lista1, lista2):
    print('\nSeleccion el producto que desea eliminar: ')
    resultado = buscar_producto(lista1, lista2)
    for i in range(len(lista1)):
        if lista1[i] == resultado:
            lista1.pop(i)
            print('\nProducto eliminado con exito.')
            return lista1
        else: 
            pass
    for i in range(len(lista2)):
        if lista2[i] == resultado:
            lista2.pop(i)
            print('\nProducto eliminado con exito.')
            return lista2
        else: 
            pass
    



comida = objectify_data_foods(db, [])
bebidas = objectify_data_drinks(db, [])

for i in bebidas:
    print(i.product_name)
eliminar_producto(comida, bebidas)
for i in bebidas:
    print(i.product_name)

#bebidas[0].show_drink()


#print(buscar_producto(comida, bebidas))

#subir_datos('C:\\Users\\Jsantos\\Desktop\\PROYECTO\\Conciertos_DB.txt', conciertos)
#subir_datos('C:\\Users\\Jsantos\\Desktop\\PROYECTO\\Obras_Teatro_DB.txt', obras_teatro)

