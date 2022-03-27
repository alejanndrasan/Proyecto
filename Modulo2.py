from tools import *
from Modulo1 import *
from Client import *
from Event import *
from Invoice import *
import emoji


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
    codigo = verificar_registro(lista, cedula) #Aqui verifica que el cliente ya esta registrado
    if codigo == 1:
        nombre = val_names('\nIngrese su nombre completo: ')
        edad = val_int('\nIngrese su edad: ', 140)
        cliente = Client(nombre, edad, cedula, [])
        lista.append(cliente)
        print('\nCliente registrado con exito') 
        return lista
    if codigo == 2:
        print("\nCliente ya registrado")

def registrar_compra(lista1, lista2, lista3, lista4):
    while True:
        cedula = val_int('\nIngrese su numero de cedula: ', 1000000000)
        codigo = verificar_registro(lista3, cedula) #Aqui verifica que el cliente ya esta registrado
        if codigo == 1:
            registrar = val_int('\nCliente no registrado, para registrarlo ingrese 1, para salir ingrese 2: ', 3)
            if registrar == 1:
                registrar_cliente(lista3) #Si no esta registrado, te lleva a la funcion registrar para que lo registres.
            else:
                break
        else:
            cliente = get_cliente(lista3, cedula) #Esta funcion busca el cliente y devuelve el objeto, para poder usarlo mas adelante
            ver_evento_compras(lista1, lista2) 
            print('\nSeleccione el evento que desea:\n')
            tipo = val_int('\n1.Tipo musical. \n2.Tipo teatral. \n==> ', 3)
            print('\nAhora busque el evento que desea seleccionar: ') #Busca el objeto del evento para usarlo en toda la funcion.
            if tipo ==1:
                resultado = buscar_evento(lista1)
                while True:
                    if resultado == 2:
                            otro = val_int('\nPara volver a intentarlo, ingrese 1, ingrese 2 para salir: ', 3)
                            if otro == 1:
                                continue
                            else:
                                break
                    else:
                        otro = 3
                        resultado.show_tickets()
                        respuesta = resultado.show_layout()
                        if respuesta == 1:
                            otro = 2
                        break
            else:
                resultado = buscar_evento(lista2)
                while True:
                    if resultado == 2:
                            otro = val_int('\nPara volver a intentarlo, ingrese 1, ingrese 2 para salir: ', 3)
                            if otro == 1:
                                continue
                            else:
                                break
                    else:
                        otro = 3
                        resultado.show_tickets()
                        respuesta = resultado.show_layout()
                        if respuesta == 1:
                            otro = 2
                        break
            
            if otro == 2:
                break

            #Cantidad de puestos y puestos:
            seccion = val_int('''\nSeleccione en que seccion quiere sentarse:
            1. General.
            2. VIP.
            ==> ''', 3)
            if seccion == 1:
                cantidad_asientos = val_int('\nIngrese la cantidad de asientos que desea comprar: ', (resultado.general_seats + 1)) 
                spots = []
                for n in range(cantidad_asientos): #Corre la cantidad de asientos insertada.
                    while True:
                        spot = input('Ingrese el asiento que desea: ') #hacer lo que dice Emily para validar.
                        if spot != emoji.emojize(':seedling:'):
                            print("\nAsiento seleccionado con exito.")
                            spots.append(spot)
                            break
                        else:
                            print('\nAsiento no disponible, intente otra vez.')

                #Cuenta: 
                tickets = cantidad_asientos * resultado.ticket[0]
                IVA = tickets * 0.16
                cuenta = tickets + IVA
                print(f'\nPuestos: {spots}. \nTotal a pagar: {cuenta}') #Imprime lo que se pagaria, y pregunta si deseas continuar, si no, no se genera la factura, ni se altera el atributo purchase del cliente.
                pagar = val_int('\nDesea proceder con su compra: \n1.Si. \n2.No. \n==> ', 3)
                if pagar == 2:
                    print('Hasta luego!')
                    break
                else:
                    resultado.select_seats_general(spot) #Se marca en la base de datos que el asiento esta ocupado


            #VIP: se realiza lo mismo que en la seccion anterior, pero casteando los atributos _vip.
            if seccion == 2:
                cantidad_asientos = val_int('\nIngrese la cantidad de asientos que desea comprar: ', (resultado.vip_seats + 1))
                spots = []
                for n in range(cantidad_asientos):
                    while True:
                        spot = input('Ingrese el asiento que desea: ') #hacer lo que Emily dice para validar
                        if spot != emoji.emojize(':blossom:'):
                            print("\nAsiento seleccionado con exito.")
                            spots.append(spot)
                            break
                        else:
                            print('\nAsiento no disponible, intente otra vez.')
                #Cuenta:
                tickets = cantidad_asientos * resultado.ticket[1] 
                IVA = tickets * 0.16
                cuenta = tickets + IVA
                print(f'\nPuestos: {spots}. \nTotal a pagar: {cuenta}')
                pagar = val_int('\nDesea proceder con su compra: \n1.Si. \n2.No. \n==> ', 3)
                if pagar == 2:
                    print('Hasta luego!')
                    break
                else:
                    resultado.select_seats_vip(spot) #Se marca en la base de datos que el asiento esta ocupado

            
            #Se le resta los asientos comprados al atributo de cantidad de asientos del evento seleccionado.
            if seccion == 1:
                resultado.general_seats = resultado.general_seats - cantidad_asientos 
            else:
                resultado.vip_seats = resultado.vip_seats - cantidad_asientos

            #Regitrar compra en el cliente: registra en la lista de compras del cliente la compra realizada.
            factura = Invoice(resultado.title, cantidad_asientos, cuenta, spots, None)
            lista4.append(factura)
            cliente.purchase.append(factura)

            #Factura:
            print(f'''\n************************************FACTURA*************************************
Nombre del cliente: {cliente.name}.
C.I: {cliente.id}.
Puestos: {spots}.
Total a pagar: {cuenta}''')
            break
        
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



    