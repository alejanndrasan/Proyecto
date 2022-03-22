class Event():
    def __init__(self, title, poster, layout, price, date):
        self.__title = title
        self.__poster = poster
        self.__date = date
        self.__layout = layout
        self.__price = price
    
    #Getters:    
    def get_title(self):
        return self.__title
    
    def get_poster(self):
        return self.__poster
    
    def get_date(self):
        return self.__date
    
    def get_layout(self):
        return self.__layout
    
    def get_price(self):
        return self.__price

    #Setters:
    
    def set_title(self, new_name):
        self.__title = new_name
    
    def set_poster(self, new_poster):
        self.__poster = new_poster
    
    def set_date(self, new_date):
        self.__date = new_date
    
    def set_price(self, new_price):
        self.__price = new_price
    

class Theater(Event):
    def __init__(self, title, poster, layout, price, date, synopsis):
        Event.__init__(self, title, poster, layout, price, date,)
        self.__synopsis = synopsis
    
    def get_synopsis(self):
        return self.__synopsis
    def set_synopsis(self, new_synopsis):
        self.__synopsis = new_synopsis
    

class Music(Event):
    def __init__(self, title, poster, layout, price, date, q_band):
        Event.__init__(self, title, poster, layout, price, date,)
        self.__q_band = q_band
    
    #Getters:
    def get_q_band(self):
        return self.__q_band

    #Setters:
    def set_q_band(self, new_q):
        self.__q_band = new_q
    







    