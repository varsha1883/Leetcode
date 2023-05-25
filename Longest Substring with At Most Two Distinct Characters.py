# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 11:57:55 2023

@author: varsh
"""

Longest Substring with At Most Two Distinct Characters

s = "abcabcbb" 
   0  1  2  3  4  5
   a  b  a  a  c  a  b  c  b  b
   s           e
      s     e
   
    
   0  1  2  3  4  5  6
   c  c  a  a  b  b  b  
s ="ccaabbb"
s = "aaaa"
tree = list(s)
start = 0
end = 0
max_len = 0
d ={}
while end <len(tree):
    print('start:',start,'end:',end)
    if len(set(tree[start:end+1])) == 2:
        
        print('array',tree[start:end+1])
    
        max_len = max(max_len,end-start+1)
    elif len(set(tree[start:end+1])) > 2:
        print('array',tree[start:end+1])
        start = end - 1
        for i in range(end-1, -1, -1):
            print('tree',tree[i],tree[i-1])
            if i > 0 and tree[i] == tree[i-1]:
                start -= 1
            else:
                break

    end += 1
    
    
start: 0 end: 0
start: 0 end: 1
start: 0 end: 2
array ['c', 'c', 'a']
start: 0 end: 3
array ['c', 'c', 'a', 'a']
start: 0 end: 4
array ['c', 'c', 'a', 'a', 'b']
tree a a
tree a c
start: 2 end: 5
array ['a', 'a', 'b', 'b']
start: 2 end: 6
array ['a', 'a', 'b', 'b', 'b']
   