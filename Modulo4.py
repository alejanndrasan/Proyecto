from Food_Invoice import FoodCourt_Invoice
from Modulo3 import buscar_producto, ver_productos
from tools import *
from Modulo1 import *
from Modulo2 import *
from Modulo4 import *
from Client import *
from Event import *
from Invoice import *
import emoji


def registrar_compra_feria(lista1, lista2, lista3, lista4):
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
            ver_productos(lista1, lista2) 
            while True:
                print('\nSeleccione el producto que desea:\n')
                resultado = buscar_producto(lista1, lista2)
                if resultado == 2:
                    otro = val_int('\nPara volver a intentarlo, ingrese 1, ingrese 2, para salir: ', 3)
                    if otro == 1:
                        continue
                    else:
                        break
                else:
                    otro = 3
                    break
        if otro == 2:
            break
        
        #Para saber el tipo de resultado:

        #Comida
        for i in lista1:
            if resultado == i:
                tipo = 1
            else:
                pass
        
        #Bebida:
        for i in lista2:
            if resultado == i:
                tipo = 2
            else:
                pass
        
        #Pedido para comidas:
        if tipo == 1:
            if resultado.stock > 0:
                producto = resultado.product_name
                cantidad = val_int('\nIngrese la cantidad que desea comprar: ', (resultado.stock + 1))
                cuenta = cantidad * resultado.price
                print(f'\nProducto: {producto}. \nTotal a pagar: {cuenta}') #Imprime lo que se pagaria, y pregunta si deseas continuar, si no, no se genera la factura, ni se altera el atributo purchase del cliente.
                pagar = val_int('\nDesea proceder con su compra: \n1.Si. \n2.No. \n==> ', 3)
                if pagar == 2:
                    print('Hasta luego!')
                    break
                pedido_n = FoodCourt_Invoice(producto, cantidad, cuenta)
                resultado.stock -= cantidad
                cliente.foodcourt_bill.append(pedido_n)
                lista4.append(pedido_n)
                #Factura:
                print(f'''\n************************************FACTURA*************************************
Nombre del cliente: {cliente.name}.
C.I: {cliente.id}.
Producto: {producto}.
Total a pagar: {cuenta}''')
                break
            else:
                print('\nProducto agotado')
                otro = val_int('\nPara volver a intentarlo, ingrese 1, ingrese 2, para salir: ', 3)
                if otro == 1:
                    continue
                else:
                    break
        
        #Pedido para bebidas:
        if tipo == 2:
            m = val_int('\nSeleccione el tamaño de su bebida: \n1. Pequeña. \n2. Mediana. \n3. Grande. \n==> ', 4)
            if resultado.stock[m-1] > 0:
                producto = resultado.product_name, resultado.sizes[m-1]
                cantidad = val_int('\nIngrese la cantidad que desea comprar: ', (resultado.stock[m-1] + 1))
                cuenta = cantidad * resultado.price[m-1]
                print(f'\nProducto: {producto}. \nTotal a pagar: {cuenta}') #Imprime lo que se pagaria, y pregunta si deseas continuar, si no, no se genera la factura, ni se altera el atributo purchase del cliente.
                pagar = val_int('\nDesea proceder con su compra: \n1.Si. \n2.No. \n==> ', 3)
                if pagar == 2:
                    print('Hasta luego!')
                    break
                pedido_n = FoodCourt_Invoice(producto, cantidad, cuenta)
                resultado.stock[m-1] -= cantidad
                cliente.foodcourt_bill.append(pedido_n)
                lista4.append(pedido_n)
                #Factura:
                print(f'''\n************************************FACTURA*************************************
Nombre del cliente: {cliente.name}.
C.I: {cliente.id}.
Producto: {producto}.
Total a pagar: {cuenta}''')
                break
            else:
                print('\nProducto agotado')
                otro = val_int('\nPara volver a intentarlo, ingrese 1, ingrese 2, para salir: ', 3)
                if otro == 1:
                    continue
                else:
                    break

            


            


            