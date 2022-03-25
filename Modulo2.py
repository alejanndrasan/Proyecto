from tools import *
from Modulo1 import *
from Client import *
from Event import *

def ver_evento_compras(lista1, lista2):
    print('\n ------------------------------------------------------------- Eventos musicales -------------------------------------------------------------\n')
    for i in lista1:
        i.show_concert_for_sales()
        print('\n******************************************************************************************************************************************\n')
        print('\n ------------------------------------------------------------- Eventos teatrales -------------------------------------------------------------\n')
    for i in lista2:
        i.show_play_for_sales()
        print('\n******************************************************************************************************************************************\n')

def registrar_compra(lista1, lista2):
    nombre_cliente = val_names('\nIngrese su nombre completo: ')
    cedula = val_int('\nIngrese su numero de cedula: ', 1000000000)
    edad = val_int('\nIngrese su edad: ', 140)]
    ver_evento_compras(lista1, lista2)
    print('\nSeleccione el evento que desea:\n')
    tipo = val_int('\n1.Tipo musical. \n2.Tipo teatral. \n==> ', 3)
    if tipo ==1:
        resultado = buscar_concierto(lista1)
        resultado.show_tickets()
        resultado.show_layout()
    else:
        resultado = buscar_obra(lista2)
        resultado.show_tickets()
        resultado.show_layout()
    
        

    