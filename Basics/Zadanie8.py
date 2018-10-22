napis = "Ala ma <kota>, a <kot> ma Alę"


licznik = 0
czy_zliczac = False

for i in napis:
    if i == "<":
        czy_zliczac = True
    elif i == ">":
        czy_zliczac = False
    elif czy_zliczac:
        licznik += 1


print(f'Ilość znaków między nawiasami to {licznik}.')


