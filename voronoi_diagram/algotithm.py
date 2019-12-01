from voronoi_diagram.delaunay2D import Delaunay2D
from voronoi_diagram.Structures import LineType, Bisection, Point, TaxiCabParabola


def voronoiDiagram(tab):
    dt = Delaunay2D()
    for point in tab:
        dt.addPoint([point.x, point.y])
    dalauayPoints = dt.exportTriangles()

    voronoiPoints = []

    for i in dalauayPoints:
        # print(tab[i[0]], tab[i[1]], tab[i[2]])
        nPoint = tab[i[0]].findPointWithEqualDistance(tab[i[1]], tab[i[2]])
        if nPoint:
            voronoiPoints.append(nPoint)

    return voronoiPoints


tab = []
tab.append(Point(1.1, 2.4))
tab.append(Point(3.3, 7.1))
tab.append(Point(4.64, 5.234))
tab.append(Point(-1.63, 5.11))
tab.append(Point(0.3, 4.123))

# print(Point(0,4).findPointWithEqualDistance(Point(-1,3), Point(1,2)))
vor = voronoiDiagram(tab)
for i in vor: print(i)
