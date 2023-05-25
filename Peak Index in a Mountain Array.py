# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:08:45 2023

@author: varsh
"""

#Peak Index in a Mountain Array
arr = [0,2,1,0]
for i in range(1, len(arr) - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        print(i)