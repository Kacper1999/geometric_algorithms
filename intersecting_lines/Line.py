class Line:
    def __init__(self, point_a, point_b):
        if point_a[0] < point_b[0]:  # this if statement ensures that self.a is "before" self.b that makes
            # later comparisons easier
            self.a = point_a
            self.b = point_b
        else:
            self.a = point_b
            self.b = point_a

        self.sort_by = (self.a[1], self.a[0])

        self.v = (self.b[0] - self.a[0], self.b[1] - self.a[1])  # simple geometry formulas
        self.slope = self.v[1] / self.v[0]
        self.intercept = self.a[1] - self.slope * self.a[0]

    def get_y_at(self, x):
        return self.slope * x + self.intercept

    def crosses(self, line2):  # this function assumes that self.a[1] < line2.a[1]
        if self.slope == line2.slope:
            return False
        cross_point = self.cross_point(line2)
        smallest_x = min(cross_point[0] - 10 ** (-8), self.a[0], line2.a[0])
        biggest_x = min(cross_point[0], self.b[0], line2.b[0])
        return smallest_x == cross_point[0] or biggest_x == cross_point[0]

    def cross_point(self, line2):  # simple geometry formulas
        x = (line2.intercept - self.intercept) / (self.slope - line2.slope)
        y = self.slope * x + self.intercept
        return x, y


def main():
    return 0


if __name__ == "__main__":
    main()
