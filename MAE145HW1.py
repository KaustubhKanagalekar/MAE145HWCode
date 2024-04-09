# MAE 145 HW 1
# Kaustubh Kanagalekar 
# A16790822 

import numpy as np 

##########################################################
def computeLineThroughTwoPoints(p1, p2):
    #result should be in Ax + By + C = 0  y-y1 = m(x-x1) y-y1(x2-x1) = (y2-y1)(x-x1)
    if abs(p1[0] - p2[0]) >= 10**-8 or abs(p1[1] - p2[1]) >= 10**-8:
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]

        #slope = (y2 - y1)/(x2 - x1)
        #equation = Eq((y - y1) , slope*(x - x1)) 
        #equation = Eq((x2-x1)*y -(y2-y1)*x, (x2-x1)*y1 - (y2-y1)*x1)
        b = (x2-x1)
        a = -(y2-y1)
        c = -((x2-x1)*y1 - (y2-y1)*x1)

        normalise =  (a**2 + b**2)**0.5
        a_norm = a/normalise
        b_norm = b/normalise
        return a,b,c
    else: 
        print("points aren't distinct")
        

##########################################################

def computeDistancePointToLine(p1,p2,q):
    #finds distance between a point and a line 
    if p1[0] != p2[0] or p1[1] != p2[1]:
        a, b, c = computeLineThroughTwoPoints(p1, p2)
        qx = q[0]
        qy = q[1]
        distance = abs((a*qx + b*qy + c))/((a**2 + b**2)**0.5)
        return distance
    elif p1[0] == p2[0]:
        # vertical line 
        distance = qx - p1[0]
        return distance
    elif p1[1] == p2[1]:
        # horizontal line 
        distance = qy - p1[1]
        return distance
    
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

        ux = px2 - px1
        uy = py2 - py1
        vx = qx - px1 
        vy = qy - py1
        u = [ux,uy]
        v = [vx,vy]

        if (u[0]*v[0] + u[1]*v[1]) < 0:
            distance = ((qx - px1)**2 + (qy-py1)**2)**0.5
            w = 1
        elif (u[0]*u[0] + u[1]*u[1]) <= (u[0]*v[0] + u[1]*v[1]):
            distance = ((qx - px2)**2 + (qy-py2)**2)**0.5
            w = 2
        else:
            distance = computeDistancePointToLine(p1,p2,q)
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
        ux = px2 - px1
        uy = py2 - py1
        vx = qx - px1 
        vy = qy - py1
        u = [ux,uy]
        v = [vx,vy]
        if (u[0]*v[0] + u[1]*v[1]) < 0:
            w = 1
        elif (u[0]*u[0] + u[1]*u[1]) <= (u[0]*v[0] + u[1]*v[1]):
            w = 2
        else:
            w = 0 
        return distance, w
         
#####################################################
# part a
p1 = [1,1]
p2 = [2,2]
q = [3,4]

a,b,c = computeLineThroughTwoPoints(p1, p2)
print('a =', a, 'b =', b, 'c =', c)
distance = computeDistancePointToLine(p1,p2,q)
print('distance = ', distance)
distance, w = computeDistancePointToSegment(p1,p2,q)
print('distance = ', distance, 'w = ', w)
print("the above values are for part a")
print(" ")

# part b 
p1 = [0,2]
p2 = [2,2]
q = [1,2]

a,b,c = computeLineThroughTwoPoints(p1, p2)
print('a =', a, 'b =', b, 'c =', c)
distance = computeDistancePointToLine(p1,p2,q)
print('distance = ', distance)
distance, w = computeDistancePointToSegment(p1,p2,q)
print('distance = ', distance, 'w = ', w)
print("the above values are for part b")
print(" ")

# part c
p1 = [2,0]
p2 = [2,2]
q = [5,2]

a,b,c = computeLineThroughTwoPoints(p1, p2)
print('a =', a, 'b =', b, 'c =', c)
distance = computeDistancePointToLine(p1,p2,q)
print('distance = ', distance)
distance, w = computeDistancePointToSegment(p1,p2,q)
print('distance = ', distance, 'w = ', w)
print("the above values are for part c")
print(" ")
