from configuration_for_visualization import *
from intersecting_lines.intersecting_lines_algorithm import *
from intersecting_lines.get_lines import get_lines, generate_lines


def add_scene(scenes, lines, prior_q, crossing_points, current_point):
    event_points = []
    for point in prior_q:
        event_points.append(point)
    converted_lines = []
    for line in lines:
        converted_lines.append([line.a, line.b])

    copied_crossing_points = crossing_points.copy()
    scene = Scene([PointsCollection(copied_crossing_points, color="red"),
                   PointsCollection(event_points, color="gold"),
                   PointsCollection([current_point], color="darkblue")],
                  [LinesCollection(converted_lines)])
    scenes.append(scene)


def visualize_lines_and_points(lines, points=None):
    if points is None:
        point = []
    converted_lines = []
    for line in lines:
        converted_lines.append([line.a, line.b])
    scenes = [Scene([PointsCollection(points, color="red")],
                    [LinesCollection(converted_lines)])]
    plot = Plot(scenes)
    plot.draw()


def visualize_intersecting_lines_algorithm(lines=None):
    if lines is None:
        lines = get_lines()
    state_structure = SortedDict()
    prior_q = initialize_event_points(lines)
    lines_and_points = associate_lines_and_points(lines)
    prev_point = (-maxsize, 0)
    crossing_points = []

    scenes = []

    while prior_q:
        current_point = prior_q.pop(0)
        rev_point = (current_point[1], current_point[0])  # we need to sort by y coordinate that's why we reverse it
        line = lines_and_points[current_point]
        event_type = determine_event_type(line, current_point)

        if prev_point[0] > current_point[0] or current_point == prev_point:
            continue

        add_scene(scenes, lines, prior_q, crossing_points, current_point)

        if event_type == "left endpoint":
            state_structure[rev_point] = line
        elif event_type == "right endpoint":
            del state_structure[line.sort_by]
        else:
            change_order(current_point, state_structure, lines_and_points)
            crossing_points.append(current_point)

        prev_point = current_point
        actualize_prior_q(current_point, prior_q, state_structure, lines_and_points)

    return scenes


def main():
    lines = generate_lines()
    scenes = visualize_intersecting_lines_algorithm()

    plot = Plot(scenes)
    plot.draw()


if __name__ == "__main__":
    main()
