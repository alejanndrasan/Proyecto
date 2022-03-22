from Food_court import Food, Drink
from Client import Client



class Food_Order(Client, Food, Drink):
    def __init__(self, name, age, id, product_name, price, is_prepared, is_packed, size, ):
        Client().__init__(name, age, id)
        Food().__init__(product_name, price, is_prepared, is_packed)
        Drink().__init__(product_name, price, size)
       