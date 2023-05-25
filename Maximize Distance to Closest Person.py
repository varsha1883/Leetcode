# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 18:52:47 2023

@author: varsh
"""

Maximize Distance to Closest Person

seats = [1,0,0,0,1,0,1]

#seats = [1,0,0,0] 
index_0 = [i for i,val in enumerate(seats) if val == 0]  
#[1,2,3,5]    
index_1 = [i for i,val in enumerate(seats) if val == 1]     
#[0,4,6]
dis = []


end = 0

while end < len(index_0):
    print('end',end)
    if len(index_1) == 1:
        dis.append(abs(index_0[end]-index_1[0]))
       
    elif index_0[end] == len(seats) - 1:
        min_limit = max(i for i in index_1 if i < index_0[end])
        dis.append(index_0[end]-min_limit)
        
    elif index_0[end] == 0:
        min_limit = min(i for i in index_1 if i > index_0[end])
        dis.append(min_limit-index_0[end])
        
    
    else:
        min_limit = max(i for i in index_1 if i < index_0[end])
        max_limit = min(i for i in index_1 if i > index_0[end])
        
        dis.append((index_0[end]-min_limit,max_limit-index_0[end]))
    print('distance',dis)   
    end +=1
        
def util_func(a):
    try:
        return min(a)
    except:
        return a
distance = max([util_func(d) for d in dis])      
    