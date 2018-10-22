liczby = [5 ,2, 1, 4, 3]

min_ = liczby[0]
max_ = liczby[0]

print(liczby)

for liczba in liczby:
    if liczba  < min_:
        min_ = liczba
    if liczba > max_:
        max_ = liczba

print(min_, max_)
print(liczby.index(min_), liczby.index(max_))

liczby[liczby.index(min_)], liczby[liczby.index(max_)] = max_, min_


# assert False
# assert True

assert liczby == [1, 2, 5, 4, 3]

print(liczby)

# for x in liczby:
#     print(f"{max(liczby)}")

# for i in range(len(liczby)):
#     print(liczby[i])

