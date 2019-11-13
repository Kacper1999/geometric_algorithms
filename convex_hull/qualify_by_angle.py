from convex_hull import check_orientation as check_o
import functools


# This function returns a function that qualifies points "a" and "b" in respect to the angle that those points
# make with a "reference_point" - a > b if "a" lies on the left side of the line from "reference_point" to "b"
# (if collinear point closer to "reference_point" is bigger).
# Inner "orientation" function is designed to be changed to a key using cmp_to_key
def greater(reference_point, error=10 ** (-8)):
    def orientation(a, b):
        det_sign = check_o.calc_det_sign1(reference_point, a, b, error)
        if det_sign == 0:
            return decide_collinear(reference_point, a, b, error)
        return -det_sign

    return orientation


def decide_collinear(reference_point, a, b, error=10 ** (-8)):
    v1 = (a[0] - reference_point[0], a[1] - reference_point[1])
    v2 = (b[0] - reference_point[0], b[1] - reference_point[1])
    if v1[0] * v2[0] < 0 or v1[1] * v2[1] < 0:
        return -1
    if abs(v1[0]) < abs(v2[0]) or abs(v1[1]) < abs(v2[1]):
        return 1
    return -1


def get_key(point, error):
    temp = greater(point, error)
    return functools.cmp_to_key(temp)


def sort_by_angle(points, point, error=10 ** (-8)):
    key = get_key(point, error)
    points.sort(key=key)
