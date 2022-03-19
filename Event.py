class Event():
    def __init__(self, event_name, poster, layout, price, date):
        self.__event_name = event_name
        self.__poster = poster
        self.__date = date
        
    def get_event_name(self):
        return self.__event_name
    
    def get_poster(self):
        return self.__poster
    
    def get_date(self):
        return self.__date
    
    def get_layout(self):
        return self.__layout
    
    def get_price(self):
        return self.__price

class Concert(Event):
    def __init__(self, event_name, poster, layout, price, date, q_band):
        Event.__init__(self, event_name, poster, layout, price, date,)
        self.__q_band = q_band
    
    def get_q_band(self):
        return self.__q_band

class Play(Event):
    def __init__(self, event_name, poster, layout, price, date, synopsis):
        Event.__init__(self, event_name, poster, layout, price, date,)
        self.__synopsis = synopsis
    
    def get_synopsis(self):
        return self.__synopsis


    