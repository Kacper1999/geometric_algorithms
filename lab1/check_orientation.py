import numpy as np
from lab1 import ploting_points as plot_p, generating_random_points as rand_points, my_types


def get_sign(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0


def calc_det_sign1(a, b, c, precision=np.float_):
    temp = np.array([[a.x, a.y, 1],
                     [b.x, b.y, 1],
                     [c.x, c.y, 1]])
    result = np.linalg.det(temp)
    result = precision(result)
    return get_sign(result)


def calc_det_sign2(a, b, c, precision=np.float_):
    temp = np.array([[(a.x - c.x), (a.y - c.y)],
                     [(b.x - c.x), (b.y - c.y)]])
    result = np.linalg.det(temp)
    result = precision(result)
    return get_sign(result)


def how_many_different_result(c_points, a=my_types.Point(0, 0), b=my_types.Point(1, 1), precision=np.float_):
    result = []
    for c in c_points:
        sign1 = calc_det_sign1(a, b, c, precision)
        sign2 = calc_det_sign2(a, b, c, precision)
        if sign1 != sign2:
            result.append(c)
    return result


def check_diff_in_sign_calc(tries, a=my_types.Point(0, 0), b=my_types.Point(1, 1), precision=np.float_):
    average = 0
    for i in range(tries):
        how_many = 10 ** 5
        lower_bound = -1000
        upper_bound = -lower_bound
        random_points = rand_points.get_rand_points(how_many, lower_bound, upper_bound)
        different_calc = how_many_different_result(random_points, a, b, precision)
        average += len(different_calc)
        # plot_p.plot_points(different_calc)
    print(average / tries)

    average = 0
    for i in range(tries):
        how_many = 10 ** 5
        lower_bound = -10 ** 14
        upper_bound = -lower_bound
        random_points = rand_points.get_rand_points(how_many, lower_bound, upper_bound)
        different_calc = how_many_different_result(random_points, a, b, precision)
        average += len(different_calc)
        plot_p.plot_points(different_calc)
    print(average / tries)

    average = 0
    for i in range(tries):
        how_many = 1000
        center = my_types.Point(0, 0)
        radius = 100
        random_points = rand_points.get_rand_points_circle(how_many, radius, center, )
        different_calc = how_many_different_result(random_points, a, b, precision)
        average += len(different_calc)
        # plot_p.plot_points(different_calc)
    print(average / tries)

    average = 0
    for i in range(tries):
        how_many = 1000
        lower_bound = -1000
        upper_bound = -lower_bound
        random_points = rand_points.get_rand_points_line(how_many, a, b, lower_bound, upper_bound)
        different_calc = how_many_different_result(random_points, a, b, precision)
        average += len(different_calc)
        # plot_p.plot_points(different_calc)
    print(average / tries)


def main():
    precision = np.float32
    a = my_types.Point(-1, 0)
    b = my_types.Point(1, 0.1)
    tries = 15

    check_diff_in_sign_calc(tries, a, b, precision)


if __name__ == "__main__":
    main()
