# def foo(pierwszy, *reszta ):
#     print("pierwszy: ", pierwszy)
#     print("reszta", reszta)
#     if reszta:
#         return pierwszy + reszta[-1]
#
# print(foo(1))
# print(foo(1, 2))
# print(foo(1, 2, 5, 10))
# print(foo(1, 2, 5, 10, 15))
#
# reszta = [1, 2, 5, "coś tam jeszcze"]
# print(1, 2, 5, "coś tam jeszcze")
# print(*reszta)
#
#
#
# def druga_funkcja(**slownik):
#     if 'd' in slownik:
#         return slownik['a'] + slownik['d']
#     if slownik:
#         return slownik['a']
#     return "Żaden warunek nie był spełniony"
#
#
#      return wynik
#
#
# print('a', druga_funkcja(a=2))
# print('a i d', druga_funkcja(a=2, b=2, c=3, d=4))
# print('a i d drugi raz', druga_funkcja(a=2, b=2, c=3, d=4, zosia=5, adas=15))
# print('a drugi raz ale bez d', druga_funkcja(a=2, b=2, c=3, d=4, zosia=5, adas=15))


#
# co_na_co = {"Ala": "Kot", "kota":"Alę"}
#
# # "Ala ma kota" -> "Kot ma Alę"
#
# def zamien(jakis_tekst, **co_na_co):
#     for klucz in co_na_co:
#         jakis_tekst = jakis_tekst.replace(klucz, co_na_co[klucz])
#
#     return jakis_tekst
#
# print(zamien("Ala ma kota", Ala="Kot", kota="Alę"))
#
# slownik = dict(a=1, b=2, ma="bije")
# print(slownik)



napis = "Ten $produkt kosztuje $cena"
napis2 = "Zajecia z $przedmiot zostały odwołane"

# produkt = {"$produkt":"Samochód", "$cena":"20000"}

def formatuj(napis, **produkt):
    for klucz in produkt:
        # print("$"+klucz)
        napis = napis.replace("$"+klucz, produkt[klucz])

    return napis

print(formatuj("Ten $produkt kosztuje $cena", produkt="Samochód", cena="20000"))


def formatuj(*napisy, **co_na_co):
    wynik = []
    for napis in napisy:
        for klucz in co_na_co:
            napis = napis.replace("$"+klucz, co_na_co[klucz])
        wynik.append(napis)
    if len(wynik) == 1:
        return wynik[0]
    return wynik


assert formatuj(napis, produkt="Samochód", cena="20000") == "Ten Samochód kosztuje 20000"

# assert format(napis, przedmiot="Fizyki") == "Zajecia z Fizyki zostały odwołane"


