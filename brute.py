import math
def distance(p1,p2):
    dx=p1[0]-p2[0]
    dy=p1[1]-p2[1]
    return math.sqrt(dx*dx+dy*dy)

def brute(points):
    mindistance=float('inf')
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            d=distance(points[i],points[j])
            if d<mindistance:
                mindistance=d
    return mindistance

points=[(2,3),(12,30),(40,50),(5,1),(12,10),(3,4)]
print("Closest distance :",brute(points))
