import random
from crossing_lines.Line import Line


def is_vertical(line, error=10 ** (-8)):
    return abs(line.a[0] - line.b[0]) < error


def generate_lines(how_many=20, lower_bound=-100, upper_bound=100, error=10 ** (-8)):
    lines = []
    while len(lines) != how_many:
        x1 = random.uniform(lower_bound, upper_bound)
        y1 = random.uniform(lower_bound, upper_bound)
        x2 = random.uniform(lower_bound, upper_bound)
        y2 = random.uniform(lower_bound, upper_bound)
        a = (x1, y1)
        b = (x2, y2)
        line = Line(a, b)
        if is_vertical(line, error):
            continue
        lines.append(line)
    return lines


def main():
    pass


if __name__ == "__main__":
    main()
