a = (input('Liczba pierwsza: '))
b = (input('Liczba druga: '))

if a.isnumeric() and b.isnumeric():

    a = int(a)
    b = int(b)

    znak = input('Podaj rodzaj operacji [+-*/]: ')

    if znak == '+':
        wynik = a + b
    elif znak =='-':
        wynik = a - b
    elif znak =='*':
        wynik = a * b
    elif znak =='/':
        if b == 0:
            wynik = "Nie dziel przez zero!"
        else:
             wynik = a / b
    else:
        print('Nieznana operacja')


print(f'Wynik działania {znak} na argumentach: {a}, {b} to: {wynik}')