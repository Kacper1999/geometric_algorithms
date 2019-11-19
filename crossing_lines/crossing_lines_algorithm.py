from crossing_lines.state_structure import StateStructure
from crossing_lines.Line import Line
from crossing_lines.get_lines import generate_lines
from sys import maxsize
import heapq


def initialize_event_points(lines):
    prior_q = []
    for line in lines:
        heapq.heappush(prior_q, line.sort_by)
        heapq.heappush(prior_q, line.b)
    return prior_q


def associate_lines_and_points(lines):
    lines_and_points = dict()
    for line in lines:
        lines_and_points[line.sort_by] = line
        lines_and_points[line.b] = line
    return lines_and_points


# returns "left.." if "broom_position" is the left endpoint of a line "right..." if right and "cross..." if its a
# crossing point
def determine_event_type(line, broom_position):
    if broom_position == line.a:
        return "left endpoint"
    elif broom_position == line.b:
        return "right endpoint"
    return "crossing"


def remove_duplicates(prior_q):
    to_pop = []
    for i in range(len(prior_q) - 1):
        for j in range(i, len(prior_q)):
            if prior_q[i] == prior_q[j]:
                to_pop.append(j)
    for i in to_pop:
        prior_q


def actualize_prior_q(prior_q, state_structure, lines_and_points):
    for i in range(len(state_structure.points) - 1):
        line1 = lines_and_points[state_structure.points[i]]  # we know that line1.a[1] < line2.a[1]
        line2 = lines_and_points[state_structure.points[i + 1]]
        if line1.are_crossing(line2):  # and we use that fact in "are_crossing"
            cross_p = line1.cross_point(line2)
            heapq.heappush(prior_q, cross_p)
            lines_and_points[cross_p] = line1
    remove_duplicates(prior_q)


def change_position(broom_position, prior_q, lines_and_points, state_structure):
    next_event_x = prior_q[0][0]
    line1 = lines_and_points[broom_position]
    i = state_structure.get_index(line1.sort_by)

    line2 = lines_and_points[state_structure.points[i + 1]]

    state_structure.remove(line1.sort_by)
    state_structure.remove(line2.sort_by)

    line1.sort_by = (line1.get_y_at(next_event_x), next_event_x)
    line2.sort_by = (line2.get_y_at(next_event_x), next_event_x)

    lines_and_points[line1.sort_by] = line1
    lines_and_points[line2.sort_by] = line2
    state_structure.add(line1.sort_by)
    state_structure.add(line2.sort_by)


def crossing_lines_algorithm(lines):
    state_structure = StateStructure()

    prior_q = initialize_event_points(lines)

    lines_and_points = associate_lines_and_points(lines)

    prev_position = (-maxsize, 0)
    crossing_points = []

    while prior_q:
        broom_position = heapq.heappop(prior_q)
        line = lines_and_points[broom_position]

        event_type = determine_event_type(line, broom_position)

        if prev_position[0] > broom_position[0] or broom_position == prev_position:
            continue

        # the state_structure needs to be sorted first by the y coordinate and then the x coordinate that's why
        # sorted dict keys are "reversed" points (y, x) of a left endpoints or right depending the case
        line = lines_and_points[broom_position]
        if event_type == "left endpoint":
            state_structure.add(broom_position)
        elif event_type == "right endpoint":
            state_structure.remove(line.sort_by)
        else:
            change_position(broom_position, prior_q, lines_and_points, state_structure)
            if broom_position not in crossing_points:
                crossing_points.append(broom_position)

        actualize_prior_q(prior_q, state_structure, lines_and_points)

    return crossing_points


def print_state_structure(ss, lines_and_points):
    for i in range(len(ss.points)):
        point = ss.points[i]
        line = lines_and_points[point]
        print(f"key: {point} line from {line.a} to {line.b}")
    print()


def main():
    points = [(0, 0), (2, 2), (0, 3), (1, -2), (0, 2), (2, 0), (1, 1.5), (1.5, 2.5), (-1, 1), (-2, 3)]
    lines = []
    i = 0
    while i < len(points):
        lines.append(Line(points[i], points[i + 1]))
        i += 2
    lines += generate_lines()



    print(crossing_lines_algorithm(lines))


if __name__ == "__main__":
    main()
