class Event():
    def __init__(self, title, poster, layout, ticket, date):
        self.title = title
        self.poster = poster
        self.date = date
        self.layout = layout
        self.ticket = ticket
    
    def show_title(self):
        print(f'''\nTitulo de Evento: {self.title}''')
    
    def show_poster(self):
        cont = 0
        print('\n')
        for i in self.poster:
            cont+=1
            print(f'{cont}. {i}')
    
    def show_date(self):
        print(f'\nFecha: {self.date}')
    
    def show_tickets(self):
        print(f'''
        \nSala General: {self.ticket[0]}
        Sala VIP: {self.ticket[0]}''')
    
    def show_layout(self):
        pass
    
    
    

class Theater(Event):
    def __init__(self, title, poster, layout, price, date, synopsis):
        Event.__init__(self, title, poster, layout, price, date,)
        self.synopsis = synopsis
    
    
    

class Music(Event):
    def __init__(self, title, poster, layout, price, date, q_band):
        Event.__init__(self, title, poster, layout, price, date,)
        self.q_band = q_band
    
    
    







    