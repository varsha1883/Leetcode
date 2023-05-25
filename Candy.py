# -*- coding: utf-8 -*-
"""
Created on Wed May 24 15:33:13 2023

@author: varsh
"""

#others

ratings = [1,2,0,1,0,2]
ratings = [1,2,2]
ratings = [1,0,2]
#Assign 1 candy to lowest rating first
#Each child must have at least one candy.
#Children with a higher rating get more candies than their neighbors.

candies = []
for i, rating in enumerate(ratings):
    if i <= len(ratings) -2:
        if ratings[i] <= ratings[i+1] and ratings[i] <= ratings[i-1]:
            candies.append(1)
        else:
            candies.append(2)
    else:
        if ratings[i] <= ratings[i-1]:
            candies.append(1)
        else:
            candies.append(2)
        
print(candies)
        
        