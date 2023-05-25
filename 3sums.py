# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 02:10:35 2023

@author: varsh
"""

Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.


nums = [-1,0,1,2,-1,-4]

sort nums

nums = sorted(nums)

  if sum < 0 ---->        <----- if sum > 0
-4   -3    -2    -1    0     1    2   3   4

[-4, -1, -1, 0, 1, 2]

  i   j            k
      --->     <----
  
  
nums = [-1,0,1,2,-1,-4]
nums = [0,0,0]
nums = sorted(nums)
lst = []
for i in range(len(nums)): 
    print(nums[i])
    if nums[i] > 0:
        break
    if i == 0 or nums[i] != nums[i-1]:
        print('yes')
        print(nums[i])
        j = i+1
        k = len(nums) - 1 
        while j < k:
            print(nums[i]+nums[j]+nums[k])
            if nums[i]+nums[j]+nums[k] < 0:
                j +=1
            elif nums[i]+nums[j]+nums[k] > 0:
                k -=1
            else:
                lst.append([nums[i],nums[j],nums[k]])
                j +=1
                k -=1
                while j < k and  nums[j] == nums[j - 1]:
                    j += 1  
            
  if sum < 0 ---->        <----- if sum > 0
-4   -3    -2    -1    0     1    2   3   4

[-4, -1, -1, 0, 1, 2]

  i   s            e
      --->     <----

                
nums = [-1,0,1,2,-1,-4]            
triplets = []
nums.sort()
for i in range(len(nums)):
    target = -nums[i]
    start = i + 1
    end = len(nums) - 1
    while start < end:
        if nums[start] + nums[end] == target:
            triplets.append([nums[i], nums[start], nums[end]])
            start += 1
            end -= 1
        elif nums[start] + nums[end] < target:
            start += 1
        else:
            end -= 1





         
    