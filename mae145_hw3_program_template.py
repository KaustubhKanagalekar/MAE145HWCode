#!/usr/bin/env python3
"""
Guidelines for program submission: 
    
 Your homework should follow the similar structure as this template

 Keep in mind some minor points:
    
    0-- Your code should be bug free before submission!!!

    1-- make sure the function name is identical to that in the problem set (HW3)
            ---(function names are case sensitive! )---
    
    2-- The order of the function arguments should be the same as that in HW 

    2a-- The data type of the argument should be the same as that in template
                      
    3-- make sure your function return the value which the HW requested
    
    4-- make sure the order of the output arguments the same as those in template
    
    5-- Do not round up your output values
    
    6-- Do not use input function in your function
        
    7-- if you need uncommon modules, contact TA before submission or post it on Piazza

    8-- Please do not add any variable clearing command in the file, as this may terminate grader
    


If you had any question about the guidelines, 
    contact TAs or post questions on piazza for response.
        
@authors: Pengcheng Cao (p5cao@ucsd.edu) at UCSD
@Date: April 17, 2024
"""



"""
The template starts from here
"""

# A16790822 #PID

# import all modules here if you need any

import numpy as np
import random
# your file should always start from definition of functions 



def computeBFStree(AdjTable, start): 
    """ descriptions here """
    # computes BFS tree of an adjacency matrix 
    ##########
    #### Your code goes here ####
    ##########
    
    # keep track of all visited nodes
    visited = []
    # keep track of nodes to be checked
    queue = [start]
    # visits all the nodes of a AdjTable (connected component) using BFS
    while queue:
          i = queue.pop(0)
          if i not in visited:   
            visited.append(i)
            for neighbour in AdjTable[i]:
                if neighbour not in visited:
                    queue.append(neighbour)
                
    return visited
    # or a vector of pointers parents describing the BFS tree rooted at start
    # equivalently, a list of nodes in visited order, start from the 'start node' 
     # list of visited node e.g. [ 'A', 'B', 'C', 'D']

    # keep looping until there are nodes still to be checked
    # there should be three different types of results to return:  
    for neighbour in neighbours:
        if neighbour not in AdjTable:
            return 'AdjTable is invalid'
    
    if start not in AdjTable:
        return 'No start node in the graph'
    
    
    



def computeBFSpath(AdjTable, start, goal):
    """ descriptions here """
    #computes BFS path from start to goal

    # define some variables etc.
    
    
    ##########
    #### Your code goes here ####
    ##########
    
    # there should be four different types of results to return:  
    
        
    if start not in AdjTable:
        return 'No start node in the graph'
    if goal not in AdjTable:
        return 'No goal node in the graph'

    
    # keep track of visited nodes
    visited = []
    # keep track of all the paths to be checked
    queue = [[start]]
    # return path if start is goal
    
    #Condition 1
    
    while queue:
        i = queue.pop(0)
        path = i[-1]
        if path not in visited:
            neighbours = AdjTable[path]
            for neighbour in neighbours:
                new_path = list(i)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            visited.append(path)

    for neighbour in neighbour:
        if neighbour not in AdjTable:
            return 'AdjTable is invalid'
    # in case there's no path between the 2 nodes
    return "No path" # Condition 2
     
    
    
    
if __name__ == '__main__':
    """ 
    This is the place where you can test your function. 
    You can define variables, feed them into your function and check the output   
    """
    
    # AdjTable defined as a dictionary 
    
    #Testing with input of AdjTable
    AdjTable = {'A': ['B', 'D'],
                'B': ['A'],
                'C': ['D'],
                'D': ['A', 'F', 'C'],
                'E': ['F'],
                'F': ['D', 'E']}
    
      
    start='A'
    goal='C'
    
    myBFSTree=computeBFStree(AdjTable, start)
    print(myBFSTree)
    # output should be a list: 
    # ['A', 'B', 'D', 'F', 'C', 'E']

    myBFSPath=computeBFSpath(AdjTable, start, goal)
    print(myBFSPath)
    # output should be a list: 
    # ['A', 'D', 'C']
    
    
    #Writing maze graph in E2.8 as the AdjTable1 and testing based on the nodes marked 
    AdjTable1 = {1: [2,3],2: [1,4,17],3: [1,4,5],4: [2,4,6],5: [3,6,7],6: [4,5,8],7:[5,8,9],
                 8: [6,7,10],9: [7,10],10: [8,9,11],11: [10,12],12: [11,13],13:[12,14],
             14: [13,15],15: [14,26,16],16: [15,32],17: [2,18],18: [17,19], 
             19:[18,20,21],20: [19,22], 21: [19,22,23],22: [20,21,24],23: [21,24,27],
             24:[22,23,25],25: [24,26],26: [25,15],27: [23,28],28: [27,29],29: [28,30],
             30:[29,31],31: [30,32],32: [16,31]}
    start, goal = 1, 32
    myBFSTree=computeBFStree(AdjTable1, start)
    print(myBFSTree)
    # solution should be a list: 
    #[1, 2, 3, 4, 17, 5, 6, 18, 7, 8, 19, 9, 10, 20, 21, 11, 22, 23, 12, 24, 
    #27, 13,25, 28, 14, 26, 29, 15, 30, 16, 31, 32]
     
    myBFSPath=computeBFSpath(AdjTable1, start,goal)
    print(myBFSPath)
    # [1, 2, 4, 6, 8, 10, 11, 12, 13, 14, 15, 16, 32]







