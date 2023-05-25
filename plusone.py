# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 00:15:15 2023

@author: varsh
"""

@ You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. The digits are 
ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

#digits = [1,2,3]
digits = [9]
i = len(digits) - 1
while i >= 0:
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
[1,0]

digits = [1,2,3]
digits = [9]
result = ""
temp = 0
i = len(digits) - 1
while i >= 0:
    p = 1 if i == len(digits) - 1 else 0
    s = digits[i]+p+temp
    result += str(s % 10)
    temp = s // 10
    if temp > 0:
        result += str(temp)
        print(result[::-1])
        break       
    i -= 1
print(result[::-1])
[10]       
    