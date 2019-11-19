class StateStructure:
    def __init__(self, points=None):
        if points is not None:
            self.points = sorted(points, key=lambda tup: (tup[1], tup[0]))
        else:
            self.points = []

    def add(self, point):
        for i, p in enumerate(self.points):
            if p[1] == point[1] and p[0] > point[0]:
                self.points.insert(i, point)
                return
            if p[1] > point[1]:
                self.points.insert(i, point)
                return
        self.points.append(point)

    def remove(self, point):
        self.points.remove(point)

    def get_index(self, point):
        def equals(p1, p2):
            epsilon = 10 ** (-8)
            return abs(p1[0] - p2[0]) < epsilon and abs(p1[1] - p2[1]) < epsilon
        for i, p in enumerate(self.points):
            if equals(p, point):
                return i


def main():
    pass


if __name__ == "__main__":
    main()
