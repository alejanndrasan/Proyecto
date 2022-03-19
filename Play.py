from Event import Event

class Play(Event):
    def __init__(self, event_name, poster, layout, price, date, synopsis):
        Event.__init__(self, event_name, poster, layout, price, date,)
        self.__synopsis = synopsis
    
    def get_synopsis(self):
        return self.__synopsis