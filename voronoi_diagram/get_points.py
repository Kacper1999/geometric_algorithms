from configuration_for_visualization import *
from voronoi_diagram.Structures import Point


def get_points_collection():  # zwraca punkty w formacie PointsCollection
    return get_scene().points[0]


def get_points():  # zwraca liste punktów w formacie Point z pliku Structures
    points_collection = get_scene().points[0]
    points = []
    for point in points_collection.points:
        points.append(Point(point[0], point[1]))
    return points


def main():
    print(get_points()[0])


if __name__ == "__main__":
    main()
