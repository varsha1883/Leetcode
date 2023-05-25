# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 16:55:53 2023

@author: varsh
"""

Find And Replace in String

You are given a 0-indexed string s that you must perform k replacement 
operations on. The replacement operations are given as three 0-indexed 
parallel arrays, indices, sources, and targets, all of length k.

To complete the ith replacement operation:

- Check if the substring sources[i] occurs at index indices[i] in the original 
string s.

- If it does not occur, do nothing.

- Otherwise if it does occur, replace that substring with targets[i].

s = "abcd" 
indices = [0, 2] 
sources = ["a", "cd"] 
targets = ["eee", "ffff"]

Output: "eeebffff"
s = "abc"
indices = [0, 1]
sources = ["ab","bc"]
word = s
end = 0
for i,val in enumerate(indices):
    if end >= val:
        print("replacement overlap")
        break
    start = val
    end = start
    
    
    while end < len(s):
        print("start",start,"end",end)
        
        if s[start:end+1] == sources[i]:
            word = word.replace(s[start:end+1],targets[i])
            print("word",word)
            break
        else:
            end +=1
    