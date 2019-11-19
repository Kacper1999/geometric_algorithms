class Line:
    def __init__(self, point_a, point_b):
        if point_a[0] < point_b[0]:  # this if statement ensures that self.a is "before" self.b that makes
            # later comparisons easier
            self.a = point_a
            self.b = point_b
        else:
            self.a = point_b
            self.b = point_a

        self.sort_by = self.a

        self.v = (point_b[0] - point_a[0], point_b[1] - point_a[1])  # simple geometry formulas
        self.slope = self.v[1] / self.v[0]
        self.intercept = (point_a[1] + point_b[1] - self.slope * (point_a[0] + point_b[0])) / 2

    def get_y_at(self, x):
        return self.slope * x + self.intercept

    def are_crossing(self, line2):  # this function assumes that line1.a[1] < line2.a[1]
        x = line2.b[0]
        y = self.get_y_at(x)
        return y > line2.b[1]

    def cross_point(self, line2):  # simple geometry formulas
        x = (line2.intercept - self.intercept) / (self.slope - line2.slope)
        y = self.slope * x + self.intercept
        return x, y


def main():
    return 0


if __name__ == "__main__":
    main()
