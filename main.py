from msilib.schema import ODBCTranslator
import emoji
from tools import *
from Modulo1 import *
from Modulo2 import *

db = get_json()

#Conciertos_DB.txt contiene todos los eventos del tipo musical, bajados de la API.
#Obras_Teatro_DB.txt contiene todos los eventos del tipo teatro, bajados de la API
#Los datos de los archivos de texto de los eventos puede ser alterada (se pueden eliminar eventos), y se vuelve a usar la API cuando se quiera reiniciar la data a su estado inicial.


def main():
    conciertos = cargar_datos('C:\\Users\\Jsantos\\Desktop\\PROYECTO\\Conciertos_DB.txt')
    obras_teatro = cargar_datos('C:\\Users\\Jsantos\\Desktop\\PROYECTO\\Obras_Teatro_DB.txt')
    clientes = cargar_datos('C:\\Users\\Jsantos\\Desktop\\PROYECTO\\Clientes.txt')
    facturas = cargar_datos('C:\\Users\\Jsantos\\Desktop\\PROYECTO\\Facturas.txt')
    print(emoji.emojize('\n---------------------- Saman Show :deciduous_tree: ----------------------\n'))
    print(conciertos[0].poster)
    while True:
        menu = val_int('''\nBienvenido a Saman Show, seleccione que accion desea realizar:
        1. Ver eventos.
        2. Abrir o cerrar venta de tickets.
        3. Buscar evento.
        4. Registrar cliente.
        5. Registrar compra.
        6. Salir
        ==> ''', 7)

        #MODULO 1:
        if menu == 1:
            ver_evento(conciertos, obras_teatro)
        if menu == 2:
            abrir_cerrar(conciertos, obras_teatro)
            subir_cambios(conciertos, obras_teatro)
        if menu == 3:
            tipo = val_int('\nIngrese el tipo de evento que busca: \n1.Tipo musical. \n2.Tipo teatral. \n==> ', 3)
            if tipo ==1:
                while True:
                    resultado = buscar_evento(conciertos)
                    if resultado == 2:
                        otro = val_int('\nPara volver a intentarlo, ingrese 1, ingrese 2, para salir: ', 3)
                        if otro == 1:
                            continue
                        else:
                            break
                    else:
                        resultado.show_concert()
                        break
            else:
                resultado = buscar_evento(obras_teatro)
                while True:
                    if resultado == 2:
                            otro = val_int('\nPara volver a intentarlo, ingrese 1, ingrese 2, para salir: ', 3)
                            if otro == 1:
                                continue
                            else:
                                break
                    else:
                        resultado.show_play()
                        break
        #MODULO 2:
        if menu == 4:
            registrar_cliente(clientes)
            subir_datos('C:\\Users\\Jsantos\\Desktop\\PROYECTO\\Clientes.txt', clientes)
        if menu == 5:
            registrar_compra(conciertos, obras_teatro, clientes, facturas)
            subir_datos('C:\\Users\\Jsantos\\Desktop\\PROYECTO\\Clientes.txt', clientes)
            subir_datos('C:\\Users\\Jsantos\\Desktop\\PROYECTO\\Facturas.txt', facturas)
            subir_cambios(conciertos, obras_teatro)
        if menu == 6:
            break
    print('bye bye!')


            
    

    

main()