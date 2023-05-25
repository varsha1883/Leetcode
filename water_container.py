# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 01:12:22 2023

@author: varsh
"""

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the 
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

height = [1,8,6,2,5,4,8,3,7]


area between two verticle line should be the highest
 0 1 2 3 4 5 6 7 8
[1,8,6,2,5,4,8,3,7]
 s
   e
 
stop = 9

 
start = 0
end = 0
dist = 0
max_area = 0

d ={}
while end <len(height):
    print('start:',start,'end:',end)
    max_area = max(max_area, min(height[start],height[end]) * (end-start))
    print('max_area',max_area)
    end += 1
    if end == len(height):
        start += 1
        end = start + 1
        
 0 1 2 3 4 5 6 7 8
[1,8,6,2,5,4,8,3,7]
 l               r
   
moving the pointer at longest line inwards wont help much as its depends on 
shorter length ( no chance of increment)

But, moving the pointer at shorter line inwards may help to increase the
area vertically if inwards lines are longest

maxarea = 0
left = 0
right = len(height) - 1

while left < right:
    print('start:',left,'end:',right)
    width = right - left
    maxarea = max(maxarea, min(height[left], height[right]) * width)
    print('max_area',maxarea)
    if height[left] <= height[right]:
        left += 1
    else:
        right -= 1

    