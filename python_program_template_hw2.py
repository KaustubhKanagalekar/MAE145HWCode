#!/usr/bin/env python3
"""
Guidelines for program submission: 
    
A) To ensure readability by the grader, 
    please make sure the following submission format:

    1-- Please change the file name to python_program.py 
        ---(The file name is case sensitive, make sure it's identical)---
               
    2-- Please submit only the python_program.py to the autograder
        descriptions of the function should be added in .py file as comments 
       

B) Your homework should follow the similar structure as this template

C) Keep in mind some minor points:
    
    0-- Your code should not have any debug error before submission!!!

    1-- make sure the function name is identical to that in the problem set (HW2)
            ---(function names are case sensitive! )---
    
    2-- The order of the function arguments should be the same as that in HW 

    2a-- The data type of the argument should be the same as that in template
                      
    3-- make sure your function return the value which the HW requested
    
    4-- make sure the order of the output arguments the same as those in template
    
    5-- Do not round up your output values
    
    6-- Do not use input function in your function
        
    7-- if you need uncommon modules, contact TA before submission or post it on Piazza
    


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
import random
# your file should always start from definition of functions 

def create_board():
    """ Add illustrations here, if needed """
    
    # define variables you need
    
    #board = #numpy array to represent a 3 x 3 table, each element
            #should be set as an integer equal to zero
    board = np.empty([3,3])
    board = np.zeros((3,3), dtype = 'int')
    return board


def place(board , player, position):
    """ Add illustrations here, if needed """
    player 
    positionx, positiony = position
    if board[positionx, positiony] == 0:
        board[positionx, positiony] = player 
    # Operations
    
    return board #(same data type as input board)

def possibilities(board):
    ind = []
    #operations
    indx,indy = np.where(board == 0)
    ind = list(zip(indx, indy))
    
    return ind #each element in this list should be tuple or it is
               #empty (return [])

def random_place(board, player):  # Important: you need to use a random seed of 1 to show results
    #random.seed(1)                # for truly random results comment this line out
    # operations
    select_position = random.choice(possibilities(board))
    place(board, player, select_position)
    return board

def repeat(n):                     # Important: you should enter 1 to initialize the random seed
                                   #  for truly random results comment this line out     
    board = create_board()
    #random.seed(1)
    # Operations
    i = 0

    for i in range(n):
        board = random_place(board,1)
        board = random_place(board,2)
        i += 1
        
    
    return board
    
if __name__ == '__main__':
    """ 
    This is the place where you can test your function. 
    You can define variables, feed them into your function and check the output   
    """
    
    board = create_board()
    
    board = place(board, 1, (0,0))  
    
    empty_positions = possibilities(board)
    
    board = random_place(board, 1)
 
    n =  4  # an integer n < 5 since there are only 9 cells in the board and two players in turn place the mark
            # repeat n times
    board = repeat(n)

    print(board)
