
liczby = set()

while True:
    komenda = input("Podaj liczbę lub wpisz K by zakończyć: ")
    if komenda.lower() == 'k':
        break
    else:
        liczba = int(komenda)
        liczby.add(liczba)

print(f"Unikalnych liczb: {len(liczby)}")

liczby_parzyste = set(range(0, 100, 2))
print(f"W tym liczb parzystych od 0 do 100 {len(liczby & liczby_parzyste)}")

