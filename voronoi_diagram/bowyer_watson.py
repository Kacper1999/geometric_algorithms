from sys import maxsize
from voronoi_diagram.Structures import Point, Line
from voronoi_diagram.PointLocator import PointLocator


def get_outer_points(points):
    lowest_x = lowest_y = maxsize
    highest_x = highest_y = -maxsize
    for point in points:
        lowest_x = min(lowest_x, point.x)
        highest_x = max(highest_x, point.x)
        lowest_y = min(lowest_y, point.y)
        highest_y = max(highest_y, point.y)

    lower_left = (lowest_x, lowest_y)
    upper_right = (highest_x, highest_y)
    square_side_len = upper_right[0] - lower_left[0]
    tg60 = 1.8
    eps = 0.1
    delta_x = square_side_len / tg60
    p1 = Point(lower_left[0] - delta_x - eps, lower_left[1] - eps)
    p3 = Point(upper_right[0] + delta_x + eps, lower_left[1] - eps)
    delta_y = square_side_len / 2 * tg60
    p2 = Point((p3.x + p1.x) / 2, upper_right[1] + delta_y + eps)
    return p1, p2, p3


def get_triangle(point, triangulation):
    node = triangulation.in_which_triangle(point)
    return node.p1, node.p2, node.p3


def is_legal_edge(point, triangle):
    circle_centre = triangle.p1.findPointWithEqualDistance(triangle.p2, triangle.p3)
    r = circle_centre.distance(triangle.p1)
    d = circle_centre.distance(point)
    return r > d


def legalize_edge(point, start, end, triangulation):
    triangle = triangulation.get_adjacent_triangle_away_form(start, end, point)
    for vertex in triangle.vertices:
        if vertex != start and vertex != end:
            free_vertex = vertex

    if not is_legal_edge(point, triangle):
        triangulation.flip(start, end)
        legalize_edge(point, start, free_vertex, triangulation)
        legalize_edge(point, end, free_vertex, triangulation)


def remove_point_and_incident_lines(triangulation, point):
    pass


def bowyer_watson(points):
    outer_points = get_outer_points(points)
    triangulation = PointLocator(outer_points)
    for point in points:
        # zakładam że punkty nie mogą wystąpić na krawędzi triangulacji
        triangulation.add_point(point)
        triangle_vertices = get_triangle(point, triangulation)

        legalize_edge(point, triangle_vertices[0], triangle_vertices[1], triangulation)
        legalize_edge(point, triangle_vertices[0], triangle_vertices[2], triangulation)
        legalize_edge(point, triangle_vertices[1], triangle_vertices[2], triangulation)

    for point in outer_points:
        remove_point_and_incident_lines(triangulation, point)
    return triangulation


def main():
    points = [(0, 1), (0.5, 3), (0, 0), (4, 6), (-2, -3), (-3, 2)]
    my_points = []
    for point in points:
        my_points.append(Point(point[0], point[1]))
    triangulation = bowyer_watson(my_points)
    print(triangulation.get_triangles())


if __name__ == "__main__":
    main()
