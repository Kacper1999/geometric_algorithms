import numpy as np
import generating_random_points as rand_points


def get_sign(a, error=10 ** (-8)):
    if a > error:
        return 1
    elif a < -error:
        return -1
    else:
        return 0


def calc_det_sign1(a, b, c, error=10 ** (-8)):
    temp = np.array([[a[0], a[1], 1],
                     [b[0], b[1], 1],
                     [c[0], c[1], 1]])

    result = np.linalg.det(temp)
    return get_sign(result, error)


def calc_det_sign2(a, b, c, error=10 ** (-8)):
    temp = np.array([[(a[0] - c[0]), (a[1] - c[1])],
                     [(b[0] - c[0]), (b[1] - c[1])]])

    result = np.linalg.det(temp)
    return get_sign(result, error)


def how_many_different_result(c_points, a=(0, 0), b=(1, 1), error=10 ** (-8)):
    result = []
    for c in c_points:
        sign1 = calc_det_sign1(a, b, c, error)
        sign2 = calc_det_sign2(a, b, c, error)
        if sign1 != sign2:
            result.append(c)
    return result


def change_precision(a, precision):
    result = (precision(a[0]), precision(a[1]))
    return result


def check_diff_in_sign_calc(tries, a=(0, 0), b=(1, 1), error=10 ** (-8)):
    average = 0
    for i in range(tries):
        how_many = 10 ** 5
        lower_bound = -1000
        upper_bound = -lower_bound
        random_points = rand_points.get_rand_points(how_many, lower_bound, upper_bound)
        different_calc = how_many_different_result(random_points, a, b, error)
        average += len(different_calc)
        # plot_p.plot_points(different_calc)
    print(average / tries)

    average = 0
    for i in range(tries):
        how_many = 10 ** 5
        lower_bound = -10 ** 14
        upper_bound = -lower_bound
        random_points = rand_points.get_rand_points(how_many, lower_bound, upper_bound)
        different_calc = how_many_different_result(random_points, a, b, error)
        average += len(different_calc)
        # plot_p.plot_points(different_calc)
    print(average / tries)

    average = 0
    for i in range(tries):
        how_many = 1000
        center = (0, 0)
        radius = 100
        random_points = rand_points.get_rand_points_circle(how_many, radius, center, )
        different_calc = how_many_different_result(random_points, a, b, error)
        average += len(different_calc)
        # plot_p.plot_points(different_calc)
    print(average / tries)

    average = 0
    for i in range(tries):
        how_many = 1000
        lower_bound = -1000
        upper_bound = -lower_bound
        random_points = rand_points.get_rand_points_line(how_many, a, b, lower_bound, upper_bound)
        different_calc = how_many_different_result(random_points, a, b, error)
        average += len(different_calc)
        # plot_p.plot_points(different_calc)
    print(average / tries)


def main():
    tries = 10
    check_diff_in_sign_calc(tries)

    a = (-1, 0)
    b = (1, 0.1)
    check_diff_in_sign_calc(tries, a, b, 0)


if __name__ == "__main__":
    main()
