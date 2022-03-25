import pickle
import os
import requests
import json

#Cargar datos:

def cargar_datos(txt):
    file= open(txt,'rb')
    if os.stat(txt).st_size != 0:
        datos=pickle.load(file)
    file.close()
    return datos
    
#Subir datos:

def subir_datos(txt, datos):
    file=open(txt,"wb")
    pickle.dump(datos, file)
    file.close()
    


#Cargar JSON:

def get_json():
    link = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json'
    answer = requests.get(link)

    if answer.status_code == 200:
        db = answer.json()
        return db 

#validaciones:

def val_str(msg1):
    while True:
        string = input(msg1)
        if string.replace(" ", "").isalpha():
            string = string.capitalize()
            return string
            break
        else:
            print('Ingrese una opcion valida')

def val_int(msg1, n):
    while True:
        num = input(msg1)
        if num.replace(" ", "").isnumeric() and 1<=int(num)<n:
            num = int(num)
            return num
            break
        else:
            print('Ingrese una opcion valida.')

def val_names(msg1):
    while True:
        string = input(msg1)
        if string.replace(" ", "").replace('&', '').isalpha():
            string = string.title()
            return string
            break
        else:
            print('Ingrese una opcion valida')
