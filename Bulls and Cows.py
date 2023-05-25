# -*- coding: utf-8 -*-
"""
Created on Wed May 24 17:53:02 2023

@author: varsh
"""

#Others
from collections import Counter
import itertools
secret = "1123"
guess = "0111"
secret = "1807"
guess = "7810"
def string_to_dict_with_duplicates(string):
    dictionary = {}
    for index, char in enumerate(string):
        if char in dictionary:
            if not isinstance(dictionary[char], list):
                dictionary[char] = [dictionary[char]]
            dictionary[char].append(index)
        else:
            dictionary[char] = [index]
    return dictionary


secret = string_to_dict_with_duplicates(secret)
guess = string_to_dict_with_duplicates(guess)

bull =0
cow = 0

for k,v in guess.items():
    if k in secret.keys():
        print(k,v)
        intersection = list(set(secret[k]) & set(v))
        print("intersection",intersection)
        bull += len(intersection)
        print("bull",bull)
        
        non_intersection = list(set(secret[k]) ^ set(v))
        print("non_intersection",non_intersection)
        if len(non_intersection) >= 1:
            cow += 1
        print("cow",cow)

