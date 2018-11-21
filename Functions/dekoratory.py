
def prosty_dekorator(func):
    def wrapper(*args, **kwargs):
        print("Przed wywołaniem")
        result = func(*args, **kwargs)
        print("Po wywołaniu")
        return result
    return wrapper


def dwa_wywolania(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper

@prosty_dekorator
def fun():
    print("Cześć")

@prosty_dekorator
def silnia(x):
    print("Uwaga, liczę silnię")
    wynik = 1
    for i in range(1, x+1):
        wynik *= i
    return wynik

print("Akuku")
fun()
print(silnia(5))
