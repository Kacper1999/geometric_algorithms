from configuration_for_visualization import *
from voronoi_diagram.get_points import get_points_collection
from voronoi_diagram.Structures import LineType, Bisection, Point


def visualize_bisections():
    points_collection = get_points_collection()
    bisections = []
    for i, a in enumerate(points_collection.points):
        for b in points_collection.points[i + 1:]:
            bisections.append(Bisection(Point(a[0], a[1]), Point(b[0], b[1])))

    lines = []
    jump = 1
    for bisection in bisections:
        for line in bisection.lines:
            is_vertical = line.v[0] == 0
            a = (line.start.x, line.start.y)
            if line.lineType == LineType.POLPROSTA:
                if is_vertical:
                    orientation = line.v[1]  # orientation decides whether line goes up or down, left or right
                    b = (line.start.x, line.start.y + jump * orientation)
                else:
                    orientation = line.v[0]
                    b = (line.start.x + jump * orientation, line.get_y_at(line.start.x + jump * orientation))
            else:
                b = (line.end.x, line.end.y)
            lines.append([a, b])
    scenes = [Scene([points_collection],
                    [LinesCollection(lines)])]
    plot = Plot(scenes)
    plot.draw()


def main():
    visualize_bisections()


if __name__ == "__main__":
    main()
