import check_orientation as check_o
import functools


def greater(reference_point, error=10 ** (-8)):
    def orientation(a, b):
        det_sign = check_o.calc_det_sign1(reference_point, b, a, error)
        if det_sign == 0:
            if abs(a[0] - reference_point[0]) > abs(b[0] - reference_point[0]):
                return 1
            return -1
        return det_sign

    return orientation


def get_key(point, error):
    temp = greater(point, error)
    return functools.cmp_to_key(temp)


def sort_by_angle(points, point, error=10 ** (-8)):
    key = get_key(point, error)
    points.sort(key=key)
