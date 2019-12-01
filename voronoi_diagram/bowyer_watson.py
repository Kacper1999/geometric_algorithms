from sys import maxsize
from voronoi_diagram.Structures import Point


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
    pass


def add_edge(point, triangle_vertex):
    pass


def legalize_edge(point, triangle_vertex):
    pass


def remove_point_and_incident_lines(triangulation, point):
    pass


def bowyer_watson(points):
    outer_points = get_outer_points(points)
    triangulation = []  # nwm jeszcze jakiej struktury trzeba bedzie uzyc moze trzeba bedzie swoja stworzyc
    for point in outer_points:
        triangulation.append(point)
    for point in points:
        triangulation.append(point)
        triangle_vertices = get_triangle(point, triangulation)  # zakładam że punkty nie mogą wystąpić na krawędzi triangulacji
        for triangle_vertex in triangle_vertices:  # dlatego tutaj nie ma zadnego ifa
            add_edge(point, triangle_vertex)
        for triangle_vertex in triangle_vertices:
            legalize_edge(point, triangle_vertex)
    for point in outer_points:
        remove_point_and_incident_lines(triangulation, point)
    return triangulation


def main():
    points = [(1, 1), (0, 1), (0.5, 3), (0, 0), (4, 6), (-2, -3), (-3, 2)]
    my_points = []
    for point in points:
        my_points.append(Point(point[0], point[1]))
    tmp = (1, 2, 3, 4, 5)
    for t in tmp:
        print(t)

if __name__ == "__main__":
    main()
