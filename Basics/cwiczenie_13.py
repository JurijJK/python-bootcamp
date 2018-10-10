suma_temperatur = 0
i = 0

while i < 7:
    d = (input('Temperatura: '))
    #d = (d + d) / (a+1)



    if d == 'stop':
        break

    suma_temperatur += float(d)

print("średnia temperatura to:", round(suma_temperatur/i,2))

