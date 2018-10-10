x = int(input('Podaj pozycję gracza X: '))
y = int(input('Podaj pozycję gracza Y: '))

if x > 100 or x < 0 or y > 100 or y < 0:
    print('Jesteś poza planszą!')
else:
    if x < 10 and y < 10:
        print('Jesteś w LD')
    if x < 10 and y > 90:
        print('Jesteś w LG')
    if x > 90 and y < 10:
        print('Jesteś w PD')
    if x > 90 and y > 90:
        print('Jesteś w PG')
    if x > 10 and x < 90 and y < 10:
        print('Jesteś na DK')
    if x > 10 and x < 90 and y > 90:
        print('Jesteś na GK')
    if y> 10 and y < 90 and x > 90:
        print('Jesteś na PK')
    if y> 10 and y < 90 and x < 10:
        print('Jesteś na LK')
    else:
        print('Jesteś w Centrum')