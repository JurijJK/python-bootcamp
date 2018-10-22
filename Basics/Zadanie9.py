suma = 0
Zakupy = {}

Zakupy["Ser"] = 11
Zakupy["Kiełbasa"] = 15
Zakupy["Chleb"] = 4

print(Zakupy)

print("W naszym sklepie oferujemy:")

for produkt in Zakupy:
    print(f" - {produkt} - w cenie: {Zakupy[produkt]} PLN")

print()

wybor_produktu = input("Który produkt chcesz kupić? ")
ile = input(f'Ile kilogramów chcesz kupić [{wybor_produktu}]')

Cena = wybor_produktu * int(ile)
print(Cena)


# input('Wprowadź produkt: ')
#
# for x in Zakupy:
#
#     suma = suma + Zakupy[x]
#
