from sys import maxsize
from voronoi_diagram.Structures import Point


def get_outer_points(points):
    lower_left = (maxsize, maxsize)
    upper_right = (-maxsize, -maxsize)
    for point in points:
        lower_left = min(lower_left, point.to_tuple())
        upper_right = max(upper_right, point.to_tuple())
    square_side_len = upper_right[0] - lower_left[0]
    tg60 = 1.8
    eps = 0.1
    delta_x = square_side_len / tg60
    p1 = (lower_left[0] - delta_x - eps, lower_left[1] - eps)
    p3 = (upper_right[0] + delta_x + eps, lower_left[1] - eps)
    delta_y = square_side_len / 2 * tg60
    p2 = (p3[0] - p1[0], upper_right[1] + delta_y + eps)
    return p1, p2, p3


def bowyer_watson(points):
    p1, p2, p3 = get_outer_points(points)


def main():
    points = [(1, 1), (0, 1), (0.5, 3), (0, 0), (4, 6), (-2, -3), (-3, 2)]
    my_points = []
    for point in points:
        my_points.append(Point(point[0], point[1]))
    print(get_outer_points(my_points))


if __name__ == "__main__":
    main()
