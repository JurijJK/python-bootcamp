from random import randint

graczX = randint(1, 10)
graczY = randint(1, 10)

skarbX = randint(1, 10)
skarbY = randint(1, 10)



while True:
    kierunek = input("Podaj kierunek: ")

    print(f"Położenie gracza to ({graczX}, {graczY})")
    #print(f"Odległość od skarbu to {minKrokow} kroków")

    minKrokowPrzed = abs(skarbX - graczX) + abs(skarbY - graczY)

    if kierunek == "w":
        graczY += 1
    elif kierunek == "s":
        graczY -= 1
    elif kierunek == "a":
        graczX -= 1
    elif kierunek == 'd':
        graczX += 1

    minKrokowPo = abs(skarbX - graczX) + abs(skarbY - graczY)

    if minKrokowPo == 0:
        print("!!!You Won!!!")
        break


    if randint(1, 5) < 5
        if minKrokowPrzed < minKrokowPo:
            print("Oddalasz się")
        else:
            print("Zbliżasz się")



   # print(f"({skarbX}, {skarbY})")



    if graczX < 1 or graczX > 10 or graczY < 1 or graczY > 10:
        print('Game Over :-(')
        break
