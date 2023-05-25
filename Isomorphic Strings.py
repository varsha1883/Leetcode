# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:25:06 2023

@author: varsh
"""

#Others
s = "foo"
t = "bar"
s = "paper"
t = "title"

def create_mapping_dict(string1, string2):
    mapping_dict = {}
    
    if len(s) != len(t):
        return("Non Isomorphic")
    
    for i in range(len(s)):
        char1 = s[i]
        char2 = t[i]
        if char1 in mapping_dict:
            if mapping_dict[char1] != char2:
                return("Non Isomorphic")
        mapping_dict[char1] = char2
    
    return("Isomorphic")

mapping_dict = create_mapping_dict(s, t)
print(mapping_dict)
