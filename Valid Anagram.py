# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:22:05 2023

@author: varsh
"""

#Valid Anagram

s = "anagram"
from collections import Counter
dic = Counter(s)
t = "nagaram"


dic_t = {e:t.count(e) for e in set(t)}
dic_s = {e:s.count(e) for e in set(s)}

if dic_t == dic_s:
    print(True)