from configuration_for_visualization import *
from voronoi_diagram.Structures import Point
from voronoi_diagram.algotithm import voronoiDiagram
import random


def makePointsCollection(tab, colora='blue'):
    pom = []
    for i in tab:
        pom.append((i.x, i.y))
    return PointsCollection(pom, color=colora)


def makeLinesCollection(tab, colora='red'):
    pom = []
    for i in range(len(tab)):
        pom.append([(tab[i].start.x, tab[i].start.y), (tab[i].end.x, tab[i].end.y)])

    return LinesCollection(pom, color=colora)


def main():
    tab = []
    random.seed()
    for _ in range(20):
        tab.append(Point(random.uniform(-9, 9), random.uniform(-9, 9)))
    scenes = []
    scenes.append(Scene([makePointsCollection(tab, 'green')]))
    vor = voronoiDiagram(tab, scenes)
    voronoiPoints = vor[0]
    voronoiBisections = vor[1]
    bounds = vor[2]
    voronoiLines = []

    for i in voronoiBisections:
        for j in i.lines:
            voronoiLines.append(j)

    scenes.append(Scene([makePointsCollection(voronoiPoints), makePointsCollection(tab, 'green')],
                        [makeLinesCollection(voronoiLines), makeLinesCollection(bounds, 'purple')]))

    scenes.append(Scene([makePointsCollection(tab, 'green')],
                        [makeLinesCollection(voronoiLines), makeLinesCollection(bounds, 'purple')]))

    plot = Plot(scenes)
    plot.draw()


if __name__ == "__main__":
    main()
