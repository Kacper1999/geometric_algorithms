from voronoi_diagram.Structures import LineType, Bisection, Point, Line
from configuration_for_visualization import *

EPS = 10e-8
upperRightPoint = Point(10, 10)
lowerLeftPoint = Point(-10, -10)
lowerRightPoint = Point(10, -10)
upperLeftPoint = Point(-10, 10)


def isVoronoiPoint(tab, i, j, k, proposedPoint):
    if (not proposedPoint): return False

    distance = tab[i].distance(proposedPoint)
    for l in range(len(tab)):
        if (l != i and l != j and l != k):
            if (distance > tab[l].distance(proposedPoint)): return False

    return True


def createVoronoiPoints(tab, scenes):
    foundPoints = []
    for i in range(2, len(tab)):
        for j in range(1, i):
            for k in range(j):
                proposedPoint = tab[i].findPointWithEqualDistance(tab[j], tab[k])
                if (isVoronoiPoint(tab, i, j, k, proposedPoint)):
                    proposedPoint.closestPoints = set([i, j, k])
                    foundPoints.append(proposedPoint)  # Dodać informacje o punktach
                    scenes.append(Scene([makePointsCollection(foundPoints), makePointsCollection(tab, 'green')],
                                        [makeLinesCollection(boundLines, 'purple')]))

    return foundPoints


def isVoronoiLine(voronoiPoints, i, j):  # Sprawdza czy linia pomiędzy punktami voronoi i i j należy do diagramu
    if (i == j): return False
    if (len(voronoiPoints[i].closestPoints.intersection(voronoiPoints[j].closestPoints))) == 2: return True
    return False


def createVoronoiPolprosta(tab, voronoiPoint, sec1, sec2, notBelonging):
    # print("Polprosta od punktu: ",voronoiPoint, " z sektorów ",tab[sec1],tab[sec2])
    bisec1 = Bisection(tab[sec1], tab[sec2])
    bisec2 = Bisection(tab[sec1], tab[sec2])

    boudaryCrossingPoints = []

    for i in bisec1.lines:
        # print(i)
        if (i.doLinesCross(Line(upperRightPoint, lowerRightPoint))):
            boudaryCrossingPoints.append(i.crossingPoint(Line(upperRightPoint, lowerRightPoint)))

        if (i.doLinesCross(Line(lowerRightPoint, lowerLeftPoint))):
            boudaryCrossingPoints.append(i.crossingPoint(Line(lowerRightPoint, lowerLeftPoint)))

        if (i.doLinesCross(Line(lowerLeftPoint, upperLeftPoint))):
            boudaryCrossingPoints.append(i.crossingPoint(Line(lowerLeftPoint, upperLeftPoint)))

        if (i.doLinesCross(Line(upperLeftPoint, upperRightPoint))):
            boudaryCrossingPoints.append(i.crossingPoint(Line(upperLeftPoint, upperRightPoint)))

    # print('Dla punktu voronoi: ',voronoiPoint, ' Szukamy dla obszarów ',tab[sec1], tab[sec2])
    # print(bisec1)
    bisec1.restrictBisection(voronoiPoint, boudaryCrossingPoints[0])
    bisec2.restrictBisection(voronoiPoint, boudaryCrossingPoints[1])

    if (boudaryCrossingPoints[0].distance(tab[sec1]) < boudaryCrossingPoints[0].distance(tab[notBelonging])):
        return bisec1
    else:
        return bisec2


def createVoronoiLines(tab, voronoiPoints, scenes):
    voronoiLines = []

    for i in voronoiPoints: i.createdLinesWithSectors = []

    for i in range(0, len(voronoiPoints) - 1):
        count = 0
        for j in range(i, len(voronoiPoints)):
            if (isVoronoiLine(voronoiPoints, i, j)):
                intersect = voronoiPoints[i].closestPoints.intersection(voronoiPoints[j].closestPoints)
                a = intersect.pop()
                b = intersect.pop()

                voronoiLines.append(Bisection(tab[a], tab[b]))
                voronoiLines[-1].restrictBisection(voronoiPoints[i], voronoiPoints[j])

                voronoiPoints[i].createdLinesWithSectors.append(set([a, b]))
                voronoiPoints[j].createdLinesWithSectors.append(set([a, b]))

                scenes.append(Scene([makePointsCollection(voronoiPoints), makePointsCollection(tab, 'green')],
                                    [makeLinesCollectionFromBisection(voronoiLines),
                                     makeLinesCollection(boundLines, 'purple')]))

    for i in range(len(voronoiPoints)):
        closestSectors = list(voronoiPoints[i].closestPoints)
        for sec1 in range(1, 3):
            for sec2 in range(0, sec1):
                # print(sec1,sec2)
                flag = False
                for chceckedSector in voronoiPoints[i].createdLinesWithSectors:
                    if (set([closestSectors[sec1], closestSectors[sec2]]) == chceckedSector): flag = True

                if (not flag):
                    if (sec1 != 0 and sec2 != 0):
                        sec3 = 0
                    elif (sec1 != 1 and sec2 != 1):
                        sec3 = 1
                    else:
                        sec3 = 2
                    voronoiLines.append(
                        createVoronoiPolprosta(tab, voronoiPoints[i], closestSectors[sec1], closestSectors[sec2],
                                               closestSectors[sec3]))
                    scenes.append(Scene([makePointsCollection(voronoiPoints), makePointsCollection(tab, 'green')],
                                        [makeLinesCollectionFromBisection(voronoiLines),
                                         makeLinesCollection(boundLines, 'purple')]))
    return voronoiLines


def voronoiDiagram(tab, scenes, ur=Point(10, 10), ll=Point(-10, -10)):
    global upperRightPoint
    global lowerLeftPoint
    global lowerRightPoint
    global upperLeftPoint
    global boundLines

    upperRightPoint = ur
    lowerLeftPoint = ll
    lowerRightPoint = Point(ur.x, ll.y)
    upperLeftPoint = Point(ll.x, ur.y)

    boundLines = []
    boundLines.append(Line(upperRightPoint, upperLeftPoint))
    boundLines.append(Line(upperRightPoint, lowerRightPoint))
    boundLines.append(Line(lowerRightPoint, lowerLeftPoint))
    boundLines.append(Line(lowerLeftPoint, upperLeftPoint))

    voronoiPoints = createVoronoiPoints(tab, scenes)

    voronoiLines = createVoronoiLines(tab, voronoiPoints, scenes)

    return [voronoiPoints, voronoiLines, boundLines]


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


def makeLinesCollectionFromBisection(tab, colora='red'):
    pom = []
    for i in tab:
        for j in i.lines:
            if (j.lineType == LineType.ODCINEK):
                pom.append([(j.start.x, j.start.y), (j.end.x, j.end.y)])

    return LinesCollection(pom, color=colora)
