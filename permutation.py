# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 03:59:04 2023

@author: varsh
"""
find the next permutation of nums
The next permutation of an array of integers is the next lexicographically 
greater permutation of its integer(Next greater number)

permutation means rearranging a set of given objects in all the 
possible orders.


i = len-2 
i > i+1
   yes
   i -=1
i > i+1
   no
   stop
   
check next larger number from i to right side, swap and ascending order 
from i

If such arrangement is not possible, the array must be rearranged as 
the lowest possible order (i.e., sorted in ascending order).

            
def nextPermutation(nums):
    i = len(nums) -2
    while i >= 0:
        if len(set(nums)) ==1:
            return nums
        elif nums[i] > nums[i+1]:
            i -=1
            if i == -1:
                nums.sort()
                return nums

        else:
            temp = 0
            index = 0
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    temp = nums[j]
                    index = j
            nums[index] = nums[i]
            nums[i] = temp
            nums = nums[0:i+1] + sorted(nums[i+1:len(nums)])
            return nums
nums = [1,3,2]
nums = nextPermutation(nums)
print(nums)