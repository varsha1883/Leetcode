# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 23:12:09 2023

@author: varsh
"""

Multiply Strings

num1 = "23"
num2 = "456"

  4 5 6        6  5  4           3  2
    2 3        3  2              6  5  4
---------    -----------        ------------
1 3  6  8      8  6  3  1        8   3  1
9 1  2  0      0  2  1  9        0   5  1  1
==========

num1 = "23"
num2 = "456"

num1 = num1[::-1]
num2 = num2[::-1]
result = ""
i = 0
temp = 0
min_val = min(num1, num2, key= len)
max_val = max(num1, num2, key= len)
results = []
for index, m in enumerate(min_val):
    print('index',index,'m',m)
    result = '0' * index
    print(result)
    while i < max(len(num1),len(num2)):
        x = int(max_val[i]) if i < len(max_val) else 0
        print('x',x,'m',m,'temp',temp)
        s = (x*int(m))+temp
        print('s:',s)
        result += str(s % 10)
        temp = s // 10
        i += 1
    if temp > 0:
        result += str(temp)
        results.append(result[::-1])
        i = 0
        temp = 0
        print('results',results)
    else:
        results.append(result[::-1])
        i = 0
        temp = 0
        print('results',results)

num1 = results[0]
num1 = num1[::-1]

num2 = results[1]
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
                