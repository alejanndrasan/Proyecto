from Client import Client

class Invoice():
    def __init__(self, event, tickets_q, tickets_bill, spots, food_bill):
        self.event= event
        self.tickets_q= tickets_q
        self.tickets_bill= tickets_bill
        self.spots = spots
        self.food_bill = food_bill

    

    