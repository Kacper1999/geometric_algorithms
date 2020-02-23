from triangulation.Polygon import Polygon
from triangulation.Line import Line
from configuration_for_visualization import *


def lines_to_lines_collection(lines, color="blue"):
    prepared_lines = []
    for line in lines:
        prepared_lines.append([line.a, line.b])
    return LinesCollection(prepared_lines, color=color)


def lines_collection_to_lines(lines_collection):
    lines = []
    for line in lines_collection.lines:
        lines.append(Line(line[0], line[1]))
    return lines


def list_lines_to_my_lines(list_lines):
    my_lines = []
    for line in list_lines:
        my_lines.append(Line(line.a, line.b))
    return my_lines


def get_chain(polygon, mode):  # gets left chain if "mode" = 1 and right if = -1
    if mode != 1 and mode != -1:
        print(f"bad mode input {mode}")

    top = max(polygon.vertices, key=lambda tup: (tup[1], tup[0]))
    bot = min(polygon.vertices, key=lambda tup: (tup[1], tup[0]))
    start = polygon.vertices.index(top)
    stop = polygon.vertices.index(bot)
    chain = []
    while start != stop:
        chain.append(polygon.vertices[start])
        start = (start + mode) % len(polygon.vertices)
    chain.append(polygon.vertices[start])
    return chain


def get_left_right_chains(polygon):
    left_chain = get_chain(polygon, 1)
    right_chain = get_chain(polygon, - 1)
    return left_chain, right_chain


def get_polygons():
    plot = Plot()
    plot.draw()
    added_figure = plot.get_added_figure()
    polygons = []
    for lines_collection in added_figure:
        if not lines_collection.lines:
            break
        lines = []
        for line in lines_collection.lines:
            lines.append(Line(line[0], line[1]))
        polygons.append(Polygon(lines))
    return polygons


def make_lines_from_vertices(vertices):
    lines = []
    for i in range(len(vertices)):
        lines.append(Line(vertices[i], vertices[(i + 1) % len(vertices)]))
    return lines


def main():
    pass


if __name__ == "__main__":
    main()
