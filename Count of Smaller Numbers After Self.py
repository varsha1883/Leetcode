# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:58:50 2023

@author: varsh
"""

#Count of Smaller Numbers After Self

nums = [5,2,6,1]
Output = [2,1,1,0]

start = 0
end = len(nums) 
lst = []
while start < end:
    val = [x for x in nums[start+1:end] if x < nums[start]]
    lst.append(len(val))
    start += 1