# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 02:52:29 2023

@author: varsh
"""

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"


Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Binary Rule:
    
    1+1 = 10
    1+0 = 1
    0+0 = 0
    
1 1
  1
---------
1 0 0

result += str(s % 2)
        carry = s // 2
        
a = "1111"
a = a[::-1]
b = "1111"
b = b[::-1]
result = ""
i = 0
temp = 0
while i < max(len(a),len(b)):
    x = int(a[i]) if i < len(a) else 0
    y = int(b[i]) if i < len(b) else 0
    s = x+y+temp
    result += str(s % 2)
    temp = s // 2
    if temp > 0:
        result += str(temp)
        print(result[::-1])
        break       
    i += 1
print(result[::-1])
        
    
    
    
    
    
    if digits[i] < 9:
        digits[i] = digits[i] + 1
        print(digits)
        break
    else:
        digits[i] = 0
        if i == 0:
            digits = [1]+digits
            print(digits)
        i -= 1
print(digits)
    