# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 20:10:13 2023

@author: varsh
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
l1 = [1,3,4,9,9,9,9,9,9]
l2 = [8,9,9,9]

      1  3  4  9  9  9  9  9  9
-1  
      8  9  9  9

## list to link list
#l1=[2,4,3]
def createLinkedList(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head

l1 = createLinkedList(l1)
l2 = createLinkedList(l2)

def mergeTwoLists(l1, l2):
       # maintain an unchanging reference to node ahead of the return node.
       prehead = ListNode(-1)

       prev = prehead
       while l1 and l2:
           print('previous',prev.val)
           if l1.val <= l2.val:
               prev.next = l1
               l1 = l1.next
           else:
               prev.next = l2
               l2 = l2.next            
           prev = prev.next

       # At least one of l1 and l2 can still have nodes at this point, so connect
       # the non-null list to the end of the merged list.
       prev.next = l1 if l1 is not None else l2

       return prehead.next
   
lst = mergeTwoLists(l1, l2)
curr = lst
values = []
while curr:
    values.append(str(curr.val))
    curr = curr.next
print(" ".join(values))

#Median

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def findMedian(head):
    slow = fast = head
    count = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        count += 1
    if fast:
        count += 1
    if count % 2 == 1:
        return slow.val
    else:
        return (slow.val + slow.next.val) / 2

print(findMedian(lst))

# Median
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

        
def findMedian(head):
    ptr1 = ptr2 = head 
    while (ptr1 != None and ptr1.next != None):
        ptr1 = ptr1.next.next
        pre_ptr = ptr2
        ptr2 = ptr2.next
                 
    if ptr1:
        return ptr2.val
    else:
        return (ptr2.val + pre_ptr.val) / 2

print(findMedian(lst))


    
