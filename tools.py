import pickle
import os
import requests
import json

#Cargar datos:

def read_db(txt, data):
    a = open(txt, "rb")
    if os.stat(txt).st_size != 0:
        data = pickle.load(a)
    a.close()

    return data

#Subir datos:

def write(txt, data):
    
    b = open(txt, "wb")
    pickle.dump(data, b)
    b.close()


#Cargar JSON:

def _json():
    link = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json'
    answer = requests.get(link)

    if answer.status_code == 200:
        db = answer.json()
        return db 