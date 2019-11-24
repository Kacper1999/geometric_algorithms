from random import uniform
from intersacting_lines.Line import Line
from configuration_for_visualization import *


def is_vertical(line, error=10 ** (-8)):
    return abs(line.a[0] - line.b[0]) < error


def get_lines():
    scene = get_scene()
    lines_collection = scene.lines[0]
    lines = []
    for line in lines_collection.lines:
        if not is_vertical(Line(line[0], line[1])):
            lines.append(Line(line[0], line[1]))
    return lines


def generate_lines(how_many=10, lower_bound=-100, upper_bound=100, error=10 ** (-8)):
    lines = []
    while len(lines) != how_many:
        x1 = uniform(lower_bound, upper_bound)
        y1 = uniform(lower_bound, upper_bound)
        x2 = uniform(lower_bound, upper_bound)
        y2 = uniform(lower_bound, upper_bound)
        a = (x1, y1)
        b = (x2, y2)
        line = Line(a, b)
        if is_vertical(line, error):
            continue
        lines.append(line)
    return lines


def main():
    scene = get_lines()
    plot = Plot([scene])
    plot.draw()


if __name__ == "__main__":
    main()
