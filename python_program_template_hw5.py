#!/usr/bin/env python3
"""
Guidelines for program submission: 
    
A) To ensure readability by the grader, 
    please make sure the following submission format:

    1-- Please change the file name to python_program.py 
        ---(The file name is case sensitive, make sure it's identical)---
               
    2-- The *.py file should be compressed to the root of the *.zip file
        e.g., when you submit your homework.zip, 
                Please compress the python files directly 
        ---(Do Not compress the directory!)---
                    aka, if you unzip your *.zip, *.py files should appear
                        in the directory of *.zip file. 
                        
    ---FAIL TO FOLLOW INSTRUCTION A) MAY COST YOU SOME POINTS--- 


B) Your homework should follow the similar structure as this template

C) Keep in mind some minor points:
    
    1-- Your code should not have any debug error before submission!!!

    2-- The order of the function arguments should be the same as that in HW 

    2a-- The data type of the argument should be the same as that in template
                      
    3-- make sure your function return the value which the HW requested
    
    4-- make sure the order of the output arguments the same as those in template
    
    5-- Do not round up your output values
    
    6-- Do not use input function in your function
        
    7-- if you need uncommon modules, contact TA before submission or post it on Piazza

    8-- Please do not add any variable clearing command in the file, as this may terminate grader
    


If you had any question about the guideline, 
    contact TAs or post questions on piazza for response.
        
@author: Dan Li (lidan@ucsd.edu) & Yunhai Han (y8han@eng.ucsd.edu) at UCSD
@date: Jan 2021
"""


"""
The template starts from here
"""

# A16790822 #PID

# import all modules here if you need any

import numpy as np
import matplotlib.pyplot as plt
# your file should always start from definition of functions 


def computeGridSukharev(n): 
    """ descriptions here """
#computes the Sukharev grid of [0,1] plane with d = 2 and n points. 
    # define some variables etc.
    X = np.array([0])
    Y = np.array([0])
    start_x = 0 
    start_y = 0
    end_x = 1
    end_y = 1
    ##########
    #### Your main code here ####

    dispersion_of_centre = 1/(2*(n)**0.5)
    spacing = int(n**0.5 + 1) 

    space_x = np.linspace(start_x,end_x,spacing)
    space_y = np.linspace(start_y,end_y, spacing )

    for i in range(1,len(space_x)):
        for j in range(1,len(space_y)):
            X= np.append(X, space_x[i] - dispersion_of_centre)
            Y= np.append(Y,space_y[j] - dispersion_of_centre)
    X = np.delete(X,0)
    Y = np.delete(Y,0)
    ##########
    return X, Y, list(zip(X,Y))
        
    
    

def computeGridRandom(n):
    #np.random.seed(1)
    """ descriptions here """
# creates a grid [0,1] with random points placed 
    # define some variables etc.
    
    X = np.array([0])
    Y = np.array([0])

    ##########
    #### Your main code here ####
    X = np.random.uniform(0.0, 1.0, n)
    Y = np.random.uniform(0.0, 1.0, n)
    points = list(zip(X,Y))
    ##########
    
    
    return X, Y, points
     
    
def computeGridHalton(n, b1, b2):
    """ descriptions here """
#computes the Halton series of 2 prime numbers given a range n 
    # define some variables etc.
    
    X = np.zeros(n)
    Y = np.zeros(n)
    ##########
    #### Your main code here ####
    for i in range(n):
        itmpx = i +1
        itmpy =  i + 1
        f1 = 1/b1 
        f2 = 1/b2 
        while itmpx > 0:
            q1= itmpx//b1
            q2 = itmpy//b2 
            r1 = itmpx % b1 
            r2 = itmpy % b2
            X[i] = X[i] + f1*r1
            Y[i] = Y[i] + f2*r2
            itmpx = q1 
            itmpy = q2 
            f1 = f1/b1 
            f2 = f2/b2 

    ##########
    
    
    return X, Y
    
if __name__ == '__main__':
    """ 
    This is the place where you can test your function. 
    You can define variables, feed them into your function and check the output   
    """
    
    n = 100
    X, Y, pts = computeGridSukharev(n)
    #X = [0.25, 0.75, 0.25, 0.75]
    #Y = [0.25, 0.25, 0.75, 0.75]
    #The order of points could be different, but it should be the same point set.
    
    #The points are (X[i], Y [i]) : (0.25, 0.25),(0.75, 0.25),(0.25, 0.75),(0.75, 0.75)
    #You can put the visualization codes here
    plt.scatter(X, Y, color='r', marker='o')
    plt.title("Sukharev Grid")
    plt.xlim((0,1))
    plt.ylim((0,1))
    plt.show()
    
    n = 100
    X, Y, pts= computeGridRandom(n)
    
    #You can put the visualization codes here
    plt.scatter(X, Y, color='r', marker='o')
    plt.title("Random Grid")
    plt.xlim((0,1))
    plt.ylim((0,1))
    plt.show()

    n = 100
    b1 = 2
    b2 = 3
    
    X, Y = computeGridHalton(n, b1, b2)

    #You can put the visualization codes here
    plt.scatter(X, Y, color='r', marker='o')
    plt.title("Halton Grid")
    plt.xlim((0,1))
    plt.ylim((0,1))
    plt.show()






