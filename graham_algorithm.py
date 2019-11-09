import generating_random_points as rand_p
import check_orientation as check_o
import time_functions as time_f
import qualify_by_angle as qualify_by_a


def graham(points, write_to_file=False, error=10 ** (-8)):
    copied_points = points.copy()

    o_point = min(copied_points, key=lambda tup: (tup[1], tup[0]))

    # I remove and append "o_point" after a sort to protect myself from adding "o_point" to stack in different
    # position than start and the end.
    copied_points.remove(o_point)
    qualify_by_a.sort_by_angle(copied_points, o_point, error)
    copied_points.append(o_point)

    stack = [o_point, copied_points.pop(0)]
    for point in copied_points:
        det_sign = check_o.calc_det_sign1(stack[-2], stack[-1], point, error)
        while det_sign == -1:
            stack.pop()
            det_sign = check_o.calc_det_sign1(stack[-2], stack[-1], point, error)
        if det_sign == 0:
            stack.pop()
        stack.append(point)

    if write_to_file:
        with open('result.txt', 'w') as f:
            for point in stack:
                f.write(str(point) + "\n")
    return stack


def main():
    random_points = rand_p.get_rand_points(10 ** 3, -100, 100)
    print(time_f.time_func(graham, random_points))


if __name__ == "__main__":
    main()
