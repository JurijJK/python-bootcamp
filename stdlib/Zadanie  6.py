from threading import Thread
from urllib.request import urlopen
from time import time
from time import sleep

# Pierwsza Metoda

przed = time()
i = urlopen("https://www.metaweather.com/api/location/search/?query=london")
for i in range(10):
    with urlopen("https://www.metaweather.com/api/location/search/?query=london") as plik:
        print(plik.read())


po = time()


print(f"Czas {po - przed}s")

# Druga Metoda

przed2 = time()

class MyThread(Thread):


    def run(self):
        with urlopen("https://www.metaweather.com/api/location/search/?query=london") as plik2:
            print(plik2.read())


watki = []
for i in range(10):
    watek = MyThread()
    watek.start()
    watki.append(watek)

for watek in watki:
    watek.join()

po2 = time()

print(f"Czas {po2 - przed2}s")