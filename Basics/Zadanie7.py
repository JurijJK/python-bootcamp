napis = input("Podaj napis: ")

licznik = 0

SAMOGLOSKI = "aeiouy"





for litera in napis.lower():
    if litera in SAMOGLOSKI:
        licznik +=1

print(f'W napisie wstępuje {licznik} samogłosek')




