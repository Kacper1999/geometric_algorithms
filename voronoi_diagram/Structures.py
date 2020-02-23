import numpy as np
from enum import Enum

EPS = 10e-8
largeNumber = 1000000


def det(a, b, c):  # Wyznacznik pomiędzy 3 punktami
    return a.x * b.y + a.y * c.x + b.x * c.y - a.x * c.y - a.y * b.x - b.y * c.x


def orientation(a, b, c):  # Orientacja wyznacznika: zwraca 0, 1, lub -1
    detVal = det(a, b, c)
    return 0 if abs(detVal) < EPS else np.sign(detVal)


class Point:
    # Klasa przechowująca punkty
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, second):
        return abs(self.x - second.x) + abs(self.y - second.y)

    def findPointWithEqualDistance(self, firstPoint, secondPoint):
        # Zwraca punkt znajdujący sie w równej odległości od 3 podanych punktów
        # Jeśli takowy nie istnieje zwraca False
        bisection1 = Bisection(self, firstPoint)
        bisection2 = Bisection(self, secondPoint)
        if bisection1.doBisectionsCross(bisection2):
            return bisection1.crossingPoint(bisection2)
        return False

    def __str__(self):
        stri = (self.x, self.y)
        stri = str(stri)
        return stri

    def __eq__(self, second):
        return (abs(self.x - second.x) < EPS and abs(self.y - second.y) < EPS)

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y)

    def multiplyByScalar(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def divideByScalar(self, scalar):
        return Point(self.x / scalar, self.y / scalar)

    def to_tuple(self):
        return self.x, self.y


class LineType(Enum):
    ODCINEK = 'ODCINEK'
    POLPROSTA = 'POLPROSTA'


class Line:
    # Klasa przechowująca linie
    # Konstruktor przyjmyuje dwa punkty i opcjonalnie argument mówiący o typie linii
    # Gdy linia jest półprostą self.start punkt startu, a self.end to wektor
    def __init__(self, startingPoint, endingPoint, lineType=LineType.ODCINEK):

        self.start = startingPoint
        self.end = endingPoint
        self.lineType = lineType

        if self.lineType == LineType.POLPROSTA:
            self.v = (self.end.x, self.end.y)
        else:
            self.v = self.v = (
                self.end.x - self.start.x, self.end.y - self.start.y)

        if self.v[0] != 0:
            self.slope = self.v[1] / self.v[0]
            self.intercept = self.start.y - self.slope * self.start.x
            self.is_vertical = False
        else:
            self.is_vertical = True

    def get_y_at(self, x):
        return self.slope * x + self.intercept

    def lineContainsPoint(self, point):  # True jeżeli punkt należy do prostej False w przeciwnym przyapdku

        if (self.lineType == LineType.POLPROSTA):
            if (orientation(self.start, self.start + self.end, point) != 0): return False

            if (self.end.x != 0):
                a = (point.x - self.start.x) / self.end.x
            elif (self.end.y != 0):
                a = (point.y - self.start.y) / self.end.y
            if (a > 0): return True

        else:
            if orientation(self.start, self.end, point) != 0: return False

            if (self.start.x <= point.x and point.x <= self.end.x): return True
            if (self.end.x <= point.x and point.x <= self.start.x): return True

        return False

    def doLinesCross(self, secondLine):
        if self.is_vertical or secondLine.is_vertical:
            if self.is_vertical and secondLine.is_vertical:
                return False
            if self.is_vertical:
                vertical = self
                not_vertical = secondLine
            else:
                vertical = secondLine
                not_vertical = self

            if not_vertical.lineType == LineType.POLPROSTA:
                not_vertical_end_point = not_vertical.end.multiplyByScalar(largeNumber)
            else:
                not_vertical_end_point = not_vertical.end

            # taki trick w tym ifie bo nwm czy secondLine.start.x < secondLine.end.x to mnoze roznice
            # i to daje <0 dla ulozenia secondLine.leftPoint < self.start.x < secondLine.rightPoint
            if (not_vertical.start.x - vertical.start.x) * (not_vertical_end_point.x - vertical.start.x) < 0:
                y = not_vertical.get_y_at(vertical.start.x)
                if vertical.lineType == LineType.POLPROSTA:
                    line_goes_up = vertical.end.y > 0
                    if line_goes_up:
                        return y > vertical.start.y
                    return y < vertical.start.y
                return (y - vertical.start.y) * (y - vertical.end.y) < 0
            return False

        if (self.lineType == LineType.POLPROSTA and secondLine.lineType == LineType.POLPROSTA):
            pom1 = Line(self.start, self.start + self.end.multiplyByScalar(largeNumber))
            pom2 = Line(secondLine.start, secondLine.start + secondLine.end.multiplyByScalar(largeNumber))

        elif (self.lineType == LineType.POLPROSTA and secondLine.lineType == LineType.ODCINEK):
            pom1 = Line(self.start, self.start + self.end.multiplyByScalar(largeNumber))
            pom2 = secondLine

        elif (self.lineType == LineType.ODCINEK and secondLine.lineType == LineType.POLPROSTA):
            pom1 = Line(secondLine.start, secondLine.start + secondLine.end.multiplyByScalar(largeNumber))
            pom2 = self
        else:
            pom1 = self
            pom2 = secondLine

        o1 = orientation(pom1.start, pom1.end, pom2.start)
        o2 = orientation(pom1.start, pom1.end, pom2.end)

        o3 = orientation(pom2.start, pom2.end, pom1.start)
        o4 = orientation(pom2.start, pom2.end, pom1.end)

        if (pom1.lineContainsPoint(pom2.start)): return True
        if (pom1.lineContainsPoint(pom2.end)): return True
        if (pom2.lineContainsPoint(pom1.start)): return True
        if (pom2.lineContainsPoint(pom1.end)): return True

        if (o1 != o2 and o3 != o4):
            return True

        return False

    def crossingPoint(self, secondLine):
        # print(self, secondLine)
        if (not self.doLinesCross(secondLine)): return False

        if self.is_vertical or secondLine.is_vertical:
            if self.is_vertical and secondLine.is_vertical:  # chyba doLinesCross to wychwytuje ale co tam
                return False
            if self.is_vertical:
                vertical = self
                not_vertical = secondLine
            else:
                vertical = secondLine
                not_vertical = self
            x = vertical.start.x
            y = not_vertical.get_y_at(x)
            return Point(x, y)

        if (self.lineType == LineType.POLPROSTA and secondLine.lineType == LineType.POLPROSTA):
            pom1 = Line(self.start, self.start + self.end.multiplyByScalar(largeNumber))
            pom2 = Line(secondLine.start, secondLine.start + secondLine.end.multiplyByScalar(largeNumber))

        elif (self.lineType == LineType.POLPROSTA and secondLine.lineType == LineType.ODCINEK):
            pom1 = Line(self.start, self.start + self.end.multiplyByScalar(largeNumber))
            pom2 = secondLine

        elif (self.lineType == LineType.ODCINEK and secondLine.lineType == LineType.POLPROSTA):
            pom1 = Line(secondLine.start, secondLine.start + secondLine.end.multiplyByScalar(largeNumber))
            pom2 = self
        else:
            pom1 = self
            pom2 = secondLine

        if (pom1.lineContainsPoint(pom2.start)): return pom2.start
        if (pom1.lineContainsPoint(pom2.end)): return pom2.end
        if (pom2.lineContainsPoint(pom1.start)): return pom1.start
        if (pom2.lineContainsPoint(pom1.end)): return pom1.end

        if (abs(pom1.start.x - pom1.end.x) < EPS):
            a = (pom2.end.y - pom2.start.y) / (pom2.end.x - pom2.start.x)
            b = pom2.start.y - pom2.start.x * a
            return Point(pom1.start.x, a * pom1.start.x + b)

        elif (abs(pom2.start.x - pom2.end.x) < EPS):
            a = (pom1.end.y - pom1.start.y) / (pom1.end.x - pom1.start.x)
            b = pom1.start.y - pom1.start.x * a
            return Point(pom2.start.x, a * pom2.start.x + b)

        else:
            a1 = (pom2.end.y - pom2.start.y) / (pom2.end.x - pom2.start.x)
            b1 = pom2.start.y - pom2.start.x * a1

            a2 = (pom1.end.y - pom1.start.y) / (pom1.end.x - pom1.start.x)
            b2 = pom1.start.y - pom1.start.x * a2

            x = (b2 - b1) / (a1 - a2)
            y = a1 * x + b1
            return Point(x, y)

    def makeOdcinekFromPolprosta(self, endingPoint):  # Zamienia półprostą na odcinek o końcu w endingPoint
        if (self.lineType == LineType.POLPROSTA and self.lineContainsPoint(endingPoint)):
            self.end = endingPoint

            self.lineType = LineType.ODCINEK

    def __str__(self):
        return '(({self.start.x},{self.start.y}),({self.end.x},{self.end.y})) {self.lineType}'.format(self=self)


class Bisection:
    # Klasa przechowująca symetralne 
    # Konstruktor przyjmuje dwa punkty i tworzy symetralną stworzoną za pomocą obiektów typu Line zawierających się w tablicy lines
    def __init__(self, firstPoint, secondPoint):
        self.lines = []
        if (secondPoint.x < firstPoint.x):  # SWAP
            swapPom = secondPoint
            secondPoint = firstPoint
            firstPoint = swapPom

        middlePoint = Point((firstPoint.x + secondPoint.x) / 2, (firstPoint.y + secondPoint.y) / 2)

        if (firstPoint.y > secondPoint.y and firstPoint.x < secondPoint.x):
            wector = 1
        else:
            wector = -1

        # print(firstPoint, secondPoint)

        if (abs(firstPoint.y - secondPoint.y) < abs(firstPoint.x - secondPoint.x)):
            if (firstPoint.y > secondPoint.y and firstPoint.x < secondPoint.x):
                firstStartingPoint = Point(middlePoint.x + wector * abs(firstPoint.y - secondPoint.y) / 2, firstPoint.y)
                secondStartingPoint = Point(middlePoint.x - wector * abs(firstPoint.y - secondPoint.y) / 2,
                                            secondPoint.y)
                self.lines.append(Line(firstStartingPoint, Point(0, wector), LineType.POLPROSTA))
                self.lines.append(Line(secondStartingPoint, Point(0, -wector), LineType.POLPROSTA))
            else:
                firstStartingPoint = Point(middlePoint.x + wector * abs(firstPoint.y - secondPoint.y) / 2,
                                           secondPoint.y)
                secondStartingPoint = Point(middlePoint.x - wector * abs(firstPoint.y - secondPoint.y) / 2,
                                            firstPoint.y)
                self.lines.append(Line(firstStartingPoint, Point(0, -wector), LineType.POLPROSTA))
                self.lines.append(Line(secondStartingPoint, Point(0, wector), LineType.POLPROSTA))



        elif (abs(firstPoint.x - secondPoint.x) < abs(firstPoint.y - secondPoint.y)):

            if (firstPoint.y > secondPoint.y and firstPoint.x < secondPoint.x):
                firstStartingPoint = Point(firstPoint.x, middlePoint.y - wector * abs(firstPoint.x - secondPoint.x) / 2)
                secondStartingPoint = Point(secondPoint.x,
                                            middlePoint.y + wector * abs(firstPoint.x - secondPoint.x) / 2)
                self.lines.append(Line(firstStartingPoint, Point(-wector, 0), LineType.POLPROSTA))
                self.lines.append(Line(secondStartingPoint, Point(wector, 0), LineType.POLPROSTA))

            else:
                firstStartingPoint = Point(firstPoint.x, middlePoint.y - wector * abs(firstPoint.x - secondPoint.x) / 2)
                secondStartingPoint = Point(secondPoint.x,
                                            middlePoint.y + wector * abs(firstPoint.x - secondPoint.x) / 2)
                self.lines.append(Line(firstStartingPoint, Point(wector, 0), LineType.POLPROSTA))
                self.lines.append(Line(secondStartingPoint, Point(-wector, 0), LineType.POLPROSTA))

        self.lines.append(Line(firstStartingPoint, secondStartingPoint, LineType.ODCINEK))

    def doBisectionsCross(self, second):
        for i in self.lines:
            for j in second.lines:
                if (i.doLinesCross(j)): return True
        return False

    def crossingPoint(self, second):
        for i in self.lines:
            for j in second.lines:
                if (i.doLinesCross(j)):
                    return i.crossingPoint(j)
        return False

    def restrictBisection(self, firstPoint, secondPoint):
        firstLine = secondLine = None
        for i in range(len(self.lines)):  # Znajdź linie które zawierają te punkty
            if self.lines[i].lineContainsPoint(firstPoint):
                firstLine = i
            if self.lines[i].lineContainsPoint(secondPoint):
                secondLine = i

        if (
                firstLine is None or secondLine is None): return  # Oba punkty muszą należeć do symetralnej jeśli nie należą zwróć

        if (firstLine == secondLine):  # Jeśli symetralną trzeba ograniczyć na dwóch punktach leżących na prostej
            self.lines = [Line(firstPoint, secondPoint, LineType.ODCINEK)]

        elif (self.lines[firstLine].lineType == LineType.POLPROSTA and self.lines[
            secondLine].lineType == LineType.POLPROSTA):
            # Jeśli symetralną trzeba ograniczyć na dwóch różnych półprostych
            self.lines[firstLine].makeOdcinekFromPolprosta(firstPoint)
            self.lines[secondLine].makeOdcinekFromPolprosta(secondPoint)
        else:
            # Trzeci przypadek gdy trzeba ograniczyć półprostą i odcinek. 

            if (self.lines[firstLine].lineType == LineType.POLPROSTA and self.lines[
                secondLine].lineType == LineType.ODCINEK):
                self.lines[firstLine].makeOdcinekFromPolprosta(firstPoint)

                if (self.lines[secondLine].start == self.lines[firstLine].start):

                    self.lines[secondLine].end = secondPoint
                    # print("Wchodzimy do przypadku 3.1.1")
                else:
                    self.lines[secondLine].start = secondPoint
                    # print("Wchodzimy do przypadku 3.1.2")

            elif (self.lines[firstLine].lineType == LineType.ODCINEK and self.lines[
                secondLine].lineType == LineType.POLPROSTA):
                self.lines[secondLine].makeOdcinekFromPolprosta(secondPoint)

                if (self.lines[secondLine].start == self.lines[firstLine].start):
                    self.lines[firstLine].end = firstPoint
                    # print("Wchodzimy do przypadku 3.2.1")

                else:
                    self.lines[firstLine].start = firstPoint
                    # print("Wchodzimy do przypadku 3.2.2")

            if (0 != firstLine and 0 != secondLine):
                self.lines.pop(0)
            elif (1 != firstLine and 1 != secondLine):
                self.lines.pop(1)
            elif (2 != firstLine and 2 != secondLine):
                self.lines.pop(2)

    def __str__(self):
        strPom = ''
        for i in self.lines:
            strPom += str(i)
            strPom += "\n"

        return str(strPom)


def main():
    pass


if __name__ == "__main__":
    main()
