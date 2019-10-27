import random
import math
import math_types


def get_rand_points(how_many, lower_bound=0, upper_bound=100):
    random_points = []
    for i in range(how_many):
        x = random.uniform(lower_bound, upper_bound)
        y = random.uniform(lower_bound, upper_bound)
        p = math_types.Point(x, y)
        random_points.append(p)
    return random_points


def get_rand_points_circle(how_many, center, radius):
    random_points = []
    for i in range(how_many):
        x = radius * math.cos(random.uniform(0, 2 * math.pi)) + center.x
        y = radius * math.sin(random.uniform(0, 2 * math.pi)) + center.y
        p = math_types.Point(x, y)
        random_points.append(p)
    return random_points


def get_rand_points_line(how_many, a, b, lower_bound, upper_bound):
    v = math_types.Vector(b.x - a.x, b.y - a.y)
    random_points = []

    if v.y > v.x:
        for i in range(how_many):
            x = random.uniform(lower_bound, upper_bound)
            y = v.x / v.y * x
            p = math_types.Point(x, y)
            random_points.append(p)
    else:
        for i in range(how_many):
            y = random.uniform(lower_bound, upper_bound)
            x = v.y / v.x * y
            p = math_types.Point(x, y)
            random_points.append(p)

    return random_points


def print_points(points, size):
    for i in range(size):
        print("(" + str(points[i].x) + ", " + str(points[i].y) + ")")


def main():
    size = 20
    lower_bound = -10
    upper_bound = -lower_bound

    center = math_types.Point(1, 0)
    radius = 1

    a = math_types.Point(-1, 0)
    b = math_types.Point(1, 0.1)

    random_points = get_rand_points_line(size, a, b, lower_bound, upper_bound)

    print_points(random_points, size)


if __name__ == "__main__":
    main()
