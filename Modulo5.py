from tools import *
from Client import *
from Invoice import *
from Food_Invoice import *

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
    
    total = lista_tickets + lista_feria
    promedio = total/purchase

    return promedio

            

