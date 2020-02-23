from configuration_for_visualization import *


def lines_to_lines_collection(lines):
    prepared_lines = []
    for line in lines:
        prepared_lines.append([line.a, line.b])
    return LinesCollection(prepared_lines)


class Polygon:
    def __init__(self, lines):
        self.lines = lines
        self.vertices = []
        for line in lines:
            self.vertices.append(line.a)

    def draw(self):
        lines_collection = lines_to_lines_collection(self.lines)
        scenes = [Scene([PointsCollection(self.vertices, color='red')],
                        [lines_collection])]
        plot = Plot(scenes)
        plot.draw()
