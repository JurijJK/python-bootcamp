class Product():
    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f'Produkt {self.nazwa}, id {self.id}, cena {self.cena}')

    def daj_cene(self):
        return self.cena

class BasketEntry:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.cena * self.quantity

    def __str__(self):
        return f'{self.product.nazwa} | {self.product.quantity}'

class Basket:
    def __init__(self):
        self.entries = []

    def add_product(self, product, qty):
        self.entries.append([product, qty])

    def count_total_price(self):
        total_price = 0
        for entry in self.entries:
            total_price += entry.count_price()
        return total_price

    def generate_report(self):
        pass


pr1 = Product(1, 'Woda', 2)
pr2 = Product(2, 'Piwo', 3)
pr3 = Product(3, 'Salceson', 2)

basket = Basket()
basket.add_product(pr1, 4)
basket.add_product(pr2, 2)
basket.add_product(pr3, 1)
basket.add_product(pr1, 3)

print(basket.count_total_price())


