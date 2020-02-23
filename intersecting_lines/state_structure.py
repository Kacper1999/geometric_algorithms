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
        for i, p in enumerate(self.points):
            if p == point:
                return i


def main():
    pass


if __name__ == "__main__":
    main()
