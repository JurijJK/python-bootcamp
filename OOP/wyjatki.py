
lista = [1, 2, 3]

try:
    print(lista[3])
    list.add(5)
except IndexError as e:
     raise IndexError("Próbujesz pobrać jakiś element spoza zakresu listy")

except AttributeError as e:
    print("Prawdopodobnie wywołujesz metodę, której ten obiekt nie ma")

print("aaa")
