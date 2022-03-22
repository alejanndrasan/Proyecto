
import requests
import json

#Cargar datos:

def cargar_datos(txt, db):
    with open(txt) as dbe:
        db = dbe.readlines()
    return db

#Subir datos:

def write(txt, datos):
    with open(txt,"a+") as dbe:
        dbe.write(datos)
    


#Cargar JSON:

def _json():
    link = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json'
    answer = requests.get(link)

    if answer.status_code == 200:
        db = answer.json()
        return db 



