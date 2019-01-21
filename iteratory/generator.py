def wypisz_samogloski(napis):
    for litera in napis:
        if litera in "aeiouy":
            yield litera

for l in wypisz_samogloski('drzewo i krzew'):
    print(l)