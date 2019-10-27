import random
import math
import my_types


def get_rand_points(how_many=100, lower_bound=0, upper_bound=100):
    random_points = []
    for i in range(how_many):
        x = random.uniform(lower_bound, upper_bound)
        y = random.uniform(lower_bound, upper_bound)
        p = my_types.Point(x, y)
        random_points.append(p)
    return random_points


def get_rand_points_circle(how_many=100, center=my_types.Point(0, 0), radius=1):
    random_points = []
    for i in range(how_many):
        angle = random.uniform(0, 2 * math.pi)
        x = radius * math.cos(angle) + center.x
        y = radius * math.sin(angle) + center.y
        p = my_types.Point(x, y)
        random_points.append(p)
    return random_points


def get_rand_points_line(how_many=100, a=my_types.Vector(0, 0), b=my_types.Vector(1, 1), lower_bound=0,
                         upper_bound=100):
    v = b.subtract(a)
    random_points = []

    if v.y > v.x:
        for i in range(how_many):
            x = random.uniform(lower_bound, upper_bound)
            y = v.x / v.y * x
            p = my_types.Point(x, y)
            random_points.append(p)
    else:
        for i in range(how_many):
            y = random.uniform(lower_bound, upper_bound)
            x = v.y / v.x * y
            p = my_types.Point(x, y)
            random_points.append(p)

    return random_points


def print_points(points):
    for point in points:
        print("(" + str(point.x) + ", " + str(point.y) + ")")


def main():
    how_many = 20
    lower_bound = -10
    upper_bound = -lower_bound
    center = my_types.Point(1, 0)
    radius = 1
    a = my_types.Vector(-1, 0)
    b = my_types.Vector(1, 0.1)

    random_points = get_rand_points_line(how_many, a, b, lower_bound, upper_bound)

    print_points(random_points)


if __name__ == "__main__":
    main()
