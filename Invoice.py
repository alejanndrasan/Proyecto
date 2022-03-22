from Client import Client

class Invoice(Client):
    def __init__(self, name, age, id, event, tickets_q, spots, tickets_bill):
        super().__init__(name, age, id)
        self.__event= event
        self.__tickets_q= tickets_q
        self.__spots = spots
        self.__tickets_bill= tickets_bill

    #getters:
    def get_event(self):
        return self.__event
    def get_tickets_q(self):
        return self.__tickets_q
    def get_spots(self):
        return self.__spots
    def get_tickets_bill(self):
        return self.__tickets_bill
    
    
    #setters:
    def set_event(self, new_event):
        self.__event = new_event
    def set_tickets_q(self, new_q):
        self.__tickets_q = new_q
    def set_spots(self, new_spots):
        self.__spots = new_spots
    def set_tickets_bill(self, new_bill):
        self.__tickets_bill = new_bill

    