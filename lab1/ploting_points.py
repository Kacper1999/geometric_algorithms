import matplotlib.pyplot as plt
from lab1 import generating_random_points as rand_points, my_types


def plot_points(points):
    data = my_types.Data(points)
    plt.scatter(data.x_cor, data.y_cor)
    plt.show()


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
    center = my_types.Point(0, 0)
    radius = 100
    random_points = rand_points.get_rand_points_circle(how_many, radius, center, )
    plot_points(random_points)

    a = my_types.Point(-1, 0)
    b = my_types.Point(1, 0.1)
    lower_bound = -1000
    upper_bound = -lower_bound
    random_points = rand_points.get_rand_points_line(how_many, a, b, lower_bound, upper_bound)
    plot_points(random_points)


if __name__ == "__main__":
    main()
