# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 15:54:26 2023

@author: varsh
"""

Expressive Words

conditions
choose a group consisting of characters c, and add some number of characters 
c to the group so that the size of the group is three or more.


>>> import itertools
>>> ''.join(g[0] for g in itertools.groupby('hiiii how are you??'))
'hi how are you?'


s = "heeellooo"

words = ["hello", "hi", "helo"]

s = "zzzzzyyyyy"
words = ["zzyy","zy","zyy"]

find group
def create_group(s):
    last = ''
    results = []
    d = {}
    for letter in s:
        if letter == last:
            results[-1] = (letter, results[-1][1] +1)
        else:
            results.append((letter, 1))
            last = letter
            
    return results
results = create_group(s)
result_1 = [tup for tup in results if tup[1] >= 3]
[('e', 3), ('o', 3)]
[('z', 5), ('y', 5)]


res = 0
for word in words:
    import re
    word = re.sub(r"(.)\1+", r"\1", word)
    for tup in result_1:
        print(tup)
        word = word.replace(tup[0], tup[0]*tup[1], 1) 
        print(word)
    if word == s:
        res +=1
print(res)
