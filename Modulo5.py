from tools import *
from Client import *
from Invoice import *
from Food_Invoice import *
from Event import *
from Food_court import *

def promedio_gastos(lista):
    lista_tickets = 0
    lista_feria = 0
    purchase = 0 

    #TICKETS:
    for cliente in lista:
        for factura in cliente.purchase:
            lista_tickets+= factura.tickets_bill
            purchase+=1

    #FERIA:
    for cliente in lista:
        for factura in cliente.foodcourt_bill:
            lista_feria+= factura.payment
            purchase+=1
    
    if purchase != 0:
        total = lista_tickets + lista_feria
        promedio = total/purchase
        return round(promedio, 2)
    else:
        return '\nTodavia no se registra ninguna compra.'


def porcentaje_sin_feria(lista):
    x = 0
    for cliente in lista:
        if len(cliente.foodcourt_bill) == 0:
            x +=1
    y = len(lista)
    if y != 0:
        porcentaje = (x*100)/y
        return str(round(porcentaje, 2)) + '%'
    else:
        return '\nTodavia no se registra ninguna compra.'

def top3_clientes(lista, lista2):
    if len(lista2)==0:
        return 0
    else:
        gastos = []

        for cliente in lista:
            gastos_n = len(cliente.purchase) + len(cliente.foodcourt_bill)
            gastos.append([gastos_n, cliente.id])
        
        gastos_ordenados = sort_clientes(gastos)

        top_clientes = []

        for i in range(len(lista)):
            if gastos_ordenados[i][1] == lista[i].id:
                top_clientes.append(lista[i])
        
        if len(top_clientes) == 0:
            return 0
        elif 0 < len(top_clientes) <= 3:
            return top_clientes
        else:
            top3 = [top_clientes[0], top_clientes[1], top_clientes[2]]
            return top3

def top_eventos_productos(conciertos, obras, comida, bebidas):
    eventos = combinar_listas(conciertos, obras, [])
    productos = combinar_listas(comida, bebidas, [])
    eventos_ordenados = sort_eventos_productos(eventos)
    productos_ordenados = sort_eventos_productos(productos)

    return eventos_ordenados, productos_ordenados

def sort_clientes(lista): 
    long = len(lista)

    for i in range(long-1):
        menor = i
        for j in range(i+1, long):
            if lista[menor][0]>lista[j][0]:
                menor = j
        temp = lista[i]
        lista[i]=lista[menor]
        lista[menor]=temp
    
    return lista.reverse()

def sort_eventos_productos(lista): 
    long = len(lista)

    for i in range(long-1):
        menor = i
        for j in range(i+1, long):
            if lista[menor].ventas>lista[j].ventas:
                menor = j
            elif lista[menor].ventas==lista[j].ventas:
                return lista
                break
        temp = lista[i]
        lista[i]=lista[menor]
        lista[menor]=temp
    return lista.reverse()

def combinar_listas(lista1, lista2, lista_final):

    for i in lista1:
        lista_final.append(i)
    
    for j in lista2:
        lista_final.append(j)
    
    return lista_final



'''cont=0
            top = top3_clientes(clientes, facturas)
            if top == 0:
                print('\nTodavia no hay ningun cliente registrado.')
            else:
                for i in top:
                    cont+=1
                    print(f'\nTop {cont}: {i.name}')'''
