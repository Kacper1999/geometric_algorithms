import generating_random_points as rand_points
import math_types


def calc_det_sign1(a, b, c):
    result = a.x * b.y + b.x * c.y + c.x * a.y - b.y * c.x - a.y * b.x - a.x * c.y
    if result == 0:
        return 0
    return result
    # return round(result / abs(result))


def calc_det_sign2(a, b, c):
    result = ((a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x))
    if result == 0:
        return 0
    return result
    # return round(result / abs(result))


def main():
    how_many = 10 ** 5
    lower_bound = -10
    upper_bound = -lower_bound

    origin = math_types.Point(0, 0)

    a = math_types.Point(-1, 0)
    b = math_types.Point(1, 0.1)

    c_points = rand_points.get_rand_points(how_many, lower_bound, upper_bound)

    j = 0
    for i in range(how_many):
        det1 = calc_det_sign1(a, b, c_points[i])
        det2 = calc_det_sign2(a, b, c_points[i])
        if det1 != det2:
            j += 1
    print(j)


if __name__ == "__main__":
    main()
