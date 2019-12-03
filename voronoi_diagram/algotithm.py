from Structures import LineType, Bisection, Point, TaxiCabParabola

EPS = 10e-8


def isVoronoiPoint(tab, i, j, k, proposedPoint):
    if (not proposedPoint): return False

    distance = tab[i].distance(proposedPoint)
    for l in range(len*tab):
        if(l != i and l != j and l != k):
            if(distance > tab[l].distance(proposedPoint)): return False
    
    return True
 
def createVoronoiPoints(tab):
    foundPoints = []
    for i in range(2, len(tab)):
        for j in range(1, i):
            for k in range(j):
                proposedPoint = tab[i].findPointWithEqualDistance(tab[j],tab[k])
                if(isVoronoiPoint(tab, i, j, k, proposedPoint)):
                    proposedPoint.closestPoints = set([i,j,k])
                    foundPoints.append(proposedPoint) #Dodać informacje o punktach
    
    return foundPoints 

def isVoronoiLine(voronoiPoints, i, j): #Sprawdza czy linia pomiędzy punktami voronoi i i j należy do diagramu
    if(i == j): return False;     
    if(len(voronoiPoints[i].closestPoints.intersection(voronoiPoints[j].closestPoints))) == 2: return True
    return False

def createVoronoiLines(tab, voronoiPoints):
    voronoiLines = []
    for i in range(0, len(voronoiPoints)-1):
        count = 0
        for j in range(i, len(voronoiPoints)):
            if(isVoronoiLine(voronoiPoints, i, j):
                voronoiLines.append((i,j)) #Wiemy że pomiędzy punktami tab[i] i tab[j] będzie linia 
                count+=1
        if(count == 2):
            print("Z punktu wychodzi jedna półprosta")
        if(count == 1)
            print("Z punktu wychodzą dwie półproste")
        if(count == 0)
            print("Z punktu wychodzą trzy półproste") #nie wiem czy taka sytuacja jest wgl możliwa




def voronoiDiagram(tab):
    voronoiPoints = createVoronoiPoints(tab)
    voronoiLines = createVoronoiLines(tab, voronoiPoints)


    
        
    return voronoiPoints

tab = []
tab.append(Point(1.1,2.4))
tab.append(Point(3.3,7.1))
tab.append(Point(4.64,5.234))
tab.append(Point(-1.63,5.11))
tab.append(Point(0.3,4.123))

# print(Point(0,4).findPointWithEqualDistance(Point(-1,3), Point(1,2)))
vor = voronoiDiagram(tab)
for i in vor: print(i)
