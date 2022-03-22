from Event import *
diccionario = {
            'eventos': [
            {
                "title": "Saman Fest",
                "type": 1,
                "bands": 4,
                "cartel": [
                    "Los Cocineros",
                    "Ramayana",
                    "CacetVersus",
                    "La vida Hippie"
                ],
                "layout": {
                    "general": [
                        4,
                        10
                    ],
                    "vip": [
                        1,
                        10
                    ]
                },
                "prices": [50, 100],
                "date": "2022-04-01"
		    },
            {
			"title": "El famtasma del paraninfo",
			"synopsis": "En esencia, la trama de El Fantasma del Paraninfo es una historia que combina romance, música, terror, misterio y tragedia. Trata de Eric, un hombre misterioso, un genio musical, que se enamora perdidamente de Cristina, una joven y talentosa artista, a quien inspira musicalmente",
			"type": 2,
			"cartel": [
				"Leonardo DeCapo",
				"Cendella",
				"Ed Ramiro"
			],
			"layout": {
				"general": [
					5,
					10
				],
				"vip": [
					4,
					3
				]
			},
			"prices": [5, 10],
			"date": "2022-05-10"
		},
        {
			"title": "KenaAna & Guako",
			"type": 1,
			"bands": 2,
			"cartel": [
				"Guako",
				"kenaAna"
			],
			"layout": {
				"general": [
					4,
					10
				],
				"vip": [
					1,
					6
				]
			},
			"prices": [30, 50],
			"date": "2022-04-01"
		},
        {
			"title": "Romeo & Julieta",
			"synopsis": "En Verona, dos jóvenes enamorados, de dos familias enemigas, son víctimas de una situación de odio y violencia que ni desean ni pueden remediar. En una de esas tardes de verano en que el calor «inflama la sangre», Romeo, recién casado en secreto con su amada Julieta, mata al primo de ésta",
			"type": 2,
			"cartel": [
				"Romeo Gonzalez",
				"Julieta Hernandez"
			],
			"layout": {
				"general": [
					1,
					5
				],
				"vip": [
					1,
					5
				]
			},
			"prices": [10, 25],
			"date": "2022-12-31"
		}
        ]
    }

#Las siguientes funciones son para volver los datos dentro de la base de datos en listas de objetos:

def objectify_data_concerts(dicc, lista): #tengo que cargar los valores en una db (dicc=db) y hacer una lista al inicio del programa que me cargue los objetos
    for key, value in dicc.items():
        for i in range(0, (len(dicc[key]))): 
            if value[i]['type']==1:       
                concert_n = Music(value[i]['title'], value[i]['cartel'], value[i]['layout'], value[i]['prices'], value[i]['date'], value[i]['bands'])
                lista.append(concert_n)
    return lista

def objectify_data_plays(dicc, lista): #tengo que cargar los valores en una db (dicc=db) y hacer una lista al inicio del programa que me cargue los objetos
    for key, value in dicc.items():
        for i in range(0, (len(dicc[key]))): 
            if value[i]['type']==2:

                play_n = Theater(value[i]['title'], value[i]['cartel'], value[i]['layout'], value[i]['prices'], value[i]['date'], value[i]['sinopsis'])
                lista.append(play_n)
    return lista




#funciones para alterar los datos de los objetos:

'''def matrix(x, y, m):
    i = 0
    matriz = [m] * x
    for i in range (x):
        matriz [i] = [m] * y
    return matriz

matriz = matrix(4,10,'G')'''





            





