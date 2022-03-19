from Event import Event

class Concert(Event):
    def __init__(self, event_name, poster, layout, price, date, q_band):
        Event.__init__(self, event_name, poster, layout, price, date,)
        self.__q_band = q_band
    
    #getters:
    def get_q_band(self):
        return self.__q_band

    #Setters:
    def set_q_band(self, new_q):
        self.__q_band = new_q
    