import numpy as np


def below(a, b, error=10 ** (-8)):
    return a[1] - b[1] + error < 0


def above(a, b, error=10 ** (-8)):
    return b[1] - a[1] + error < 0


def get_sign(a, error=10 ** (-8)):
    if a > error:
        return 1
    elif a < -error:
        return -1
    else:
        return 0


# return -1 if point "c" is on the right of the line form "a" to "b"
# 1 if it's on the left side
# and 0 if its more or less on the line
def check_orientation(a, b, c, error=10 ** (-8)):
    temp = np.array([[a[0], a[1], 1],
                     [b[0], b[1], 1],
                     [c[0], c[1], 1]])

    result = np.linalg.det(temp)
    return get_sign(result, error)
