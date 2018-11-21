
from random import randint
from Zadanie4aPrzedmiot import Przedmiot


class Postac():
    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self.atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.ekwipunek = []

    @property
    def atak(self):
        wynik = self._atak
        for p in self.ekwipunek:
            wynik +=p.bonus_atk
        return wynik

    def przedstaw_sie(self):
        print(f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.")

    def __str__(self):
        if self.czy_zyje() == True:
            napis = "EKWIPUNEK:\n"
            for x in self.ekwipunek:
                napis += str(x) + "\n"
            return (f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.\n") + napis
        else:
            return (f"Cześć byłem {self.imie}, ale już mnie nie ma.")

    def otrzymane_obrazenia(self, ile):
        self.zdrowie -= ile
        if self.zdrowie <= 0:
            self.zdrowie = 0

    def czy_zyje(self):
        return self.zdrowie > 0

    def wylecz(self, healing):
        if self.czy_zyje() == True:
            if (self.zdrowie + healing) > self.max_zdrowie:
                self.max_zdrowie = self.zdrowie
            else:
                self.zdrowie += healing

        else:
            return print("Jesteś martwy, nie możesz się wyleczyć!")

    def moc_ataku(self):
        return randint(self.atak//2, int(self.atak*1.5))

    def daj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def atak_pus(self):

    @staticmethod
    def walka(atakujacy, broniacy):
        print(f"Walka: {atakujacy.imie} vs. {broniacy.imie}")
        while atakujacy.czy_zyje() and broniacy.czy_zyje():
            print(atakujacy)
            print(broniacy)
            atak_atakujacego = atakujacy.moc_ataku()
            atak_broniacego = broniacy. moc_ataku()
            print(f"{atakujacy.imie} uderza {broniacy.imie} za {atak_atakujacego} obrażeń")
            broniacy.otrzymane_obrazenia(atak_atakujacego)
            print(f"{broniacy.imie} atakuje {atakujacy.imie} za {atak_broniacego} obrażeń")
            atakujacy.otrzymane_obrazenia(atak_broniacego)
        print("Koniec Walki")


rufus = Postac("Rufus", 60, 1000)
janusz = Postac("Janusz", 70, 800)
Postac.walka(rufus, janusz)
print(rufus)
print(janusz)

tulipan = Przedmiot("Zielony tulipan zniszczenia", 5)
rufus.daj_przedmiot(tulipan)



def test_nowa_postac():
    postac = Postac("Albert", 1, 20)
    assert postac.imie == "Albert" and postac.atak == 1 and postac.zdrowie == 20 and postac.max_zdrowie == 20

def test_obrazenia():
    postac = Postac("Rafał", 5, 200)
    assert postac.zdrowie == 200
    postac.otrzymane_obrazenia(80)
    assert postac.zdrowie == 120
    postac.otrzymane_obrazenia(200)
    assert postac.zdrowie == 0

def test_leczenie_nieboszczyka():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymane_obrazenia(800)
    assert postac.zdrowie == 0
    postac.wylecz(50)
    assert postac.zdrowie == 0

def test_za_duze_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymane_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(500)
    assert postac.zdrowie == 200