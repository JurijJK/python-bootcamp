class Product():

    def __init__(self, id, nazwa, cena):

        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f'Produkt: ID: {self.id} Nazwa: {self.nazwa} Cena: {self.cena}')



product = Product(1, 'Woda', 10.99)
product2 = Product(2, 'Chleb', 5.99)
product.print_info()
product2.print_info()
