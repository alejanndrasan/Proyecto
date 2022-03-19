class Event():
    def __init__(self, event_name, poster, layout, price, date):
        self.__event_name = event_name
        self.__poster = poster
        self.__date = date
    
    #Getters:    
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

    #Setters:
    
    def set_event_name(self, new_name):
        self.__event_name = new_name
    
    def set_poster(self, new_poster):
        self.__poster = new_poster
    
    def set_date(self, new_date):
        self.__date = new_date
    
    def set_price(self, new_price):
        self.__price = new_price
    







    