import matplotlib.pyplot as plt
import generating_random_points as rand_points


def plot_points(points):
    x_cor = []
    y_cor = []
    for point in points:
        x_cor.append(point[0])
        y_cor.append(point[1])

    plt.scatter(x_cor, y_cor)
    plt.show()


def print_points(points):
    for point in points:
        print(point)


def main():
    how_many = 10 ** 5
    lower_bound = -1000
    upper_bound = -lower_bound
    random_points = rand_points.get_rand_points(how_many, lower_bound, upper_bound)
    plot_points(random_points)

    lower_bound = -10 ** 14
    upper_bound = -lower_bound
    random_points = rand_points.get_rand_points(how_many, lower_bound, upper_bound)
    plot_points(random_points)

    how_many = 1000
    center = (0, 0)
    radius = 100
    random_points = rand_points.get_rand_points_circle(how_many, radius, center, )
    plot_points(random_points)

    a = (-1, 0)
    b = (1, 0.1)
    lower_bound = -1000
    upper_bound = -lower_bound
    random_points = rand_points.get_rand_points_line(how_many, a, b, lower_bound, upper_bound)
    plot_points(random_points)


if __name__ == "__main__":
    main()
