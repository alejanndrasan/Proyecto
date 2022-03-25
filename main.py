from tools import *
from Modulo1 import *

db = get_json()

#Conciertos_DB.txt contiene todos los eventos del tipo musical, bajados de la API.
#Obras_Teatro_DB.txt contiene todos los eventos del tipo teatro, bajados de la API
#Los datos de los archivos de texto de los eventos puede ser alterada (se pueden eliminar eventos), y se vuelve a usar la API cuando se quiera reiniciar la data a su estado inicial.

def main():
    conciertos = cargar_datos('C:\\Users\\Jsantos\\Desktop\\PROYECTO\\Conciertos_DB.txt')
    obras_teatro = cargar_datos('C:\\Users\\Jsantos\\Desktop\\PROYECTO\\Obras_Teatro_DB.txt')
    print('\n---------------------- Saman Show ----------------------\n')
    while True:
        menu = val_int('''\nBienvenido a Saman Show, seleccione que acion desea realizar:
        1. Ver eventos.
        2. Abrir o cerrar venta de tickets.
        3. Buscar evento.
        4. Salir
        ==> ''', 5)

        #MODULO 1:
        if menu == 1:
            ver_evento(conciertos, obras_teatro)
        if menu == 2:
            abrir_cerrar(conciertos, obras_teatro)
            subir_cambios(conciertos, obras_teatro)
        if menu == 3:
            tipo = val_int('\nIngrese el tipo de evento que busca: \n1.Tipo musical. \n2.Tipo teatral. \n==> ', 3)
            if tipo ==1:
                resultado = buscar_concierto(conciertos)
                resultado.show_concert()
            else:
                resultado = buscar_obra(obras_teatro)
                resultado.show_play()
        if menu == 4:
            break
    print('bye bye!')


            
    

    

main()