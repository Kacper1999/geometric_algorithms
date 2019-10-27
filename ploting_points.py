import matplotlib.pyplot as plt
import generating_random_points as rand_points
import my_types


def main():
    how_many = 10000
    lower_bound = -10
    upper_bound = -lower_bound
    center = my_types.Point(1, 0)
    radius = 1
    a = my_types.Vector(-1, 0)
    b = my_types.Vector(1, 0.1)

    random_points = rand_points.get_rand_points_circle(how_many)

    data = my_types.Data(random_points)

    plt.scatter(data.x_cor, data.y_cor)
    plt.show()


if __name__ == "__main__":
    main()
