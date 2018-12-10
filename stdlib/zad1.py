import json


try:
    with open("pracownicy.json", "r") as plik:
        pracownicy = json.load(plik)
except FileNotFoundError:
    pracownicy = []

op = input("Co chcesz zarobić? [d - dodaj, w - wypisz] ")
if op == 'd':
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    rok_urodzenia = int(input("Rok urodzenia: "))
    pensja = float(input("Pensja: "))
    print(f'{imie} {nazwisko} - rok: {rok_urodzenia}, pensja: {pensja} PLN')
    pracownicy.append({"imie": imie, "nazwisko": nazwisko, "rok urodzenia": rok_urodzenia, "pensja": pensja})
    with open("pracownicy.json", "w") as plik:
        json.dump(pracownicy, plik)

elif op == 'w':
    for nr, p in enumerate(pracownicy, 1):
        print(f"- [{nr}] {p['imie']} {p['nazwisko']} - rok: {p['rok urodzenia']}, pensja: {p['pensja']} PLN")