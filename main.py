import emoji
from tools import *
from Modulo1 import *
from Modulo2 import *
from Modulo3 import *
from Modulo4 import *
from Modulo5 import *

#db = get_json()

#Conciertos_DB.txt contiene todos los eventos del tipo musical, bajados de la API.
#Obras_Teatro_DB.txt contiene todos los eventos del tipo teatro, bajados de la API
#Los datos de los archivos de texto de los eventos puede ser alterada (se pueden eliminar eventos), y se vuelve a usar la API cuando se quiera reiniciar la data a su estado inicial.


def main():
    conciertos = cargar_datos('Conciertos_DB.txt')
    obras_teatro = cargar_datos('Obras_Teatro_DB.txt')
    clientes = cargar_datos_vacios('Clientes.txt')
    facturas = cargar_datos_vacios('Facturas.txt')
    comida = cargar_datos('Comida.txt')
    bebidas = cargar_datos('Bebidas.txt')
    facturas_comida = cargar_datos_vacios('Facturas_comida.txt')
    while True:
        print(emoji.emojize('\n---------------------- Saman Show :deciduous_tree: ----------------------\n'))
        menu = val_int('''\nBienvenido a Saman Show, seleccione que accion desea realizar:
\n1. Ver eventos.
\n2. Abrir o cerrar venta de tickets.
\n3. Buscar evento.
\n4. Registrar cliente.
\n5. Comprar Tickets.
\n6. Buscar productos de la feria de comida.
\n7. Eliminar productos de la feria de comida.
\n8. Comprar articulo de la feria.
\n9. Calcular promedio de gastos de los clientes.
\n10. Porcentaje de clientes que no compran en la feria.
\n11. Top 3 Shows mas vendidos.
\n12. Top 5 Productos de la feria mas comprados.
\n13. Reiniciar data.
\n14. Salir. 
\n==> ''', 15)

        #MODULO 1:
        if menu == 1:
            ver_evento(conciertos, obras_teatro)
        if menu == 2:
            abrir_cerrar(conciertos, obras_teatro)
            subir_cambios(conciertos, obras_teatro)
        if menu == 3:
            tipo = val_int('\nIngrese el tipo de evento que busca: \n1.Tipo musical. \n2.Tipo teatral. \n==> ', 3)
            if tipo ==1:
                print('\n ------------------------------------------------------------- Eventos musicales -------------------------------------------------------------\n')
                for i in conciertos:
                    i.show_concert()
                    print('\n******************************************************************************************************************************************\n')
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
                print('\n ------------------------------------------------------------- Eventos teatrales -------------------------------------------------------------\n')
                for i in obras_teatro:
                    i.show_play()
                    print('\n******************************************************************************************************************************************\n')
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
            subir_datos('Clientes.txt', clientes)
        if menu == 5:
            registrar_compra(conciertos, obras_teatro, clientes, facturas)
            subir_datos('Clientes.txt', clientes)
            subir_datos('Facturas.txt', facturas)
            subir_cambios(conciertos, obras_teatro)

        #MODULO 3:
        if menu == 6:
            resultado = buscar_producto_show(comida, bebidas)
        if menu == 7:
            eliminar_producto(comida, bebidas)
            subir_datos('Comida.txt', comida)
            subir_datos('Bebidas.txt', bebidas)
        
        #MODULO 4:
        if menu == 8:
            registrar_compra_feria(comida, bebidas, clientes, facturas)
            subir_datos('Clientes.txt', clientes)
            subir_datos('Facturas_comida.txt', facturas_comida)
            subir_datos('Comida.txt', comida)
            subir_datos('Bebidas.txt', bebidas)
        
        #MODULO 5:
        if menu == 9:
            print(f'\nPromedio de gastos de los clientes: {promedio_gastos(clientes)}')
        if menu == 10:
            print(f'\nPorcentaje de clientes que no compran en la feria: {porcentaje_sin_feria(clientes)}')

        #Shows y productos:
        top_eventos, top_productos = top_eventos_productos(conciertos, obras_teatro, comida, bebidas)

        if menu == 11:
            cont=0
            if len(top_eventos) == 0:
                print('\nNo se han registrado eventos.')
            elif 0 < len(top_eventos) <= 3:
                for i in top_eventos:
                    cont+=1
                    print(f'\nTop {cont}: {i.title}')
            else:
                top3 = [top_eventos[0], top_eventos[1], top_eventos[2]]
                for i in top3:
                    cont+=1
                    print(f'\nTop {cont}: {i.title}')
        
        if menu == 12:
            cont=0
            if len(top_productos) == 0:
                print('\nNo se han registrado productos.')
            elif 0 < len(top_productos) <= 3:
                for i in top_productos:
                    cont+=1
                    print(f'\nTop {cont}: {i.product_name}')
            else:
                top3 = [top_productos[0], top_productos[1], top_productos[2], top_productos[3], top_productos[4]]
                for i in top3:
                    cont+=1
                    print(f'\nTop {cont}: {i.product_name}')
        if menu == 13:
            reiniciar_data(comida, bebidas)
            reiniciar_data_eventos(conciertos, obras_teatro)
            pass
        
        if menu == 14:
            break
    print('bye bye!')


            
    

    

main()