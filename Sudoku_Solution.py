# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:31:26 2017

@author: Kara
Solution for sudoku game. 
Once the user enters a sudoku, this program will check if the sudoku is correct or not.
The it will give the solution for sudoku. 
"""

import numpy as np
from copy import deepcopy

# Getiing the user input for the sudoku

sudoku_org = [];
for n in range(0,9):
    print("Please enter the",n+1,"line in your sudoku with spaces between numbers:");
    line = [int(x) for x in input().split()];
    sudoku_org.append(line);
print(sudoku_org);
    
# Check if the entered sudoku is a correct sudoku or not
    
    

sudoku = deepcopy(sudoku_org);
check = 0;
#""" Check how many zero-cells in sudoku """
for n1 in range(0,9):
    for n2 in range(0,9):
        if sudoku[n1][n2] == 0:
            check = check++1;
print("\nA number of cells to be filled out in your Sudoku is", check);
 
for temp in range(0,15): 
    if check == 0:
        print("\nCongratulations! You have solved this Sudoku with our help ^^");
        print(np.array(sudoku));
        break;
    sudoku1 = deepcopy(sudoku);
    check1 = check;     
    #""" Find the matrixes of rows, columns and squares of zero-cells"""
    #""" matrix of rows """
    m1 = [];
    #""" matrix of columns """
    m2 = [];
    #""" matrix of 9 squares 3x3 """
    m3 = [];
                
    for i in range (0,9):
        row = [];
        col = [];
        for j in range (0,9):
            if sudoku[i][j] != 0:
                row.append(sudoku[i][j]);
            if sudoku[j][i] != 0:
                col.append(sudoku[j][i]);
            square = [];
            z = [0,3,6];
            if(i in z and j in z):
                for x in range (i,i+3):
                    for y in range (j,j+3):
                        if sudoku[x][y] !=0:
                            square.append(sudoku[x][y]);
                m3.append(square);
            
        m1.append(row);
        m2.append(col);
        #""" finish finding matrixes m1, m2, m3 """
        
    #""" Start playing Sudoku """
    number_list = [1,2,3,4,5,6,7,8,9];
    sudoku2 = deepcopy(sudoku);
    for i in range (0,9):
        for j in range (0,9):
            if sudoku[i][j] == 0:
                #""" initial - possible list """
                pos_list = [1,2,3,4,5,6,7,8,9];
                #""" find the imposibilities of this cell """
                impos_list = [];
                for k1 in m1[i]:
                    impos_list.append(k1);
                for k2 in m2[j]:
                    impos_list.append(k2);
                #""" determine the square that the cell is belonged to """
                k3 = 3*(i//3) + (j//3);
                for k4 in m3[k3]:
                    impos_list.append(k4);
                for k in number_list:
                    if k in impos_list:
                        pos_list.remove(k);
                sudoku2[i][j] = deepcopy(pos_list);
                if len(pos_list)==1:
                    sudoku[i][j] = pos_list[0];
                    check = check-1;
    if check == check1:
        print();
        print(np.array(sudoku));
        print("\nThere is no more recommendation for you.");
        #print("Number of cells to be filled out after the", temp, "time is", check);
        print("From now on, you should choose by yourself :P");
        print();
        print(sudoku2);
        break;

    
        
    
 

    
 

        
            
        

