from voronoi_diagram.Structures import Point, Line


class Node:
    def __init__(self, p1, p2, p3):
        self.vertices = [p1, p2, p3]
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.sons = None

    def is_point_inside(self, point):
        # https://stackoverflow.com/questions/2049582/how-to-determine-if-a-point-is-in-a-2d-triangle
        area = 0.5 * (-self.p2.y * self.p3.x + self.p1.y * (-self.p2.x + self.p3.x) +
                      self.p1.x * (self.p2.y - self.p3.y) + self.p2.x * self.p3.y)
        s = 1 / (2 * area) * (self.p1.y * self.p3.x - self.p1.x * self.p3.y + (self.p3.y - self.p1.y)
                              * point.x + (self.p1.x - self.p3.x) * point.y)
        t = 1 / (2 * area) * (self.p1.x * self.p2.y - self.p1.y * self.p2.x + (self.p1.y - self.p2.y)
                              * point.x + (self.p2.x - self.p1.x) * point.y)
        return s > 0 and t > 0 and 1 - s - t > 0

    def is_leaf(self):
        return self.sons is None

    def in_which_triangle(self, point):
        while not self.is_leaf():
            for son in self.sons:
                if son.is_point_inside(point):
                    return son.in_which_triangle(point)
            return self  # jezeli punkt jest na boku jakiegos trojkata
        return self

    def add_point(self, point):
        if not self.is_leaf():
            print("trying to sons to with sons")
            return None
        self.sons = [Node(point, self.p1, self.p2), Node(point, self.p1, self.p3), Node(point, self.p2, self.p3)]

    def __str__(self):
        default = f"Triangle vertices: {self.p1}, {self.p2}, {self.p3}"
        if self.sons is not None:
            sons = " with sons"
            return default + sons
        return default


class PointLocator:
    def __init__(self, root):  # root w naszym przypadku 3 punkty zwnetrznego trojkata
        self.root = Node(root[0], root[1], root[2])

    def in_which_triangle(self, point):
        node = self.root
        return node.in_which_triangle(point)

    def add_point(self, point):
        triangle = self.in_which_triangle(point)
        triangle.add_point(point)

    def flip(self, line):
        start = line.start
        end = line.end

        delta_x = 10 ** (-5)
        if line.is_vertical:
            tmp1 = Point(start.x + delta_x, (start.y + end.y) / 2)
            tmp2 = Point(start.x - delta_x, (start.y + end.y) / 2)
        else:
            delta_y = -1 / line.slope * delta_x
            tmp1 = Point((start.x + end.x) / 2 + delta_x, (start.y + end.y) / 2 + delta_y)
            tmp2 = Point((start.x + end.x) / 2 - delta_x, (start.y + end.y) / 2 - delta_y)
        triangle1 = self.in_which_triangle(tmp1)
        triangle2 = self.in_which_triangle(tmp2)

        for point in triangle1.vertices:
            if point != start and point != end:
                p1 = point
        for point in triangle2.vertices:
            if point != start and point != end:
                p2 = point

        new_triangle1 = Node(p1, p2, end)
        new_triangle2 = Node(p1, p2, start)
        triangle1.sons = [new_triangle1, new_triangle2]
        triangle2.sons = [new_triangle1, new_triangle2]

    def __str__(self):
        return str(self.root)


def main():
    points = [(1, 1), (0, 1), (0.5, 3), (0, 0), (4, 6), (-2, -3), (-3, 2), (0.25, 0.75)]
    my_points = []
    for point in points:
        my_points.append(Point(point[0], point[1]))

    root = my_points[0], my_points[1], my_points[3]

    tmp_node = PointLocator(root)
    tmp_node.add_point(my_points[-1])
    point = Point(0.5, 0.9)
    tmp_node.add_point(point)

    line = Line(my_points[-1], my_points[0])

    tmp_node.flip(line)
    point = Point(0.28, 0.76)  # ten punkt  nie dzial i chyba dlatego ze nie ma precyzji 
    print(tmp_node.in_which_triangle(point))

    # for point in my_points:
    #     print(tmp_node.in_which_triangle(point))


if __name__ == '__main__':
    main()
