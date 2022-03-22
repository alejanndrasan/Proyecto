class Client:
    def __init__(self, name, age, id):
        self.__name= name
        self.__age= age
        self.__id = id

    #getters:
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_id(self):
        return self.__id
    
    #setters:
    def set_name(self, new_name):
        self.__name = new_name
    def set_age(self, new_age):
        self.__age = new_age
    def set_id(self, new_id):
        self.__id = new_id
    
    
        