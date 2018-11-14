class Employee():

    def __init__(self, imie, nazwisko, stawka):

        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.godzin = 0

    def register_time(self, godzin):

        self.godzin += godzin
        if godzin > 8:
            self.godzin += godzin - 8


    def pay_salary(self):

        pensja = self.stawka * self.godzin
        self.godzin = 0
        return pensja

pracownik1 = Employee('Jerzy', 'Kasprzak', 50.00)
print(pracownik1.pay_salary())
pracownik1.register_time(5)
pracownik1.register_time(10)
print(pracownik1.pay_salary())






