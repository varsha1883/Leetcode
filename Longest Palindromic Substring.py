# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:17:19 2023

@author: varsh
"""
#Longest Palindromic Substring
s = "babad"
n = len(s)
dp = [[False for i in range(n)] for j in range(n)]
ans = ""
max_len = 0
for i in range(n - 1, -1, -1):
    print(i)
    for j in range(i, n):
        dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i + 1][j - 1])
        if dp[i][j] and (j - i + 1) > max_len:
            max_len = j - i + 1
            ans = s[i:j + 1]
print(ans)