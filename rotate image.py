# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:08:42 2023

@author: varsh
"""


Rotate Image   90 degrees (clockwise)    90 degrees (anticlockwise).
              
  1  2  3      7  4  1                   3  6  9
  4  5  6      8  5  2                   2  5  8
  7  8  9      9  6  3                   1  4  7
  
  
 180 degree

 9 8 7
 6 5 4
 3 2 1
 

 
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

import numpy as np
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = matrix[::-1]
m = np.array(matrix)
r,c = m.shape

r,c = len(matrix), len(matrix[0])

i = 0
res = []

while i < c:
    lst = [inner_list[i] for inner_list in matrix]
    res.append(lst)
    i += 1

matrix = [[1,2,3],[4,5,6],[7,8,9]]
anti output : [[3,6,9],[2,5,8],[1,4,7]]

i = c-1
res = []

while i >= 0:
    lst = [inner_list[i] for inner_list in matrix]
    res.append(lst)
    i -= 1
    
    
180 degree

matrix = [[1,2,3],[4,5,6],[7,8,9]]
[[9,8,7],[6,5,4],[3,2,1]] 
matrix = matrix[::-1]
res = []
i = 0
while i < r:
    res.append(matrix[i][::-1])
    i +=1
    
    

        
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = matrix[::-1]
r,c = len(matrix), len(matrix[0])
i = 0
res = []

while i < c:
    lst = [inner_list[i] for inner_list in matrix]
    res.append(lst)
    i += 1
print(res)