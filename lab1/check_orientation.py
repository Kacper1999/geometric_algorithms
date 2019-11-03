import numpy as np
import generating_random_points as rand_points


def get_sign(a, error=10 ** (-5)):
    if a > error:
        return 1
    elif a < -error:
        return -1
    else:
        return 0


def calc_det_sign1(a, b, c, error=10 ** (-5)):
    temp = np.array([[a[0], a[1], 1],
                     [b[0], b[1], 1],
                     [c[0], c[1], 1]])

    result = np.linalg.det(temp)
    return get_sign(result, error)


def calc_det_sign2(a, b, c, error=10 ** (-5)):
    temp = np.array([[(a[0] - c[0]), (a[1] - c[1])],
                     [(b[0] - c[0]), (b[1] - c[1])]])

    result = np.linalg.det(temp)
    return get_sign(result, error)


def how_many_different_result(c_points, a=(0, 0), b=(1, 1), error=10 ** (-5)):
    result = []
    for c in c_points:
        sign1 = calc_det_sign1(a, b, c)
        sign2 = calc_det_sign2(a, b, c)
        if sign1 != sign2:
            result.append(c)
    return result


def change_precision(a, precision):
    result = (precision(a[0]), precision(a[1]))
    return result


def main():
    how_many = 10 ** 5
    lower_bound = -1000
    upper_bound = -lower_bound
    a = (-1, 0)
    b = (1, 0.1)

    precision = np.float16

    a = change_precision(a, precision)
    b = change_precision(b, precision)
    random_points = rand_points.get_rand_points_line(how_many, a, b, lower_bound, upper_bound)

    print(format(random_points[0][0], ".34g"))

    print(how_many_different_result(random_points, a, b))

















    # how_many = 10 ** 5
    # lower_bound = -10 ** 14
    # upper_bound = -lower_bound
    #
    # random_points = rand_points.get_rand_points(how_many, lower_bound, upper_bound)
    #
    # for point in random_points:
    #     point = change_precision(point, precision)
    #
    # print(how_many_different_result(random_points, a, b))


if __name__ == "__main__":
    main()
