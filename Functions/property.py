class Temperatura():
    def __init__(self, x):
        self.wartosc = x

    def __str__(self):
        return (f"Temperatura: {self.wartosc} stopni Celcjusza.")

    @property
    def wartosc(self):
        print("getter")
        return self._wartosc

    @wartosc.setter
    def wartosc(self, x):
        print("setter")
        if x < -273:
            raise ValueError("Temperatura za niska!")
        self._ wartosc = x



x = Temperatura(20)
print(x)
x.wartosc = 100
print(x)
print(x.wartosc)
x.wartosc = -300
print(x)