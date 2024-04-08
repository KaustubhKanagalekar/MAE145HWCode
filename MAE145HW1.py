# MAE 145 HW 1
# Kaustubh Kanagalekar 
# A16790822 
from sympy import symbols, Eq
import numpy as np 

##########################################################
def computeLineThroughTwoPoints(p1, p2):
    #result should be in Ax + By + C = 0  
    x = symbols('x')
    y = symbols('y')
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    slope = (y2 - y1)/(x2 - x1)
    equation = Eq((y - y1) , slope*(x - x1)) 
    equation = Eq((x2-x1)*y -(y2-y1)*x, (x2-x1)*y1 - (y2-y1)*x1)
    b = (x2-x1)
    a = -(y2-y1)
    c = -((x2-x1)*y1 - (y2-y1)*x1)

    normalise =  (a**2 + b**2)**0.5
    a_norm = a/normalise
    b_norm = b/normalise

    return equation, a,b,c, a_norm, b_norm

print(computeLineThroughTwoPoints([3,2], [4,5]))

##########################################################

def computeDistancePointToLine(p1,p2,q):
    #finds distance between a point and a line 
    a = (computeLineThroughTwoPoints(p1,p2)[1])
    b = (computeLineThroughTwoPoints(p1,p2)[2])
    c = (computeLineThroughTwoPoints(p1,p2)[3])
    qx = q[0]
    qy = q[1]
    distance = abs((a*qx + b*qy + c))/((a**2 + b**2)**0.5)
    return distance, a,b,c
    

print(computeDistancePointToLine([3,2],[4,5], [0,0]))
print(computeDistancePointToLine([3,2],[4,5], [0,0])[0])
#############################################################


def computeDistancePointToSegment(p1,p2,q):
    #finds the distance and indicates which point is the closest
    if abs(p1[0] - p2[0]) >= 10**-8 or abs(p1[1] - p2[1]) >= 10**-8:
        qx = q[0]
        qy = q[1]
        px1 = p1[0]
        py1 = p1[1]
        px2 = p2[0]
        py2 = p2[1]

        u = np.array([px2 - px1, py2 - py1])
        v = np.array([qx - px1, qy - py1])
        projection = u * (u[0]*v[0] + u[1]*v[1])/(u[0]*u[0] + u[1]*u[1])
        distance = v - projection
        distance = (distance[0]**2 + distance[1]**2)**0.5
        
        if (u[0]*v[0] + u[1]*v[1]) < 0:
            w = 1
        elif (u[0]*u[0] + u[1]*u[1]) <= (u[0]*v[0] + u[1]*v[1]):
            w = 2
        else:
            w = 0 
        return distance, w
    else:  
        qx = q[0]
        qy = q[1]
        px1 = p1[0]
        py1 = p1[1]
        px2 = p2[0]
        py2 = p2[1]
        distance = ((qx-px1)**2 + (qy - px2)**2)**0.5
        u = np.array([px2 - px1, py2 - py1])
        v = np.array([qx - px1, qy - py1])
        if (u[0]*v[0] + u[1]*v[1]) < 0:
            w = 1
        elif (u[0]*u[0] + u[1]*u[1]) <= (u[0]*v[0] + u[1]*v[1]):
            w = 2
        else:
            w = 0 
        return distance, w
         
print(computeDistancePointToSegment([7.02222,5.012],[7.02222,5.012], [7,4]))
