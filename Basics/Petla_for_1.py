lista = [1,2,-4,-9,5,6,7,-8]
lista_plus = []
lista_minus = []
liczba = 0
d = 0
u = 0

for l in lista:
    if l < 0:
        lista_minus.append(l)
    elif l > 0:
        lista_plus.append(l)

#print(lista_minus)
x = len(lista_minus)
print(f'Liczba ujemnych: {x}')

#print(lista_plus)
y = len(lista_plus)
print(f'Liczba ujemnych: {y}')

for liczba in lista:
    if liczba > 0:
        d += 1

    elif liczba <  0:
        u += 1


print(f'Ilość dodatnich: {d}, ilość ujemnych: {u}')



