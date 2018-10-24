suma = 0
produkty = {}
magazyn = {}
koszyk = {}

magazyn["Ser"] = 20
magazyn["Kiełbasa"] = 15
magazyn["Chleb"] = 12

produkty["Ser"] = 11
produkty["Kiełbasa"] = 15
produkty["Chleb"] = 4

print(produkty)
print(magazyn)
while True:
    komenda = input("""Wybierz opcję:
    [d] - dodaj do magazynu
    [k] - kup
    [z] - zakończ
    """)
    if komenda == 'k':

    if komenda == 'd':
        co = input("Jaki produk chcesz dodać?")
        ile = int(input(f'Ile {co} chcesz dodac?'))
        magazyn[co] = magazyn.get(co, 0) + ile
        if co not in produkty:
            cena = float(input(f'Jaka cena za {co}'))
            produkty[co] = cena
    elif komenda == 'z':
        break

while True:
    print(f"W naszym sklepie oferujemy:")
    for produkt in produkty:
         print(f" - {produkt} - w cenie: {produkty[produkt]} PLN")

    print()

    wybor_produktu = input("Który produkt chcesz kupić? ")
    if wybor_produktu == "koniec":
        break
    if wybor_produktu in produkty:
        ile = input(f'Ile kilogramów chcesz kupić [{wybor_produktu}]')

        if ile <= magazyn[wybor_produktu]:
            koszyk[wybor_produktu] = ile
            magazyn[wybor_produktu] -= ile
        else:
            print("Nie mam tyle produktu. Postało {magazyn[wybor_produktu}")
            cena = produkty[wybor_produktu] * int(ile)
            koszyk[wybor_produktu] = cena
            print(f'Zapłacisz: {cena}')
            # magazyn[wybor_produktu] = magazyn[wybor_produktu] - int(ile)

    else:
        print("Nie mam takiego produktu")
    print()
    print("-"*40)

print("Twój rachunek: ")
sumarycznie = 0
for produkt in koszyk:
    print(f' - {produkt}: {koszyk[produkt]} PLN')
    sumarycznie += koszyk[produkt]

print("-"*30)
print(f'Suma: {sumarycznie} PLN')

print("Dziękujemy! Zapraszamy ponownie!")


# input('Wprowadź produkt: ')
#
# for x in Zakupy:
#
#     suma = suma + Zakupy[x]
#
