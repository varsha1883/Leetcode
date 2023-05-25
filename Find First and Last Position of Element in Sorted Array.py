# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:36:48 2023

@author: varsh
"""

#Find First and Last Position of Element in Sorted Array

nums = [5,7,7,8,8,10]
nums= [2,7,7,7,8,10]
target = 7
l = [i for i in nums if i > target]
right = len(nums) - (len(l)+1)

lst = []
default_lst = [-1,-1]
left = 0

    

while left < right:
    print('left',left,'right',right)
    if target not in nums:
        print(default_lst)
        break
    
    if nums[left] == target:
        lst.append(left) 
        lst.append(right)
        print(lst)
        break
   
    left += 1       
    
    
    