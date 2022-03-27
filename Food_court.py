class Food_court:
    def __init__(self, product_name, price): #AGREGAR OPEN PORQUE SE ACABA EL STOCK
        self.product_name = product_name
        self.price = price
    


class Drink(Food_court):
    def __init__(self, product_name, price, sizes):
        super().__init__(product_name, price)
        self.sizes=sizes

class Food(Food_court):
    def __init__(self, product_name, price, is_prepared, is_packed):
        super().__init__(product_name, price)
        self.is_prepared = is_prepared
        self.is_packed = is_packed
        

    