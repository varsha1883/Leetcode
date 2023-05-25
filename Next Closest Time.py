# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:44:35 2023

@author: varsh
"""

Next Closest Time

Input: time = "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 
19:39, which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.

Input: time = "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is 
smaller than the input time numerically.

import re
time = "19:34"

def util_func(a):
    try:
        return int(a)
    except ValueError:
        pass

digits = list(map(int,filter(str.isdigit, string)))
digits = [int(x) for x in string if x.isdigit()]
digits = [char for char in re.findall(r'\d+',time)]

digits = [util_func(x) for x in time if util_func(x) != None]
digits = digits[::-1]

[2, 1, 1, 1]  14:35
    s     e

def next(digits):
    if all(digits[i] >= digits[i + 1] for i in range(len(digits) - 1)):
        
        return str(digits[len(digits)-1])+str(digits[len(digits)-1])+':'+str(digits[len(digits)-1])+str(digits[len(digits)-1])
    
    
    start = 0
    end = 0
    while start < len(digits):
        
        temp = 0
        for end in range(start+1,len(digits)):
        
            if digits[end] > digits[end-1]:
                temp = digits[end]
                index = end
            
        if index != start:
            digits[start] = temp
            break
        else:
            start += 1
    return str(digits[3])+str(digits[2])+':'+str(digits[1])+str(digits[0])

#time = "19:34"
time = "23:59" 

digits = [util_func(x) for x in time if util_func(x) != None]
digits = digits[::-1]
res = next(digits)