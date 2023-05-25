# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:30:43 2023

@author: varsh
"""

Valid Parentheses

s = "()"
s = "()[]{}"
s = "(]"

dic = {}
s = "()[]{}"

# First Method
dic = {x: dic.get(x, 0) + 1 for x in s}
if len(list(set(list(dic.values())))) == 1:
    print('valid')

# Second Method
digit1 = 0
digit2 = 0
digit3 = 0
end = 0

while end < len(s):
    
    if s[end] == "(":
        digit1 +=1
    elif s[end] == ")":
        digit1 -= 1
    elif s[end] == "{":
        digit2 +=1
    elif s[end] == "}":
        digit2 -=1
    elif s[end] == "[":
        digit3 +=1
    elif s[end] == "]":
        digit3 -=1
    print(s[end])
    print(digit1,digit2,digit3)
    end +=1 
#print(digit1,digit2,digit3)
if digit1 == 0 and digit2 == 0 and digit3 == 0:
    print('valid')
else:
    print('invalid')
    
    
    
(
1 0 0
)
0 0 0
[
0 0 1
]
0 0 0
{
0 1 0
}
0 0 0
valid