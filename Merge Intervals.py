# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:50:09 2023

@author: varsh
"""

#Merge Intervals

intervals = [[1,3],[0,2],[2,6],[8,10],[15,18]]

intervals = [[0, 5],[5,7],[8, 10],[15, 18]]
intervals.sort(key=lambda x: x[0])

merged = []
for interval in intervals:
    # if the list of merged intervals is empty or if the current
    # interval does not overlap with the previous, simply append it.
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
    # otherwise, there is overlap, so we merge the current and previous
    # intervals.
        merged[-1][1] = max(merged[-1][1], interval[1])

print(merged)

intervals = [[0, 5], [8, 10], [15, 18]]
newInterval = [5,8]


intervals.sort(key=lambda x: x[0])

merged = []
for interval in intervals:
    # if the list of merged intervals is empty or if the current
    # interval does not overlap with the previous, simply append it.
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
    # otherwise, there is overlap, so we merge the current and previous
    # intervals.
        intervals[i][1] = max(intervals[i][1], newInterval[1])
        intervals[i][0] = min(intervals[i][0], newInterval[0])

print(merged)






n= len(intervals) - 1
output = [[0, 7], [8, 10], [15, 18]]

i = 0
while i < n:
    
    if intervals[i][1] < newInterval[0]:
        i +=1
        if newInterval[1] < intervals[i][0]:
            intervals.append(newInterval)
            intervals.sort(key=lambda x: x[0])
            print(intervals)
            break
        else:
            intervals[i][1] = max(intervals[i][1], newInterval[1])
            
        
    else:
        intervals[i][1] = max(intervals[i][1], newInterval[1])
        intervals[i][0] = min(intervals[i][0], newInterval[0])
        if newInterval[1] < intervals[i+1][0]:
            break
        else:
            intervals[i][1] = max(intervals[i][1], newInterval[1])
        
    i += 1
    
print(intervals)
        
                

