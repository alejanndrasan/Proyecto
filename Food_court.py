class Food_court:
    def __init__(self, product_name, price, stock, ventas): #AGREGAR OPEN PORQUE SE ACABA EL STOCK
        self.product_name = product_name
        self.price = price
        self.stock = stock
        self.ventas = ventas


class Drink(Food_court):
    def __init__(self, product_name, price, stock, sizes, ventas):
        super().__init__(product_name, price, stock, ventas)
        self.sizes=sizes
    
    def show_drink(self):
        print('\n*********************************\n')
        print(f'Bebida: {self.product_name}\n')
        for i in range(len(self.stock)):
            if self.stock[i] > 0:
                print(f'''Tamaño: {self.sizes[i]}
Precio: Bs. {round(self.price[i], 2)}''')
            print('*********************************')


class Food(Food_court):
    def __init__(self, product_name, price, stock, presentation, ventas):
        super().__init__(product_name, price, stock, ventas)
        self.presentation = presentation
    def show_presentation(self):
        if self.presentation == 1:
            return 'Preparado'
        else:
            return 'Empacado'
    
    def show_food(self):
        print(f'Producto: {self.product_name}')
        if self.stock > 0:
            print(f'''Presentacion: {self.show_presentation()}
Precio: Bs. {round(self.price, 2)}''')

    