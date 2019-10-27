import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_unit_vector(self):
        norm = math.sqrt(self.x ** 2 + self.y ** 2)
        return Vector(self.x / norm, self.y / norm)
