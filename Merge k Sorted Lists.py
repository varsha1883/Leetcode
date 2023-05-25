# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 17:25:06 2023

@author: varsh
"""

Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted 
in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

lists = [[1,4,5],[1,3,4],[2,6]]


for list in list:
    for i in list:
lst = [i for list in lists for i in list]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next

        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next

        return head.next