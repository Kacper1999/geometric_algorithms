import numpy as np


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


# How many points were differently qualified by two ways of calculating determinant.
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


def main():
    print("Hello World!")


if __name__ == "__main__":
    main()
