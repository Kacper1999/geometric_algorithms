import math
import heapq

import numpy as np
from bintrees import AVLTree
from enum import Enum


EPS = 10e-8
largeNumber = 1000000


def det(a,b,c): #Wyznacznik pomiędzy 3 punktami
        return a.x*b.y + a.y*c.x + b.x*c.y - a.x*c.y - a.y*b.x - b.y*c.x

def orientation(a,b, c): #Orientacja wyznacznika: zwraca 0, 1, lub -1
        detVal = det(a,b,c)
        return 0 if abs(detVal)<EPS else np.sign(detVal)

class Point:
    #Klasa przechowująca punkty
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, second):
        return abs(self.x-second.x)+abs(self.y-second.y)

    def findPointWithEqualDistance(self, firstPoint, secondPoint): #TODO
        #Zwraca punkt znajdujący sie w równej odległości od 3 podanych punktów
        #Jeśli takowy nie istnieje zwraca False
        return 0

    def __str__(self):
        stri = (self.x,self.y)
        stri = str(stri)
        return stri
    
    def __lt__(self, second):
        return self.y<second.y

    def __gt__(self, second):
        return self.y>second.y

    def __add__(self, point):
        return Point(self.x+point.x, self.y+point.y)

    def __sub__(self, point):
        return Point(self.x-point.x, self.y-point.y)
    
    def multiplyByScalar(self, scalar):
        return Point(self.x*scalar, self.y*scalar)

    def divideByScalar(self, scalar):
        return Point(self.x/scalar, self.y/scalar)
    
class LineType(Enum):
     ODCINEK = 'ODCINEK'
     POLPROSTA = 'POLPROSTA'


class Line:
    # Klasa przechowująca linie
    # Konstruktor przyjmyuje dwa punkty i opcjonalnie argument mówiący o typie linii
    # Gdy linia jest półprostą self.start punkt startu, a self.end to wektor
    def __init__(self, startingPoint, endingPoint, lineType = LineType.ODCINEK):
        
        self.start = startingPoint
        self.end = endingPoint
        self.lineType = lineType

    def lineCoinainsPoint(self, point): #True jeżeli punkt należy do prostej False w przeciwnym przyapdku
        if(self.lineType == LineType.POLPROSTA):
            if(orientation(self.start, self.start+self.end, point) != 0): return False
            
            if(self.end.x != 0):
                a = (point.x-self.start.x)/self.end.x
            elif(self.end.y != 0):
                a = (point.y-self.start.y)/self.end.y
            if(a>0): return True 
        
        else:
            if orientation(self.start, self.end, point) != 0: return False

            if(self.start.x <= point.x and point.x <= self.end.x): return True
            if(self.end.x <= point.x and point.x <= self.start.x): return True

        return False

    def doLinesCross(self, secondLine): #True jeżli linie się przecinają

        if (self.lineType == LineType.POLPROSTA and secondLine.lineType == LineType.POLPROSTA):
            pom1 = Line(self.start, self.start+self.end.multiplyByScalar(largeNumber))
            pom2 = Line(secondLine.start, secondLine.start+secondLine.end.multiplyByScalar(largeNumber))

        elif(self.lineType == LineType.POLPROSTA and secondLine.lineType == LineType.ODCINEK):
            pom1 = Line(self.start, self.start+self.end.multiplyByScalar(largeNumber))
            pom2 = secondLine
        
        elif(self.lineType == LineType.ODCINEK and secondLine.lineType == LineType.POLPROSTA):
            pom1 = Line(secondLine.start, secondLine.start+secondLine.end.multiplyByScalar(largeNumber))
            pom2 = self
        else:
            pom1 = self
            pom2 = secondLine

        

        o1 = orientation(pom1.start, pom1.end, pom2.start)
        o2 = orientation(pom1.start, pom1.end, pom2.end)

        o3 = orientation(pom2.start, pom2.end, pom1.start)
        o4 = orientation(pom2.start, pom2.end, pom1.end)
        
        if(pom1.lineCoinainsPoint(pom2.start)): return True
        if(pom1.lineCoinainsPoint(pom2.end)): return True
        if(pom2.lineCoinainsPoint(pom1.start)): return True
        if(pom2.lineCoinainsPoint(pom1.end)): return True
        
        if (o1 != o2 and o3 != o4):
            return True

        return False

    def crossingPoint(self, secondLine):
        if(not self.doLinesCross(secondLine)): return False
        if (self.lineType == LineType.POLPROSTA and secondLine.lineType == LineType.POLPROSTA):
            pom1 = Line(self.start, self.start+self.end.multiplyByScalar(largeNumber))
            pom2 = Line(secondLine.start, secondLine.start+secondLine.end.multiplyByScalar(largeNumber))

        elif(self.lineType == LineType.POLPROSTA and secondLine.lineType == LineType.ODCINEK):
            pom1 = Line(self.start, self.start+self.end.multiplyByScalar(largeNumber))
            pom2 = secondLine
        
        elif(self.lineType == LineType.ODCINEK and secondLine.lineType == LineType.POLPROSTA):
            pom1 = Line(secondLine.start, secondLine.start+secondLine.end.multiplyByScalar(largeNumber))
            pom2 = self
        else:
            pom1 = self
            pom2 = secondLine

        if(abs(pom1.start.x-pom1.end.x) < EPS and abs(pom2.start.x-pom2.end.x) < EPS):
            if(pom1.lineCoinainsPoint(pom2.start)): return pom2.start
            if(pom1.lineCoinainsPoint(pom2.end)): return pom2.end
            if(pom2.lineCoinainsPoint(pom1.start)): return pom1.start
            if(pom2.lineCoinainsPoint(pom1.end)): return pom1.end

        elif(abs(pom1.start.x-pom1.end.x) < EPS):
            a = (pom2.end.y-pom2.start.y)/(pom2.end.x-pom2.start.x)
            b = pom2.start.y-pom2.start.x*a
            return Point(pom1.start.x,a*pom1.start.x+b)

        elif(abs(pom2.start.x-pom2.end.x) < EPS):
            a = (pom1.end.y-pom1.start.y)/(pom1.end.x-pom1.start.x)
            b = pom1.start.y-pom1.start.x*a
            return Point(pom2.start.x,a*pom2.start.x+b)

        else:
            a1 = (pom2.end.y-pom2.start.y)/(pom2.end.x-pom2.start.x)
            b1 = pom2.start.y-pom2.start.x*a1

            a2 = (pom1.end.y-pom1.start.y)/(pom1.end.x-pom1.start.x)
            b2 = pom1.start.y-pom1.start.x*a2

            x = (b2-b1)/(a1-a2)
            y=a1*x+b1
            return Point(x,y)
        

    def __str__(self):
        return '(({self.start.x},{self.start.y}),({self.end.x},{self.end.y})) {self.lineType}'.format(self=self)



class Bisection:
    # Klasa przechowująca symetralne 
    # Konstruktor przyjmuje dwa punkty i tworzy symetralną stworzoną za pomocą obiektów typu Line zawierających się w tablicy lines
    def __init__(self, firstPoint, secondPoint):
        self.lines = []
        if(secondPoint.x < firstPoint.x): #SWAP
            swapPom = secondPoint
            secondPoint = firstPoint
            firstPoint = swapPom

        
        middlePoint = Point((firstPoint.x+secondPoint.x)/2,(firstPoint.y+secondPoint.y)/2)

        if(firstPoint.y > secondPoint.y and firstPoint.x < secondPoint.x): wector = 1
        else: wector = -1


        if(abs(firstPoint.y-secondPoint.y)<abs(firstPoint.x-secondPoint.x)):
            if(firstPoint.y > secondPoint.y and firstPoint.x < secondPoint.x):
                firstStartingPoint  = Point(middlePoint.x + wector * abs(firstPoint.y-secondPoint.y)/2, firstPoint.y)
                secondStartingPoint = Point(middlePoint.x - wector * abs(firstPoint.y-secondPoint.y)/2, secondPoint.y)
                self.lines.append(Line(firstStartingPoint, Point(0, wector), LineType.POLPROSTA))
                self.lines.append(Line(secondStartingPoint, Point(0, -wector), LineType.POLPROSTA))
            else:
                firstStartingPoint  = Point(middlePoint.x + wector * abs(firstPoint.y-secondPoint.y)/2, secondPoint.y)
                secondStartingPoint = Point(middlePoint.x - wector * abs(firstPoint.y-secondPoint.y)/2, firstPoint.y)
                self.lines.append(Line(firstStartingPoint, Point(0, -wector), LineType.POLPROSTA))
                self.lines.append(Line(secondStartingPoint, Point(0, wector), LineType.POLPROSTA))

            

        elif (abs(firstPoint.x-secondPoint.x)<abs(firstPoint.y-secondPoint.y)):
            
            if(firstPoint.y > secondPoint.y and firstPoint.x < secondPoint.x):
                firstStartingPoint  = Point(firstPoint.x, middlePoint.y - wector * abs(firstPoint.x-secondPoint.x)/2)
                secondStartingPoint = Point(secondPoint.x, middlePoint.y + wector * abs(firstPoint.x-secondPoint.x)/2)
                self.lines.append(Line(firstStartingPoint, Point(-wector, 0), LineType.POLPROSTA))
                self.lines.append(Line(secondStartingPoint, Point(wector, 0), LineType.POLPROSTA))

            else:
                firstStartingPoint  = Point(firstPoint.x, middlePoint.y - wector * abs(firstPoint.x-secondPoint.x)/2)
                secondStartingPoint = Point(secondPoint.x, middlePoint.y + wector * abs(firstPoint.x-secondPoint.x)/2)
                self.lines.append(Line(firstStartingPoint, Point(wector, 0), LineType.POLPROSTA))
                self.lines.append(Line(secondStartingPoint, Point(-wector, 0), LineType.POLPROSTA))


        self.lines.append(Line(firstStartingPoint, secondStartingPoint, LineType.ODCINEK))

    def doBissectionsCross(self, second):
        for i in self.lines:
            for j in second.lines:
                if(i.doLinesCross(j)): return True
        return False
    
    def crossingPoint(self, second):
        for i in self.lines:
            for j in second.lines:
                if(i.doLinesCross(j)):
                    return i.crossingPoint(j)
        return False

    def __str__(self):
        strPom = ''
        for i in self.lines:
            strPom += str(i)
            strPom += "\n"

        return str(strPom)


# def FortuneAlgorithm(points):
#     heap = []
#     for i in points:
#         heap.append(i)
#     heapq.heapify(heap)
