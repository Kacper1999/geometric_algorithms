import generating_random_points as rand_p
import time_functions as time_f
import qualify_by_angle as qualify_by_a
import ploting_points as plot_p


def jarvis(points, error=10 ** (-8)):
    copied_points = points.copy()
    p0 = min(copied_points, key=lambda tup: (tup[1], tup[0]))

    # I first remove "p0" so it won't get in trouble while getting a point with smallest angle
    copied_points.remove(p0)
    stack = [p0]
    # I add append another point to stack so that I can append "p0" to "copied_points" and write a simple while loop,
    # if I were not to do that I wouldn't be able to write simple condition like "stack[0] != stack[-1].
    key = qualify_by_a.get_key(stack[-1], error)
    p = min(copied_points, key=key)
    # I append p so that I will know when I created a convex hull
    stack.append(p)

    copied_points.append(p0)

    while stack[0] != stack[-1]:
        key = qualify_by_a.get_key(stack[-1], error)
        p = min(copied_points, key=key)
        copied_points.remove(p)
        stack.append(p)
    return stack


def main():
    random_points = rand_p.get_rand_points_rectangle(10 ** 3)
    plot_p.plot_points(random_points)
    result = jarvis(random_points)
    plot_p.plot_points(result)
    time_f.time_func(jarvis, random_points)


if __name__ == "__main__":
    main()
