class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Wektor ({self.x}, {self.y})"

    def __add__(self, other):
        nowy_x = self.x + other.x
        nowy_y = self.y + other.y
        return Vector(nowy_x, nowy_y)

    def __sub__(self, other):
        nowy_x = self.x - other.x
        nowy_y = self.y - other.y
        return Vector(nowy_x, nowy_y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x*other, self.y*other)
        else:
            return Vector(self.x*len(other), self.y*len(other))

    def __truediv__(self, other):
        if isinstance(other, Vector):
            return self.x / other.x + self.y / other.y
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x/other, self.y/other)
        else:
            return Vector(self.x/len(other), self.y/len(other))


v1 = Vector(1,3)
v2 = Vector(2,2)
print(v1)
print(v2)
v3 = v1 + v2
print(v3)
v4 = v1.__add__(v2)
print(v4)
v5 = v1 - v2
print(v5)
v6 = v1 * v2
print(v6)

print(v3, v1/v2)

# # operatory
# +  - __add__
# - - __sub__
# * -



