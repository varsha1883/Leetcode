# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 22:33:48 2023

@author: varsh
"""

Given two non-negative integers, num1 and num2 represented as string, 
return the sum of num1 and num2 as a string.

   1 2 3 
     1 1
     
   3 2 1
   1 1

num1 = "11"
num1 = num1[::-1]

num2 = "123"
num2 = num2[::-1]
result = ""
i = 0
temp = 0
while i < max(len(num1),len(num2)):
    x = int(num1[i]) if i < len(num1) else 0
    y = int(num2[i]) if i < len(num2) else 0
    s = x+y+temp
    print('s:',s)
    result += str(s % 10)
    temp = s // 10
    i += 1
if temp > 0:
    result += str(temp)
    print(result[::-1])      
print(result[::-1])
        