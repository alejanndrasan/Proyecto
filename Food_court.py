class Food_court:
    def __init__(self, product_name, price):
        self.__product_name = product_name
        self.__price = price
    
    #getters:
    def get_product_name(self):
        return self.__product_name
    def get_age(self):
        return self.__price
    
    #setters:
    def set_product_name(self, new_product_name):
        self.__product_name = new_product_name
    def set_price(self, new_price):
        self.__price = new_price

class Drink(Food_court):
    def __init__(self, product_name, price, size):
        super().__init__(product_name, price)
        self.__size=size

    #getters:
    def get_size(self):
        return self.__size
    
    #setters:
    def set_size(self, new_size):
        self.__size = new_size

class Food(Food_court):
    def __init__(self, product_name, price, is_prepared, is_packed):
        super().__init__(product_name, price)
        self.__is_prepared = is_prepared
        self.__is_packed = is_packed
        
    #getters:
    def get_is_prepared(self):
        return self.__is_prepared
    def get_is_packed(self):
        return self.__is_packed
    
    #setters:
    def set_is_prepared(self, new_boolean):
        self.__is_prepared = new_boolean
    def set_is_packed(self, new_boolean):
        self.__is_packed = new_boolean
    