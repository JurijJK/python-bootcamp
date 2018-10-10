import datetime

year = datetime.datetime.now().year



rok_ur = float(input('Rok urodzenia: '))
#rok_b = float(input('Rok bieżący: '))

wiek = year - rok_ur
wiek = int(wiek)

print(f'Twój wiek to: {wiek}')

if wiek > 18:
    print('Jesteś pełnoletni!')
else:
    print('Jesteś niepełnoletni!')



