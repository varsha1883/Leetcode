# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 10:59:48 2023

@author: varsh
"""

Read N Characters

def read(buff):
    
    
    return len(buff)


file = "abcdf"
  0   1   2   3   4
  a   b   c   d   f
  s   e
          s    e        
                  s

file = "abc"
queries = [1,2,1]
file = "abcdf"
queries = [2,2,1]
res = []
start = 0
i = 0
while i < len(queries):
    print('start',start, 'end',start+queries[i])
    buff = file[start:start+queries[i]]
    print('buff',buff)
    buff_c = read(buff)
    start = start + queries[i]
    i +=1
    
    res.append(buff_c)
    
    
print(res)


class Solution:
    def __init__(self):
        self.buffer = []
        
    def read(self, buf, n):
        i = 0
        while i < n:
            if self.buffer:
                buf[i] = self.buffer.pop(0)
                i += 1
            else:
                temp = [''] * 4
                count = read4(temp)
                if count == 0:
                    break
                self.buffer += temp[:count]
        return i

    