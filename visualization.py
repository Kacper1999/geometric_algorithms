from check_orientation import calc_det_sign1
from qualify_by_angle import sort_by_angle, get_key, greater
from configuration_for_visualization import *

from generating_random_points import get_rand_points


def append_scene(scenes, points, marked=None, considered=None, wrong=None):
    copied_points = points.copy()
    copied_marked = []
    convex_hull = []
    copied_considered = []
    considered_lines = []
    copied_wrong = []
    wrong_lines = []

    if marked is not None:
        copied_marked = marked.copy()
        convex_hull = return_lines(marked)
        if considered is not None:
            copied_considered = considered.copy()
            considered_lines = return_lines(considered)
            if wrong is not None:
                copied_wrong = wrong.copy()
                wrong_lines = return_lines(copied_wrong)

    scenes.append(Scene([PointsCollection(copied_points),
                         PointsCollection(copied_marked, "lime"),
                         PointsCollection(copied_considered, "gold"),
                         PointsCollection(copied_wrong, "red")],
                        [LinesCollection(convex_hull, "lime"),
                         LinesCollection(considered_lines, "gold"),
                         LinesCollection(wrong_lines, "red")]))


def return_lines(points):
    lines = []
    for i in range(len(points) - 1):
        lines.append([points[i], points[i + 1]])
    return lines


def visualize_graham(points, error=10 ** (-8)):
    copied_points = points.copy()
    scenes = [Scene([PointsCollection(copied_points)])]

    p0 = min(copied_points, key=lambda tup: (tup[1], tup[0]))

    # I remove and append "p0" after a sort to protect myself from adding "p0" to stack in different
    # position than start and the end.
    copied_points.remove(p0)

    append_scene(scenes, copied_points, [], [p0])

    sort_by_angle(copied_points, p0, error)

    copied_points.append(p0)

    stack = [p0, copied_points.pop(0)]

    append_scene(scenes, copied_points, [], stack)

    for point in copied_points:
        append_scene(scenes, points, stack[:-1], stack[-2:] + [point])
        det_sign = calc_det_sign1(stack[-2], stack[-1], point, error)
        while det_sign == -1:
            append_scene(scenes, points, stack[:-1], [], stack[-2:] + [point])
            stack.pop()
            det_sign = calc_det_sign1(stack[-2], stack[-1], point, error)

            append_scene(scenes, points, stack[:-1], stack[-2:] + [point])

        if det_sign == 0:
            stack.pop()
            append_scene(scenes, points, stack[:-1], stack[-2:] + [point])

        stack.append(point)

    append_scene(scenes, points, stack)
    return scenes


def visualize_getting_min(scenes, points, marked_points, reference_point, min_point, error=10 ** (-8)):
    smallest = points[0]
    orientation = greater(reference_point, error)
    append_scene(scenes, points, marked_points, [reference_point, smallest])
    # we start from [1:] so that we won't compare the same point, that causes a weird visualization
    for point in points[1:]:
        if orientation(smallest, point) == 1:
            prev_smallest = smallest
            smallest = point
            append_scene(scenes, points, marked_points, [reference_point, smallest], [reference_point, prev_smallest])
        else:
            append_scene(scenes, points, marked_points, [reference_point, smallest], [reference_point, point])
    append_scene(scenes, points, marked_points + [smallest])


def visualize_jarvis(points, error=10 ** (-8)):
    copied_points = points.copy()
    scenes = [Scene([PointsCollection(copied_points)])]
    p0 = min(copied_points, key=lambda tup: (tup[1], tup[0]))

    # I first remove "p0" so it won't get in trouble while getting a point with smallest angle
    copied_points.remove(p0)
    stack = [p0]
    append_scene(scenes, copied_points, stack, stack)
    # I add append another point to stack so that I can append "p0" to "copied_points" and write a simple while loop,
    # if I were not to do that I wouldn't be able to write simple condition like "stack[0] != stack[-1].
    key = get_key(stack[-1], error)
    p = min(copied_points, key=key)
    visualize_getting_min(scenes, copied_points, [p0], p0, p)
    # I append p so that I will know when I have created a hull convex
    stack.append(p)
    copied_points.append(p0)

    copied_points.remove(p)
    while stack[0] != stack[-1]:
        key = get_key(stack[-1], error)
        p = min(copied_points, key=key)
        visualize_getting_min(scenes, copied_points, stack, stack[-1], p)
        copied_points.remove(p)
        stack.append(p)
    return scenes


def main():
    random_points = get_rand_points(20)
    scenes = visualize_jarvis(random_points)

    plot = Plot(scenes)
    plot.draw()


if __name__ == "__main__":
    main()
