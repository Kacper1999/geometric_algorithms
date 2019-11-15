from convex_hull import generating_random_points as rand_p
from convex_hull.check_orientation import calc_det_sign1
from convex_hull.qualify_by_angle import sort_by_angle, decide_collinear
from convex_hull.time_functions import time_func


def graham(points, write_to_file=False, error=10 ** (-8)):
    copied_points = points.copy()

    o_point = min(copied_points, key=lambda tup: (tup[1], tup[0]))

    # I remove and append "o_point" after a sort to protect myself from adding "o_point" to stack in
    # position other than the beginning and the end.
    copied_points.remove(o_point)
    sort_by_angle(copied_points, o_point, error)
    copied_points.append(o_point)

    stack = [o_point, copied_points.pop(0)]
    for point in copied_points:
        det_sign = calc_det_sign1(stack[-2], stack[-1], point, error)
        while det_sign == -1:
            stack.pop()
            det_sign = calc_det_sign1(stack[-2], stack[-1], point, error)
        if det_sign == 0:
            if decide_collinear(stack[-2], stack[-1], point, error) == -1:
                continue
            stack.pop()
        stack.append(point)

    if write_to_file:
        with open('result.txt', 'w') as f:
            for point in stack:
                f.write(str(point) + "\n")
    return stack


def main():
    random_points = rand_p.get_rand_points(10 ** 5, -500, 500)
    print(time_func(graham, random_points))


if __name__ == "__main__":
    main()
