import random
import math
import ploting_points as plot_p


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


def get_rand_points_line(how_many=100, a=(0, 0), b=(1, 1), lower_bound=0, upper_bound=100):
    v = (b[0] - a[0], b[1] - a[1])

    random_points = []

    if v[0] == 0:
        x = a[0]
        for i in range(how_many):
            y = random.uniform(lower_bound, upper_bound)
            random_points.append((x, y))
    elif v[1] == 0:
        y = a[1]
        for i in range(how_many):
            x = random.uniform(lower_bound, upper_bound)
            random_points.append((x, y))
    elif abs(v[1]) > abs(v[0]):
        b = a[1] - v[1] / v[0] * a[0]

        for i in range(how_many):
            x = random.uniform(lower_bound, upper_bound)
            y = v[0] / v[1] * x + b
            p = (x, y)
            random_points.append(p)
    else:
        for i in range(how_many):
            b = a[1] - v[1] / v[0] * a[0]

            y = random.uniform(lower_bound, upper_bound)
            x = v[1] / v[0] * (y - b)
            p = (x, y)
            random_points.append(p)

    return random_points


def get_rand_points_rectangle(how_many=100, vertices=None):
    if vertices is None:
        vertices = [(-10, -10), (10, -10), (10, 10), (-10, 10)]
    random_points = []
    for i in range(how_many):
        which_line = random.randint(0, 3)
        a = vertices[which_line]
        b = vertices[(which_line + 1) % 4]
        random_points.append(get_point(a, b))
    return random_points


def get_rand_points_rectangle_axis_and_diagonal(p_on_axis=25, p_on_diagonal=20,
                                                vertices=None):
    if vertices is None:
        vertices = [(0, 0), (10, 0), (10, 10), (0, 10)]
    random_points = []

    for i in range(p_on_axis):
        a = vertices[0]
        b = vertices[3]
        random_points.append(get_point(a, b))

        a = vertices[0]
        b = vertices[1]
        random_points.append(get_point(a, b))
    for i in range(p_on_diagonal):
        a = vertices[0]
        b = vertices[2]
        random_points.append(get_point(a, b))

        a = vertices[1]
        b = vertices[3]
        random_points.append(get_point(a, b))

    return random_points


def get_point(a, b):
    lower_bound = min([a[0], a[1], b[0], b[1]])
    upper_bound = max([a[0], a[1], b[0], b[1]])
    temp = get_rand_points_line(1, a, b, lower_bound, upper_bound)
    return temp[0]


def main():
    plot_p.plot_points(get_rand_points_rectangle_axis_and_diagonal())


if __name__ == "__main__":
    main()
