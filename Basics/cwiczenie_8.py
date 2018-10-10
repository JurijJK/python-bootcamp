wys = float(input('Wysokość [cm}: '))
dlu = float(input('Długość [cm]: '))
sze = float(input('Szerokość [cm]: '))

objetosc = (wys * dlu * sze) / 1000

print(f'Objętość wynosi [litr]: {objetosc}')

if objetosc > 1:
    print('Objętość większa niż 1 litr.')
elif objetosc < 1:
    print('Objętość mniejsza niż 1 litr.')
else:
   print('Objętość równa się 1 litr.')