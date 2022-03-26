from tools import *
from Modulo1 import *
from Client import *
from Event import *
from Invoice import *
import emoji

conciertos = cargar_datos('C:\\Users\\Jsantos\\Desktop\\PROYECTO\\Conciertos_DB.txt')
obras_teatro = cargar_datos('C:\\Users\\Jsantos\\Desktop\\PROYECTO\\Obras_Teatro_DB.txt')

def ver_evento_compras(lista1, lista2):
    print('\n ------------------------------------------------------------- Eventos musicales -------------------------------------------------------------\n')
    for i in lista1:
        i.show_concert_for_sales()
        print('\n******************************************************************************************************************************************\n')
    print('\n ------------------------------------------------------------- Eventos teatrales -------------------------------------------------------------\n')
    for i in lista2:
        i.show_play_for_sales()
        print('\n******************************************************************************************************************************************\n')

def registrar_cliente(lista):
    print('''\n-----------------------------------------------------------------------------------------------------------------------------------------------
    Ingrese los datos que se le pediran a continuacion para registrar el cliente.''')
    cedula = val_int('\nIngrese su numero de cedula: ', 1000000000)
    codigo = verificar_registro(lista, cedula)
    if codigo == 1:
        nombre = val_names('\nIngrese su nombre completo: ')
        edad = val_int('\nIngrese su edad: ', 140)
        cliente = Client(nombre, edad, cedula, None)
        lista.append(cliente)
        print('\nCliente registrado con exito')
        return lista
    if codigo == 2:
        print("\nCliente ya registrado")

def registrar_compra(lista1, lista2, lista3):
    while True:
        cedula = val_int('\nIngrese su numero de cedula: ', 1000000000)
        codigo = verificar_registro(lista3, cedula)
        if codigo == 1:
            print('\nCliente no registrado, registrelo primero.')
            registrar_cliente(lista3)
        else:
            cliente = get_cliente(lista3, cedula)
            ver_evento_compras(lista1, lista2)
            print('\nSeleccione el evento que desea:\n')
            tipo = val_int('\n1.Tipo musical. \n2.Tipo teatral. \n==> ', 3)
            print('\nAhora busque el evento que desea: ')
            if tipo ==1:
                resultado = buscar_concierto(lista1)
                resultado.show_tickets()
                resultado.show_layout()
            else:
                resultado = buscar_obra(lista2)
                resultado.show_tickets()
                resultado.show_layout()
            #Cantidad de puestos y puestos:
            seccion = val_int('''\nSeleccione en que seccion quiere sentarse:
            1. General.
            2. VIP.''', 3)
            if seccion == 1:
                cantidad_asientos = val_int('\nIngrese la cantidad de asientos que desea comprar: ', (resultado.general_seats + 1))
                spots = []
                for n in range(cantidad_asientos):
                    while True:
                        spot = input('Ingrese el asiento que desea: ') 
                        if spot != emoji.emojize(':seedling:'):
                            resultado.select_seats_general(spot)
                            print("\nAsiento seleccionado con exito.")
                            spots.append(spot)
                            break
                        else:
                            print('\nAsiento no disponible, intente otra vez.')
                #Cuenta:
                tickets = cantidad_asientos * resultado.ticket[0]
                IVA = tickets * 0.16
                cuenta = tickets + IVA
                print(f'\nPuestos: {spots}. \nTotal a pagar: {cuenta}')
                pagar = val_int('\nDesea proceder con su compra: \n1.Si. \n2.No. \n==> ', 3)
                if pagar == 2:
                    mensaje = 'Hasta luego!'
                    break
            resultado.general_seats = resultado.general_seats - cantidad_asientos
            if seccion == 2:
                cantidad_asientos = val_int('\nIngrese la cantidad de asientos que desea comprar: ', (resultado.vip_seats + 1))
                spots = []
                for n in range(cantidad_asientos):
                    while True:
                        spot = input('Ingrese el asiento que desea: ')
                        if spot != emoji.emojize(':blossom:'):
                            resultado.select_seats_vip(spot)
                            print("\nAsiento seleccionado con exito.")
                            spots.append(spot)
                            break
                        else:
                            print('\nAsiento no disponible, intente otra vez.')
                #Cuenta:
                tickets = cantidad_asientos * resultado.ticket[0]
                IVA = tickets * 0.16
                cuenta = tickets + IVA
                print(f'\nPuestos: {spots}. \nTotal a pagar: {cuenta}')
                pagar = val_int('\nDesea proceder con su compra: \n1.Si. \n2.No. \n==> ', 3)
                if pagar == 2:
                    mensaje = 'Hasta luego!'
                    break
            resultado.vip_seats = resultado.vip_seats - cantidad_asientos
            #Regitrar compra en el cliente:
            cliente.purchase = Invoice(resultado.title, cantidad_asientos, cuenta, spots)
            #Factura:
            print(f'''\n************************************FACTURA*************************************
            \nNombre del cliente: {cliente.name}.
            C.I: {cliente.id}.
            Puestos: {spots}.
            Total a pagar: {cuenta}''')
            mensaje = "\nCompra exitosa, hasta luego!"
            break
        print(mensaje)
        

def verificar_registro(lista, cedula):
    index = -1
    for i in range(len(lista)):
        if lista[i].id == cedula:
            index=i
    if index==-1:
        return 1
    else:
        return 2

def get_cliente(lista, cedula):
    for i in range(len(lista)):
        if lista[i].id == cedula:
            return lista[i]

while True:
    clientes = registrar_cliente([])
    registrar_compra(conciertos, obras_teatro, clientes)
    input = input('1 salir, 2 seguir')
    if input==1:
        break
    else:
        continue

    