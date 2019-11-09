import check_orientation as check_o
import functools


# This function returns a function that qualifies points "a" and "b" in respect to the angle that those points
# make with a "reference_point" - a > b if a lies on the left side of the line from reference_point to b
# (if collinear point closer to "reference_point" is bigger).
# Inner "orientation" function is designed to be changed to a key using cmp_to_key
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
