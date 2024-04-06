# MAE 145 HW 1
# Kaustubh Kanagalekar 
# A16790822 
from sympy import symbols, Eq
import math 
import matplotlib.pyplot as plt
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

    normalise =  math.sqrt(a**2 + b**2)
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
    distance = abs((a*qx + b*qy + c))/math.sqrt(a**2 + b**2)
    return distance, a,b,c
    

print(computeDistancePointToLine([3,2],[4,5], [0,0]))
print(computeDistancePointToLine([3,2],[4,5], [0,0])[0])
#############################################################

'''
def computeDistancePointToSegment(p1,p2,q):
    computeDistancePointToLine(p1,p2,q)
    qx = q[0]
    qy = q[1]
    p1x = p1[0]
    py1 = p1[1]
    px2 = p2[0]
    py2 = p2[1]

    x = symbols('x')
    y = symbols('y')
    equation = Eq((px2-p1x)*y -(py2-py1)*x, (px2-p1x)*py1 - (py2-py1)*p1x)
    #this equation should only be valid in the domain of [px1, px2]
    b = (px2-p1x)
    a = -(py2-py1)
    c = -((px2-p1x)*py1 - (py2-py1)*p1x)
    distance = abs((a*qx + b*qy + c))/math.sqrt(a**2 + b**2)
    if 

    if computeDistancePointToLine(p1,p2,q)[0] >= math.sqrt((p1x-qx)**2 + (py1-qy)**2):
        w = 1
    elif computeDistancePointToLine(p1,p2,q)[0] >= math.sqrt((px2-qx)**2 + (py2-qy)**2):
        w = 2
    else: 
        w = 0
    
    return computeDistancePointToLine(p1,p2,q)[0], w
'''

def computeDistancePointToSegment(p1,p2,q):
    #finds the distance and indicates which point is the closest
    qx = q[0]
    qy = q[1]
    px1 = p1[0]
    py1 = p1[1]
    px2 = p2[0]
    py2 = p2[1]

    u = np.array([px2 - px1, py2 - py1])
    v = np.array([qx - px1, qy - py1])
    projection = u * np.dot(u, v)/np.dot(u,u) 
    distance = np.linalg.norm(v - projection)
    
    if np.dot(u,v) < 0:
        w = 1
    elif np.dot(u,u) <= np.dot(u,v):
        w = 2
    else:
        w = 0 
    return distance, w
print(computeDistancePointToSegment([7,5],[9,9], [8,12]))
