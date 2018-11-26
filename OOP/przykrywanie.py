
class Square:
    def __init__(self, a):
        self.a = a
        self.field = self.a**2

    def add_fields(self, other):
        return self.field + other.field

kw1 = Square(2)
kw2 = Square(3)

print(kw1.field)
print(kw2.field)

print(Square.add_fields(kw1, kw2))
print(kw1.add_fields(kw2))
