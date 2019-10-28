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


def get_rand_points_circle(how_many=100, radius=1, center=my_types.Point(0, 0)):
    random_points = []
    for i in range(how_many):
        angle = random.uniform(0, 2 * math.pi)
        x = radius * math.cos(angle) + center.x
        y = radius * math.sin(angle) + center.y
        p = my_types.Point(x, y)
        random_points.append(p)
    return random_points


def get_rand_points_line(how_many=100, a=my_types.Point(0, 0), b=my_types.Point(1, 1), lower_bound=0,
                         upper_bound=100):
    v = a.make_vector(b)
    random_points = []

    if abs(v.y) > abs(v.x):
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


def main():
    how_many = 20
    lower_bound = -10
    upper_bound = -lower_bound
    center = my_types.Point(1, 0)
    radius = 1
    a = my_types.Point(-1, 0)
    b = my_types.Point(1, 0.1)


if __name__ == "__main__":
    main()
