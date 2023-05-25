# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 13:44:59 2023

@author: varsh
"""
Missing Ranges

You are given an inclusive range [lower, upper] and a sorted unique integer 
array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] 
and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number 
exactly. That is, no element of nums is in any of the ranges, and each 
missing number is in one of the ranges.

["2","4->49","51->74","76->99"]

nums = [0,1,3, 50,75]
lower = 0
upper = 99
res = []
end = 1
i = 1

nums = [lower-1] + nums + [upper+1]

while end < len(nums):
    
    if nums[end] != nums[end-1]+1:

        r1 = nums[end-1] +1
        r2 = nums[end] - 1
        if r1 == r2:
            val = str(r1)
        else:
            val = str(r1)+"->"+str(r2)
            
        res.append(val)
           
    end +=1