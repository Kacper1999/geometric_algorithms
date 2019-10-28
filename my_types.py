import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def make_vector(self, p):
        return Vector(self.x - p.x, self.y - p.y)


def print_points(points):
    for point in points:
        print("(" + str(point.x) + ", " + str(point.y) + ")")


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_unit_vector(self):
        norm = math.sqrt(self.x ** 2 + self.y ** 2)
        return Vector(self.x / norm, self.y / norm)

    def subtract(self, v):
        return Vector(self.x - v.x, self.y - v.y)

    def add(self, v):
        return Vector(self.x + v.x, self.y + v.y)


class Data:
    def __init__(self, random_points):
        self.x_cor = []
        self.y_cor = []
        for point in random_points:
            self.x_cor.append(point.x)
            self.y_cor.append(point.y)
