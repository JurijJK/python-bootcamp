# #tworzenie funkcji
# def hello():
#     print("Hello World")
#     return 10
#
# print(type(hello))   #obiekt funkcji
#
# hello()   # wywołanie funkcji
#
# def hello2(name):
#     print(f'Hello: {name}')
#
# hello2("Jurek")
#
# def hello3(name = "World"):
#     print(f'Hello: {name}')
#
# hello3("Balzac")
#
# x = print("testuje co zwraca print")
#
# print("x:", x)
#
# y = dir()
# print("y: ", y)
#
# z = hello()
#
# print('z: ', z)
#
def dodaj(a, b):
    return a + b


def test_dodaj_dwie_liczby():
    assert dodaj(1, 2) == 3

def test_dodaj_dwa_napisy():
    assert  dodaj("1", "2") == "12"


# wynik = dodaj(10, 11)
# wynik2 = dodaj(1.1, 20.2)
# wynik3 = dodaj("a", "b")
# #wynik4 = dodaj("a", 2)
#
# print(wynik, wynik2, wynik3)



def klon(imie, wiek=18, wzrost=181):
    print(f"witaj {imie}")
    if wiek == 18 and wzrost == 181:
        print(f'Masz standardowe parametry')
    else:
        print(f'Różnisz się od pozostałych')
        print("wiek", wiek)
        print("wzrost", wzrost)

klon("Adam")

klon("Adam", 19)
