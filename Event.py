class Event():
    def __init__(self, title, poster, layout_general, layout_vip, ticket, date, opened):
        self.title = title
        self.poster = poster
        self.date = date
        self.layout_general = layout_general
        self.layout_vip = layout_vip
        self.ticket = ticket
        self.opened = opened #Pasar este atributo a False una vez que se llenen todos los puestos
    
    def show_title(self):
        print(f'''\n------------------ Titulo ------------------\n
    {self.title}''')
    
    def show_poster(self):
        cont = 0
        print('\n------------------ Actores ------------------\n')
        for i in self.poster:
            cont+=1
            print(f'''{cont}. {i}''')
    
    def show_date(self):
        print(f'''\n------------------ Fecha ------------------\n
        {self.date}''')
    
    def show_tickets(self):
        print(f'''\n------------------ Tickets ------------------\n
        Sala General: Bs. {self.ticket[0]}. 
        Sala VIP: Bs. {self.ticket[1]}.''')
    
    def show_layout(self):
        print(f'''\n------------------ Puestos ------------------\n''')
        print('''\n------------------ General ------------------\n''')
        for i in self.layout_general: 
            print(i)
        print('''\n------------------ VIP ------------------\n''')
        for i in self.layout_vip: 
            print(i)
        
    
    def open_close(self, msg):
        if msg == 'Abrir venta':
            self.opened=True
        elif msg == 'Cerrar venta':
            self.opened = False


class Theater(Event):
    def __init__(self, title, poster, layout_general, layout_vip,  ticket, date, synopsis, opened):
        Event.__init__(self, title, poster, layout_general, layout_vip,  ticket, date, opened)
        self.synopsis = synopsis
    
    def show_synopsis(self):
        print(f'''\n------------------ Sinopsis ------------------ 
        \n{self.synopsis}''')
    
    def show_whole_play(self):
        if self.opened == True:
            self.show_title()
            self.show_synopsis()
            self.show_poster()
            self.show_date()
            self.show_tickets()
            self.show_layout()

    
class Music(Event):
    def __init__(self, title, poster, layout_general, layout_vip,  ticket, date, q_band, opened):
        Event.__init__(self, title, poster, layout_general, layout_vip,  ticket, date, opened)
        
        self.q_band = q_band
    
    def show_q_band(self):
        print(f'''\nNumero de bandas: {self.q_band}''')

    def show_whole_concert(self):
        if self.opened==True:
            self.show_title()
            self.show_q_band()
            self.show_poster()
            self.show_date() 
            self.show_tickets()
            self.show_layout()
        
    
    







    