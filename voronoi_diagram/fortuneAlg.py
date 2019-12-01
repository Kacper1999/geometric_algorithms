from voronoi_diagram import Structures as S
from bintrees import AVLTree
import heapq
from enum import Enum


class EventType(Enum):
    SiteEvent = 'SiteEvent'
    CircleEvent = 'CircleEvent'


def fortuneAlf(points):
    voronoiPoints = []
    voronoiLines = []
    heap = []
    tree = AVLTree()
    for i in points:
        i.eventType = EventType.SiteEvent
        heapq.heappush(heap, i)

    while (heap):
        currentPoint = heapq.heappushpop(heap)

        handleSiteEvent(voronoiPoints, voronoiLines, heap, tree, currentPoint)
        handleCircleEvent(voronoiPoints, voronoiLines, heap, tree, currentPoint)


def handleSiteEvent(voronoiPoints, voronoiLines, heap, tree, currentPoint):
    if (tree.is_empty()):  # Jeśli drzewo jest puste wstaw do drzewa i wróć
        tree.insert(currentPoint.x, currentPoint)
        return

    tree.insert(currentPoint.x, currentPoint)
    minTree = tree.min_item()[1]
    maxTree = tree.max_item()[1]

    if (minTree.x < currentPoint.x):
        leftClosest = tree.prev_item(currentPoint.x)[1]
        distance = abs(minTree.y - leftClosest.y)
        if (abs(leftClosest.x - currentPoint.x) < distance):
            voronoiLines.append(S.Bisection(leftClosest, currentPoint))  # TUTAJ TRZEBA DODAĆ LINIE NA RAZIE JEST ŹLE

    if (currentPoint.x < maxTree.x):
        rightClosest = tree.succ_item(currentPoint.x)[1]
        distance = abs(minTree.y - rightClosest.y)
        if (abs(leftClosest.x - currentPoint.x) < distance):
            voronoiLines.append(S.Bisection(rightClosest, currentPoint))  # TUTAJ TRZEBA DODAĆ LINIĘ NA RAZIE JEST ŹLE

    if (minTree.x < currentPoint.x and currentPoint.x < maxTree.x):
        leftClosest = tree.prev_item(currentPoint.x)[1]
        rightClosest = tree.succ_item(currentPoint.x)[1]
        eqDistancePoint = currentPoint.findPointWithEqualDistance(leftClosest, rightClosest)
        if (eqDistancePoint):
            voronoiPoints.append(eqDistancePoint)
            if (eqDistancePoint.y < currentPoint.y):
                heapq.heappush(currentPoint)

    return 0  # TODO FIRST


def handleCircleEvent(voronoiPoints, voronoiLines, heap, tree, currentPoint):
    return 0  # TODO SECOND


def main():
    points = [(1, 1), (0, 1), (2, 3), (-1, 4), (7, 8), (-3, 4), (10, -7)]
    our_points = []
    for point in points:
        our_points.append(S.Point(point[0], point[1]))
    prior_q = []
    tree = AVLTree()
    for i, point in enumerate(points):
        tree.insert(point, i)
    print(tree)
    for tuple_point in points:
        if tree.max_key() != tuple_point:
            next_item = tree.succ_item(tuple_point)
            print(f"current item = {tuple_point}")
            print(f"next item = {next_item}")
            print()
        if tree.min_key() != tuple_point:
            prev_item = tree.prev_item(tuple_point)
            print(f"prev item = {prev_item}")
            print()


if __name__ == "__main__":
    main()
