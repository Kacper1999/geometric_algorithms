from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from sys import maxsize
from intersecting_lines.get_lines import get_lines


# I know this code ain't pretty but I've lost sanity while writing so I will just leave it while it works

def reverse_point(point):
    return point[1], point[0]


def initialize_event_points(lines):
    prior_q = SortedSet()
    for line in lines:
        prior_q.add(line.a)
        prior_q.add(line.b)
    return prior_q


def associate_lines_and_points(lines):
    lines_and_points = dict()
    for line in lines:
        lines_and_points[line.a] = line
        lines_and_points[line.b] = line
    return lines_and_points


# returns "left.." if "broom_position" is the left endpoint of a line "right..." if right and "cross..." if its a
# crossing point
def determine_event_type(line, current_point):
    if current_point == line.a:
        return "left endpoint"
    elif current_point == line.b:
        return "right endpoint"
    return "crossing"


def change_order(point, state_structure, lines_and_points):
    line1 = lines_and_points[point]
    i = state_structure.index(line1.sort_by)
    _, line2 = state_structure.peekitem(i + 1)

    # line.sort_by is reversed so we need to reversed it back :) SortedDict maybe wasn't the best idea
    del lines_and_points[reverse_point(line1.sort_by)]
    del lines_and_points[reverse_point(line2.sort_by)]
    del state_structure[line1.sort_by]
    del state_structure[line2.sort_by]

    eps = 10 ** (-8)
    x = point[0]
    line1.sort_by = (line1.get_y_at(x + eps), x + eps)
    line2.sort_by = (line2.get_y_at(x + eps), x + eps)

    lines_and_points[reverse_point(line1.sort_by)] = line1
    lines_and_points[reverse_point(line2.sort_by)] = line2
    state_structure[line1.sort_by] = line1
    state_structure[line2.sort_by] = line2


def actualize_prior_q(current_point, prior_q, state_structure, lines_and_points):
    for i, key1 in enumerate(state_structure):
        for j, key2 in enumerate(state_structure):
            if i >= j:
                continue
            line1 = state_structure[key1]
            line2 = state_structure[key2]
            if line1.crosses(line2):
                cross_point = line1.cross_point(line2)
                lines_and_points[cross_point] = line1
                prior_q.add(cross_point)


def intersecting_lines_algorithm(lines=None):
    if lines is None:
        lines = get_lines()
    state_structure = SortedDict()
    prior_q = initialize_event_points(lines)
    lines_and_points = associate_lines_and_points(lines)
    prev_point = (-maxsize, 0)
    crossing_points = []

    while prior_q:
        current_point = prior_q.pop(0)
        rev_point = (current_point[1], current_point[0])  # we need to sort by y coordinate that's why we reverse it
        line = lines_and_points[current_point]
        event_type = determine_event_type(line, current_point)

        if prev_point[0] > current_point[0] or current_point == prev_point:
            continue

        if event_type == "left endpoint":
            state_structure[rev_point] = line
        elif event_type == "right endpoint":
            del state_structure[line.sort_by]
        else:
            change_order(current_point, state_structure, lines_and_points)
            crossing_points.append(current_point)

        prev_point = current_point
        actualize_prior_q(current_point, prior_q, state_structure, lines_and_points)
    return crossing_points


def main():
    pass


if __name__ == "__main__":
    main()
