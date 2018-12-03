

with open("dane/input.txt") as f:
    # print(f.read())
    for linia in f:
        if len(linia) > 600:
            print(linia)



with open("info.txt", "w") as f:
    for i in range(10):
        f.write("Jakiś tekst\n")


with open("info.txt", 'a', encoding='utf8') as f:
    f.write('Inny tekst')