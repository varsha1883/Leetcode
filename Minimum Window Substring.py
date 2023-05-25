# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 07:26:22 2023

@author: varsh
"""
Minimum Window Substring

s = "ADOBECBODEBANC" 
t = "ABBC"
if set(list1) - set(list2):
[A D O B E C B O D E B A N C]  
[A D O B E C B]
 s
             e
       s        e
                       e
                       
                       
from collections import Counter

def contains(t, s):
    return not (Counter(t) - Counter(s))

Counter(t)
Counter({'A': 1, 'B': 2, 'C': 1})
                       
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' 
from string t.
all(x in s[start:end+1] for x in t):
    
    
s = "ADOBECBODEBANC" 
t = "ABBC"
s = "ADOBECODEBANC"
t = "ABC"
s = "a"
t = "a"
s = "a"
t = "aa"
s="ab"
b="b"
s = list(s)
t = list(t)
start = 0
end = 0
min_len = 0
def counter():
    d ={}
    for w in s.split():
        if w in d.keys():
            d[w] = d[w]+1
        else:
            d[w] = 1
    return d
#d = dict.fromkeys(t,None)
min_len = []
while end < len(s):
    print('start:',start,'end:',end)
    if len(Counter(t) - Counter(s[start:end+1])) == 0:
        print(s[start:end+1])
        min_len.append(s[start:end+1])
        result = [i+start for i, e in enumerate(s[start:end+1]) if e in t]
        print('index',result)
        
        if len(result) > 1:
            start = result[1]
    end += 1
if min_len:   
    print("".join(min(min_len, key = len)))
else:
    print("")
    