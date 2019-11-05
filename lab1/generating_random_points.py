import random
import math


def get_rand_points(how_many=100, lower_bound=0, upper_bound=100):
    random_points = []
    for i in range(how_many):
        x = random.uniform(lower_bound, upper_bound)
        y = random.uniform(lower_bound, upper_bound)
        p = (x, y)
        random_points.append(p)
    return random_points


def get_rand_points_circle(how_many=100, radius=1, center=(0, 0)):
    random_points = []
    for i in range(how_many):
        angle = random.uniform(0, 2 * math.pi)
        x = radius * math.cos(angle) + center[0]
        y = radius * math.sin(angle) + center[1]
        p = (x, y)
        random_points.append(p)
    return random_points


def get_rand_points_line(how_many=100, a=(0, 0), b=(1, 1), lower_bound=0,
                         upper_bound=100):
    v = (b[0] - a[0], b[1] - a[1])
    random_points = []

    if abs(v[1]) > abs(v[0]):
        for i in range(how_many):
            x = random.uniform(lower_bound, upper_bound)
            y = v[0] / v[1] * x
            p = (x, y)
            random_points.append(p)
    else:
        for i in range(how_many):
            y = random.uniform(lower_bound, upper_bound)
            x = v[1] / v[0] * y
            p = (x, y)
            random_points.append(p)

    return random_points


def main():
    how_many = 20
    lower_bound = -10
    upper_bound = -lower_bound
    center = (1, 0)
    radius = 1
    a = (-1, 0)
    b = (1, 0.1)


if __name__ == "__main__":
    main()
