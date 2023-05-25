# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:52:16 2023

@author: varsh
"""
#Others
def reverse(x):
    if x<0:
        x = -x
        x_reversed = int(str(x)[::-1])
        x_reversed = - x_reversed
    
    else:
        x_reversed = int(str(x)[::-1])
    
    if -2**31 <= x_reversed and x_reversed <= 2**31 -1:
        return x_reversed
    else:
        return 0

x = 1230  
x_reversed = reverse(x)
print(x_reversed)