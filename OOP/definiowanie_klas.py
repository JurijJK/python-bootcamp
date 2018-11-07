

class Animal: # może być nawias ale nie musi przy tworzeniu klasy. Przy funkcjach nawias niezbędny.
    krolestwo = "Fauna"

    def __init__(self, nazwa):
        self.nazwa = nazwa

zyrafa = Animal() # to jest Instancja Klasy. przy tworzeniu obiektu nawias już potrzebny

print(type(zyrafa))
print(zyrafa.krolestwo)
