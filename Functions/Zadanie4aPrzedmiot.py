
class Przedmiot():
    def __init__(self, nazwa, bonus_do_ataku):
        self.nazwa = nazwa
        self.bonus_atk = bonus_do_ataku

    def __str__(self):
        return (f"Przedmiot wsparcia to{self.nazwa}, dodaję {self.bonus_atk} do ataku.")