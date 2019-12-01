from configuration_for_visualization import *
from voronoi_diagram.get_points import get_points_collection
from voronoi_diagram.Structures import LineType, Bisection, Point, TaxiCabParabola
from voronoi_diagram.bowyer_watson import get_outer_points


def visualize_bisections(display=True, lower_left=(0, 0), upper_right=(1, 1), points_collection=None):
    if points_collection is None:
        points_collection = get_points_collection()
    bisections = []
    for i, a in enumerate(points_collection.points):
        for b in points_collection.points[i + 1:]:
            bisections.append(Bisection(Point(a[0], a[1]), Point(b[0], b[1])))

    lines = []
    for bisection in bisections:
        for line in bisection.lines:
            a = (line.start.x, line.start.y)
            if line.lineType == LineType.POLPROSTA:
                if line.is_vertical:
                    orientation = line.v[1]  # orientation decides whether line goes up or down, left or right
                    if orientation == 1:
                        b = (line.start.x, upper_right[1])
                    else:
                        b = (line.start.x, lower_left[1])
                else:
                    orientation = line.v[0]
                    if orientation == 1:
                        b = (upper_right[0], line.start.y)
                    else:
                        b = (lower_left[0], line.start.y)
            else:
                b = (line.end.x, line.end.y)
            lines.append([a, b])
    scene = Scene([points_collection],
                  [LinesCollection(lines)])
    if display:
        plot = Plot([scene])
        plot.draw()
    return scene


def visualize_points_with_equal_dist(display=True, lower_left=(0, 0), upper_right=(1, 1), points_collection=None):
    points = []
    if points_collection is None:
        points_collection = get_points_collection()
    for i, a in enumerate(points_collection.points[:-2]):
        for j, b in enumerate(points_collection.points[i + 1:-1]):
            for c in points_collection.points[j + i + 2:]:
                a_ = Point(a[0], a[1])
                b_ = Point(b[0], b[1])
                c_ = Point(c[0], c[1])
                point = a_.findPointWithEqualDistance(b_, c_)
                if point:
                    points.append((point.x, point.y))
    bisections = visualize_bisections(False, lower_left, upper_right, points_collection).lines[0]
    scene = Scene([points_collection,
                   PointsCollection(points, color="red")],
                  [bisections])
    if display:
        plot = Plot([scene])
        plot.draw()
    return scene


def visualize_parabolas(sweep_line_position=0, display=True, upper_right=(1, 1), points_collection=None):
    if points_collection is None:
        points_collection = get_points_collection()
    parabolas = []
    for point in points_collection.points:
        parabolas.append(TaxiCabParabola(Point(point[0], point[1]), sweep_line_position))
    lines = []
    for parabola in parabolas:
        for line in parabola.lines:
            start_point = (line.start.x, line.start.y)
            if line.lineType == LineType.POLPROSTA:
                end_point = (line.start.x, upper_right[1])
            else:
                end_point = (line.end.x, line.end.y)
            lines.append([start_point, end_point])

    crossing_points = []
    for i, parabola1 in enumerate(parabolas[:-1]):
        for parabola2 in parabolas[i + 1:]:
            points = parabola1.crossing_points(parabola2)
            for cross_point in points:
                crossing_points.append((cross_point.x, cross_point.y))

    scene = Scene([points_collection,
                   PointsCollection(crossing_points, color="red")],
                  [LinesCollection(lines)])
    if display:
        plot = Plot([scene])
        plot.draw()
    return scene


def visualize_proper_crossing_points(sweep_line_position=0, display=True, upper_right=(1, 1), points_collection=None):
    if points_collection is None:
        points_collection = get_points_collection()
    parabolas = []
    for point in points_collection.points:
        parabolas.append(TaxiCabParabola(Point(point[0], point[1]), sweep_line_position))
    lines = []
    for parabola in parabolas:
        for line in parabola.lines:
            start_point = (line.start.x, line.start.y)
            if line.lineType == LineType.POLPROSTA:
                end_point = (line.start.x, upper_right[1])
            else:
                end_point = (line.end.x, line.end.y)
            lines.append([start_point, end_point])

    proper_crossing_points = []
    for i, parabola1 in enumerate(parabolas[:-1]):
        for parabola2 in parabolas[i + 1:]:
            cross_point = parabola1.proper_crossing_point(parabola2)
            if cross_point:
                proper_crossing_points.append(cross_point.to_tuple())

    scene = Scene([points_collection,
                   PointsCollection(proper_crossing_points, color="red")],
                  [LinesCollection(lines)])
    if display:
        plot = Plot([scene])
        plot.draw()
    return scene


def visualize_outer_points(display=True, points_collection=None):
    if points_collection is None:
        points_collection = get_points_collection()
    points = []
    for point in points_collection.points:
        points.append(Point(point[0], point[1]))
    p1, p2, p3 = get_outer_points(points)
    lines = [[p1.to_tuple(), p2.to_tuple()], [p1.to_tuple(), p3.to_tuple()], [p2.to_tuple(), p3.to_tuple()]]
    scene = Scene([points_collection,
                   PointsCollection([p1.to_tuple(), p2.to_tuple(), p3.to_tuple()], color="red")],
                  [LinesCollection(lines)])
    if display:
        plot = Plot([scene])
        plot.draw()
    return scene


def main():
    # visualize_bisections()
    # visualize_points_with_equal_dist()
    # visualize_proper_crossing_points()
    visualize_outer_points()


if __name__ == "__main__":
    main()
