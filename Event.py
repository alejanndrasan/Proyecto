import emoji

class Event():
    def __init__(self, title, poster, layout_general, layout_vip, general_seats, vip_seats, ticket, date, opened, ventas):
        self.title = title
        self.poster = poster
        self.date = date
        self.layout_general = layout_general
        self.layout_vip = layout_vip
        self.ticket = ticket
        self.opened = opened #Pasar este atributo a False una vez que se llenen todos los puestos
        self.general_seats = general_seats
        self.vip_seats = vip_seats
        self.ventas = ventas 
    
    def show_title(self):
        print(f'''\n-Titulo:{self.title}''')
    
    def show_poster(self):
        cont = 0
        print('\n-Actores: \n')
        for i in self.poster:
            cont+=1
            print(f'''{cont}. {i}''')
    
    def show_date(self):
        print(f'''\n-Fecha:{self.date}''')
    
    def show_tickets(self):
        if self.opened == True:
            print(f'''\n-Tickets: \n
Sala General: Bs. {self.ticket[0]}. 
Sala VIP: Bs. {self.ticket[1]}.''')
        else: 
            print('\nLa venta de este evento esta cerrada.') 
    
    def show_layout(self):
        if self.opened == True:
            print(f'''\n-Puestos:\n''')
            print('''\n------------------ General -------------------\n
Nota: los puestos con la plantita se encuentran ocupados.\n''')
            for i in self.layout_general: 
                print(i)
            print('''\n------------------ VIP ------------------\n
Nota: los puestos con la flor se encuentran ocupados.''')
            for i in self.layout_vip: 
                print(i)
            print(f'''      \n------------------ Escenario ------------------\n''') #ponerle emoji de pantalla
        else: 
            return 1
    
    
    def select_seats_general(self, spot):
        for i in range(len(self.layout_general)):
            for j in range(len(self.layout_general[i])):
                if spot == self.layout_general[i][j]:
                    temp = [i, j]
                    self.layout_general[i][j] = emoji.emojize(':seedling:')
                    return temp
    
    def deselect_seats_general(self, spot, temp):
        for i in range(len(self.layout_general)):
            for j in range(len(self.layout_general[i])):
                if self.layout_general[temp[0]][temp[1]] == emoji.emojize(':seedling:'):
                    self.layout_general[temp[0]][temp[1]] = spot
    
    def select_seats_vip(self, spot):
        for i in range(len(self.layout_vip)):
            for j in range(len(self.layout_vip[i])):
                if spot == self.layout_vip[i][j]:
                    temp = [i, j]
                    self.layout_vip[i][j] = emoji.emojize(':blossom:')
                    return temp
    
    def deselect_seats_vip(self, spot, temp):
        for i in range(len(self.layout_vip)):
            for j in range(len(self.layout_vip[i])):
                if self.layout_vip[temp[0]][temp[1]] == emoji.emojize(':blossom:'):
                    self.layout_vip[temp[0]][temp[1]] = spot

    def open_close(self, msg):
        if msg == 1:
            self.opened = True
        elif msg == 2:
            self.opened = False


class Theater(Event):
    def __init__(self, title, poster, layout_general, layout_vip,  general_seats, vip_seats, ticket, date, synopsis, opened, ventas):
        Event.__init__(self, title, poster, layout_general, layout_vip, general_seats, vip_seats, ticket, date, opened, ventas)
        self.synopsis = synopsis
    
    def show_synopsis(self):
        print(f'''\n- Sinopsis: 
        \n{self.synopsis}''')
    
    def show_play(self):
        self.show_title()
        self.show_synopsis()
        self.show_poster()
        self.show_date()
        self.show_tickets()
        self.show_layout()
    
    def show_play_for_sales(self):
        if self.opened == True:
            self.show_title()
            self.show_synopsis()
            self.show_poster()
            self.show_date()
            self.show_tickets()
            self.show_layout()
        else:
            print('\nLa venta de este evento esta cerrada.')       

    
class Music(Event):
    def __init__(self, title, poster, layout_general, layout_vip,  general_seats, vip_seats, ticket, date, q_band, opened, ventas):
        Event.__init__(self, title, poster, layout_general, layout_vip, general_seats, vip_seats, ticket, date, opened, ventas)
        
        self.q_band = q_band
    
    def show_q_band(self):
        print(f'''\nNumero de bandas: {self.q_band}''')

    def show_concert(self):
        self.show_title()
        self.show_q_band()
        self.show_poster()
        self.show_date() 
        self.show_tickets()
        self.show_layout()
    
    def show_concert_for_sales(self):
        if self.opened == True:
            self.show_title()
            self.show_q_band()
            self.show_poster()
            self.show_date() 
            self.show_tickets()
            self.show_layout()
        else:
            print('\nLa venta de este evento esta cerrada.')    
        
    
    







    