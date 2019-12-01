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
        def sign(a, b, c):
            return (a.x - c.x) * (b.y - c.y) - (b.x - c.x) * (a.y - c.y)

        d1 = sign(point, self.p1, self.p2)
        d2 = sign(point, self.p2, self.p3)
        d3 = sign(point, self.p3, self.p1)
        has_neg = d1 < 0 or d2 < 0 or d3 < 0
        has_pos = d1 > 0 or d2 > 0 or d3 > 0

        return not (has_neg and has_pos)

    def is_leaf(self):
        return self.sons is None

    def in_which_triangle(self, point):
        while not self.is_leaf():
            for son in self.sons:
                if son.is_point_inside(point):
                    return son.in_which_triangle(point)
            # return self  # nieskonczona petla jezeli jest zakomentowane ale wiadomo ze algorytm nie zadzialal
        return self

    def add_point(self, point):
        if not self.is_leaf():
            print("trying to sons to with sons")
            return None
        self.sons = [Node(point, self.p1, self.p2), Node(point, self.p1, self.p3), Node(point, self.p2, self.p3)]

    def get_leafs(self, result):
        if self.is_leaf():
            result.add([self.p1, self.p2, self.p3])
        for son in self.sons:
            son.get_leafs(result)

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

    def get_adjacent_triangles(self, start, end):
        line = Line(start, end)
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
        return triangle1, triangle2

    def get_adjacent_triangle_away_form(self, start, end, away_from):
        tmp_line = Line(away_from, Point((start.x + end.x) / 2, (start.y + end.y) / 2))
        delta_x = tmp_line.v[0] / 1000
        delta_y = tmp_line.v[1] / 1000
        tmp_point = Point((start.x + end.x) / 2 + delta_x, (start.y + end.y) / 2 + delta_y)

        return self.in_which_triangle(tmp_point)

    def flip(self, start, end):
        triangle1, triangle2 = self.get_adjacent_triangles(start, end)

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

    def get_triangles(self):
        result = {[self.root.p1, self.root.p2, self.root.p3]}
        node = self.root
        node.get_leafs(result)
        return result


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

    tmp_node.flip(my_points[-1], my_points[0])
    point = Point(0.28, 0.76)  # ten punkt  nie dzial i chyba dlatego ze nie ma precyzji 
    print(tmp_node.in_which_triangle(point))

    # for point in my_points:
    #     print(tmp_node.in_which_triangle(point))


if __name__ == '__main__':
    main()
